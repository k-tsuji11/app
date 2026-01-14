from pyscript import display
from js import document

def calculate(event):
    # 入力値を取得
    wage_str = document.getElementById("wage").value
    hours_str = document.getElementById("hours").value
    
    result_div = document.getElementById("result")
    
    # バリデーション
    if not wage_str or not hours_str:
        result_div.innerHTML = '<p style="color: #ef4444;">値を入力してください</p>'
        return

    try:
        wage = float(wage_str)
        hours = float(hours_str)
        total = wage * hours
        
        # カンマ区切りのフォーマット
        formatted_total = "{:,}".format(int(total))
        
        # HTMLを流し込む
        result_div.innerHTML = f"""
            <div style="font-size: 0.9rem; color: #666;">概算支給額</div>
            <div class="result-amount">{formatted_total}<span class="currency">円</span></div>
        """
    except Exception as e:
        result_div.innerHTML = f'<p style="color: #ef4444;">エラーが発生しました</p>'