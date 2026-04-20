import { haversineDistanceMeters } from './geo.js';

export function calculateDistanceMatrix(origins, destinations) {
  if (!origins || !destinations) return [];

  const matrix = [];
  for (let i = 0; i < origins.length; i++) {
    const row = [];
    for (let j = 0; j < destinations.length; j++) {
      const d = haversineDistanceMeters(
        origins[i].lat,
        origins[i].lng,
        destinations[j].lat,
        destinations[j].lng
      );
      row.push(d);
    }
    matrix.push(row);
  }
  return matrix;
}
