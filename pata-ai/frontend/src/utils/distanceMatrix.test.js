import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import { calculateDistanceMatrix } from './distanceMatrix.js';

describe('distanceMatrix module', () => {
  it('calculates 2x2 distance matrix', () => {
    const o = [{ lat: 17.38, lng: 78.48 }];
    const d = [{ lat: 17.38, lng: 78.48 }, { lat: 17.43, lng: 78.49 }];
    const mat = calculateDistanceMatrix(o, d);
    assert.equal(mat.length, 1);
    assert.equal(mat[0].length, 2);
    assert.equal(mat[0][0], 0);
    assert.ok(mat[0][1] > 0);
  });
});
