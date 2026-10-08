import os
import re

def extract_summary_from_readme(file_path):
    """READMEファイルから日付と要約・タイトルを抽出する"""
    filename = os.path.basename(file_path)
    # ファイル名例: README.2026.10.08.AM.md -> 2026-10-08 AM
    date_match = re.search(r'README\.(\d{4}\.\d{2}\.\d{2}(?:\.[A-Z]+)?)', filename)
    date_str = date_match.group(1).replace('.', '-') if date_match else "Unknown Date"

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1行目の見出し(# タイトル)または最初の数行を要約として取得
    lines = [line.strip() for line in content.split('\n') if line.strip() and not line.startswith('##')]
    summary = lines[0].replace('#', '').strip() if lines else "新しい対話ログが追加されました。"
    
    return f"- **{date_str}:** {summary}"

def update_context_md():
    context_file = 'CONTEXT.md'
    if not os.path.exists(context_file):
        return

    # README.*.md ファイルを全検索して最新順に並べる
    readme_files = sorted(
        [f for f in os.listdir('.') if f.startswith('README.') and f.endswith('.md')],
        reverse=True
    )

    summaries = []
    for r_file in readme_files:
        summaries.append(extract_summary_from_readme(r_file))

    new_summary_text = "\n".join(summaries)

    with open(context_file, 'r', encoding='utf-8') as f:
        context_content = f.read()

    # タグの間を自動置き換え
    pattern = r'(<!-- AUTO-GENERATED-SUMMARY:START -->)(.*?)(<!-- AUTO-GENERATED-SUMMARY:END -->)'
    replacement = f'\\1\n{new_summary_text}\n\\3'
    updated_content = re.sub(pattern, replacement, context_content, flags=re.DOTALL)

    with open(context_file, 'w', encoding='utf-8') as f:
        f.write(updated_content)
    print("CONTEXT.md has been successfully updated!")

if __name__ == '__main__':
    update_context_md()
