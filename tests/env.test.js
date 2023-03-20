require("dotenv").config();

describe("Environment variables", () => {
  test("DENTAL_CLINICS_API_URL should be defined and a valid URL", () => {
    expect(process.env.DENTAL_CLINICS_API_URL).toBeDefined();
    expect(process.env.DENTAL_CLINICS_API_URL).toMatch(
      /^https?:\/\/[\w-]+(\.[\w-]+)+([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?$/
    );
  });

  test("VET_CLINICS_API_URL should be defined and a valid URL", () => {
    expect(process.env.VET_CLINICS_API_URL).toBeDefined();
    expect(process.env.VET_CLINICS_API_URL).toMatch(
      /^https?:\/\/[\w-]+(\.[\w-]+)+([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?$/
    );
  });

  test("STATUS should be defined", () => {
    expect(process.env.STATUS).toBeDefined();
  });

  test("PROD_PORT should be defined if STATUS is set to production", () => {
    if (process.env.STATUS === "production") {
      expect(process.env.PORT).toBeDefined();
    }
  });
});
