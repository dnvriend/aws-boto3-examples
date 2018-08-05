from __future__ import annotations

import boto3
from botocore.client import BaseClient


class CostExplorer:
    """An AWS cost explorer service"""

    def __init__(self, client: BaseClient):
        self.client = client

    @classmethod
    def new_instance(cls) -> CostExplorer:
        """Returns a new instance of the cost explorer"""
        return CostExplorer(boto3.client('ce'))

    def get_cost_and_usage(self, start_date: str, end_date: str) -> dict:
        """calculates cost and usage based on DAILY granularity, and AmortizedCost metrics"""
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
