const {
  mapVetClinicToUnifiedFormat,
} = require("../../src/utils/vetClinicUtil");

const stateNames = require("../../src/constants/states");

describe("mapVetClinicToUnifiedFormat function", () => {
  test("maps vet clinic data to unified format", () => {
    const clinic = {
      clinicName: "ABC Veterinary Clinic",
      stateCode: "CA",
      opening: {
        from: "09:00",
        to: "17:00",
      },
    };
    const expected = {
      name: "ABC Veterinary Clinic",
      state: stateNames["CA"],
      availability: {
        from: "09:00",
        to: "17:00",
      },
    };
    expect(mapVetClinicToUnifiedFormat(clinic)).toEqual(expected);
  });

  test("handles missing state name conversion gracefully", () => {
    const clinic = {
      clinicName: "XYZ Veterinary Clinic",
      stateCode: "AB", // invalid state code
      opening: {
        from: "09:00",
        to: "17:00",
      },
    };
    const expected = {
      name: "XYZ Veterinary Clinic",
      state: "AB", // should remain the same
      availability: {
        from: "09:00",
        to: "17:00",
      },
    };
    expect(mapVetClinicToUnifiedFormat(clinic)).toEqual(expected);
  });
});
