from pyscript import document

def calculate(event):
    wage_val = document.querySelector("#wage").value
    hours_val = document.querySelector("#hours").value
    
    if wage_val and hours_val:
        total = int(wage_val) * float(hours_val)
        document.querySelector("#result").innerText = f"合計: {total:,.0f} 円"