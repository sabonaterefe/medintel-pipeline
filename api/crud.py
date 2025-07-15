from api.database import get_conn

def top_products(limit):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT product_name, COUNT(*) AS mentions
        FROM fct_messages
        GROUP BY product_name
        ORDER BY mentions DESC
        LIMIT %s
    """, (limit,))
    data = cur.fetchall()
    cur.close()
    conn.close()
    return [{"product": r[0], "mentions": r[1]} for r in data]

def channel_activity(channel_name):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT message_date, COUNT(*) FROM fct_messages
        WHERE channel = %s
        GROUP BY message_date
        ORDER BY message_date
    """, (channel_name,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"date": r[0], "count": r[1]} for r in rows]

def search_messages(query):
    conn = get_conn()
    cur = conn.cursor()
    cur.execute("""
        SELECT message_id, channel, text
        FROM fct_messages
        WHERE text ILIKE %s
        LIMIT 50
    """, (f"%{query}%",))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id": r[0], "channel": r[1], "text": r[2]} for r in rows]
