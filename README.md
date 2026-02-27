# S2S - Scrap to Spark - Integrated Battery Evaluation System

## 🚀 Quick Start

### Prerequisites
- **Python 3.9+** - Backend ML services
- **Node.js 18+** - Frontend build system
- **Git** - For cloning the repository

### One-Command Startup (Windows)

```bash
# Clone and run the integrated system
git clone https://github.com/pulkittaneja09/sdg-hackthon.git
cd sdg-hackthon
start_integrated.bat
```

This script will:
1. ✅ Check system requirements
2. � Install all dependencies
3. 🔨 Build the frontend
4. 🚀 Start the integrated server on `http://localhost:8000`

## 🎯 What is S2S - Scrap to Spark?

S2S - Scrap to Spark is an **AI-powered battery evaluation system** that:
- 🔋 Predicts Remaining Useful Life (RUL) for EV batteries
- 🏭 Recommends optimal second-life deployment strategies
- 🌱 Calculates environmental sustainability impact
- 📊 Generates comprehensive analysis reports
- 📈 Provides interactive data visualization

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Frontend      │    │    Backend      │    │   ML Model      │
│   (React +      │◄──►│   (FastAPI)     │◄──►│   (Random       │
│   TypeScript)   │    │                 │    │   Forest)       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │                       │                       │
         ▼                       ▼                       ▼
   User Interface        API Endpoints        Trained Model
   Data Visualization    Data Processing      RUL Prediction
   File Upload           Feature Engineering  Confidence Scoring
```

## 📁 Project Structure

```
sdg-hackthon/
├── backend/                    # Python FastAPI backend
│   ├── main.py                # Main API server
│   ├── model_loader.py        # ML model loading
│   ├── feature_engineering.py # Battery data processing
│   ├── rul_predictor.py       # RUL prediction logic
│   ├── deployment_engine.py   # Deployment recommendations
│   ├── sustainability_calculator.py # Environmental impact
│   ├── report_generator.py    # AI-powered reports
│   ├── pdf_generator.py       # PDF report generation
│   ├── models/                # Trained ML model (.pkl file)
│   └── requirements.txt       # Python dependencies
├── frontend/                   # React TypeScript frontend
│   ├── src/
│   │   ├── components/        # React components
│   │   ├── pages/             # Page components
│   │   └── App.tsx            # Main application
│   ├── package.json           # Node.js dependencies
│   └── vite.config.ts         # Build configuration
├── start_integrated.bat        # Windows startup script
└── README.md                  # This file
```

## 🔧 API Endpoints

### `POST /predict`
Upload CSV battery data for comprehensive analysis.

**Request:**
- `file`: CSV file with battery telemetry data

**Response:**
```json
{
  "battery_summary": {
    "predicted_rul": 45.2,
    "confidence_score": 85.5,
    "grade": "B",
    "recommended_use": "Backup Storage Systems"
  },
  "sustainability": {
    "usable_energy_kwh": 52.5,
    "co2_saved_kg": 4725,
    "lithium_saved_kg": 42,
    "tree_equivalent": 215
  },
  "ai_report": {
    "executive_summary": { ... },
    "technical_analysis": { ... },
    "ai_insights": { ... },
    "recommendations": { ... },
    "risk_assessment": { ... }
  },
  "visualization_data": {
    "capacity_trend": [...],
    "soh_trend": [...],
    "voltage_trend": [...],
    "temperature_trend": [...]
  }
}
```

### `POST /download-report`
Generate and download a comprehensive PDF report.

**Request:** Same CSV file as `/predict`
**Response:** PDF file download

## 📊 CSV Data Format

Upload CSV files with these required columns:

| Column | Description | Units |
|--------|-------------|-------|
| `cycle` | Charge/discharge cycle number | - |
| `Capacity` | Battery capacity | Ah |
| `Voltage_measured` | Measured voltage | V |
| `Current_measured` | Measured current | A |
| `Temperature_measured` | Temperature | °C |
| `Time` | Time within cycle | seconds |

**Sample CSV:**
```csv
cycle,Capacity,Voltage_measured,Current_measured,Temperature_measured,Time
1,1.5,4.2,-2.0,25.0,0
1,1.5,3.8,-2.1,25.5,1000
1,1.5,3.5,-2.0,26.0,2000
2,1.45,4.2,-2.0,24.8,0
```

## 🎯 Features

### 🔋 Battery Analysis
- **RUL Prediction**: AI-powered remaining useful life prediction
- **Confidence Scoring**: Model confidence metrics
- **Health Assessment**: Overall battery health evaluation
- **Degradation Analysis**: Capacity degradation trends

### 🏭 Deployment Recommendations
- **Grade Assignment**: A/B/C grading system
- **Use Case Suggestions**: Optimal deployment scenarios
- **Risk Assessment**: Deployment risk factors
- **Economic Viability**: Cost-benefit analysis

### 🌱 Sustainability Impact
- **CO₂ Savings**: Environmental impact in kg CO₂
- **Lithium Conservation**: Resource savings in kg
- **Tree Equivalent**: Environmental impact visualization
- **Circular Economy**: Extended lifecycle benefits

### 📈 Data Visualization
- **Capacity Trends**: Battery degradation over time
- **Voltage Curves**: Performance characteristics
- **Temperature Analysis**: Thermal performance
- **State of Health**: SOH evolution tracking

### 📋 Reporting
- **AI-Powered Insights**: Intelligent analysis summaries
- **Risk Assessment**: Comprehensive risk evaluation
- **Recommendations**: Actionable deployment guidance
- **PDF Reports**: Professional downloadable reports

## 🛠️ Development

### Backend Development
```bash
cd backend
pip install -r requirements.txt
python -m uvicorn main:app --reload
```

### Frontend Development
```bash
cd frontend
npm install
npm run dev
```

### Running Tests
```bash
# Backend tests
cd backend
python -m pytest

