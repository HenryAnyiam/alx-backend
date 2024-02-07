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


const values = {
  "Portland": 50,
  "Seattle": 80,
  "New York": 20,
  "Bogota": 20,
  "Cali": 40,
  "Paris": 2,
}

for (let i in values) {
  await client.hSet("HolbertonSchools", i, values[i], redis.print);
}

const hash = await client.hGetAll("HolbertonSchools");
console.log(hash);
