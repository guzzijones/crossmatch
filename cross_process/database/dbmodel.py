from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import create_session, sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table

import pdb

# Create and engine and get the metadata
class DBBasic(object):

    Base = declarative_base()
    engine = create_engine(
              'postgresql+psycopg2://' +
              'crossmatch:hinton50@localhost:5432/crossmatch')

    metadata = MetaData(bind=engine)

# Reflect each database table we need to use, using metadata


class Users(DBBasic.Base):
    __table__ = Table('users', DBBasic.metadata, autoload=True)


class SupMaster(DBBasic.Base):
    __table__ = Table('sup_master',DBBasic.metadata, autoload=True)


class SupplierData(DBBasic.Base):
    __table__ = Table('sup_data', DBBasic.metadata, autoload=True)


class AccountMaster(DBBasic.Base):
    __table__ = Table('account_master', DBBasic.metadata, autoload=True)


class AccountType(DBBasic.Base):
    __table__ = Table('account_type', DBBasic.metadata, autoload=True)


class ChainCode(DBBasic.Base):
    __table__ = Table('chain_code', DBBasic.metadata, autoload=True)


class CodeMatching(DBBasic.Base):
    __table__ = Table('code_matching', DBBasic.metadata, autoload=True)


class Depl(DBBasic.Base):
    __table__ = Table('depl', DBBasic.metadata, autoload=True)


class DistMaster(DBBasic.Base):
    __table__ = Table('dist_master', DBBasic.metadata, autoload=True)


class DistSupCrossreference(DBBasic.Base):
    __table__ = Table('dist_sup_crossreference', DBBasic.metadata, autoload=True)


class FoodType(DBBasic.Base):
    __table__ = Table('food_type', DBBasic.metadata, autoload=True)


class LicenseType(DBBasic.Base):
    __table__ = Table('license_type',DBBasic. metadata, autoload=True)


class Rad(DBBasic.Base):
    __table__ = Table('rad', DBBasic.metadata, autoload=True)


class RadInvc(DBBasic.Base):
    __table__ = Table('rad_invc', DBBasic.metadata, autoload=True)


class RetailerXref(DBBasic.Base):
    __table__ = Table('retailer_xref', DBBasic.metadata, autoload=True)


class SMan(DBBasic.Base):
    __table__ = Table('sman', DBBasic.metadata, autoload=True)


class States(DBBasic.Base):
    __table__ = Table('states', DBBasic.metadata, autoload=True)


class SupIncomingFiles(DBBasic.Base):
    __table__ = Table('sup_incoming_files', DBBasic.metadata, autoload=True)


class TradeChannel(DBBasic.Base):
    __table__ = Table('trade_channel',DBBasic.metadata, autoload=True)


class ZipCode(DBBasic.Base):
    __table__ = Table('zipcode', DBBasic.metadata, autoload=True)


class LiscenseType(DBBasic.Base):
    __table__ = Table('license_type', DBBasic.metadata, autoload=True)


db_session_maker = sessionmaker(bind=DBBasic.engine)




if __name__ == "__main__":
    session = create_session(bind=DBBasic.engine)
    pdb.set_trace()
    values = session.query(SupMaster).all()
    pass
