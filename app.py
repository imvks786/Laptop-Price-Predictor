# Developed by Vivek Singh
import pandas as pd
import numpy as np
from flask import request
import pickle
from flask import Flask, render_template,jsonify
from sklearn.linear_model import LinearRegression

# Get the directory where the app.py file is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# LOADING THE PICKEL FILE FROM DIRECTORY.
# model_train = pickle.load(open('C:/Users/Vivek/Desktop/LAPTOP PREDICTOR PROJECT/FRONT END DATA/model_ignore_cate.pkl','rb'))
# LOADING DATASET FOR FETECHING REQUIRED INFOMATIONS.
# df = pd.read_csv('C:/Users/Vivek/Desktop/LAPTOP PREDICTOR PROJECT/FRONT END DATA/final_data.csv')

# Load the pickled model file from the same directory as app.py
model_path = os.path.join(BASE_DIR, 'model_ignore_cate.pkl')
model_train = pickle.load(open(model_path, 'rb'))

# Load the dataset CSV from the same directory as app.py
data_path = os.path.join(BASE_DIR, 'final_data.csv')
df = pd.read_csv(data_path)


brand = sorted(df.brand.unique())
model = sorted(df.model.unique())
processor_name = sorted(df.processor_name.unique())
processor_brand = sorted(df.processor_brand.unique())
processor_gnrtn = sorted(df.processor_gnrtn.unique())
ram_gb = sorted(df.ram_gb.unique())
ssd = sorted(df.ssd.unique())
hdd = sorted(df.hdd.unique())
graphic_card_gb = sorted(df.graphic_card_gb.unique())
ram_type = sorted(df.ram_type.unique())
display = sorted(df.display_size.unique())
app = Flask(__name__)
 
 
@app.route("/")
def index():
    return render_template("index.html",
    brand=brand,
    display=display,
    ssd=ssd,
    hdd=hdd,
    model=model,
    processor_brand=processor_brand,
    processor_name=processor_name,
    processor_gnrtn=processor_gnrtn,
    ram_gb=ram_gb,
    graphic_card_gb = graphic_card_gb,
    ram_type = ram_type)


@app.route('/predict', methods=['POST'])
def predict():

    brand = request.form['brand_name']
    model = request.form['model']
    processor_brand = request.form['processor_brand']
    processor_name = request.form['processor_name']
    processor_gnrtn= request.form['processor_gnrtn']
    ram1 = request.form['ram_gb']
    ram = int(ram1)
    ram_type = request.form['ram_type']
    ssd1 = request.form['ssd']
    ssd = int(ssd1)
    hdd1 = request.form['hdd']
    hdd = int(hdd1)
    os = request.form['os']
    os_bit = request.form['os_bit']
    g = request.form['graphic_card_gb']
    graphic_card_gb = int(g)

    type = request.form['type']
    d = request.form['display_size']
    display_size = float(d)
    Touchscreen = request.form['Touchscreen']
    msoffice = request.form['msoffice']

    result = model_train.predict(pd.DataFrame(
        [[brand,model,processor_brand,processor_name,processor_gnrtn,ram,ram_type,ssd,hdd,os,os_bit,graphic_card_gb,
        type,display_size,Touchscreen,msoffice]],
        columns=['brand','model','processor_brand','processor_name','processor_gnrtn','ram_gb','ram_type','ssd','hdd','os','os_bit','graphic_card_gb','type',
          'display_size','Touchscreen','msoffice']
    ))
    r = str(float(np.round((result),2)))


    return render_template("predict.html",
    brand=brand,
    model=model,
    processor_brand=processor_brand,
    processor_name=processor_name,
    processor_gnrtn=processor_gnrtn,
    ram=ram,
    ssd=ssd,
    hdd=hdd,
    os=os,
    os_bit=os_bit,
    display_size=display_size,
    Touchscreen=Touchscreen,
    msoffice=msoffice,
    graphic_card_gb = graphic_card_gb,
    ram_type = ram_type,
    r=r)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/get_model', methods=['POST'])
def get_model():
    data = request.form['brand']
    b_model = df.loc[df['brand'] == data, 'model']
    b_model = b_model.unique()
    b_model = b_model.tolist()

    return jsonify(sorted(b_model))

@app.route('/get_processor',methods=['POST'])
def get_processor():
    pdata = request.form['p_brand']
    p_model = df.loc[df['processor_brand'] == pdata, 'processor_name']
    p_model = p_model.unique()
    p_model = p_model.tolist()
    if 'Genuine Windows' and 'Ryzen 7' and 'GeForce GTX' and 'GeForce RTX' and 'GEFORCE RTX' in p_model:
        p_model.remove('Genuine Windows')
        p_model.remove('Ryzen 7')
        p_model.remove('GeForce GTX')
        p_model.remove('GeForce RTX')
        p_model.remove('GEFORCE RTX')
        return jsonify(sorted(p_model))
    else:
        return jsonify(sorted(p_model))
    

app.run(debug=True)
# Developed by Vivek Singh
