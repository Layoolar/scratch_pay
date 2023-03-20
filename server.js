const http = require("http");
const app = require("./app");
const { logger } = require("./documentation/winstonLogger");
require("dotenv").config();

const PORT = process.env.PORT || 3000;

const server = http.createServer(app);

server.listen(PORT, () => {
  logger.info(
    `app is running in ${process.env.STATUS} mode, listening on port ${PORT}`
  );
});
