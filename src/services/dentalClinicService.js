const axios = require("axios");
const { mapDentalClinicToUnifiedFormat } = require("../utils/dentalClinicUtil");

const DENTAL_CLINICS_API_URL = process.env.DENTAL_CLINICS_API_URL;
async function getUnifiedDentalClinics() {
  // Get all clinics
  const response = await axios.get(DENTAL_CLINICS_API_URL);
  const dentalClinics = response.data;
  // Convert to unified format
  return dentalClinics.map(mapDentalClinicToUnifiedFormat);
}

module.exports = {
  getUnifiedDentalClinics,
};
