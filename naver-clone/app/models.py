from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class SearchResult(db.Model):
    __tablename__ = 'search_results'

    id = db.Column(db.Integer, primary_key=True)
    query = db.Column(db.String(255), nullable=False)
    result = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

    def __repr__(self):
        return f'<SearchResult {self.query}>'