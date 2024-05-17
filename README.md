# Discussion Board

## Initial setup
1. Clone the repository
```bash
git clone https://github.com/JackHalverson/discussion_board.git
```
2. Navigate to the backend folder
```bash
cd backend/
```
3. Set up and activate your virtual enviroment
```bash
python -m venv .venv

source .venv/bin/activate
```
4. Install requirements
```bash
pip install -r requirements.txt
```
## Running the Aplication

### Launching the backend
Navigate to /discussion_board/backend/ in your terminal and run uvicorn
```bash
uvicorn main:app --reload
```
You should now be able to veiw the backend at:
http://127.0.0.1:8000/docs

### Launching the frontend
Navigate to /discussion_board/frontend/ in a seperate terminal and start the frontend using npm
```bash
npm run start
```
the frontend is now avalable at:
http://localhost:3000/