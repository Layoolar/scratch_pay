const axios = require("axios");
const { mapVetClinicToUnifiedFormat } = require("../utils/vetClinicUtil");
const VET_CLINICS_API_URL = process.env.VET_CLINICS_API_URL;
async function getUnifiedVetClinics() {
  // Get all Vet Clinics
  const response = await axios.get(VET_CLINICS_API_URL);
  const vetClinics = response.data;
  // Map response to the same format
  return vetClinics.map(mapVetClinicToUnifiedFormat);
}

module.exports = {
  getUnifiedVetClinics,
};
