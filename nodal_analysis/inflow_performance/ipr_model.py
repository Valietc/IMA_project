class WellInflow: 
    def __init__(self, productivity_index: float, reservoir_pressure: float, accumulated_production: float = 0) -> None:
        self.productivity_index = productivity_index
        self.reservoir_pressure = reservoir_pressure
        self.accumulated_production = accumulated_production

    def calculate_flow_rate(self, bottomhole_pressure: float) -> float:
        if bottomhole_pressure > self.reservoir_pressure:
            raise ValueError("Забойное давление не может превышать пластового давления.")
        flow_rate = self.productivity_index * (self.reservoir_pressure - bottomhole_pressure)
        self.accumulated_production += flow_rate
        return flow_rate

    def __str__(self) -> str:
        return (f"WellInflow(productivity_index={self.productivity_index}, "
                f"reservoir_pressure={self.reservoir_pressure}, "
                f"accumulated_production={self.accumulated_production})")

class InvertedWell(WellInflow):
    def __call__(self, flow_rate: float) -> float:
        if flow_rate < 0:
            raise ValueError("Дебит не может быть отрицательным.")
        bottomhole_pressure = self.reservoir_pressure - flow_rate / self.productivity_index
        if bottomhole_pressure < 0:
            raise ValueError("Забойное давление не может быть отрицательным.")
        self.accumulated_production += flow_rate
        return bottomhole_pressure
