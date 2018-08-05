import boto3
from botocore.client import BaseClient


class CostExplorer:
    """A cost explorer service"""

    def __init__(self, client: BaseClient):
        self.client = client

    def get_cost_and_usage(self, start_date: str, end_date: str) -> dict:
        return self.client.get_cost_and_usage(
            TimePeriod={
                'Start': f"{start_date}",
                'End': f'{end_date}'
            },
            Granularity='DAILY',
            Metrics=['AmortizedCost'],
            GroupBy=[{
                "Type": "DIMENSION",
                "Key": "SERVICE"
            }, {
                "Type": "DIMENSION",
                "Key": "REGION"
            }])


def new_cost_explorer() -> CostExplorer:
    """Constructor for a Cost Explorer"""
    return CostExplorer(boto3.client('ce'))
