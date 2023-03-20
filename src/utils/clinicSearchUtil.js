const stateNames = require("../constants/states");

function filterClinics(unifiedClinics, searchParams) {
  let { name, state, availabilityFrom, availabilityTo } = searchParams;

  // Handle Searches with state codes
  if (stateNames[state]) {
    state = stateNames[state];
  }

  const filteredClinics = unifiedClinics.filter((clinic) => {
    // Check if the clinic name matches the search term
    if (name && clinic.name.toLowerCase().indexOf(name.toLowerCase()) === -1) {
      return false;
    }

    // Check if the clinic state matches the search term
    if (
      state &&
      clinic.state.toLowerCase().indexOf(state.toLowerCase()) === -1
    ) {
      return false;
    }

    // Check if the clinic availability matches the search term
    if (availabilityTo || availabilityFrom) {
      const clinicAvailability = clinic.availability;
      const from = clinicAvailability.from.split(":").join("");
      const to = clinicAvailability.to.split(":").join("");

      // Check if the clinic availability overlaps with the search availability
      if (availabilityFrom && availabilityTo) {
        let searchFrom = availabilityFrom.split(":").join("");
        let searchTo = availabilityTo.split(":").join("");

        if (
          parseInt(from) > parseInt(searchFrom) ||
          parseInt(to) < parseInt(searchTo)
        ) {
          return false;
        }
      } else if (availabilityFrom) {
        let searchFrom = availabilityFrom.split(":").join("");

        if (parseInt(to) <= parseInt(searchFrom)) {
          return false;
        }
      } else if (availabilityTo) {
        let searchTo = availabilityTo.split(":").join("");

        if (parseInt(to) <= parseInt(searchTo)) {
          return false;
        }
      }
    }

    // If all search terms match, include the clinic in the search results
    return true;
  });

  return filteredClinics.map((clinic) => ({
    name: clinic.name,
    state: clinic.state,
    availability: clinic.availability,
  }));
}

module.exports = {
  filterClinics,
};
