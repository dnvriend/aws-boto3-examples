from examples.ce.cost_explorer import CostExplorer


def determine_cost(client: CostExplorer) -> None:
    total: float = 0
    for result in client.get_cost_and_usage("2018-08-01",
                                            "2018-08-05").get('ResultsByTime'):
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
