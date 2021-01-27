import numpy as np
from ds_nlp.ae_extraction import ae_extraction
import pandas as pd
import pyreadr
import tensorflow

def test_string_function(string):
	return(string)
	
def test_math_function(x,y):
	return(x+y)
	
def test_numpy_function(x,y):
	return(np.add(x,y))

ae_model = ae_extraction()
def predict_ae(df):
  ae = ae_model.predict_df(df)
  ae['Date of Encounter'] = ae['Date of Encounter'].map(str)
  return ae

df=pyreadr.read_r('/share/mda_trial_PA19_0095/data/standardized/dat_notes_deltalake_current_pts.RDS')[None]
pt='AA';dt='2020-12-01'
df_test = df[(df.patient_letter==pt) & (df.encounter_date_local_tz.map(str)==dt)]
print('PY TESTING...')
print(predict_ae(df_test))
