/* eslint-disable */
import redis from 'redis'


const client = await redis.createClient()
  .on('connect', () => {
    console.log("Redis client connected to the server");
  })
  .on('error', (err) => {
    console.log("Redis client not connected to the server:", err);
  })
  .connect();


const publishMessage = async (message, time) => {
  console.log("About to send", message);
  await setTimeout(async () => {
    await client.publish("holberton school channel", message);
  }, time);
}

await publishMessage("Holberton Student #1 starts course", 100);
await publishMessage("Holberton Student #2 starts course", 200);
await publishMessage("KILL_SERVER", 300);
await publishMessage("Holberton Student #3 starts course", 400);
