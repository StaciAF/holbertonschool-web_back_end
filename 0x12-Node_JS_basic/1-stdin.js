process.stdout.write(
  'Weclome to Holberton School, what is your name?\n',
);
process.stdin.setEncoding('utf8');
process.stdin.on('readable', () => {
  const done = process.stdin.read();

  if (done) {
    process.stdout.write(`Your name is: ${done}`);
  }
});

process.stdin.on('end', () => {
  process.stdout.write('This important software is now closing\n');
});
