/* eslint-disable */
import kue from "kue"
const queue = kue.createQueue();

const data = {
  phoneNumber: "4153518780",
  message: "This is the code to verify your account",
}

let job = queue.create("push_notification_code", data)
  .save((err) => {
    if (!err) {
      console.log("Notification job created:", job.id);
    }
  });

job.on("complete", (result) => {
  console.log("Notification job completed");

}).on("failed", (err) => {
  console.log("Notification job failed");

});
