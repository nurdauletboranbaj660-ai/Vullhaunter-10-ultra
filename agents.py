# 10 ULTRA AGENTS
class SQLAgent:
    def name(self): return "SQLi Hunter"
    def scan(self, content): return "select" in content.lower() and "from" in content.lower()

class XSSAgent:
    def name(self): return "XSS Hunter"
    def scan(self, content): return "<script" in content or "onload=" in content

class RCEAgent:
    def name(self): return "RCE Hunter"
    def scan(self, content): return "eval(" in content or "exec(" in content

AGENTS = [SQLAgent(), XSSAgent(), RCEAgent()]
print(f"[AGENTS] Loaded {len(AGENTS)} agents: {[a.name() for a in AGENTS]}")
