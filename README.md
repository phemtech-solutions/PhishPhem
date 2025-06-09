# 🛡️ PhishPhem — Phishing Email Analyzer

PhishPhem is an AI-powered phishing email analysis tool built for cybersecurity analysts, researchers, and individuals. It allows you to analyze `.eml` files or raw email content using both rule-based heuristics and AI-powered models. The output includes a phishing risk score, red flags, summary advice, and a downloadable PDF report.

**🔗 Live App:** [https://phishphem-nhpbco2xj2y5zvclpfsvhx.streamlit.app](https://phishphem-nhpbco2xj2y5zvclpfsvhx.streamlit.app)

## 📌 Features

- Upload `.eml` email files or paste raw email content
- Rule-based phishing detection:
  - Suspicious links (e.g., shortened URLs)
  - Urgent or manipulative phrases
  - Sender vs. link domain mismatch
- AI-based phishing risk assessment (via OpenRouter API)
- Clear, actionable summary advice
- Downloadable PDF report
- Streamlit interface with real-time feedback

## 🚀 Getting Started

### Requirements

- Python 3.10 or newer
- Streamlit account (optional for deployment)
- GitHub account (for development or contributions)
- OpenRouter API key (or OpenAI key with minor adjustments)

## 📦 Installation

```bash
git clone https://github.com/phemtech-solutions/PhishPhem.git
cd PhishPhem
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## 🔐 API Configuration

Create the secret configuration file with the following commands:

```bash
mkdir -p .streamlit
nano .streamlit/secrets.toml
```

Paste the content below into `.streamlit/secrets.toml` and save it:

```toml
OPENROUTER_API_KEY = "sk-or-your-api-key-here"
```

Replace the value with your actual key from [https://openrouter.ai/settings/keys](https://openrouter.ai/settings/keys).

## 🧠 Run the App

To start the app locally:

```bash
streamlit run streamlit_app.py
```

You’ll see output like:

```bash
Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
```

Open the local URL in your browser to use the app.

## 📤 Output

The tool provides:

- **AI-generated phishing summary**
- **Rule-based analysis**, including:
  - Suspicious links
  - Urgency phrases
  - Domain mismatches
- **Risk score**: total red flags detected
- **Advice section**: summarizes the email’s risk level
- **Downloadable PDF report** including all analysis and your name

## 🧪 Rule-Based Detection Heuristics

| Heuristic Type   | Description                                                 |
| ---------------- | ----------------------------------------------------------- |
| Suspicious Links | Detects shortened or suspicious redirection URLs            |
| Urgency Phrases  | Flags pressurizing text like "verify now", "update account" |
| Domain Mismatch  | Compares sender’s domain with linked domain(s)              |

## 💼 Use Cases

- Phishing awareness training for staff or students
- SOC analysis and testing in lab environments
- Academic cybersecurity demonstrations
- Personal portfolio project for AI in security
- Quick email forensics with PDF report output

## 👨‍💻 Author

**Ajijola Oluwafemi Blessing**  
Cybersecurity | Software | IT | Research

- GitHub: [phemtech-solutions](https://github.com/oluwafemiab/ajijola.github.io)  
- LinkedIn: [https://www.linkedin.com/in/ajijola-oluwafemi-ba839712a/)
