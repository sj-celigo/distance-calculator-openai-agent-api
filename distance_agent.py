import os
from typing import Dict
from dotenv import load_dotenv
import googlemaps
from agents import Agent, Runner, function_tool

# Load environment variables
load_dotenv()

# Initialize Google Maps client
gmaps = googlemaps.Client(key=os.getenv('GOOGLE_MAPS_API_KEY'))

@function_tool
def calculate_distance(origin: str, destination: str) -> Dict[str, str]:
    """Calculate the distance between two places using Google Maps."""
    try:
        # Get the distance matrix
        result = gmaps.distance_matrix(
            origins=[origin],
            destinations=[destination],
            mode="driving",
            units="metric"
        )

        # Extract distance and duration
        distance = result['rows'][0]['elements'][0]['distance']['text']
        duration = result['rows'][0]['elements'][0]['duration']['text']

        return {
            "distance": distance,
            "duration": duration,
            "origin": origin,
            "destination": destination
        }
    except Exception as e:
        return {"error": f"Error calculating distance: {str(e)}"}

# Create an agent with the distance calculation tool
distance_agent = Agent(
    name="Distance Calculator",
    instructions="""You are a helpful agent that calculates distances between places.
    When asked about distance between two places, use the calculate_distance tool.
    Provide the results in a clear, friendly manner.""",
    tools=[calculate_distance]
)

async def main():
    # Example usage
    result = await Runner.run(
        distance_agent,
        "What's the distance between New York and Los Angeles?"
    )
    print(result.final_output)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main()) 