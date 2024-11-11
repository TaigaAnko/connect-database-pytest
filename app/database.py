from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.exc import SQLAlchemyError


class ConnectDB:
    
    def connection_test(self, engine:Engine) -> None:
        # 接続のテスト
        try:
            with engine.connect():
                print("Connection to the database is successful!")
        except SQLAlchemyError as e:
            print(f"An error occurred: {e}")
            
    def set_engine(self, url: str) -> Engine:
        return create_engine(url)
    
    def set_db_url(self, user: str, password: str, host: str, port: int, database: str) -> str:
        return (
            f"mysql+mysqlconnector://{user}:"
            f"{password}@{host}:"
            f"{port}/{database}"
        )
        
if __name__ == '__main__':
    pass