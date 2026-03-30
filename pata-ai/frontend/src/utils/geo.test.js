import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import { haversineDistanceMeters, isWithinBoundingBox } from './geo.js';

describe('Geo Utilities', () => {
  it('haversineDistanceMeters should calculate accurate zero distance', () => {
    assert.equal(haversineDistanceMeters(17.385, 78.486, 17.385, 78.486), 0);
  });

  it('haversineDistanceMeters should calculate approx distance', () => {
    const d = haversineDistanceMeters(17.385, 78.486, 17.439, 78.498);
    assert.ok(d > 6000 && d < 10000);
  });

  it('isWithinBoundingBox should identify inside points', () => {
    const bounds = { minLat: 17.0, maxLat: 18.0, minLon: 78.0, maxLon: 79.0 };
    assert.equal(isWithinBoundingBox(17.5, 78.5, bounds), true);
    assert.equal(isWithinBoundingBox(19.0, 78.5, bounds), false);
  });
});
