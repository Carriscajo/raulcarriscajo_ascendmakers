sudo apt update
sudo apt install -y python3 python3-pip
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
pip insatall fastapi uvicorn sqlalchemy pydanitc
python -c "from app.database import Base, engine; Base.meta.create_all(bind=engine)
echo "Done"