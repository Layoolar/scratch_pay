const swaggerDefinition = {
  openapi: "3.0.0",
  info: {
    title: "Express API for clinic search",
    version: "1.0.0",
    description:
      "This API recieves parameter and search for clinics available matching the parameters.",
    license: {
      name: "Licensed Under MIT",
      url: "https://spdx.org/licenses/MIT.html",
    },
  },
  servers: [
    {
      url: "http://localhost:5000/api/v1",
      description: "Development server",
    },
  ],
};

const options = {
  swaggerDefinition,
  // Paths to files containing OpenAPI definitions
  apis: ["./src/routes/*.js"],
  swaggerOptions: {
    tryItOutEnabled: false,
  },
};

module.exports = {
  options,
};
