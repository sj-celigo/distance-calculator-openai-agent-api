# Distance Calculator with OpenAI Agent API

This project implements a distance calculation service that combines OpenAI's agent capabilities with Google Maps API to provide intelligent responses to distance-related queries. The service can understand natural language questions about distances between locations and respond with accurate distance and travel duration information.

## Features

- Natural language query processing using OpenAI Agents
- Distance and duration calculations powered by Google Maps API
- Simple REST API endpoint built with FastAPI
- Asynchronous request handling
- Error handling and formatted responses

## Prerequisites

- Python 3.8 or higher
- Google Maps API key (obtain from [Google Cloud Console](https://console.cloud.google.com/))
- OpenAI API key (obtain from [OpenAI Platform](https://platform.openai.com/api-keys))

## Installation

1. Clone the repository and navigate to the project directory

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
```

5. Edit `.env` file with your API keys:
```
GOOGLE_MAPS_API_KEY=your_google_maps_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

### Starting the API Server

Run the FastAPI server:
```bash
python app.py
```

The server will start at `http://localhost:8000`

### API Endpoint

#### Calculate Distance
- **URL**: `/calculate-distance`
- **Method**: `POST`
- **Request Body**:
```json
{
    "query": "What's the distance between San Francisco and Seattle?"
}
```
- **Response**:
```json
{
    "response": "The distance between San Francisco and Seattle is [distance] and it would take approximately [duration] to drive."
}
```

### Testing the Distance Agent

You can test the distance calculation agent directly using:

```bash
python distance_agent.py
```

This runs a sample query calculating the distance between New York and Los Angeles.

## Project Structure

- `app.py` - FastAPI application setup and API endpoint definition
- `distance_agent.py` - OpenAI Agent implementation with Google Maps integration
- `requirements.txt` - Project dependencies
- `.env.example` - Template for environment variables
- `README.md` - Project documentation

## Dependencies

- FastAPI - Web framework for building the API
- uvicorn - ASGI server implementation
- googlemaps - Google Maps API client
- python-dotenv - Environment variable management
- pydantic - Data validation
- openai-agents - OpenAI Agents framework
- openai - OpenAI API client

## Error Handling

The API includes error handling for:
- Missing or invalid API keys
- Invalid location queries
- Google Maps API errors
- Server-side errors

Error responses follow the format:
```json
{
    "detail": "Error description"
}
```

## Development

For development with auto-reload:
```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

## License

This project is open source and available under the MIT License. 