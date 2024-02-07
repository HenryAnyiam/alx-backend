/* eslint-disable */
import redis from 'redis';


const client = await redis.createClient()
  .on('connect', () => {
    console.log("Redis client connected to the server");
  })
  .on('error', (err) => {
    console.log("Redis client not connected to the server:", err);
  })
  .connect();



const setNewSchool = async function (schoolName, value) {
  await client.set(schoolName, value, redis.print);
}

const displaySchoolValue = async function (schoolName) {
  const value = await client.get(schoolName);
  console.log(value);
}


displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
