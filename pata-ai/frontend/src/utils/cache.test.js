import { describe, it } from 'node:test';
import assert from 'node:assert/strict';
import { GeocodeCache } from './cache.js';

describe('GeocodeCache', () => {
  it('stores and retrieves cached items', () => {
    const cache = new GeocodeCache(5, 10000);
    cache.set('hyd', { lat: 17.38, lon: 78.48 });
    const item = cache.get('hyd');
    assert.equal(item.lat, 17.38);
  });

  it('evicts least recently used item when capacity is reached', () => {
    const cache = new GeocodeCache(2, 10000);
    cache.set('k1', 1);
    cache.set('k2', 2);
    cache.set('k3', 3); // should evict k1
    assert.equal(cache.get('k1'), null);
    assert.equal(cache.get('k2'), 2);
    assert.equal(cache.get('k3'), 3);
  });

  it('clears all items', () => {
    const cache = new GeocodeCache();
    cache.set('a', 1);
    cache.clear();
    assert.equal(cache.get('a'), null);
  });
});
