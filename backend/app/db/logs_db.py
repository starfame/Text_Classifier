from .base_db import BaseDb


class LogsDb(BaseDb):
    async def add_log(self, query: str, response: str):
        query_str = """
        INSERT INTO logs (query, response) VALUES ($1, $2);
        """
        try:
            await self.execute(query_str, query, response)
        except Exception as e:
            print(f"Error adding log: {e}")

    async def get_all_logs(self):
        query = """
        SELECT * FROM logs;
        """
        try:
            result = await self.fetch(query)
            return result
        except Exception as e:
            print(f"Error fetching all logs: {e}")
            return []
