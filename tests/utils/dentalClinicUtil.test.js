const {
  mapDentalClinicToUnifiedFormat,
} = require("../../src/utils/dentalClinicUtil");

describe("mapDentalClinicToUnifiedFormat function", () => {
  test("maps a dental clinic to a unified format", () => {
    const clinic = {
      name: "Sunshine Dental",
      stateName: "California",
      availability: {
        from: "09:00",
        to: "17:00",
      },
    };

    const expected = {
      name: "Sunshine Dental",
      state: "California",
      availability: {
        from: "09:00",
        to: "17:00",
      },
    };

    const actual = mapDentalClinicToUnifiedFormat(clinic);
    expect(actual).toEqual(expected);
  });
});
