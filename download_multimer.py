import os
import requests
import pandas as pd

header = [
    "#", "Model", "Gr.Code", "Group", "QSglob", "QSbest", "Mol.Size", "Stoich.",
    "Symm.", "SymmSize", "ICS(F1)", "Prec.Iface", "Recal.Iface", "lDDT",
    "DockQ_Avg", "IPS(JaccCoef)", "TMscore"
]

multimers = [
    "T0206o", "H0208", "H0215", "H0217", "T0218o", "H0220", "H0222", "H0223",
    "H0225", "H0227", "H0229", "H0230", "H0232", "H0233", "T0234o", "T0235o",
    "H0236", "T0237o", "T0240o", "H0244", "H0245", "T0257o", "H0258", "T0259o",
    "H0265", "H0267", "T0270o", "H0272", "T1201o", "H1202", "H1204", "T1206o",
    "H1208", "H1213", "H1215", "H1217", "T1218o", "T1219v1o", "H1220", "H1222",
    "H1223", "H1225", "H1227", "H1229", "H1230", "H1232", "H1233", "T1234o",
    "T1235o", "H1236", "T1237o", "T1240o", "H1244", "H1245", "T1249v1o",
    "T1249v2o", "T1257o", "H1258", "T1259o", "H1265", "H1265_v1", "H1265_v2",
    "H1265_v3", "H1267", "T1269v1o", "T1270o", "H1272", "T1292o", "T1294v1o",
    "T1295o", "T1295o_v2", "T1298o", "T2201o", "H2202", "H2204", "T2206o",
    "H2208", "H2213", "H2215", "H2217", "T2218o", "H2220", "H2222", "H2223",
    "H2225", "H2227", "H2229", "H2230", "H2232", "H2233", "T2234o", "T2235o",
    "H2236", "T2237o", "T2240o", "H2244", "H2245", "T2249v1o", "T2249v2o",
    "T2257o", "H2258", "T2259o", "H2265", "H2267", "T2270o", "H2272"
]

def multimer_url(target):
    return f'https://predictioncenter.org/casp16/multimer_results.cgi?target={target}&view=txt'

def download_multimer(target, csv_fn):
    response = requests.get(multimer_url(target))
    lines = [line.strip().split() for line in response.text.split('\n') if line.strip()]
    rows = [line_splt[:16] + line_splt[-1:] for line_splt in lines[2:]]
    df = pd.DataFrame(rows, columns=header)
    df.drop('#', axis=1, inplace=True)
    df.to_csv(csv_fn, index=False)
    
csv_dir = 'multimers'
os.makedirs(csv_dir, exist_ok=True)

for i, target in enumerate(multimers):
    print(f'Processing {target} ({i+1}/{len(multimers)})')
    download_multimer(target, os.path.join(csv_dir, target + '.csv'))
    