const { mergeClinics } = require("../services/clinicService");
const { filterClinics } = require("../utils/clinicSearchUtil");

async function searchClinic(req, res) {
  try {
    // Check if availabilityFrom and availabilityTo are within the valid time range
    const { availabilityFrom, availabilityTo } = req.body;
    if (
      availabilityFrom &&
      (availabilityFrom < "00:00" || availabilityFrom > "23:59")
    ) {
      throw new Error("Invalid availabilityFrom value");
    }
    if (
      availabilityTo &&
      (availabilityTo < "00:00" || availabilityTo > "23:59")
    ) {
      throw new Error("Invalid availabilityTo value");
    }

    const mergedClinics = await mergeClinics();
    const clinics = filterClinics(mergedClinics, req.body);
    res.json(clinics);
  } catch (err) {
    console.error(err);
    res.status(400).send(err.message);
  }
}

module.exports = {
  searchClinic,
};
