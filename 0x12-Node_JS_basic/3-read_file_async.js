const fs = require('fs').promises;

const countStudents = async (path) => {
  try {
    const content = await fs.readFile(path, 'utf8');
    let lines = content.toString().split(/\r?\n/);
    lines = lines.filter((line) => line !== '');
    lines.shift();
    console.log(`Number of students: ${lines.length}`);
    const findCS = lines.filter((line) => line.endsWith('CS')).map((line) => {
      const stdntCS = line.split(',');
      return stdntCS[0];
    });
    console.log(`Number of students in CS: ${findCS.length}. List: ${findCS.join(', ')}`);
    const findSWE = lines.filter((line) => line.endsWith('SWE')).map((line) => {
      const stdntSWE = line.split(',');
      return stdntSWE[0];
    });
    console.log(`Number of students in SWE: ${findSWE.length}. List: ${findSWE.join(', ')}`);
    return { lines, findCS, findSWE };
  } catch (err) {
    throw new Error('Cannot load the database');
  }
};
module.exports = countStudents;
