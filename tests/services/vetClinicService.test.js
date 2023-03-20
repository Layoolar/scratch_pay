const { getUnifiedVetClinics } = require("../../src/services/vetClinicService");
const {
  mapVetClinicToUnifiedFormat,
} = require("../../src/utils/vetClinicUtil");
const axios = require("axios");

jest.mock("axios");

describe("Vet Clinic Service", () => {
  it("should return unified vet clinics", async () => {
    const mockResponse = {
      data: [
        {
          clinicName: "Good Health Home",
          stateCode: "FL",
          opening: {
            from: "15:00",
            to: "20:00",
          },
        },
        {
          clinicName: "National Veterinary Clinic",
          stateCode: "CA",
          opening: {
            from: "15:00",
            to: "22:30",
          },
        },
        {
          clinicName: "German Pets Clinics",
          stateCode: "KS",
          opening: {
            from: "08:00",
            to: "20:00",
          },
        },
        {
          clinicName: "City Vet Clinic",
          stateCode: "NV",
          opening: {
            from: "10:00",
            to: "22:00",
          },
        },
        {
          clinicName: "Scratchpay Test Pet Medical Center",
          stateCode: "CA",
          opening: {
            from: "00:00",
            to: "24:00",
          },
        },
      ],
    };

    const expectedClinics = mockResponse.data.map(mapVetClinicToUnifiedFormat);

    axios.get.mockResolvedValue(mockResponse);

    const actualClinics = await getUnifiedVetClinics();

    expect(actualClinics).toEqual(expectedClinics);
  });
});
