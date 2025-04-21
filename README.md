# Distance Calculator API with OpenAI Agents

This project demonstrates the use of OpenAI Agents framework to create an intelligent distance calculation service that uses Google Maps API. The service can understand natural language queries about distances between locations and provide detailed responses including distance and travel duration.

## Features

- Natural language processing using OpenAI Agents
- Distance and duration calculations using Google Maps API
- RESTful API endpoint using FastAPI
- Async support for better performance
- Built-in error handling and response formatting
- Interactive API documentation with Swagger UI

## Prerequisites

- Python 3.8+
- Google Maps API key (get it from [Google Cloud Console](https://console.cloud.google.com/))
- OpenAI API key (get it from [OpenAI Platform](https://platform.openai.com/api-keys))

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/distance-calculator-api.git
cd distance-calculator-api
```

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

5. Edit `.env` file and add your API keys:
```
GOOGLE_MAPS_API_KEY=your_google_maps_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

### Running the API Server

Start the FastAPI server:
```bash
python app.py
```

The server will start at `http://localhost:8000`

### API Documentation

You can access the interactive API documentation at:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### API Endpoints

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
    "response": "The driving distance between San Francisco and Seattle is 808 mi (1,300 km), and it would take approximately 12 hours 46 minutes to drive between these cities."
}
```
- **Curl Example**:
```bash
curl -X POST "http://localhost:8000/calculate-distance" \
     -H "Content-Type: application/json" \
     -d '{"query": "What is the distance between New York and Boston?"}'
```

### Testing the Agent Directly

You can also test the distance calculation agent directly using the Python script:

```bash
python distance_agent.py
```

This will run a sample query calculating the distance between New York and Los Angeles.

## Project Structure

- `app.py` - FastAPI application and API endpoints
- `distance_agent.py` - OpenAI Agent implementation with Google Maps integration
- `requirements.txt` - Project dependencies
- `.env.example` - Example environment variables file
- `README.md` - Project documentation

## Built With

- [OpenAI Agents](https://github.com/openai/openai-agents-python) - Multi-agent workflow framework
- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework for building APIs
- [Google Maps API](https://developers.google.com/maps) - Distance calculation service
- [Python-dotenv](https://github.com/theskumar/python-dotenv) - Environment variable management

## Error Handling

The API includes error handling for:
- Invalid API keys
- Invalid location names
- Google Maps API errors
- General server errors

Example error response:
```json
{
    "detail": "Error message describing what went wrong"
}
```

## Development

To run the server in development mode with auto-reload:
```bash
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenAI for the Agents framework
- Google Maps Platform for the distance calculation API
- FastAPI team for the excellent web framework 