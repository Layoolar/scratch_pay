const winston = require("winston");
const DailyRotateFile = require("winston-daily-rotate-file");

const { combine, timestamp, label, printf } = winston.format;

const myFormat = printf(({ level, message, label, timestamp }) => {
  return `${timestamp} [${label}] ${level}: ${message}`;
});

const errorTransport = new DailyRotateFile({
  filename: "logs/error-%DATE%.log",
  level: "error",
  handleExceptions: true,
  maxFiles: "30d",
  zippedArchive: true,
  maxSize: "20m",
  format: combine(label({ label: "clinic-api" }), timestamp(), myFormat),
});

const infoTransport = new DailyRotateFile({
  filename: "logs/info-%DATE%.log",
  level: "info",
  maxFiles: "30d",
  zippedArchive: true,
  maxSize: "20m",
  format: combine(label({ label: "clinic-api" }), timestamp(), myFormat),
});

const logger = winston.createLogger({
  level: "info",
  transports: [errorTransport, infoTransport],
});

if (process.env.NODE_ENV !== "production") {
  logger.add(
    new winston.transports.Console({
      format: winston.format.simple(),
    })
  );
}

const newTransport = new DailyRotateFile({
  filename: "logs/access-%DATE%.log",
  level: "info",
  maxFiles: "30d",
  zippedArchive: true,
  maxSize: "20m",
  format: combine(winston.format.colorize(), winston.format.json()),
});

module.exports = {
  logger,
  errorTransport,
  infoTransport,
  newTransport,
};
