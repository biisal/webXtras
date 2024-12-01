# WebXtras - OpenSource Multi-Tool Web Project

Welcome to **WebXtras**! 🎉  
This is an open-source project designed to provide a collection of useful utilities for both web developers and regular users. The project includes a **Next.js** frontend with **Tailwind CSS** and **Shadcn UI**, and a **FastAPI** backend.

---

## Features  
- **Frontend** built with **Next.js**, **Tailwind CSS**, and **Shadcn UI** for a modern, responsive, and intuitive user interface.  
- **Backend** powered by **FastAPI**, delivering a fast, scalable, and reliable API.  
- **Open-source**: Feel free to contribute and improve the project.  
- **User-friendly**: Designed for simplicity and ease of use.

---

## Table of Contents  
1. [Getting Started](#getting-started)  
2. [Frontend Setup](#frontend-setup)  
3. [Backend Setup](#backend-setup)  
4. [Project Structure](#project-structure)  
5. [Contributing](#contributing)  
6. [License](#license)  

---

## Getting Started  

To get started with **WebXtras**, follow these steps:

### Prerequisites  
Make sure you have the following installed:
- **Node.js** (for the frontend)  
- **Python** (for the backend)  

---

### Installation  

1. **Clone the repository**  
    ```bash
    git clone https://github.com/biisal/webXtras.git
    ```  

2. **Navigate to the project directory**  
    ```bash
    cd webXtras
    ```  

---

## Frontend Setup  

The frontend is built with **Next.js**, **Tailwind CSS**, and **Shadcn UI**. Follow these steps to set it up:

1. **Navigate to the frontend directory**  
    ```bash
    cd frontend
    ```  

2. **Install dependencies**  
    ```bash
    npm install
    ```  

3. **Run the development server**  
    ```bash
    npm run dev
    ```  

The frontend should now be accessible on `http://localhost:3000`.

---

## Backend Setup  

The backend is built using **FastAPI**. Here's how to get it running:

1. **Navigate to the backend directory**  
    ```bash
    cd backend/app
    ```  

2. **Create a virtual environment** (if not already created)  
    - On Windows:  
        ```bash
        python -m venv venv
        venv\Scripts\activate
        ```  
    - On Linux/macOS:  
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```  

3. **Install backend dependencies**  
    ```bash
    pip install -r requirements.txt
    ```  

4. **Start the FastAPI server**  
    Run the following command to start the backend in development mode:  
    ```bash
    fastapi dev main.py
    ```  

Your FastAPI backend should now be accessible on `http://localhost:8000`.

---

## Project Structure  

### Backend  

- `backend/app/`  
  - `shared/`: Shared resources such as downloads  
  - `tools/`: Utility implementations  
  - `config.py`: Backend configuration  
  - `.env`: Environment variables  
  - `main.py`: Entry point for the FastAPI app  
  - `requirements.txt`: Backend dependencies  

### Frontend  

- `frontend/`: All frontend code built with Next.js, Tailwind CSS, and Shadcn UI
---

## Contributing  

We welcome contributions from developers around the world. Here's how you can contribute:

1. **Fork the repository**  
    Click the **Fork** button at the top-right of this repository.  

2. **Clone your fork**  
    ```bash
    git clone https://github.com/<your-username>/webXtras.git
    ```  

3. **Create a new feature branch**  
    ```bash
    git checkout -b feature/new-feature
    ```  

4. **Make your changes**  
    Add a new feature, fix bugs, or improve the existing codebase.  

5. **Commit your changes**  
    ```bash
    git commit -m "Added xyz feature"
    ```  

6. **Push your changes**  
    ```bash
    git push origin feature/new-feature
    ```  

7. **Create a pull request**  
    Go to the original repository and create a pull request with your changes.

---

## License  

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.  

---

### Our Team

**WebXtras** is a collaborative effort made possible by the contributions of these talented developers who are actively working together to build and enhance the project:

- [**Amanbabuhemant**](https://github.com/amanbabuhemant)  
- [**Biisal**](https://github.com/biisal)  
- [**PanditSiddharth**](https://github.com/PanditSiddharth)  
- [**PyGuru123**](https://github.com/pyGuru123)  

Together, we're working to make **WebXtras** an amazing collection of web tools and utilities for everyone.

---

### Ready to get started? 🚀  
Explore and contribute to **WebXtras** today! If you have any questions or run into issues, feel free to open an issue or contact the community.

Check out the project on [GitHub](https://github.com/biisal/webXtras/).
