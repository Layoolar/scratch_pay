const { mergeClinics } = require("../../src/services/clinicService");
const {
  getUnifiedDentalClinics,
} = require("../../src/services/dentalClinicService");
const { getUnifiedVetClinics } = require("../../src/services/vetClinicService");

// mock the dental and vet clinic services
jest.mock("../../src/services/dentalClinicService");
jest.mock("../../src/services/vetClinicService");

// create sample data to test with
const dentalClinics = [
  {
    name: "Good Health Home",
    state: "Alaska",
    availability: {
      from: "10:00",
      to: "19:30",
    },
  },
  {
    name: "Mayo Clinic",
    state: "Florida",
    availability: {
      from: "09:00",
      to: "20:00",
    },
  },
  {
    name: "Cleveland Clinic",
    state: "New York",
    availability: {
      from: "11:00",
      to: "22:00",
    },
  },
];
const vetClinics = [
  {
    name: "Good Health Home",
    state: "Alaska",
    availability: {
      from: "10:00",
      to: "19:30",
    },
  },
  {
    name: "Mayo Clinic",
    state: "Florida",
    availability: {
      from: "09:00",
      to: "20:00",
    },
  },
  {
    name: "Cleveland Clinic",
    state: "New York",
    availability: {
      from: "11:00",
      to: "22:00",
    },
  },
];
const expectedOutput = [
  {
    name: "Good Health Home",
    state: "Alaska",
    availability: {
      from: "10:00",
      to: "19:30",
    },
  },
  {
    name: "Mayo Clinic",
    state: "Florida",
    availability: {
      from: "09:00",
      to: "20:00",
    },
  },
  {
    name: "Cleveland Clinic",
    state: "New York",
    availability: {
      from: "11:00",
      to: "22:00",
    },
  },
];

describe("mergeClinics", () => {
  beforeEach(() => {
    // reset the mock implementation before each test
    getUnifiedDentalClinics.mockReset();
    getUnifiedVetClinics.mockReset();
  });

  it("mergeClinics should not have any duplicate objects", async () => {
    // set up the mock implementation for the dental and vet clinic services
    getUnifiedDentalClinics.mockResolvedValue(dentalClinics);
    getUnifiedVetClinics.mockResolvedValue(vetClinics);

    // call the function being tested
    const result = await mergeClinics();

    // check that the function returned the expected output
    expect(result).toEqual(expectedOutput);
  });
});
