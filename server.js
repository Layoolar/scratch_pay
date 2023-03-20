const http = require("http");

const { logger } = require("./documentation/winstonLogger");
require("dotenv").config();

const PORT = process.env.PORT || 3000;

const server = http.createServer();

server.listen(PORT, () => {
  logger.info(
    `app is running in ${process.env.STATUS} mode, listening on port ${PORT}`
  );
});
