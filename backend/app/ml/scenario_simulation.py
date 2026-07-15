import pandas as pd

def simulate_road_closure(df:pd.DataFrame):
    
    simulation_df = df.copy()

    busiest_route = (simulation_df.groupby("route_id")["vehicle_count"].mean().idxmax())

    route_data = simulation_df[simulation_df["route_id"] == busiest_route]

    estimated_congestion = round(route_data["congestion_level"].mean() * 1.40,2)

    estimated_delay = 15.0

    estimated_travel_time = 20.0

    return {
        "scenario_type": "Road Closure",

        "affected_route": busiest_route,

        "estimated_congestion": estimated_congestion,

        "estimated_delay": estimated_delay,

        "estimated_travel_time": estimated_travel_time
    }

def simulate_rain_impact(df:pd.DataFrame):
    
    simulation_df = df.copy()

    estimated_congestion = round(simulation_df["congestion_level"].mean() * 1.25,2)

    estimated_delay = 10.0

    estimated_travel_time = 15.0

    simulation_df["average_speed"] *= 0.80

    return {
    
       "scenario_type": "Rain Impact",

       "affected_route": "ALL_ROUTES",

       "estimated_congestion": estimated_congestion,

       "estimated_delay": estimated_delay,

       "estimated_travel_time": estimated_travel_time
    }


def simulate_event_traffic(df:pd.DataFrame):

    simulation_df = df.copy()

    simulation_df["vehicle_count"] *= 1.35

    estimated_congestion = round(simulation_df["congestion_level"].mean() * 1.30,2)

    estimated_delay = 18.0

    estimated_travel_time = 28.0

    return {
        "scenario_type": "Festival/Event Traffic",

        "affected_route": "ALL_ROUTES",

        "estimated_congestion": estimated_congestion,

        "estimated_delay": estimated_delay,

        "estimated_travel_time": estimated_travel_time
    }


def simulate_vehicle_load(df:pd.DataFrame):

    simulation_df = df.copy() 

    simulation_df["vehicle_count"] *= 1.25
    
    estimated_congestion = round(simulation_df["congestion_level"].mean() * 1.20, 2)

    estimated_delay = 12.0

    estimated_travel_time = 22.0
    
    return {
        "scenario_type": "Increased Vehicle Load",

        "affected_route": "ALL_ROUTES",

        "estimated_congestion": estimated_congestion,

        "estimated_delay": estimated_delay,

        "estimated_travel_time": estimated_travel_time
    }

def generate_simulation(df:pd.DataFrame):

    road_closure = simulate_road_closure(df)

    rain_impact = simulate_rain_impact(df)

    event_traffic = simulate_event_traffic(df)

    vehicle_load = simulate_vehicle_load(df)

    simulation_results = []

    simulation_results.append(road_closure)

    simulation_results.append(rain_impact)

    simulation_results.append(event_traffic)

    simulation_results.append(vehicle_load)

    return simulation_results