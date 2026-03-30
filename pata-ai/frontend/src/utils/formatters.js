/**
 * Text formatting helpers for Indian address display.
 */
export function formatPincode(pincode) {
  if (!pincode) return '';
  const digits = String(pincode).replace(/\D/g, '');
  if (digits.length === 6) {
    return `${digits.slice(0, 3)} ${digits.slice(3)}`;
  }
  return digits;
}

export function truncateCoordinate(coord, decimals = 5) {
  if (typeof coord !== 'number' || isNaN(coord)) return 0;
  return Number(coord.toFixed(decimals));
}

export function toTitleCase(str) {
  if (!str) return '';
  return str
    .toLowerCase()
    .split(' ')
    .map(word => word.charAt(0).toUpperCase() + word.slice(1))
    .join(' ');
}
