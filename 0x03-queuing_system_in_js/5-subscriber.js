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


const listener = (message, channel) => {
  console.log(message);
  if (message == "KILL_SERVER") {
    client.unsubscribe(channel);
    client.quit();
  }
}

await client.subscribe("holberton school channel", listener);
