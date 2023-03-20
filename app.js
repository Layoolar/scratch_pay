const express = require("express");
const bodyParser = require("body-parser");
const cors = require("cors");
const helmet = require("helmet");
const winston = require("winston");
const expressWinston = require("express-winston");
const swaggerJSDoc = require("swagger-jsdoc");
const swaggerUi = require("swagger-ui-express");
const { logger, newTransport } = require("./documentation/winstonLogger");
const { options } = require("./documentation/swaggerDocumentation");
const app = express();
require("dotenv").config();

// Routes Definition
const clinicRoutes = require("./src/routes/clinicRoute");

// Middlewares
app.use(cors());
app.use(bodyParser.json());
app.use(helmet());

// Documentation and Logging
const swaggerSpec = swaggerJSDoc(options);
app.use("/docs", swaggerUi.serve, swaggerUi.setup(swaggerSpec));
app.use(
  expressWinston.logger({
    transports: [newTransport],
    format: winston.format.combine(
      winston.format.colorize(),
      winston.format.json()
    ),
  })
);

// Routes
app.use("/api/v1", clinicRoutes);

module.exports = app;
