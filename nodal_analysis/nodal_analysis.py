from .inflow_performance import WellInflow, InvertedWell

def run_analysis():
    inflow = WellInflow(productivity_index=0.8, reservoir_pressure=3000)
    q1 = inflow.calculate_flow_rate(2500)
    q2 = inflow.calculate_flow_rate(2000)

    print(f"Flow rate 1: {q1}, accumulated: {inflow.accumulated_production}")
    print(f"Flow rate 2: {q2}, accumulated: {inflow.accumulated_production}")

    inv = InvertedWell(productivity_index=1.2, reservoir_pressure=3500)
    pwf1 = inv(500)
    pwf2 = inv(800)

    print(f"Bottomhole 1: {pwf1}, accumulated: {inv.accumulated_production}")
    print(f"Bottomhole 2: {pwf2}, accumulated: {inv.accumulated_production}")
