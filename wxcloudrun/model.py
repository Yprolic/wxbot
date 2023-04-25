from datetime import datetime

from wxcloudrun import db


# 计数表
class Counters(db.Model):
    # 设置结构体表格名称
    __tablename__ = 'Counters'

    # 设定结构体对应表格的字段
    id = db.Column(db.Integer, primary_key=True)
    count = db.Column(db.Integer, default=1)
    created_at = db.Column('createdAt', db.TIMESTAMP, nullable=False, default=datetime.now())
    updated_at = db.Column('updatedAt', db.TIMESTAMP, nullable=False, default=datetime.now())


class Jhscard(db.Model):
    # 设置结构体表格名称
    __tablename__ = 'jhscard'

    # 设定结构体对应表格的字段
    id = db.Column(db.Integer, primary_key=True)
    card_id = db.Column(db.Integer, default=0)
    card_version_id = db.Column(db.Integer, default=0)
    name = db.Column(db.VARCHAR, default='')
    pack_number = db.Column(db.VARCHAR, default='')
    rarity = db.Column(db.VARCHAR, default='')
    init_price = db.Column(db.Float, default=0)
    img = db.Column(db.VARCHAR, default='')
