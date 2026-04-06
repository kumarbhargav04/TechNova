import React from 'react';

export default function MetricCard({ label, value, subtext, trend }) {
  return (
    <div className="bg-slate-900/60 border border-slate-800 rounded-xl p-4 flex flex-col justify-between">
      <span className="text-xs font-medium text-slate-400 uppercase tracking-wider">{label}</span>
      <div className="my-2 flex items-baseline gap-2">
        <span className="text-2xl font-bold text-white tracking-tight">{value}</span>
        {trend && (
          <span className="text-xs text-emerald-400 font-medium">+{trend}%</span>
        )}
      </div>
      {subtext && <span className="text-xs text-slate-500">{subtext}</span>}
    </div>
  );
}
