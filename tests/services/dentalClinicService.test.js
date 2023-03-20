const axios = require("axios");
const {
  getUnifiedDentalClinics,
} = require("../../src/services/dentalClinicService");
const {
  mapDentalClinicToUnifiedFormat,
} = require("../../src/utils/dentalClinicUtil");

jest.mock("axios");

describe("Dental clinic service", () => {
  test("getUnifiedDentalClinics returns dental clinics in unified format", async () => {
    const mockResponse = {
      data: [
        {
          name: "Good Health Home",
          stateName: "Alaska",
          availability: {
            from: "10:00",
            to: "19:30",
          },
        },
        {
          name: "Mayo Clinic",
          stateName: "Florida",
          availability: {
            from: "09:00",
            to: "20:00",
          },
        },
      ],
    };

    const expectedClinics = mockResponse.data.map(
      mapDentalClinicToUnifiedFormat
    );

    axios.get.mockResolvedValue(mockResponse);

    const actualClinics = await getUnifiedDentalClinics();

    expect(actualClinics).toEqual(expectedClinics);
  });
});
