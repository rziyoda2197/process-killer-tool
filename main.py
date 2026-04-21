import re

def sql_injection_detector(query):
    # SQL Injection kuchi uchun tekshiruvlar
    sql_injection_keywords = ["SELECT", "INSERT", "UPDATE", "DELETE", "DROP", "CREATE", "ALTER", "TRUNCATE"]
    for keyword in sql_injection_keywords:
        if re.search(r"\b" + keyword + r"\b", query, re.IGNORECASE):
            return True

    # SQL Injection kuchi uchun tekshiruvlar
    sql_injection_characters = ["'", "\"", ";", "--", "//", "/*", "*/"]
    for character in sql_injection_characters:
        if character in query:
            return True

    # SQL Injection kuchi uchun tekshiruvlar
    sql_injection_functions = ["OR 1=1", "UNION", "JOIN", "SUBSTRING", "EXTRACT"]
    for function in sql_injection_functions:
        if function in query:
            return True

    return False

# Test qo'llanishi
print(sql_injection_detector("SELECT * FROM users WHERE id = 1"))  # True
print(sql_injection_detector("Hello, world!"))  # False
print(sql_injection_detector("SELECT * FROM users WHERE id = 1 OR 1=1"))  # True
