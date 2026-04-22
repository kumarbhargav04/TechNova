export const METRO_PINCODE_CENTROIDS = {
  '500001': { city: 'Hyderabad', state: 'Telangana', lat: 17.385, lng: 78.4867 },
  '560001': { city: 'Bengaluru', state: 'Karnataka', lat: 12.9716, lng: 77.5946 },
  '110001': { city: 'New Delhi', state: 'Delhi', lat: 28.6139, lng: 77.209 },
  '400001': { city: 'Mumbai', state: 'Maharashtra', lat: 18.9322, lng: 72.8347 },
};

export function lookupMetroPincode(pincode) {
  const p = String(pincode).trim();
  return METRO_PINCODE_CENTROIDS[p] || null;
}
