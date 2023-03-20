const request = require("supertest");
const app = require("../../app");

describe("Clinic Search", () => {
  it("should respond with a list of clinics for a valid query", async () => {
    const response = await request(app)
      .post("/api/v1/search")
      .send({
        name: "Scratchpay",
        state: "California",
        availableFrom: "01:00",
        availableTo: "23:00",
      })
      .set("Accept", "application/json")
      .expect("Content-Type", /json/)
      .expect(200);

    const clinics = response.body;

    expect(Array.isArray(clinics)).toBe(true);
    expect(clinics[0]).toHaveProperty("name");
    expect(clinics[0]).toHaveProperty("state");
    expect(clinics[0]).toHaveProperty("availability");
    expect(clinics[0].availability).toHaveProperty("from");
    expect(clinics[0].availability).toHaveProperty("to");
  });

  it("should return an empty list for an invalid search query", async () => {
    const response = await request(app)
      .post("/api/v1/search")
      .send({
        name: "Scratch",
        state: "CA",
        availablilityFrom: "26:30",
        availabilityTo: "27:59", // Invalid time
      })
      .expect(400);

    const clinics = response.body;

    console.log(clinics);
  });

  it("should respond with a list of clinics for a valid query", async () => {
    const response = await request(app)
      .post("/api/v1/search")
      .send({
        name: "Non Existent", // Non existing name
        state: "Invalid", // Invalid State
        availableFrom: "01:00",
        availableTo: "26:00",
      })
      .set("Accept", "application/json")
      .expect("Content-Type", /json/)
      .expect(200);

    const clinics = response.body;

    expect(clinics.length).toBe(0);
  });
});
