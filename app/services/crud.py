from sqlalchemy.orm import Session


class CRUD:

    @staticmethod
    def create(db: Session, model, **data):
        obj = model(**data)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def get_one(db: Session, model, **filters):
        query = db.query(model)

        for key, value in filters.items():
            column = getattr(model, key, None)
            if column is not None:
                query = query.filter(column == value)

        return query.first()

    @staticmethod
    def get_all(db: Session, model, skip: int = 0, limit: int = 100, **filters):
        query = db.query(model)

        for key, value in filters.items():
            column = getattr(model, key, None)
            if column is not None:
                query = query.filter(column == value)

        return query.offset(skip).limit(limit).all()

    @staticmethod
    def update(db: Session, model, obj_id: int, **data):
        obj = db.query(model).filter(model.id == obj_id).first()

        if not obj:
            return None

        for key, value in data.items():
            if hasattr(obj, key):
                setattr(obj, key, value)

        db.commit()
        db.refresh(obj)
        return obj

    @staticmethod
    def delete(db: Session, model, obj_id: int):
        obj = db.query(model).filter(model.id == obj_id).first()

        if not obj:
            return False

        db.delete(obj)
        db.commit()
        return True

crud = CRUD()