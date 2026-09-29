import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def main():
    uri = 'mongodb+srv://krishnau2097_db_user:RNe1HMkPZj4mQdgY@qlik.91dnbo8.mongodb.net/?appName=Qlik'
    client = AsyncIOMotorClient(uri)
    
    for db_name in ['QT2F_Tableau', 'QT2F']:
        db = client[db_name]
        colls = await db.list_collection_names()
        for c in ['mapping', 'mapping_results']:
            if c in colls:
                cnt = await db[c].count_documents({})
                print(f"[{db_name}].[{c}] total count: {cnt}")
                cursor = db[c].find({}).limit(10)
                docs = await cursor.to_list(10)
                for doc in docs:
                    rid = doc.get('run_id')
                    pid = doc.get('project_id')
                    wid = doc.get('workbook_id')
                    aid = doc.get('app_id')
                    pname = doc.get('project_name')
                    print(f"   run_id={rid}, project_id={pid}, workbook_id={wid}, app_id={aid}, project_name={pname}")

if __name__ == '__main__':
    asyncio.run(main())
