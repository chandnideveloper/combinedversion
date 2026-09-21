import json
import os
import sys

# Add paths for direct module importing
sys.path.insert(0, os.path.abspath("az-wa-repo-generationagent"))
sys.path.insert(0, os.path.abspath("mapping (2)/mapping"))

from app.generator import generate
from agents.coordinator_agent import CoordinatorAgent

def test_pipeline():
    print("==================================================================")
    print("TEST 1: Weather Analytics (Google BigQuery) Generation Test")
    print("==================================================================")
    with open("mapping2.md", "r", encoding="utf-8") as f:
        weather_map = json.load(f)

    # Run generation
    res_weather = generate(weather_map)
    print("Weather generation status:", res_weather.get("status"))
    print("Weather generation message:", res_weather.get("message"))
    sm_weather = res_weather.get("artifacts", {}).get("semantic_model", {})
    for k in sorted(sm_weather.keys()):
        if k.startswith("definition/tables/") or k == "definition/expressions.tmdl":
            print(f"--- {k} ---")
            lines = sm_weather[k].strip().splitlines()
            for line in lines[:10]:
                print(f"  {line}")
            if len(lines) > 10:
                print(f"  ... ({len(lines)} total lines)")

    print("\n==================================================================")
    print("TEST 2: FleetVision KSA (Amazon Redshift) Generation Test")
    print("==================================================================")
    with open("MAPPINGRESPONSE.md", "r", encoding="utf-8") as f:
        fleet_map = json.load(f)

    # Re-run mapping through coordinator to test collapsed _Raw table connection inheritance
    coord = CoordinatorAgent()
    # Let's test coordinator on fleet_map's tables and connections
    processed_tables = coord._process_tables(fleet_map.get("tables", []), fleet_map.get("connections", []))
    fleet_map["tables"] = processed_tables
    
    res_fleet = generate(fleet_map)
    print("FleetVision generation status:", res_fleet.get("status"))
    print("FleetVision generation message:", res_fleet.get("message"))
    sm_fleet = res_fleet.get("artifacts", {}).get("semantic_model", {})
    
    # Check Trips, Loads, Drivers, Calendar
    for tname in ["Trips", "Loads", "Drivers", "FuelByTrip", "Calendar"]:
        k = f"definition/tables/{tname}.tmdl"
        if k in sm_fleet:
            print(f"--- {k} ---")
            lines = sm_fleet[k].strip().splitlines()
            # print first 5 and last 8 lines
            for line in lines[:5]:
                print(f"  {line}")
            print("  ...")
            for line in lines[-8:]:
                print(f"  {line}")

if __name__ == "__main__":
    test_pipeline()
