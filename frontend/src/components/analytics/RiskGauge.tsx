import { RadialBar, RadialBarChart, ResponsiveContainer, Tooltip, PolarAngleAxis } from 'recharts'
import { chartTheme, formatTooltipValue } from '../../theme'

type RiskGaugeProps = {
  riskLevel: string
  height?: number
}

function percentAndColor(riskLevel: string): { percent: number; color: string; label: string; icon: string } {
  const normalized = riskLevel.toLowerCase()
  if (normalized === 'low') return { percent: 25, color: chartTheme.semantic.healthy, label: 'Low', icon: '🟢' }
  if (normalized === 'medium') return { percent: 55, color: chartTheme.semantic.moderate, label: 'Medium', icon: '🟡' }
  if (normalized === 'high') return { percent: 90, color: chartTheme.semantic.critical, label: 'High', icon: '🔴' }
  return { percent: 0, color: chartTheme.text.muted, label: 'Unknown', icon: '⚪' }
}

export function RiskGauge({ riskLevel, height = 220 }: RiskGaugeProps) {
  const { percent, color, label, icon } = percentAndColor(riskLevel)
  const data = [{ name: 'Risk', value: percent }]

  return (
    <div className="w-full rounded-2xl border border-white/10 bg-[rgba(20,25,30,0.6)] backdrop-blur-xl p-6 shadow-[0_20px_60px_rgba(0,0,0,0.3)] transition-all duration-300 hover:shadow-[0_30px_80px_rgba(239,68,68,0.1)]">
      <div className="mb-4 text-xs font-medium uppercase tracking-[0.18em] text-white/60">
        Flame risk level
      </div>
      <div style={{ height }} className="relative w-full">
        <ResponsiveContainer width="100%" height="100%">
          <RadialBarChart
            innerRadius="70%"
            outerRadius="100%"
            startAngle={225}
            endAngle={-45}
            data={data}
          >
            <PolarAngleAxis type="number" domain={[0, 100]} tick={false} />
            <RadialBar
              dataKey="value"
              cornerRadius={8}
              background={{ fill: 'rgba(255,255,255,0.05)' }}
              fill={color}
              isAnimationActive={true}
              animationDuration={600}
              animationEasing="ease-out"
            />
            <Tooltip
              formatter={(value: unknown) => [
                typeof value === 'number' && Number.isFinite(value) ? `${formatTooltipValue(value, { decimals: 0 })}%` : '–',
                'Flame Risk',
              ]}
              contentStyle={{
                backgroundColor: chartTheme.tooltip.bg,
                border: `1px solid ${chartTheme.tooltip.border}`,
                borderRadius: 8,
                fontSize: 12,
                backdropFilter: 'blur(8px)',
              }}
              labelStyle={{ display: 'none' }}
            />
          </RadialBarChart>
        </ResponsiveContainer>
        <div className="absolute inset-0 flex flex-col items-center justify-center pointer-events-none">
          <div className="flex items-center gap-2">
            <span className="text-2xl">{icon}</span>
            <span className="text-2xl font-bold text-white">{label}</span>
          </div>
        </div>
      </div>
      <div className="mt-4 flex justify-center gap-6 text-[10px] text-white/50">
        <span className="flex items-center gap-1">
          <div className="w-2 h-2 rounded-full bg-emerald-500"></div>
          Low risk
        </span>
        <span className="flex items-center gap-1">
          <div className="w-2 h-2 rounded-full bg-amber-500"></div>
          Medium risk
        </span>
        <span className="flex items-center gap-1">
          <div className="w-2 h-2 rounded-full bg-red-500"></div>
          High risk
        </span>
      </div>
    </div>
  )
}
