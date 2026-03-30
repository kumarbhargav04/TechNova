import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import { formatPincode, truncateCoordinate, toTitleCase } from './formatters.js';

describe('Formatters', () => {
  it('formatPincode formats 6 digits with space', () => {
    assert.equal(formatPincode('500035'), '500 035');
  });

  it('truncateCoordinate truncates to given precision', () => {
    assert.equal(truncateCoordinate(17.38501234, 4), 17.385);
  });

  it('toTitleCase normalizes casing', () => {
    assert.equal(toTitleCase('bAnJaRa hiLLs'), 'Banjara Hills');
  });
});
