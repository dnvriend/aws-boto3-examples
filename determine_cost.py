from examples.ce.cost_explorer import CostExplorer
from datetime import date, timedelta


def determine_cost(client: CostExplorer) -> None:
    total: float = 0
    today: date = date.today()
    yesterday: date = today - timedelta(days=1)
    for result in client.get_cost_and_usage(yesterday.isoformat(),
                                            today.isoformat()).get('ResultsByTime'):
        sub_total: float = 0
        start = result.get('TimePeriod').get('Start')
        end = result.get('TimePeriod').get('End')
        print(f"from: {start} - {end}")
        for group in result.get('Groups'):
            cost = group.get('Metrics').get('AmortizedCost').get('Amount')
            if cost != "0":
                total += float(cost)
                sub_total += float(cost)
                service_name = group.get('Keys')[0]
                region_name = group.get('Keys')[1]
                print(f" --> {service_name} -> {region_name} -> {cost}")
        print(f" --> total: {sub_total}")

    print("=========================================")
    print(f"total: {total}")


if __name__ == "__main__":
    determine_cost(CostExplorer.new_instance())
