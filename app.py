from flask import Flask, render_template,request

app = Flask(__name__)


@app.route('/')
def input():
    return render_template('input.html')



@app.route('/post',methods=['POST'])
def calculate():
    ticketSymbol = (request.form['ticketSymbol'])
    Allotment = (request.form['Allotment'])
    Final_share_price = (request.form['Final_share_price'])
    Sell_commission = (request.form['Sell_commission'])
    Inital_share_price = (request.form['Inital_share_price'])
    Buy_commission = (request.form['Buy_commission'])
    Captial_gain_tax_rate = (request.form['Captial_gain_tax_rate'])
    Proceeds = int(Allotment) * int(Final_share_price)
    gain = float(Proceeds) - float((int(Allotment) * int(Inital_share_price))) - float(int(Sell_commission) + int(Buy_commission))
    Cost = (float(round((float(Captial_gain_tax_rate) * float(gain)) / 100, 2))) + int(Sell_commission) + int(Buy_commission) + \
    (int(Allotment) * int(Inital_share_price))
    inter = Proceeds - (int(Allotment) * int(Inital_share_price)) + int(Sell_commission) + int(Buy_commission)
    NetProfit = Proceeds - Cost
    returnOI = NetProfit * 100 / Cost
    BreakEven = (float(Inital_share_price) * 100 + int(Sell_commission) + int(Buy_commission)) / 100
    return render_template('output.html',ticketSymbol=ticketSymbol,Proceeds=Proceeds,Cost=Cost,Buy_commission=Buy_commission,Sell_commission=Sell_commission,
                           NetProfit=NetProfit,  returnOI=returnOI,BreakEven=BreakEven)

if __name__ == '__main__':
    app.run()

