const stateNames = require("../constants/states");
function mapVetClinicToUnifiedFormat(clinic) {
  let state = clinic.stateCode;
  // Convert state name to state code if it exists
  if (stateNames[state]) {
    state = stateNames[state];
  }
  return {
    name: clinic.clinicName,
    state,
    availability: {
      from: clinic.opening.from,
      to: clinic.opening.to,
    },
  };
}

module.exports = {
  mapVetClinicToUnifiedFormat,
};
