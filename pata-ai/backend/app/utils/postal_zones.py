POSTAL_ZONES = {
    "1": "Northern (Delhi, Haryana, Punjab, HP, J&K)",
    "2": "Northern (UP, Uttarakhand)",
    "3": "Western (Rajasthan, Gujarat)",
    "4": "Western (Maharashtra, Goa, MP, Chhattisgarh)",
    "5": "Southern (Andhra Pradesh, Telangana, Karnataka)",
    "6": "Southern (Tamil Nadu, Kerala)",
    "7": "Eastern (West Bengal, Odisha, North Eastern)",
    "8": "Eastern (Bihar, Jharkhand)",
    "9": "Army Postal Service (APS)"
}

def get_postal_zone_name(pincode: str) -> str:
    if not pincode or len(pincode) != 6 or not pincode.isdigit():
        return "Unknown Postal Zone"
    return POSTAL_ZONES.get(pincode[0], "Unknown Postal Zone")
