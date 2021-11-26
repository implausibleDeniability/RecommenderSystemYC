import pandas as pd


class MovingAverage:
    """Exponential moving average"""

    def __init__(self, momentum, initial_value=0):
        assert 0.0 < momentum <= 1.0
        self.momentum = momentum
        self.moving_average = initial_value

    def add(self, new_value):
        self.moving_average = (
            self.moving_average * (1 - self.momentum) + new_value * self.momentum
        )

    def value(
        self,
    ):
        return self.moving_average

    def __str__(
        self,
    ):
        return str(self.moving_average)


def convert_ids_to_ordered(
    users: pd.DataFrame, organizations: pd.DataFrame, reviews: pd.DataFrame
) -> tuple:
    """Takes three dataframes with unordered sparse IDs
    and builds the same dataframes with ordered IDs without spaces
    """
    ordered_users = users.copy()
    ordered_users["ordered_id"] = range(len(ordered_users))
    ordered_organizations = organizations.copy()
    ordered_organizations["ordered_id"] = range(len(ordered_organizations))
    ordered_reviews = reviews.join(ordered_users[["ordered_id"]], on="user_id").join(
        ordered_organizations[["ordered_id"]],
        on="org_id",
        lsuffix="_user",
        rsuffix="_org",
    )
    ordered_reviews = ordered_reviews.drop(["user_id", "org_id"], axis=1)
    return ordered_users, ordered_organizations, ordered_reviews
