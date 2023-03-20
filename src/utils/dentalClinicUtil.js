function mapDentalClinicToUnifiedFormat(clinic) {
  return {
    name: clinic.name,
    state: clinic.stateName,
    availability: clinic.availability,
  };
}

module.exports = {
  mapDentalClinicToUnifiedFormat,
};
