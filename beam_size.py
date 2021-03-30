def beam_size(wavelength, diameter):
    """Input: 
	Wavelength: wavelength of the EM wave in meters
	Diameter: Diameter of the radio telescope in meters 
	Returns:
	FMWH of the primary beam in radians """
    return: 1.02 * (wavelength / diameter)
