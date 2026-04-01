import React from 'react';

export default function RiskIndicator({ riskTier = 'Low', reason }) {
  const isHigh = riskTier === 'High';
  const isMedium = riskTier === 'Medium';

  const badgeColor = isHigh
    ? 'text-red-400 bg-red-950/40 border-red-800'
    : isMedium
    ? 'text-yellow-400 bg-yellow-950/40 border-yellow-800'
    : 'text-green-400 bg-green-950/40 border-green-800';

  return (
    <div className={`p-3 rounded-lg border text-sm flex items-start gap-2 ${badgeColor}`}>
      <span className="font-semibold uppercase tracking-wider text-xs">Risk: {riskTier}</span>
      {reason && <span className="opacity-80 text-xs">({reason})</span>}
    </div>
  );
}
