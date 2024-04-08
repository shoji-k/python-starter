import pandas as pd
import random
from datetime import datetime

# サンプルデータの生成
data = {
    "案件ID": [f"AJ{1000 + i}" for i in range(10)],
    "属性[事業会社]": [random.choice(["○", "×"]) for _ in range(10)],
    "属性[Sier]": [random.choice(["○", "×"]) for _ in range(10)],
    "属性[BP]": [random.choice(["○", "×"]) for _ in range(10)],
    "会社名": [
        "株式会社" + name
        for name in [
            "ネオ",
            "アイティ",
            "サイバー",
            "テクノロジ",
            "イノベーション",
            "クリエイティブ",
            "ソリューション",
            "デジタル",
            "コネクト",
            "ネットワークス",
        ]
    ],
    "優先度": [random.choice(["高", "中", "低"]) for _ in range(10)],
    "案件タイトル": [f"システム開発プロジェクト{chr(65+i)}" for i in range(10)],
    "人月単価": [f"{random.randint(50, 500)}万円" for _ in range(10)],
    "担当営業": [
        "山田太郎",
        "鈴木一郎",
        "佐藤恵子",
        "伊藤涼子",
        "渡辺直美",
        "小林誠",
        "加藤浩次",
        "高橋由美子",
        "中村悠一",
        "田中美咲",
    ],
    "注意事項等※随時追加予定": ["", "", "", "", "", "", "", "", "", ""],
    "紹介フォーマット": [
        f"""
■タイトル：システム開発プロジェクト{chr(65+i)}
■人材要件
【必須スキル】
- Java
- Spring Framework
- MySQL
【尚可スキル】
- Docker
- Kubernetes
- React
"""
        for i in range(10)
    ],
    "ステータス[open]": [random.choice(["○", "×"]) for _ in range(10)],
    "ステータス[close]": [random.choice(["×", "○"]) for _ in range(10)],
    "作成日時": [datetime.now().strftime("%Y/%m/%d %H:%M:%S") for _ in range(10)],
    "備考": ["", "", "", "", "", "", "", "", "", ""],
}

df = pd.DataFrame(data)

# CSVに変換(SJISエンコード)
# csv_buffer = io.StringIO()
# df.to_csv(csv_buffer, index=False, encoding="cp932")
# csv_content = csv_buffer.getvalue()

# # CSV内容を表示 (ここではデータフレームを直接返して確認)
# print(csv_content)
file_path = "./sample_project_data.csv"
df.to_csv(file_path, index=False, encoding="cp932")

file_path
