const { getUnifiedDentalClinics } = require("./dentalClinicService");
const { getUnifiedVetClinics } = require("./vetClinicService");

async function mergeClinics() {
  // Get both Vet and Dental clinics in unified format
  const [dentalClinics, vetClinics] = await Promise.all([
    getUnifiedDentalClinics(),
    getUnifiedVetClinics(),
  ]);

  // Remove duplicates in file
  const unifiedClinics = [
    ...new Set(
      [...dentalClinics, ...vetClinics].map((clinic) => JSON.stringify(clinic))
    ),
  ].map((clinic) => JSON.parse(clinic));
  return unifiedClinics;
}

module.exports = {
  mergeClinics,
};
