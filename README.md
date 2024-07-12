# 🕷️ Web Scraper Project

## 📋 Description
This project is a flexible and powerful web scraper built with FastAPI and Docker. It allows you to extract data from tables on web pages and save them in JSON and Excel formats.

## 🚀 Features
- 🌐 Web table scraping
- 💾 JSON and Excel storage
- 🐳 Dockerized
- 🔄 Hot-reload development
- 📊 RESTful API to interact with the scraper

## 🛠️ Prerequisites
- Docker 🐳
- Docker Compose 🐙

## 🏗️ Project Structure
```
web_scraper/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
├── .gitignore
├── app/
│   ├── main.py
│   ├── scraper.py
│   └── data_storage.py
└── data/
```

## 🚀 Getting Started

1. **Clone the repository**
   ```
   git clone https://github.com/your-username/web-scraper.git
   cd web-scraper
   ```

2. **Build and run with Docker Compose**
   ```
   docker-compose up --build
   ```

3. **Access the API**
   - The API will be available at `http://localhost:8880`
   - Swagger UI documentation will be at `http://localhost:8880/docs`

## 🕹️ Usage

1. **Perform scraping**
   - Make a POST request to `/scrape` with the following body:
     ```json
     {
       "url": "https://example.com",
       "table_selector": "table.my-table-class"
     }
     ```
   - The `table_selector` is optional. If not provided, it will attempt to find the first table on the page.

2. **Download results**
   - Use the GET endpoint `/download/{filename}` to download the generated JSON or Excel files.

## 🧪 Development

- Changes in the code will be reflected automatically thanks to hot-reloading.
- Generated files are saved in the `./data` folder on your local machine.

## 📚 API Documentation
Visit `http://localhost:8880/docs` to see the interactive API documentation and test the endpoints.

## 🤝 Contributing
Contributions are welcome! Please open an issue or submit a pull request for any suggestions or improvements.

## 📜 License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

Happy scraping! 🎉🕷️