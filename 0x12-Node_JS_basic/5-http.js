const http = require('http');
const countStudents = require('./3-read_file_async');

const port = 1245;

const app = http.createServer(async (req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');
  if (req.method === 'GET') {
    if (req.url === '/') {
      res.end('Hello Holberton School!');
    } else if (req.url === '/students') {
      await countStudents(process.argv[2])
        .then((val) => {
          res.write('This is the list of our students\n');
          res.write(`Number of students: ${val.lines.length}\n`);
          res.write(`Number of students in CS: ${val.findCS.length}. List: ${val.findCS.join(', ')}\n`);
          res.write(`Number of students in SWE: ${val.findSWE.length}. List: ${val.findSWE.join(', ')}\n`);
          res.end();
        })
        .catch((err) => {
          res.write('This is the list of our students\n');
          res.end(err.message);
        });
    }
  }
});
app.listen(port);
module.exports = app;
