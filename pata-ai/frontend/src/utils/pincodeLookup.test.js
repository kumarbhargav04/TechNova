import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import { lookupMetroPincode } from './pincodeLookup.js';

describe('pincodeLookup module', () => {
  it('resolves Hyderabad central pincode', () => {
    const res = lookupMetroPincode('500001');
    assert.ok(res);
    assert.equal(res.city, 'Hyderabad');
  });

  it('returns null for unknown pincode', () => {
    assert.equal(lookupMetroPincode('999999'), null);
  });
});
