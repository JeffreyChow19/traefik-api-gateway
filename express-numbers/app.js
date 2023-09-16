const express = require("express");
const app = express();
const port = 3000;

app.get("/", (req, res) => {
  res.send("Hello from Numbers... Use GET /random to get a random number");
});

app.get("/random", (req, res) => {
  const randomNumber = Math.floor(Math.random() * 1000) + 1;
  res.send(`Random number: ${randomNumber}`);
});

app.listen(port, () => {
  console.log(`App listening at http://localhost:${port}`);
});
