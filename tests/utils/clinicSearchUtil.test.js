const { filterClinics } = require("../../src/utils/clinicSearchUtil");

describe("filterClinics", () => {
  const mockClinics = [
    {
      name: "ABC Animal Hospital",
      state: "California",
      availability: {
        from: "09:00",
        to: "17:00",
      },
    },
    {
      name: "XYZ Pet Clinic",
      state: "New York",
      availability: {
        from: "08:30",
        to: "16:30",
      },
    },
    {
      name: "Pet Emergency Center",
      state: "California",
      availability: {
        from: "00:00",
        to: "23:59",
      },
    },
  ];

  it("should return clinics that match name search term", () => {
    const searchParams = {
      name: "ABC",
    };
    const expected = [
      {
        name: "ABC Animal Hospital",
        state: "California",
        availability: {
          from: "09:00",
          to: "17:00",
        },
      },
    ];
    const result = filterClinics(mockClinics, searchParams);
    expect(result).toEqual(expected);
  });

  it("should return clinics that match state search term", () => {
    const searchParams = {
      state: "New York",
    };
    const expected = [
      {
        name: "XYZ Pet Clinic",
        state: "New York",
        availability: {
          from: "08:30",
          to: "16:30",
        },
      },
    ];
    const result = filterClinics(mockClinics, searchParams);
    expect(result).toEqual(expected);
  });

  it("should return clinics even when state codes are used", () => {
    const searchParams = {
      state: "NY",
    };
    const expected = [
      {
        name: "XYZ Pet Clinic",
        state: "New York",
        availability: {
          from: "08:30",
          to: "16:30",
        },
      },
    ];
    const result = filterClinics(mockClinics, searchParams);
    expect(result).toEqual(expected);
  });

  it("should return clinics that match availability search term", () => {
    const searchParams = {
      availabilityFrom: "22:00",
      availabilityTo: "23:59",
    };
    const expected = [
      {
        name: "Pet Emergency Center",
        state: "California",
        availability: {
          from: "00:00",
          to: "23:59",
        },
      },
    ];
    const result = filterClinics(mockClinics, searchParams);
    expect(result).toEqual(expected);
  });

  it("should return clinics that match both name and state search terms", () => {
    const searchParams = {
      name: "Animal",
      state: "California",
    };
    const expected = [
      {
        name: "ABC Animal Hospital",
        state: "California",
        availability: {
          from: "09:00",
          to: "17:00",
        },
      },
    ];
    const result = filterClinics(mockClinics, searchParams);
    expect(result).toEqual(expected);
  });

  it("should return clinics that match both name and availability search terms", () => {
    const searchParams = {
      name: "Pet",
      availabilityFrom: "01:00",
      availabilityTo: "23:59",
    };
    const expected = [
      {
        name: "Pet Emergency Center",
        state: "California",
        availability: { from: "00:00", to: "23:59" },
      },
    ];
    const result = filterClinics(mockClinics, searchParams);
    expect(result).toEqual(expected);
  });

  it("should return clinics that match both state and availability search terms", () => {
    const searchParams = {
      state: "New York",
      availabilityFrom: "09:00",
      availabilityTo: "11:00",
    };
    const expected = [
      {
        name: "XYZ Pet Clinic",
        state: "New York",
        availability: {
          from: "08:30",
          to: "16:30",
        },
      },
    ];
    const result = filterClinics(mockClinics, searchParams);
    expect(result).toEqual(expected);
  });

  it("should return clinics that match all name, state and availability search terms", () => {
    const searchParams = {
      name: "XYZ",
      state: "New York",
      availabilityFrom: "09:00",
      availabilityTo: "11:00",
    };
    const expected = [
      {
        name: "XYZ Pet Clinic",
        state: "New York",
        availability: {
          from: "08:30",
          to: "16:30",
        },
      },
    ];
    const result = filterClinics(mockClinics, searchParams);
    expect(result).toEqual(expected);
  });

  it("should return clinics that match availabilityFrom search term", () => {
    const searchParams = {
      availabilityFrom: "22:00",
    };
    const expected = [
      {
        name: "Pet Emergency Center",
        state: "California",
        availability: {
          from: "00:00",
          to: "23:59",
        },
      },
    ];
    const result = filterClinics(mockClinics, searchParams);
    expect(result).toEqual(expected);
  });

  it("should return clinics that match availabilityFrom search term", () => {
    const searchParams = {
      availabilityTo: "21:00",
    };
    const expected = [
      {
        name: "Pet Emergency Center",
        state: "California",
        availability: {
          from: "00:00",
          to: "23:59",
        },
      },
    ];
    const result = filterClinics(mockClinics, searchParams);
    expect(result).toEqual(expected);
  });

  it("should return clinics that match name, state, and availabilityFrom search terms", () => {
    const searchParams = {
      name: "Pet",
      state: "California",
      availabilityFrom: "22:00",
    };
    const expected = [
      {
        name: "Pet Emergency Center",
        state: "California",
        availability: {
          from: "00:00",
          to: "23:59",
        },
      },
    ];
    const result = filterClinics(mockClinics, searchParams);
    expect(result).toEqual(expected);
  });

  it("should return clinics that match name, state, and availabilityTo search terms", () => {
    const searchParams = {
      name: "Pet",
      state: "California",
      availabilityTo: "22:00",
    };
    const expected = [
      {
        name: "Pet Emergency Center",
        state: "California",
        availability: {
          from: "00:00",
          to: "23:59",
        },
      },
    ];
    const result = filterClinics(mockClinics, searchParams);
    expect(result).toEqual(expected);
  });
});
