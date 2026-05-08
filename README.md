# Genderize API Explorer

A simple web application built with Flask that provides an interface to explore and classify names by gender using the Genderize.io API. This app includes both a user-friendly web interface and RESTful API endpoints for programmatic access.

## Features

- **Web Interface**: Clean, modern UI for easy name classification
- **REST API**: JSON-based API for integrating with other applications
- **Real-time Classification**: Fetches gender data from Genderize.io API
- **Confidence Scoring**: Includes probability and sample size indicators
- **CORS Support**: Allows cross-origin requests for API usage
- **Production Ready**: Configured for deployment on platforms like Railway

## Technologies Used

- **Backend**: Python Flask
- **Frontend**: HTML, CSS (Vanilla)
- **API Integration**: Genderize.io API
- **Deployment**: Railway (with Gunicorn WSGI server)
- **Dependencies**: Flask, Flask-CORS, Requests

## Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd genderize-api-practice
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Local Development

1. **Run the application**:
   ```bash
   python app.py
   ```

2. **Open your browser** and navigate to `http://localhost:5000`

3. **Use the web interface** to enter names and see classifications

### API Usage

The application provides the following API endpoints:

#### POST /api/classify
Classify a name by gender.

**Request Body**:
```json
{
  "name": "John"
}
```

**Response**:
```json
{
  "name": "John",
  "gender": "male",
  "probability": 0.99,
  "sample_size": 1500,
  "is_confident": true,
  "request_time": "2023-10-01 12:00:00"
}
```

**Error Responses**:
- `400`: Missing or empty name parameter
- `422`: Name is not a string or is numeric
- `500`: Failed to fetch data from Genderize API

#### DELETE /api/classify/{index}
Acknowledge deletion of a result (client-side handling).

**Response**:
```json
{
  "message": "Row deleted successfully",
  "deleted_index": 1
}
```

### Example API Usage with curl

```bash
curl -X POST http://localhost:5000/api/classify \
  -H "Content-Type: application/json" \
  -d '{"name": "Alice"}'
```

## Deployment

This application is configured for deployment on Railway:

1. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Railway**:
   - Connect your GitHub repository to Railway
   - Railway will automatically detect the Python app and use the Procfile
   - The app will be available at the generated Railway URL

### Environment Variables

Railway automatically sets the `PORT` environment variable. No additional configuration is required.

## Project Structure

```
genderize-api-practice/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Procfile              # Railway deployment configuration
├── templates/
│   └── index.html        # Web interface
└── README.md             # This file
```

## API Details

- **Base URL**: `https://your-railway-app.railway.app`
- **Rate Limiting**: Subject to Genderize.io API limits
- **Data Source**: All gender data comes from the Genderize.io service

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test locally
5. Submit a pull request

## License

This project is open source and available under the MIT License.

## Disclaimer

This application uses the Genderize.io API for gender classification. Please review their terms of service and usage policies. Gender classification based on names may not be accurate and should be used responsibly.