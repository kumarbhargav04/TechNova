import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import { validateAddressInput } from './addressValidator.js';

describe('validateAddressInput', () => {
  it('should accept standard valid address', () => {
    const res = validateAddressInput('Plot 40, Road No 2, Banjara Hills, 500034');
    assert.equal(res.valid, true);
    assert.equal(res.error, null);
  });

  it('should reject empty or null inputs', () => {
    assert.equal(validateAddressInput('').valid, false);
    assert.equal(validateAddressInput(null).valid, false);
  });

  it('should reject excessively short inputs', () => {
    const res = validateAddressInput('Hyd');
    assert.equal(res.valid, false);
  });

  it('should reject inputs without alphabetic characters', () => {
    const res = validateAddressInput('123456 7890');
    assert.equal(res.valid, false);
  });
});
