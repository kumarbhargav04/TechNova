/**
 * Validates raw Indian address input before pipeline submission.
 */
export function validateAddressInput(text) {
  if (!text || typeof text !== 'string') {
    return { valid: false, error: 'Address input must be a non-empty string.' };
  }

  const trimmed = text.trim();
  if (trimmed.length < 5) {
    return { valid: false, error: 'Address is too short (min 5 characters).' };
  }

  if (trimmed.length > 500) {
    return { valid: false, error: 'Address exceeds maximum allowed length of 500 characters.' };
  }

  const hasLetter = /[a-zA-Z]/.test(trimmed);
  if (!hasLetter) {
    return { valid: false, error: 'Address must contain alphabetical descriptive characters.' };
  }

  return { valid: true, error: null, sanitized: trimmed };
}
