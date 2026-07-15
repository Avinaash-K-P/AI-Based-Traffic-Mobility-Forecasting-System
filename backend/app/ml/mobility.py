import pandas as pd

from app.ml.congestion_prediction import calculate_peak_hours

def recommend_alternative_routes(df:pd.DataFrame):
    
    route_summary = (
    df.groupby("route_id")
      .agg({
          "congestion_level": "mean",
          "vehicle_count": "mean"
      })
      .reset_index()
    )

    if route_summary.empty:
        return []

    most_congested = route_summary.loc[
    route_summary["congestion_level"].idxmax()
    ]

    least_congested = route_summary.loc[
    route_summary["congestion_level"].idxmin()
    ]

    expected_improvement = (
    most_congested["congestion_level"]
    -
    least_congested["congestion_level"]
    )

    return [
    {
        "route_id": most_congested["route_id"],

        "recommendation_type": "Alternative Route",

        "recommendation":
        f"Redirect traffic through Route "
        f"{least_congested['route_id']} "
        f"during peak hours.",

        "expected_improvement":
        round(expected_improvement, 2)
    }
    ]
    

def recommend_best_travel_times(df: pd.DataFrame):

    peak_hours = calculate_peak_hours(df)
    peak_hour = peak_hours.iloc[0]
    expected_improvement = 25.0
    
    least_busy_hour = peak_hours.sort_values(
    by="average_vehicle_count",
    ascending=True
    ).iloc[0]

    return [
    {
        "route_id": "ALL_ROUTES",

        "recommendation_type": "Best Travel Time",

        "recommendation":
        f"Peak traffic occurs around {int(peak_hour['hour'])}:00. "
        f"Consider traveling around {int(least_busy_hour['hour'])}:00 "
        f"to reduce travel time.",

        "expected_improvement": expected_improvement
    }
]

def recommend_congestion_reduction(df: pd.DataFrame):
    high_congestion = df[
    (df["congestion_level"] > 70)
    &
    (df["vehicle_count"] > 500)
    ].copy()
    
    if high_congestion.empty:
        return []
    
    recommendations = []

    for _, row in high_congestion.iterrows():
        recommendations.append(
    {
        "route_id": row["route_id"],

        "recommendation_type": "Congestion Reduction",

        "recommendation":
        f"Reduce vehicle flow on Route {row['route_id']} "
        f"during peak hours to improve traffic movement.",

        "expected_improvement": round(row["congestion_level"] * 0.20,2)
    }
    )

    return recommendations    

def recommend_route_load_balancing(df:pd.DataFrame):

    route_summary = (
    df.groupby("route_id")
      .agg({
          "vehicle_count": "mean",
          "congestion_level": "mean"
      })
      .reset_index()
    )

    if route_summary.empty:
        return []
    
    busiest_route = route_summary.loc[
    route_summary["vehicle_count"].idxmax()
    ]

    least_busy_route = route_summary.loc[
    route_summary["vehicle_count"].idxmin()
    ]

    expected_improvement = round(
    (
        busiest_route["vehicle_count"]
        -
        least_busy_route["vehicle_count"]
    )
    /
    busiest_route["vehicle_count"]
    * 100,
    2
    )    

    return [
    {
        "route_id": busiest_route["route_id"],

        "recommendation_type": "Route Load Balancing",

        "recommendation":
        f"Redirect traffic from Route "
        f"{busiest_route['route_id']} "
        f"to Route "
        f"{least_busy_route['route_id']} "
        f"during peak hours.",

        "expected_improvement":
        expected_improvement
    }
    ]

def generate_recommendations(df:pd.DataFrame):
    
    alternative_routes = recommend_alternative_routes(df)

    best_travel_times = recommend_best_travel_times(df)

    congestion_reduction = recommend_congestion_reduction(df)

    route_load_balancing = recommend_route_load_balancing(df)
    
    recommendations = []

    recommendations.extend(alternative_routes)

    recommendations.extend(best_travel_times)

    recommendations.extend(congestion_reduction)

    recommendations.extend(route_load_balancing)

    return recommendations

    

