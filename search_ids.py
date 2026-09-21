import asyncio
from motor.motor_asyncio import AsyncIOMotorClient

async def check():
    uri = 'mongodb+srv://krishnau2097_db_user:RNe1HMkPZj4mQdgY@qlik.91dnbo8.mongodb.net/?appName=Qlik'
    client = AsyncIOMotorClient(uri)
    wid = 'dcac9b34-7be9-4144-b182-6729e4d12793'
    pid = '91d5bd09-a0ec-40af-93a2-95cd2b1ec358'
    rid = 'd3658b84-df59-4053-a67b-839beba1d924'
    
    print(f"Searching for:\n wid={wid}\n pid={pid}\n rid={rid}\n")

    for db_name in ['QT2F_Tableau', 'QT2F']:
        db = client[db_name]
        colls = await db.list_collection_names()
        for c in colls:
            cursor = db[c].find({'$or': [{'workbook_id': wid}, {'project_id': pid}, {'run_id': rid}]})
            matches = await cursor.to_list(10)
            if matches:
                print(f"Found {len(matches)} record(s) in [{db_name}].[{c}]:")
                for m in matches:
                    print(f"   _id={m.get('_id')}, run_id={m.get('run_id')}, wid={m.get('workbook_id')}, pid={m.get('project_id')}")

if __name__ == '__main__':
    asyncio.run(check())
