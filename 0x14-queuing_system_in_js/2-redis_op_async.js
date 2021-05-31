import redis from 'redis';

const { promisify } = require('util');

const client = redis.createClient();

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

const setNewSchool = (schoolName, value) => client.set(schoolName, value, redis.print);
const displaySchoolValue = async (schoolName) => {
  const aget = promisify(client.get).bind(client);
  console.log(await aget(schoolName));
};

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
