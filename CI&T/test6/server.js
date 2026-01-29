const express = require("express");

const createServer = (pool, port = 3000) => {
  const app = express();

  app.get("/posts/:postId/comments", async (req, res) => {
    const { postId } = req.params;

    try {
      // check if post exists
      const postCheck = await pool.query("SELECT 1 FROM posts WHERE id = $1", [postId]);
      if (postCheck.rowCount === 0) return res.status(404).end();

      // recursive CTE to fetch all nested comments for a specific post
      const { rows } = await pool.query(`
        WITH RECURSIVE tree AS (
          SELECT id, text, parent_id, 1 as depth FROM comments 
          WHERE post_id = $1 AND parent_id IS NULL
          UNION ALL
          SELECT c.id, c.text, c.parent_id, t.depth + 1 FROM comments c
          JOIN tree t ON c.parent_id = t.id WHERE t.depth < 10
        ) SELECT id, text, parent_id FROM tree ORDER BY depth, id`, [postId]);

      // build hierarchy using an O(n) Map-based approach
      const map = new Map(rows.map(r => [r.id, { id: r.id, text: r.text, children: [] }]));
      const data = [];

      rows.forEach(row => {
        const node = map.get(row.id);
        if (row.parent_id && map.has(row.parent_id)) {
          map.get(row.parent_id).children.push(node);
        } else {
          data.push(node);
        }
      });

      // recursive cleanup: remove 'parent_id' and empty 'children' arrays
      const sanitize = (list) => list.map(({ children, ...node }) => ({
        ...node,
        ...(children.length > 0 && { children: sanitize(children) })
      }));

      res.json({ data: sanitize(data) });
    } catch (err) {
      console.error(err);
      res.status(500).end();
    }
  });

  const server = app.listen(port);
  return {
    app,
    close: () => new Promise(r => server.close(r))
  };
};

module.exports = { createServer };