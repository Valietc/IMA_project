import matplotlib.pyplot as plt

def plot_ipr_curve(well, pressures):
    rates = [well.calculate_flow_rate(p) for p in pressures]
    plt.plot(pressures, rates, marker='o')
    plt.xlabel("Bottomhole Pressure (psia)")
    plt.ylabel("Flow Rate (STB/day)")
    plt.title("IPR Curve")
    plt.grid(True)
    plt.show()