# Frontend tests  
cd frontend
npm test
```

## 📊 Model Performance

The ML model is trained on the NASA battery dataset:
- **Algorithm**: Random Forest (300 estimators)
- **Features**: 11 engineered features
- **Performance**: MAE: 9.351 cycles, R²: 0.879
- **Training Data**: 33 batteries, 2,416 cycles

## 🔒 Security & Privacy

- **No Data Persistence**: Uploaded files are processed in memory only
- **Local Processing**: All computations performed locally
- **No External APIs**: Complete offline operation capability
- **Data Privacy**: No data sent to external services

## 🐛 Troubleshooting

### Common Issues

**Backend won't start:**
```bash
# Check Python version
python --version  # Should be 3.9+

# Install dependencies
cd backend
pip install -r requirements.txt
```

**Frontend build fails:**
```bash
# Check Node.js version
node --version  # Should be 18+

# Clean install
cd frontend
rm -rf node_modules package-lock.json
npm install
```

**Model loading errors:**
- Ensure `models/s2s_scrap_to_spark_full_pipeline.pkl` exists
- Check file permissions
- Verify sklearn version compatibility

**CORS errors:**
- Backend should be running on port 8000
- Frontend proxy should be configured in `vite.config.ts`

### Port Conflicts
- **Frontend**: Change port in `vite.config.ts`
- **Backend**: Change port with `--port` flag
- **Default ports**: Frontend 5173, Backend 8000

## 📚 Technical Documentation

### ML Pipeline
1. **Data Ingestion**: CSV file parsing and validation
2. **Feature Engineering**: 11 engineered features from raw telemetry
3. **Prediction**: Random Forest model inference
4. **Confidence Calculation**: Tree-based variance estimation
5. **Post-Processing**: Result formatting and analysis

### Feature Engineering
- **Time-series features**: Discharge time, temperature variance
- **Electrical features**: Voltage slope, internal resistance
- **Degradation features**: Capacity ratio, degradation slope
- **Statistical features**: Rolling averages, trend analysis

## 🌍 Environmental Impact

S2S - Scrap to Spark promotes sustainability by:
- 🔄 **Extending Battery Life**: Second-life deployment reduces waste
- 🌱 **Reducing CO₂**: Avoids new battery manufacturing emissions
- ♻️ **Resource Conservation**: Preserves lithium and rare earth metals
- 📊 **Impact Visualization**: Quantifies environmental benefits

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📄 License

This project is part of the SDG Hackathon solution.

## 🆘 Support

For issues and questions:
1. Check the troubleshooting section above
2. Review the API documentation
3. Examine the CSV format requirements
4. Verify system requirements

---

**Built with ❤️ for the SDG Hackathon**  
*Advancing sustainable battery management through AI*
