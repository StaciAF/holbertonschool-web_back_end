const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout,
});

readline.setPrompt('Welcome to Holberton School, what is your name?\n');
readline.prompt();
readline.on('line', (name) => {
  console.log(`Your name is: ${name}`);
  readline.close();
});
readline.on('close', () => {
  console.log('This important software is now closing ');
  process.exit(0);
});
