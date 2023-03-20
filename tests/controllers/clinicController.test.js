const { searchClinic } = require("../../src/controllers/clinicController");
const { mergeClinics } = require("../../src/services/clinicService");
const { filterClinics } = require("../../src/utils/clinicSearchUtil");

jest.mock("../../src/services/clinicService");
jest.mock("../../src/utils/clinicSearchUtil");

describe("searchClinic", () => {
  beforeEach(() => {
    jest.resetAllMocks();
  });
  it("should call mergeClinics and filterClinics with the correct arguments and return the result", async () => {
    const req = {
      body: {
        availabilityFrom: "09:00",
        availabilityTo: "17:00",
      },
    };
    const res = {
      json: jest.fn(),
      status: jest.fn().mockReturnThis(),
      send: jest.fn(),
    };
    const mergedClinics = [{ id: 1 }, { id: 2 }];
    const filteredClinics = [{ id: 1 }];
    mergeClinics.mockResolvedValueOnce(mergedClinics);
    filterClinics.mockReturnValueOnce(filteredClinics);

    await searchClinic(req, res);

    expect(mergeClinics).toHaveBeenCalledTimes(1);
    expect(filterClinics).toHaveBeenCalledTimes(1);
    expect(filterClinics).toHaveBeenCalledWith(mergedClinics, req.body);
    expect(res.json).toHaveBeenCalledTimes(1);
    expect(res.json).toHaveBeenCalledWith(filteredClinics);
    expect(res.status).not.toHaveBeenCalled();
    expect(res.send).not.toHaveBeenCalled();
  });

  it("should throw an error and return a 400 status if availabilityFrom is invalid", async () => {
    const req = {
      body: {
        availabilityFrom: "invalid",
      },
    };
    const res = {
      json: jest.fn(),
      status: jest.fn().mockReturnThis(),
      send: jest.fn(),
    };
    await searchClinic(req, res);
    expect(res.status).toHaveBeenCalledWith(400);
    expect(res.send).toHaveBeenCalledWith("Invalid availabilityFrom value");
    expect(res.json).not.toHaveBeenCalled();
  });

  it("should throw an error and return a 400 status if availabilityTo is invalid", async () => {
    const req = {
      body: {
        availabilityTo: "invalid",
      },
    };
    const res = {
      json: jest.fn(),
      status: jest.fn().mockReturnThis(),
      send: jest.fn(),
    };
    await searchClinic(req, res);
    expect(res.status).toHaveBeenCalledWith(400);
    expect(res.send).toHaveBeenCalledWith("Invalid availabilityTo value");
    expect(res.json).not.toHaveBeenCalled();
  });

  it("should not throw an error if availabilityFrom and availabilityTo are not provided", async () => {
    const req = {
      body: {},
    };
    const res = {
      json: jest.fn(),
      status: jest.fn().mockReturnThis(),
      send: jest.fn(),
    };
    const mergedClinics = [{ name: "scratch" }];
    const filteredClinics = [{ name: "scratch" }];
    mergeClinics.mockResolvedValueOnce(mergedClinics);
    filterClinics.mockReturnValueOnce(filteredClinics);

    await searchClinic(req, res);

    expect(mergeClinics).toHaveBeenCalledTimes(1);
    expect(filterClinics).toHaveBeenCalledTimes(1);
    expect(filterClinics).toHaveBeenCalledWith(mergedClinics, req.body);
    expect(res.json).toHaveBeenCalledTimes(1);
    expect(res.json).toHaveBeenCalledWith(filteredClinics);
    expect(res.status).not.toHaveBeenCalled();
    expect(res.send).not.toHaveBeenCalled();
  });
});
