export interface GeocodeCandidate {
  name: string;
  latitude: number;
  longitude: number;
  confidence: number;
  type: string;
  source?: string;
  evidence: string[];
}

export interface PipelineExecutionResult {
  query: string;
  pincode?: string;
  topCandidate?: GeocodeCandidate;
  candidates: GeocodeCandidate[];
  latencyMs: number;
  riskTier: 'Low' | 'Medium' | 'High';
}
