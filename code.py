from pyscript import display, window

from pyodide.ffi import create_proxy

def calculate(event=None):
    # （計算処理...）
    if event: # クリックイベントなどが発生した場合
        window.document.getElementById("coin-sound").play()

# ボタンクリックを監視する設定
btn = window.document.getElementById("calc-btn")
btn.addEventListener("click", create_proxy(calculate))

def calculate(event):
    # documentオブジェクトをwindowから取得
    doc = window.document
    
    # 入力値の取得
    wage_input = doc.getElementById("wage")
    hours_input = doc.getElementById("hours")
    result_div = doc.getElementById("result")
    
    # 値が空でないかチェック
    if not wage_input.value or not hours_input.value:
        result_div.innerHTML = '<p style="color: #ef4444;">数値を入力してください</p>'
        return

    try:
        # 計算処理
        wage = float(wage_input.value)
        hours = float(hours_input.value)
        total = int(wage * hours)
        
        # カンマ区切り
        formatted_total = "{:,}".format(total)
        
        # HTMLを更新
        result_div.innerHTML = f"""
            <div style="font-size: 0.9rem; color: #666; margin-bottom: 5px;">概算支給額</div>
            <div class="result-amount" style="font-size: 2rem; font-weight: bold; color: #6366f1;">
                {formatted_total}<span style="font-size: 1rem; margin-left: 4px;">円</span>
            </div>
        """
    except Exception as e:
        result_div.innerHTML = f'<p style="color: #ef4444;">エラー: {str(e)}</p>'