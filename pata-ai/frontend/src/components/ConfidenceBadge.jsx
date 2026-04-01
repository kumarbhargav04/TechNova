import React from 'react';

export default function ConfidenceBadge({ score }) {
  const numScore = Number(score) || 0;

  let bgClass = 'bg-emerald-500/10 text-emerald-400 border-emerald-500/20';
  let label = 'High Confidence';

  if (numScore < 50) {
    bgClass = 'bg-rose-500/10 text-rose-400 border-rose-500/20';
    label = 'Low Confidence';
  } else if (numScore < 75) {
    bgClass = 'bg-amber-500/10 text-amber-400 border-amber-500/20';
    label = 'Medium Confidence';
  }

  return (
    <span
      className={`inline-flex items-center gap-1.5 px-2.5 py-1 rounded-full text-xs font-medium border ${bgClass}`}
      role="status"
      aria-label={`Confidence score: ${numScore}% (${label})`}
    >
      <span className="w-1.5 h-1.5 rounded-full bg-current animate-pulse" />
      {numScore}% - {label}
    </span>
  );
}
