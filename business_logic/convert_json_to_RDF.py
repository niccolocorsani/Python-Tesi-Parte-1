import json

if __name__ == '__main__':
    json = {
        "NaOH KOH": [
            {
                "note": "si contabilizza come ton 100%, non soluzione tal quale"
            },
            {
                "Nome": "S810A",
                "nodo UA": "ns=2;s=0:LI810A/AI1/PV.CV",
                "UA data type": "float",
                "Nome strumento": "LI810A",
                "DV_path": "CELLE/STOCC_KOH",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "1000",
                "min / max": "2.5%-95%",
                "Prodotto": "KOH 50%",
                "densità [kg/m3]": "1500",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "OK"
            },
            {
                "Nome": "S810B",
                "nodo UA": "ns=2;s=0:LI810B/AI1/PV.CV",
                "UA data type": "float",
                "Nome strumento": "LI810B",
                "DV_path": "CELLE/STOCC_KOH",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "1000",
                "min / max": "2.5%-95%",
                "Prodotto": "KOH 50%",
                "densità [kg/m3]": "1500",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "OK"
            },
            {
                "Nome": "S803",
                "nodo UA": "N/A",
                "UA data type": "N/A",
                "Nome strumento": "LI803",
                "DV_path": "na",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "200",
                "min / max": "0%-90%",
                "Prodotto": "KOH 45-50%",
                "densità [kg/m3]": "1450-1500",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "OK"
            },
            {
                "Nome": "S 2101 A",
                "nodo UA": "ns=2;s=0:LI2101A/AI1/PV.CV",
                "UA data type": "float",
                "Nome strumento": "LT2101A",
                "DV_path": "AEREA2100/DISTR_POTASSA/LI2101A/AI1/PV",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "100",
                "min / max": "0%-95%",
                "Prodotto": "KOH 30%",
                "densità [kg/m3]": "1260",
                "destinazione": "consumo per KOH 50%",
                "Sorgente": "DCS Emerson"
            },
            {
                "Nome": "S 2101 B",
                "nodo UA": "ns=2;s=0:LI2101B/AI1/PV.CV",
                "UA data type": "float",
                "Nome strumento": "LT2101B",
                "DV_path": "AEREA2100/DISTR_POTASSA/LI2101B/AI1/PV",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "100",
                "min / max": "0%-95%",
                "Prodotto": "KOH 30%",
                "densità [kg/m3]": "1260",
                "destinazione": "consumo per KOH 50%",
                "Sorgente": "DCS Emerson"
            },
            {
                "note": "si contabilizza come ton 100%, non soluzione tal quale"
            },
            {
                "Nome": "starts-5104",
                "nodo UA": "ns=2;s=0:LI5104/AI1/PV.CV",
                "UA data type": "float",
                "Nome strumento": "LI5104",
                "DV_path": "AREA_SODA/_STOCC_SODA_CAUS//LI5104/AI1/PV",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "150",
                "min / max": "2%-95%",
                "Prodotto": "NaOH 50%",
                "densità [kg/m3]": "1500",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "OK"
            },
            {
                "Nome": "starts-822",
                "nodo UA": "ns=2;s=0:800LI822/AI1/PV.CV",
                "UA data type": "float",
                "Nome strumento": "LI822",
                "DV_path": "STOCCAGGI/STOCCAGGI-AI/800LI822",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "200",
                "min / max": "0%-90%",
                "Prodotto": "NaOH 30%",
                "densità [kg/m3]": "1330",
                "destinazione": "vendita e autoconsumo",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "OK"
            },
            {
                "Nome": "s2226b",
                "nodo UA": "ns=2;s=0:LI2226B/AI1/PV.CV",
                "UA data type": "float",
                "Nome strumento": "LI2226B",
                "DV_path": "AREA2200/PREP_NAOH/LI2226B",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "200",
                "min / max": "0%-90%",
                "Prodotto": "NaOH 30%",
                "densità [kg/m3]": "1330",
                "destinazione": "autoconsumo",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "A DCS VALORE 12,9%, ACQUISITO 13,6%"
            },
            {
                "Nome": "S5101",
                "nodo UA": "ns=2;s=0:LI5101/AI1/PV.CV",
                "UA data type": "float",
                "Nome strumento": "LI5101",
                "DV_path": "AREA_SODA/_STOCC_SODA_CAUS/LI5101",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "150",
                "min / max": "2%-95%",
                "Prodotto": "NaOH 30%",
                "densità [kg/m3]": "1330",
                "destinazione": "vendita e autoconsumo",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "OK"
            },
            {
                "note": "si contabilizza come ton 100%, non soluzione tal quale"
            },
            {
                "Nome": "s461",
                "Nome strumento": "LI461",
                "DV_path": "300-CO2/REC-CO2/300-LI461",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "20",
                "min / max": "0%-95%",
                "Prodotto": "K2CO3 sol. 50%",
                "densità [kg/m3]": "1520",
                "destinazione": "produzione e vendita",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "NON OK, VERIFCA INDIRIZZO OPCUA"
            },
            {
                "Nome": "starts-484",
                "nodo UA": "ns=2;s=0:800LI484/AI1/PV.CV",
                "UA data type": "float",
                "Nome strumento": "LI484",
                "DV_path": "STOCCAGGI/STOCCAGGI-AI/800LI484",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "25",
                "min / max": "0%-95%",
                "Prodotto": "K2CO3 sol. 50%",
                "densità [kg/m3]": "1520",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "OK"
            },
            {
                "Nome": "starts-486",
                "nodo UA": "ns=2;s=0:800LI486/AI1/PV.CV",
                "UA data type": "float",
                "Nome strumento": "LI486",
                "DV_path": "STOCCAGGI/STOCCAGGI-AI/800LI486",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "25",
                "min / max": "0%-95%",
                "Prodotto": "K2CO3 sol. 50%",
                "densità [kg/m3]": "1520",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "OK"
            },
            {
                "Nome": "starts-487",
                "nodo UA": "ns=2;s=0:800LI487/AI1/PV.CV",
                "UA data type": "float",
                "Nome strumento": "LI487",
                "DV_path": "STOCCAGGI/STOCCAGGI-AI/800LI487",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "55",
                "min / max": "0%-95%",
                "Prodotto": "K2CO3 sol. 50%",
                "densità [kg/m3]": "1520",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "OK"
            },
            {
                "Nome": "starts-488",
                "nodo UA": "ns=2;s=0:800LI488/AI1/PV.CV",
                "UA data type": "float",
                "Nome strumento": "LI488",
                "DV_path": "STOCCAGGI/STOCCAGGI-AI/800LI488",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "50",
                "min / max": "0%-95%",
                "Prodotto": "K2CO3 sol. 50%",
                "densità [kg/m3]": "1520",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "OK"
            },
            {
                "Nome": "Conversione KOH, linea 1",
                "nodo UA": "ns=2;s=0:HC-R2001-2/AO1/OUT.CV",
                "Nome strumento": "HC-R2001-2",
                "DV_path": "AREA2000/ELECTROLYSIS1_2/HC-R2001-2/AO1/OUT",
                "funzione": "regolazione carico elettrolisi (produzione)",
                "Unità di misura": "kA",
                "Volume [m3]": "n.a.",
                "min / max": "8 - 15.4 kA (28 - 53 ton/g cloro)",
                "Prodotto": "KOH",
                "densità [kg/m3]": "n.a.",
                "destinazione": "serbatoi produzione",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "NON OK, A 13,16 Ka prende 84,1 quindi la lettura è in % sul campo scala (0,841x15,4=13), si può provare a prendere lo strumento JIR 2003/4 e verificare?"
            },
            {
                "Nome": "SET POINT MODULO",
                "nodo UA": "ns=2;s=0:HC-R2001-2/BG1/SP.CV",
                "Nome strumento": "HC-R2001-2",
                "DV_path": "AREA2000/ELECTROLYSIS1_2/HC-R2001-2/BG1/SP.CV",
                "funzione": "SP regolazione carico elettrolisi (produzione)",
                "VERIFICA LETTURA DA UNIFI": "INSERIRE INDIRIZZO OPCUA PER POTER GESTIRE DA REMOTO IL SET POINT"
            },
            {
                "Nome": "Scrittura SP",
                "nodo UA": "ns=2;s=0:OPC_SP/HC-R2001-2_SP.CV",
                "Nome strumento": "HC-R2001-2"
            },
            {
                "Nome": "Conversione KOH, linea 2",
                "nodo UA": "ns=2;s=0:HC-R2003-4/AO1/OUT.CV",
                "Nome strumento": "HC-R2003-4",
                "DV_path": "AREA2000/ELECTROLYSIS1_2/HC-R2003-4/AO1/OUT",
                "funzione": "regolazione carico elettrolisi (produzione)",
                "Unità di misura": "kA",
                "Volume [m3]": "n.a.",
                "min / max": "9 - 15.4 kA (28 - 53 ton/g cloro)",
                "Prodotto": "KOH",
                "densità [kg/m3]": "n.a.",
                "destinazione": "serbatoi produzione",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "NON OK, A 13,16 Ka prende 84,1 quindi la lettura è in % sul campo scala (0,841x15,4=13), si può provare a prendere lo strumento JIR 2003/4 e verificare?"
            },
            {
                "Nome": "SET POINT MODULO",
                "nodo UA": "ns=2;s=0:HC-R2003-4/BG1/SP.CV",
                "Nome strumento": "HC-R2003-4",
                "DV_path": "AREA2000/ELECTROLYSIS1_2/HC-R2003-4/BG1/SP.CV",
                "funzione": "SP regolazione carico elettrolisi (produzione)",
                "VERIFICA LETTURA DA UNIFI": "INSERIRE INDIRIZZO OPCUA PER POTER GESTIRE DA REMOTO IL SET POINT"
            },
            {
                "Nome": "Scrittura SP",
                "nodo UA": "ns=2;s=0:OPC_SP/HC-R2003-4_SP.CV",
                "Nome strumento": "HC-R2003-4"
            },
            {
                "Nome": "Conversione KOH, linea 3",
                "nodo UA": "ns=2;s=0:HC-R2005-6/AO1/OUT.CV",
                "Nome strumento": "HC-R2005-6",
                "DV_path": "NEW_2015/FRIEM/HC-R2005-6/AO1/OUT",
                "funzione": "regolazione carico elettrolisi (produzione)",
                "Unità di misura": "kA",
                "Volume [m3]": "n.a.",
                "min / max": "10 - 15.4 kA (28 - 53 ton/g cloro)",
                "Prodotto": "KOH",
                "densità [kg/m3]": "n.a.",
                "destinazione": "serbatoi produzione",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "NON OK, A 13,16 Ka prende 84,1 quindi la lettura è in % sul campo scala (0,841x15,4=13), si può provare a prendere lo strumento JIR 2003/4 e verificare?"
            },
            {
                "Nome": "SET POINT MODULO",
                "nodo UA": "ns=2;s=0:HC-R2005-6/BG1/SP.CV",
                "Nome strumento": "HC-R2005-6",
                "DV_path": "NEW_2015/FRIEM/HC-R2005-6/BG1/SP.CV",
                "funzione": "SP regolazione carico elettrolisi (produzione)",
                "VERIFICA LETTURA DA UNIFI": "INSERIRE INDIRIZZO OPCUA PER POTER GESTIRE DA REMOTO IL SET POINT"
            },
            {
                "Nome": "Scrittura SP",
                "nodo UA": "ns=2;s=0:OPC_SP/HC-R2005-6_SP.CV",
                "Nome strumento": "HC-R2005-6"
            },
            {
                "Nome": "Conversione NaOH",
                "nodo UA": "ns=2;s=0:HC-R5001-2/AO1/OUT.CV",
                "Nome strumento": "HC-R5001-2",
                "DV_path": "AREA_SODA/FRIEM_R5001-2/HC-R5001-2/AO1/OUT",
                "funzione": "regolazione carico elettrolisi (produzione)",
                "Unità di misura": "kA",
                "Volume [m3]": "n.a.",
                "min / max": "5 - 24 kA (17 - 69 ton/g cloro)",
                "Prodotto": "NaOH",
                "densità [kg/m3]": "n.a.",
                "destinazione": "serbatoi produzione",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "NON OK, A 13,16 Ka prende 84,1 quindi la lettura è in % sul campo scala (0,841x15,4=13), si può provare a prendere lo strumento JIR 2003/4 e verificare?"
            },
            {
                "Nome": "SET POINT MODULO",
                "nodo UA": "ns=2;s=0:HC-R5001-2/BG1/SP.CV",
                "Nome strumento": "HC-R5001-2",
                "DV_path": "AREA_SODA/FRIEM_R5001-2/HC-R5001-2/BG1/SP.CV",
                "funzione": "SP regolazione carico elettrolisi (produzione)",
                "VERIFICA LETTURA DA UNIFI": "INSERIRE INDIRIZZO OPCUA PER POTER GESTIRE DA REMOTO IL SET POINT"
            },
            {
                "Nome": "Scrittura SP",
                "nodo UA": "ns=2;s=0:OPC_SP/HC-R2005-1_SP.CV",
                "Nome strumento": "HC-R5001-2"
            },
            {
                "Nome": "K2CO3 soluzione",
                "nodo UA": "N/A",
                "Nome strumento": "n.d.",
                "min / max": "max 12 ton/g (come 100%)",
                "note": "non ci sono disponibili strumenti che indichino la marcia impianto"
            },
            {
                "Nome": "KOH a scaglie",
                "nodo UA": "ns=2;s=0:198FIC-2301/PID1/PV.CV",
                "UA data type": "float",
                "Nome strumento": "FIC2301",
                "DV_path": "KOH/KOH-LOOP/198FIC-2301/PID1/PV",
                "funzione": "regolazione marcia impianto",
                "Unità di misura": "m3/h",
                "min / max": "1,15 - 1,65 (25 - 36 ton/g come 100%)",
                "Prodotto": "KOH",
                "densità [kg/m3]": "n.a.",
                "Sorgente": "DCS Emerson"
            },
            {
                "Nome": "Quantità NaOH per Batch NaClO",
                "nodo UA": "ns=2;s=0:700-FIC1702/PID1/PV.CV\r\nns=2;s=0:FQ1702-TOT/TOT.CV",
                "UA data type": "float",
                "Nome strumento": "FIC1702",
                "DV_path": "700-IPOCLORITO/700-LOOP/700FIC-1702/PID1/PV   700-IPOCLORITO/700-AI/FQ1702-TOT/TOT",
                "funzione": "misura portata e totalizzazione",
                "Unità di misura": "lt",
                "Volume [m3]": "14750",
                "Prodotto": "NaOH 30%",
                "densità [kg/m3]": "1330",
                "destinazione": "ipoclorito di sodio",
                "Sorgente": "DCS Emerson",
                "note": "la somma di queste due quantità dà il consumo di soda per ipoclorito di sodio, ma dà anche la produzione di ipoclorito di sodio",
                "VERIFICA LETTURA DA UNIFI": "ok, ma prende la totalizzazione generale, va fatta giornaliera"
            },
            {
                "Nome": "Quantità NaOH per Batch NaClO",
                "nodo UA": "ns=2;s=0:FIC2234-1/PID1/PV.CV\r\nns=2;s=0:FQI2234-1-TOT/TOT.CV ?",
                "UA data type": "float",
                "Nome strumento": "FIC2234-1",
                "DV_path": "AREA2200/PREP_NAOH/FIC2234-1/PID1/PV   AREA2200/PREP_NAOH/FQI2234-1/TOT",
                "funzione": "misura portata e totalizzazione",
                "Unità di misura": "m3",
                "Volume [m3]": "15.6",
                "Prodotto": "NaOH 30%",
                "densità [kg/m3]": "1330",
                "destinazione": "ipoclorito di sodio",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "ok, ma prende la totalizzazione generale, va fatta giornaliera"
            },
            {
                "Nome": "F_KOH Scaglie",
                "nodo UA": "ns=2;s=0:198FIC-2301/PID1/PV.CV",
                "UA data type": "float",
                "Nome strumento": "FIC2301",
                "DV_path": "KOH/KOH-LOOP/198FIC-2301/PID1/PV",
                "funzione": "regolazione portata",
                "Unità di misura": "m3/h",
                "Volume [m3]": "1.15-1.65",
                "Prodotto": "KOH 60%",
                "densità [kg/m3]": "1570",
                "destinazione": "KOH scaglie",
                "Sorgente": "DCS Emerson",
                "note": "misura al 60% va riportata al 50%, questa misura dà il consumo di KOH ma anche la produzione di KOH a scaglie"
            },
            {
                "Nome": "F_KOH K2CO3",
                "nodo UA": "ns=2;s=0:400FQI201/PROG_ACT.CV",
                "UA data type": "float",
                "Nome strumento": "FI201 distribuzione cloro idrogeno",
                "DV_path": "K2CO3/K2-AI/400FQI201/PROG_ACT",
                "funzione": "regolazione portata KOH a reattore",
                "Unità di misura": "lt/h",
                "Prodotto": "KOH 50%",
                "densità [kg/m3]": "1500",
                "destinazione": "Carbonato di Potassio gr.",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "FI201, indica 2099 l/h anziché 2480, qui però deve prendere la somma con FI407"
            },
            {
                "Nome strumento": "FI407",
                "funzione": "regolazione portata KOH a scrubber",
                "Unità di misura": "lt/h",
                "Prodotto": "KOH 50%",
                "densità [kg/m3]": "1500"
            },
            {
                "Nome": "F_KOH K2CO3 (l)",
                "nodo UA": "ns=2;s=0:300-LI461/AI1/PV.CV",
                "UA data type": "float",
                "Nome strumento": "LI461",
                "DV_path": "300-CO2/REC-CO2/300-LI461/AI1/PV",
                "Unità di misura": "%",
                "Prodotto": "KOH 50%",
                "densità [kg/m3]": "1500",
                "destinazione": "Carbonato di Potassio sol.",
                "Sorgente": "DCS Emerson",
                "note": "disponibile solo delta livello per misurare quantità consumata"
            },
            {
                "Nome": "KOH rampa 1, carico prodotti",
                "nodo UA": "ns=2;s=0:800FI801A_1/AI1/PV.CV\r\nns=2;s=0:800FQI801A_1/TOT.CV",
                "UA data type": "float",
                "Nome strumento": "FI801A/1 (FT810)",
                "DV_path": "CARICHI/800FI801A_1/AI1/PV   CARICHI/CAR_KOH/800FQI801A_1/TOT",
                "funzione": "misura portata e totalizzazione",
                "Unità di misura": "m3/ton",
                "Prodotto": "KOH 45-50%",
                "densità [kg/m3]": "1450-1500",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson"
            },
            {
                "Nome": "KOH rampa 2, carico prodotti",
                "nodo UA": "ns=2;s=0:800FI801A_2/AI1/PV.CV\r\nns=2;s=0:800FQI801A_2/TOT.CV",
                "UA data type": "float",
                "Nome strumento": "FI801A/2",
                "DV_path": "CARICHI/800FI801A_2/AI1/PV   CARICHI/CAR_KOH/800FQI801A_2/TOT",
                "funzione": "misura portata e totalizzazione",
                "Unità di misura": "m3",
                "Prodotto": "KOH 50%",
                "densità [kg/m3]": "1500",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson"
            },
            {
                "Nome": "KOH rampa 3, carico prodotti",
                "nodo UA": "ns=2;s=0:800FI801A_3/AI1/PV.CV\r\nns=2;s=0:800FQI801A_3/TOT.CV",
                "UA data type": "float",
                "Nome strumento": "FI801A/3",
                "DV_path": "CARICHI/CAR_KOH3/800FI801A_3/AI1/PV   \r\nCARICHI/CAR_KOH/800FQI801A_3/TOT",
                "funzione": "misura portata e totalizzazione",
                "Unità di misura": "m3",
                "Prodotto": "KOH 45-50%",
                "densità [kg/m3]": "1450-1500",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson"
            },
            {
                "Nome": "NaOH rampa 2, carico prodotti",
                "nodo UA": "ns=2;s=0:800FI5104/AI1/PV.CV\r\nns=2;s=0:800FQI5104/TOT.CV",
                "UA data type": "float",
                "Nome strumento": "FI5104",
                "DV_path": "CARICHI/CAR_NAOH/800FI5104/AI1/PV   CARICHI/CAR_NAOH/800FQI5104/TOT",
                "funzione": "misura portata e totalizzazione",
                "Unità di misura": "m3",
                "Prodotto": "NaOH 50%",
                "densità [kg/m3]": "1500",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson"
            },
            {
                "Nome": "NaOH rampa 3, carico prodotti",
                "nodo UA": "ns=2;s=0:800FI822/AI1/PV.CV\r\nns=2;s=0:800FQI822/TOT.CV",
                "UA data type": "float",
                "Nome strumento": "FI822",
                "DV_path": "CARICHI/CAR_NAOH/800FI822/AI1/PV   CARICHI/CAR_NAOH/800FQI822/TOT",
                "funzione": "misura portata e totalizzazione",
                "Unità di misura": "m3",
                "Prodotto": "NaOH 30%",
                "densità [kg/m3]": "1330",
                "Sorgente": "DCS Emerson"
            },
            {
                "Nome": "Quantità ordinata a vendita",
                "nodo UA": "N/A",
                "Nome strumento": "AS400",
                "Unità di misura": "kg",
                "Sorgente": "AS400",
                "note": "da uniformare unità di misura, alcuni clienti 100% altri titolo effettivo a vendita (45-50%), sia per KOH che per KOH che per K2CO3 soluzione"
            },
            {
                "Nome": "Portata KOH da elettrolisi a stocks 30%",
                "nodo UA": "ns=2;s=0:FI2004/AI1/PV.CV\r\nns=2;s=0:FQI2004-TOT/TOT.CV",
                "UA data type": "float",
                "Nome strumento": "FI2004",
                "DV_path": "AREA2000/ELECTROLYSIS_4/FI2004/AI1/PV   AREA2000/ELECTROLYSIS_4/FQI2004A-TOT/TOT",
                "funzione": "indicazione portata e totalizzazione",
                "Unità di misura": "m3/h-m3",
                "Prodotto": "KOH",
                "densità [kg/m3]": "1265",
                "destinazione": "intermedi di processo",
                "Sorgente": "DCS Emerson",
                "note": "attualmente in uso solo come indicazione perché dà un errore intorno al 2%",
                "VERIFICA LETTURA DA UNIFI": "OK"
            },
            {
                "Nome": "Portata NaOH da elettrolisi a stocks 30%",
                "nodo UA": "ns=2;s=0:FI5004/AI1/PV.CV\r\nns=2;s=0:FQI5004A-TOT/TOT.CV",
                "UA data type": "float",
                "Nome strumento": "FI5004",
                "DV_path": "AREA_SODA/_ELECTROLYSIS_4/FI5004/AI1/PV   AREA_SODA/_ELECTROLYSIS_4/FQI5004A-TOT/TOT",
                "funzione": "indicazione portata e totalizzazione",
                "Unità di misura": "m3/h-m3",
                "Prodotto": "NaOH",
                "densità [kg/m3]": "1320",
                "destinazione": "intermedi di processo",
                "Sorgente": "DCS Emerson",
                "note": "attualmente in uso solo come indicazione perché dà un errore intorno al 2%",
                "VERIFICA LETTURA DA UNIFI": "OK, STRUMENTO ROTTO"
            },
            {
                "Nome": "contatore sacchi 25 kg KOH scaglie",
                "nodo UA": "ns=2;s=0:198WI-4101/TOT.CV",
                "UA data type": "float",
                "Nome strumento": "WI4101",
                "DV_path": "KOH/KOH-DI/198WI-4101/TOT",
                "funzione": "totalizza la quantità insaccata",
                "Unità di misura": "N°",
                "Prodotto": "KOH scaglie",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "OK"
            },
            {
                "Nome": "contatore Big bags 1000 kg KOH scaglie",
                "nodo UA": "ns=2;s=0:198WI-4201/TOT.CV",
                "UA data type": "float",
                "Nome strumento": "WI4201",
                "DV_path": "KOH/KOH-DI/198WI-4201/TOT",
                "funzione": "totalizza la quantità insaccata",
                "Unità di misura": "N°",
                "Prodotto": "KOH scaglie",
                "VERIFICA LETTURA DA UNIFI": "OK"
            },
            {
                "note": "molti altri parametri di varia natura da considerare in 2° step"
            }
        ],
        "HCl": [
            {
                "Nome": "starts-871",
                "nodo UA": "ns=2;s=0:800LI871/AI1/PV.CV",
                "UA data type": "float",
                "Nome strumento": "LT871",
                "DV_path": "STOCCAGGI/STOCCAGGI-AI/800LI871/AI1/PV",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "135",
                "min max": "2%-95%",
                "Prodotto": "HCl >32%",
                "densità [kg/m3]": "1160",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson",
                "note": "OK"
            },
            {
                "Nome": "starts-872",
                "nodo UA": "ns=2;s=0:800LI872/AI1/PV.CV",
                "UA data type": "float",
                "Nome strumento": "LT872",
                "DV_path": "STOCCAGGI/STOCCAGGI-AI/800LI872/AI1/PV",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "135",
                "min max": "2%-95%",
                "Prodotto": "HCl >34%",
                "densità [kg/m3]": "1174",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson",
                "note": "OK"
            },
            {
                "Nome": "starts-873",
                "nodo UA": "ns=2;s=0:800LI873/AI1/PV.CV",
                "UA data type": "float",
                "Nome strumento": "LT873",
                "DV_path": "STOCCAGGI/STOCCAGGI-AI/800LI873/AI1/PV",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "135",
                "min max": "2%-95%",
                "Prodotto": "HCl >32%",
                "densità [kg/m3]": "1160",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson",
                "note": "OK"
            },
            {
                "Nome": "starts-874",
                "nodo UA": "ns=2;s=0:800LI874/AI1/PV.CV",
                "UA data type": "float",
                "Nome strumento": "LT874",
                "DV_path": "STOCCAGGI/STOCCAGGI-AI/800LI874/AI1/PV",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "135",
                "min max": "2%-95%",
                "Prodotto": "HCl >34%",
                "densità [kg/m3]": "1174",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson",
                "note": "OK"
            },
            {
                "Nome": "starts-875",
                "nodo UA": "ns=2;s=0:800LI875/AI1/PV.CV",
                "UA data type": "float",
                "Nome strumento": "LT875",
                "DV_path": "STOCCAGGI/STOCCAGGI-AI/800LI875/AI1/PV",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "135",
                "min max": "2%-95%",
                "destinazione": "emergenza",
                "Sorgente": "DCS Emerson",
                "note": "OK"
            },
            {
                "Nome": "starts-876",
                "nodo UA": "ns=2;s=0:800LI876/AI1/PV.CV",
                "UA data type": "float",
                "Nome strumento": "LT876",
                "DV_path": "STOCCAGGI/STOCCAGGI-AI/800LI876/AI1/PV",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "90",
                "min max": "2%-95%",
                "Prodotto": "HCl fuori specifica/HCl da CPS",
                "destinazione": "fuori specifica",
                "Sorgente": "DCS Emerson",
                "note": "OK"
            },
            {
                "Nome": "starts-877",
                "nodo UA": "ns=2;s=0:800LI877/AI1/PV.CV",
                "UA data type": "float",
                "Nome strumento": "LT877",
                "DV_path": "STOCCAGGI/STOCCAGGI-AI/800LI877/AI1/PV",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "90",
                "min max": "2%-95%",
                "Prodotto": "HCl >36%",
                "densità [kg/m3]": "1180",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson",
                "note": "OK"
            },
            {
                "Nome": "starts-878",
                "nodo UA": "ns=2;s=0:800LI878/AI1/PV.CV",
                "UA data type": "float",
                "Nome strumento": "LT878",
                "DV_path": "STOCCAGGI/STOCCAGGI-AI/800LI878/AI1/PV",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "90",
                "min max": "2%-95%",
                "Prodotto": "HCl >36%",
                "densità [kg/m3]": "1180",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson",
                "note": "OK"
            },
            {
                "Nome": "starts-879",
                "nodo UA": "ns=2;s=0:800LI879/AI1/PV.CV",
                "UA data type": "float",
                "Nome strumento": "LT879",
                "DV_path": "STOCCAGGI/STOCCAGGI-AI/800LI879/AI1/PV",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "90",
                "min max": "2%-95%",
                "Prodotto": "HCl >36%",
                "densità [kg/m3]": "1180",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson",
                "note": "OK"
            },
            {
                "Nome": "ul24",
                "nodo UA": "ns=2;s=0:100-FIC071/PID1/PV.CV",
                "UA data type": "float",
                "Nome strumento": "FIC071",
                "DV_path": "100-ACIDONE/HCL-1-LINEA/100-FIC071/PID1/PV",
                "funzione": "indicazione e controllo portata Cloro",
                "Unità di misura": "%",
                "min max": "40 - 85 (70 - 120 ton/g HCl 32%)",
                "Sorgente": "DCS Emerson",
                "note": "OK, IN %"
            },
            {
                "Nome": "ul22",
                "nodo UA": "ns=2;s=0:100-FIC072/PID1/SP.CV",
                "UA data type": "float",
                "Nome strumento": "FIC072",
                "DV_path": "100-ACIDONE/HCL-1-LINEA/100-FIC072/PID1/SP",
                "funzione": "SP portata H2",
                "note": "ACQUISIRE INIDIRIZZO OPCUA SIA DELLA MISURA STRUMENTO CHE SET POINT MODULO"
            },
            {
                "Nome": "ul22",
                "nodo UA": "ns=2;s=0:OPC_SP/100-FIC072_SP.CV",
                "UA data type": "float",
                "Nome strumento": "FIC072"
            },
            {
                "Nome": "ul31",
                "nodo UA": "ns=2;s=0:200-FIC101/PID1/PV.CV",
                "UA data type": "float",
                "Nome strumento": "FIC101",
                "DV_path": "200-ACIDINO/HCL-2-LINEA/200-FIC101/PID1/PV",
                "funzione": "indicazione e controllo portata Cloro",
                "Unità di misura": "%",
                "Sorgente": "DCS Emerson",
                "note": "ok, in Nm3/h e in kg/h"
            },
            {
                "Nome": "ul30",
                "nodo UA": "ns=2;s=0:200-FIC201/PID1/SP.CV",
                "UA data type": "float",
                "Nome strumento": "FIC201",
                "DV_path": "200-ACIDINO/HCL-2-LINEA/200-FIC201/PID1/SP",
                "funzione": "SP portata H2",
                "note": "ACQUISIRE INIDIRIZZO OPCUA SIA DELLA MISURA STRUMENTO CHE SET POINT MODULO"
            },
            {
                "Nome": "ul30",
                "nodo UA": "ns=2;s=0:OPC_SP/200-FIC201_SP.CV",
                "UA data type": "float",
                "Nome strumento": "FIC201"
            },
            {
                "Nome": "ul31",
                "nodo UA": "ns=2;s=0:FIC-101/PID1/PV.CV",
                "UA data type": "float",
                "Nome strumento": "FIC101",
                "DV_path": "SINTESI_HCL/CL-LOOP/FIC-101/PID1/PV",
                "funzione": "indicazione e controllo portata Cloro",
                "Unità di misura": "Nm3/h",
                "min max": "360 - 620 (90 - 120 ton/g HCl 35%)",
                "Sorgente": "DCS Emerson",
                "note": "ok in Nm3/h"
            },
            {
                "Nome": "portata IDROGENO a HCl 3 linea + SET POINT",
                "nodo UA": "ns=2;s=0:FIC-201/PID1/SP.CV",
                "UA data type": "float",
                "Nome strumento": "FIC201",
                "DV_path": "SINTESI_HCL/CL-LOOP/FIC-201/PID1/SP",
                "funzione": "SP portata H2",
                "note": "ACQUISIRE INIDIRIZZO OPCUA SIA DELLA MISURA STRUMENTO CHE SET POINT MODULO"
            },
            {
                "Nome": "Scrittura SP",
                "nodo UA": "ns=2;s=0:OPC_SP/FIC-201_SP.CV",
                "UA data type": "float",
                "Nome strumento": "FIC201"
            },
            {
                "Nome": "ul25",
                "nodo UA": "ns=2;s=0:500FIC-640_2/PID1/PV.CV",
                "UA data type": "float",
                "Nome strumento": "FIC640-2",
                "DV_path": "HCL_LINEA_4/CL4-LOOP/500FIC-640_2/PID1/PV",
                "funzione": "indicazione e controllo portata Cloro",
                "Unità di misura": "Nm3/h",
                "min max": "360 - 620 (90 - 120 ton/g HCl 36%)",
                "Sorgente": "DCS Emerson",
                "note": "ok in Nm3/h"
            },
            {
                "Nome": "portata IDROGENO a HCl 4 linea + SET POINT",
                "nodo UA": "ns=2;s=0:500FIC-640_1/PID1/SP.CV",
                "UA data type": "float",
                "Nome strumento": "FIC640-1",
                "DV_path": "HCL_LINEA_4/CL4-LOOP/500FIC-640_1/PID1/PV",
                "funzione": "SP portata H2",
                "Unità di misura": "Nm3/h",
                "note": "ACQUISIRE INIDIRIZZO OPCUA SIA DELLA MISURA STRUMENTO CHE SET POINT MODULO"
            },
            {
                "Nome": "Scrittura SP",
                "nodo UA": "ns=2;s=0:OPC_SP/500FIC-640_2_SP.CV",
                "UA data type": "float",
                "Nome strumento": "FIC640-1",
                "Unità di misura": "Nm3/h"
            },
            {
                "Nome": "Quantità per FeCl3 standard",
                "nodo UA": "N/A",
                "Sorgente": "DCS Emerson"
            },
            {
                "Nome": "Quantità per elettrolisi KOH",
                "nodo UA": "N/A",
                "Sorgente": "DCS Emerson"
            },
            {
                "Nome": "Quantità per elettrolisi NaOH",
                "nodo UA": "N/A",
                "Sorgente": "DCS Emerson",
                "note": "misura al 60% va riportata al 50%"
            },
            {
                "Nome": "Quantità per TAS",
                "nodo UA": "N/A",
                "Sorgente": "DCS Emerson"
            },
            {
                "Sorgente": "DCS Emerson",
                "note": "disponibile solo delta livello per misurare quantità consumata"
            },
            {
                "Nome": "HCl rampa 1, carico prodotti",
                "nodo UA": "N/A",
                "funzione": "misura portata e totalizzazione",
                "Unità di misura": "m3/ton",
                "Prodotto": "HCl 32-37%",
                "densità [kg/m3]": "1160 - 1180",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson"
            },
            {
                "Nome": "HCl rampa 2, carico prodotti",
                "nodo UA": "N/A",
                "funzione": "misura portata e totalizzazione",
                "Unità di misura": "m3",
                "Prodotto": "HCl 32-37%",
                "densità [kg/m3]": "1160 - 1180",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson"
            },
            {
                "Nome": "Quantità ordinata a vendita",
                "nodo UA": "N/A",
                "Nome strumento": "AS400",
                "Unità di misura": "kg",
                "Sorgente": "AS400",
                "note": "da suddividere il prodotto nei tre titoli 32-34-36% come gli stock"
            },
            {
                "Nome": "ul26",
                "nodo UA": "ns=2;s=0:100-FIC074/PID1/PV.CV",
                "UA data type": "float",
                "Nome strumento": "FIC074",
                "DV_path": "100-ACIDONE/HCL-1-LINEA/100-FIC074/PID1/PV",
                "funzione": "regolazione portata acqua demi",
                "Unità di misura": "%",
                "Prodotto": "acqua demi",
                "Sorgente": "DCS Emerson"
            },
            {
                "Nome": "portata HCl a stock",
                "nodo UA": "ns=2;s=0:100-FI075/AI1/PV.CV\r\nns=2;s=0:100-FQ075/TOT.CV",
                "UA data type": "float",
                "Nome strumento": "FI075",
                "DV_path": "100-ACIDONE/HCL-1-LINEA/100-FI075/AI1/PV   100-ACIDONE/HCL-1-LINEA/100-FQ075/TOT",
                "funzione": "indicazione e totalizzazione portata prodotto",
                "Unità di misura": "m3/h-m3",
                "Prodotto": "HCl",
                "Sorgente": "DCS Emerson",
                "note": "OK"
            },
            {
                "Nome": "ul35",
                "nodo UA": "ns=2;s=0:200-FIC401/PID1/PV.CV",
                "UA data type": "float",
                "Nome strumento": "FIC401",
                "DV_path": "200-ACIDINO/HCL-2-LINEA/200-FIC401/PID1/PV",
                "funzione": "regolazione portata acqua demi",
                "Unità di misura": "%"
            },
            {
                "Nome": "ul25",
                "nodo UA": "ns=2;s=0:200-FI602/AI1/PV.CV",
                "UA data type": "float",
                "Nome strumento": "FI602",
                "DV_path": "200-ACIDINO/HCL-2-LINEA/200-FI602/AI1/PV",
                "funzione": "indicazione e totalizzazione portata prodotto",
                "Unità di misura": "m3/h-m3",
                "note": "OK"
            },
            {
                "Nome": "ul35",
                "nodo UA": "ns=2;s=0:FIC-401/PID1/PV.CV",
                "UA data type": "float",
                "Nome strumento": "FIC401",
                "DV_path": "SINTESI_HCL/CL-LOOP/FIC-401/PID1/PV",
                "funzione": "regolazione portata acqua demi",
                "Unità di misura": "kg/h",
                "Prodotto": "acqua demi",
                "Sorgente": "DCS Emerson",
                "note": "OK"
            },
            {
                "Nome": "portata HCl a stock",
                "nodo UA": "ns=2;s=0:FI-600/AI1/PV.CV\r\nns=2;s=0:FQI600/PROG_ACT.CV",
                "UA data type": "float",
                "Nome strumento": "FI600",
                "DV_path": "SINTESI_HCL/CL-AI/FI-600/AI1/PV\r\nSINTESI_HCL/CL-TOT/FQI600/PROG_ACT.CV",
                "funzione": "indicazione e totalizzazione portata prodotto",
                "Unità di misura": "m3/h-m3",
                "Prodotto": "HCl",
                "Sorgente": "DCS Emerson",
                "note": "OK"
            },
            {
                "Nome": "portata acqua demi",
                "nodo UA": "ns=2;s=0:500FIC-670/PID1/PV.CV",
                "UA data type": "float",
                "Nome strumento": "FIC670",
                "DV_path": "HCL_LINEA_4/CL4-LOOP/500FIC-670/PID1/PV",
                "funzione": "regolazione portata acqua demi",
                "Unità di misura": "kg/h",
                "Prodotto": "acqua demi",
                "Sorgente": "DCS Emerson",
                "note": "OK"
            },
            {
                "Nome": "hclexit",
                "nodo UA": "ns=2;s=0:FI-604/AI1/PV.CV\r\nns=2;s=0:FQI604/PROG_ACT.CV\r\n",
                "UA data type": "float",
                "Nome strumento": "FI604",
                "DV_path": "HCL_LINEA_4/CL4-AI/FI-604/PID1/PV\r\nHCL_LINEA_4/CL4-TOT/FQI604/TOT",
                "funzione": "indicazione e totalizzazione portata prodotto",
                "Unità di misura": "m3/h-m3",
                "Prodotto": "HCl",
                "Sorgente": "DCS Emerson",
                "note": "OK"
            },
            {
                "note": "molti altri parametri di varia natura da considerare in 2° step"
            }
        ],
        "cloroparaffine (CPS)": [
            {
                "Nome": "STOCKS CLOROPARAFFINE"
            },
            {
                "Nome": "s-4303start",
                "nodo UA": "ns=2;s=0:LI4303/AI1/PV.CV",
                "Nome strumento": "LI4303",
                "DV_path": "CPS/FF_AI_/LI4303/AI1/PV",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "55",
                "min max": "0%-95%",
                "Prodotto": "Essechlor CL47",
                "densità [kg/m3]": "1210",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson",
                "note": "la tipologia di prodotto contenuta nei serbatoi può cambiare a seconda delle richieste commerciali in quanto le tipologie di Cloroparaffina a vendita sono oltre 30, i serbatoi hanno a DCS etichetta con il nome del prodotto contenuto, impostato manualemnte da operatore",
                "VERIFICA LETTURA DA UNIFI": "ok"
            },
            {
                "Nome": "s-4304",
                "nodo UA": "ns=2;s=0:LI4318/AI1/PV.CV",
                "Nome strumento": "LI4318",
                "DV_path": "CPS/FF_AI_/LI4318/AI1/PV",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "50",
                "min max": "0%-95%",
                "Prodotto": "Essechlor 52",
                "densità [kg/m3]": "1265",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "ok"
            },
            {
                "Nome": "s4305exit",
                "nodo UA": "ns=2;s=0:LI4323/AI1/PV.CV",
                "Nome strumento": "LI4323",
                "DV_path": "CPS/FF_AI_/LI4323/AI1/PV",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "50",
                "min max": "0%-95%",
                "Prodotto": "Essechlor 52",
                "densità [kg/m3]": "1265",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "ok"
            },
            {
                "Nome": "s-4306",
                "nodo UA": "ns=2;s=0:LI4328/AI1/PV.CV",
                "Nome strumento": "LI4328",
                "DV_path": "CPS/FF_AI_/LI4328/AI1/PV",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "35",
                "min max": "0%-95%",
                "Prodotto": "Essechlor 45",
                "densità [kg/m3]": "1185",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "ok"
            },
            {
                "Nome": "s-4307",
                "nodo UA": "ns=2;s=0:LI4333/AI1/PV.CV",
                "Nome strumento": "LI4333",
                "DV_path": "CPS/FF_AI_/LI4333/AI1/PV",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "35",
                "min max": "0%-95%",
                "Prodotto": "Essechlor CL40",
                "densità [kg/m3]": "1120",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "0k"
            },
            {
                "Nome": "ul151",
                "nodo UA": "ns=2;s=0:FIC4108/PID1/PV.CV",
                "Nome strumento": "FIC4108",
                "DV_path": "CPS_R4001/R4001_FF_PID/FIC4108/PID1/PV",
                "funzione": "indicazione e controllo portata Cloro R 4001",
                "Unità di misura": "Nm3/h",
                "min max": "50-350",
                "Prodotto": "cloro",
                "densità [kg/m3]": "3 kg/Nm3",
                "Sorgente": "DCS Emerson",
                "note": "misura non troppo attendibile, la produzione in CPS dipende dal tipo di prodotto oltre che dalla portata di cloro alimentata. La produzione media è 12.5 ton ogni 35 ore",
                "VERIFICA LETTURA DA UNIFI": "ok, ACQUISIRE SET POINT PORTATA"
            },
            {
                "Nome": "ul151",
                "nodo UA": "ns=2;s=0:FIC4108/PID1/SP.CV",
                "Nome strumento": "FIC4108",
                "DV_path": "CPS_R4001/R4001_FF_PID/FIC4108/PID1/SP.CV",
                "funzione": "SP portata Cloro R 4001"
            },
            {
                "Nome": "ul151",
                "nodo UA": "ns=2;s=0:OPC_SP/FIC4108_SP.CV",
                "Nome strumento": "FIC4108"
            },
            {
                "Nome": "hv4204",
                "nodo UA": "ns=2;s=0:FIC4208/PID1/PV.CV",
                "Nome strumento": "FIC4208",
                "DV_path": "CPS/FF_PID_/FIC4208/PID1/PV",
                "funzione": "indicazione e controllo portata Cloro R 4002",
                "Unità di misura": "Nm3/h",
                "min max": "50-350",
                "Prodotto": "cloro",
                "densità [kg/m3]": "3 kg/Nm3",
                "Sorgente": "DCS Emerson",
                "note": "misura non troppo attendibile, la produzione in CPS dipende dal tipo di prodotto oltre che dalla portata di cloro alimentata. La produzione media è 12.5 ton ogni 35 ore",
                "VERIFICA LETTURA DA UNIFI": "ok (strumento rotto), ACQUISIRE SET POINT PORTATA"
            },
            {
                "Nome": "hv4204",
                "nodo UA": "ns=2;s=0:FIC4208/PID1/SP.CV",
                "Nome strumento": "FIC4208",
                "DV_path": "CPS/FF_PID_/FIC4208/PID1/SP.CV",
                "funzione": "SP portata Cloro R 4002"
            },
            {
                "Nome": "hv4204",
                "nodo UA": "ns=2;s=0:OPC_SP/FIC4208_SP.CV",
                "Nome strumento": "FIC4208"
            },
            {
                "Nome": "ul144",
                "nodo UA": "ns=2;s=0:FIC4208C/PID1/PV.CV",
                "Nome strumento": "FIC4208C",
                "DV_path": "CPS_R4003/R4003_FF_PID/FIC4208C/PID1/PV",
                "funzione": "indicazione e controllo portata Cloro R 4003",
                "Unità di misura": "Nm3/h",
                "min max": "50-350",
                "Prodotto": "cloro",
                "densità [kg/m3]": "3 kg/Nm3",
                "Sorgente": "DCS Emerson",
                "note": "misura non troppo attendibile, la produzione in CPS dipende dal tipo di prodotto oltre che dalla portata di cloro alimentata. La produzione media è 12.5 ton ogni 35 ore",
                "VERIFICA LETTURA DA UNIFI": "ok, ACQUISIRE SET POINT PORTATA"
            },
            {
                "Nome": "ul144",
                "nodo UA": "ns=2;s=0:FIC4208C/PID1/SP.CV",
                "Nome strumento": "FIC4208C",
                "DV_path": "CPS_R4003/R4003_FF_PID/FIC4208C/PID1/SP.CV",
                "funzione": "SP portata Cloro R 4003"
            },
            {
                "Nome": "ul144",
                "nodo UA": "ns=2;s=0:OPC_SP/FIC4208C_SP.CV",
                "Nome strumento": "FIC4208C"
            },
            {
                "Nome strumento": "AS400",
                "Unità di misura": "kg",
                "Sorgente": "AS400",
                "note": "da suddividere il prodotto nei tre titoli 32-34-36% come gli stock"
            },
            {
                "Nome": "r-4001",
                "nodo UA": "ns=2;s=0:WI4141/AI1/PV.CV",
                "Nome strumento": "WI4141",
                "DV_path": "CPS_R4001/R4001_AI/WI4141/AI1/PV",
                "funzione": "indicazione peso reattore R 4001",
                "Unità di misura": "kg",
                "Volume [m3]": "12.5",
                "min max": "0 - 13500",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "ok"
            },
            {
                "Nome": "r-4001",
                "nodo UA": "ns=2;s=0:PI4122/AI1/PV.CV",
                "Nome strumento": "PI4122",
                "DV_path": "CPS_R4001/R4001_FF_AI/PI4122/AI1/PV",
                "funzione": "indicazione pressione reattore R 4001",
                "Unità di misura": "mmH2O",
                "min max": " -100 - 0",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "ok"
            },
            {
                "Nome": "r-4001",
                "nodo UA": "ns=2;s=0:TIC4118/PID1/PV.CV",
                "Nome strumento": "TIC4118",
                "DV_path": "CPS_R4001/R4001_FF_PID/TIC4118/PID1/PV",
                "funzione": "indicazione temperatura reattore R 4001",
                "Unità di misura": "°C",
                "min max": " 75 - 90",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "ok"
            },
            {
                "Nome": "r-4002",
                "nodo UA": "ns=2;s=0:WI4241/AI1/PV.CV",
                "Nome strumento": "WI4241",
                "DV_path": "CPS/AI_/WI42417AI1/PV",
                "funzione": "indicazione peso reattore R 4002",
                "Unità di misura": "kg",
                "Volume [m3]": "12.5",
                "min max": "0 - 13500",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "ok"
            },
            {
                "Nome": "r-4002",
                "nodo UA": "ns=2;s=0:PI4222/AI1/PV.CV",
                "Nome strumento": "PI4222",
                "DV_path": "CPS/FF_AI_/PI4222/AI1/PV",
                "funzione": "indicazione pressione reattore R 4002",
                "Unità di misura": "mmH2O",
                "min max": " -100 - 0",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "ok"
            },
            {
                "Nome": "r-4002",
                "nodo UA": "ns=2;s=0:TIC4218/PID1/PV.CV",
                "Nome strumento": "TIC4218",
                "DV_path": "CPS/FF_PID_/TIC4218PID1/PV",
                "funzione": "indicazione temperatura reattore R 4002",
                "Unità di misura": "°C",
                "min max": " 75 - 90",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "ok"
            },
            {
                "Nome": "r-4003",
                "nodo UA": "ns=2;s=0:WI4343/AI1/PV.CV",
                "Nome strumento": "WI4343",
                "DV_path": "CPS_R4003/R4003_AI/WI4343/AI1/PV",
                "funzione": "indicazione peso reattore R 4003",
                "Unità di misura": "kg",
                "Volume [m3]": "12.5",
                "min max": "0 - 13500",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "ok"
            },
            {
                "Nome": "r-4003",
                "nodo UA": "ns=2;s=0:PI4322/AI1/PV.CV",
                "Nome strumento": "PI4322",
                "DV_path": "CPS_R4003/R4003_FF_AI/PI4322/Ai1/PV",
                "funzione": "indicazione pressione reattore R 4003",
                "Unità di misura": "mmH2O",
                "min max": " -100 - 0",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "ok"
            },
            {
                "Nome": "r-4003",
                "nodo UA": "ns=2;s=0:TIC4318/AI1/PV.CV",
                "Nome strumento": "TIC4318",
                "DV_path": "CPS_R4003/R4003_FF_PID/TIC4318/PID1/PV",
                "funzione": "indicazione temperatura reattore R 4003",
                "Unità di misura": "°C",
                "min max": " 75 - 90",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "ok"
            },
            {
                "Nome": "Pressione gas ai limiti di batteria impianto",
                "nodo UA": "ns=2;s=0:PI4540/AI1/PV.CV",
                "Nome strumento": "PI4540",
                "DV_path": "CPS/AI_/PI4540/AI1/PV",
                "funzione": "indicazione di pressione",
                "Unità di misura": "mmH2O",
                "min max": " -200 - -50",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "ok"
            }
        ],
        "ipoclorito di sodio": [
            {
                "Nome": "S851",
                "nodo UA": "ns=2;s=0:800LI851/AI1/PV.CV",
                "Nome strumento": "LI851",
                "DV_path": "STOCCAGGI/STOCCAGGI-AI/800LI851/AI1/PV",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "50",
                "min max": "0%-95%",
                "Prodotto": "ipoclorito di sodio",
                "densità [kg/m3]": "1250",
                "destinazione": "vendita/fuori specifica",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "OK"
            },
            {
                "Nome": "S852",
                "nodo UA": "ns=2;s=0:800LI852/AI1/PV.CV",
                "Nome strumento": "LI852",
                "DV_path": "STOCCAGGI/STOCCAGGI-AI/800LI852/AI1/PV",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "50",
                "min max": "0%-95%",
                "Prodotto": "ipoclorito di sodio",
                "densità [kg/m3]": "1250",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "OK"
            },
            {
                "Nome": "S854",
                "nodo UA": "ns=2;s=0:800LI854/AI1/PV.CV",
                "Nome strumento": "LI854",
                "DV_path": "STOCCAGGI/STOCCAGGI-AI/800LI854/AI1/PV",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "50",
                "min max": "0%-95%",
                "Prodotto": "ipoclorito di sodio",
                "densità [kg/m3]": "1250",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "OK"
            },
            {
                "Nome": "S856",
                "nodo UA": "ns=2;s=0:800LI856/AI1/PV.CV",
                "Nome strumento": "LI856",
                "DV_path": "STOCCAGGI/STOCCAGGI-AI/800LI856/AI1/PV",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "50",
                "min max": "0%-95%",
                "Prodotto": "ipoclorito di sodio",
                "densità [kg/m3]": "1250",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "OK"
            },
            {
                "Nome": "S857",
                "nodo UA": "ns=2;s=0:800LI857/AI1/PV.CV",
                "Nome strumento": "LI857",
                "DV_path": "STOCCAGGI/STOCCAGGI-AI/800LI857/AI1/PV",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "50",
                "min max": "0%-95%",
                "Prodotto": "ipoclorito di sodio",
                "densità [kg/m3]": "1250",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "OK"
            },
            {
                "Nome": "portata cloro",
                "nodo UA": "ns=2;s=0:FT-IPOSODIO/AI1/PV.CV",
                "Nome strumento": "FI Iposodio",
                "DV_path": "HCL/FT-IPOSODIO/AI1/PV",
                "funzione": "indicazione portata",
                "Unità di misura": "kg/h",
                "min max": "0 - 800 (40 - 100 ton/g di prodotto)",
                "densità [kg/m3]": "3 kg/Nm3",
                "Sorgente": "DCS Emerson",
                "note": "non affidabile",
                "VERIFICA LETTURA DA UNIFI": "non affidabile"
            },
            {
                "Sorgente": "DCS Emerson"
            },
            {
                "Nome": "carico iposodio",
                "nodo UA": "ns=2;s=0:800FI851/AI1/PV.CV\r\nns=2;s=0:800FQI851/TOT.CV",
                "Nome strumento": "FI851",
                "DV_path": "CARICHI/800FI851/AI1/PV   CARICHI/CAR_IPOSODIO/800FQI851/TOT",
                "funzione": "misura portata e totalizzazione",
                "Unità di misura": "m3",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "OK"
            },
            {
                "Nome": "Quantità ordinata a vendita",
                "Nome strumento": "AS400",
                "Unità di misura": "kg",
                "Sorgente": "AS400"
            },
            {
                "Nome": "Analizzatore concentrazione NaOH residua (Applikon)",
                "nodo UA": "ns=2;s=0:700-AI1725/AI1/OUT.CV",
                "Nome strumento": "AI1725",
                "DV_path": "700-IPOCLORITO/700-AI/700-AI1725/AI1/OUT",
                "funzione": "misura OH",
                "Unità di misura": "g/lt",
                "min max": "10 - 250",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "OK"
            },
            {
                "Nome": "misura densità soluzione in produzione",
                "nodo UA": "ns=2;s=0:700-DI1726/AI1/OUT.CV\r\nns=2;s=0:700-DI1726/CALC2/OUT1.CV",
                "Nome strumento": "DI1726",
                "DV_path": "700-IPOCLORITO/700-AI/700-DI1726/(AI1/OUT.CV o CALC2/OUT1.CV)",
                "funzione": "misura densità soluzione in riciclo\r\n\r\nDensità non calcolata con temperatura\r\n700-IPOCLORITO/700-AI/700-DI1726/AI1/OUT\r\n\r\nDensità calcolata con temperatura\r\n700-IPOCLORITO/700-AI/700-DI1726/CALC2/OUT1",
                "Unità di misura": "kg/lt",
                "min max": "1240 - 1270",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "OK"
            },
            {
                "Nome": "Pressione collettore aspirazione",
                "nodo UA": "ns=2;s=0:700-PIC1701/PID1/PV.CV",
                "Nome strumento": "PIC1701",
                "DV_path": "700-IPOCLORITO/700-LOOP/700-PIC1701/PID1/PV",
                "funzione": "misura pressione aspirazione vari impianti",
                "Unità di misura": "mmH2O",
                "min max": " -200 - -300",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "OK"
            },
            {
                "Nome": "Pressione (rinominato: pressioneretecloro)",
                "nodo UA": "ns=2;s=0:PIC2204/PID1/PV.CV",
                "Unità di misura": "mmH2O",
                "min max": "0-6000"
            },
            {
                "Nome": "SP Pressione (rinominato: SP_pressioneretecloro)",
                "nodo UA": "ns=2;s=0:PIC2204/PID1/SP.CV",
                "Unità di misura": "mmH2O"
            },
            {
                "Nome": "Scrittura SP (rinominato: scritturaSP_pressioneretecloro)",
                "nodo UA": "ns=2;s=0:OPC_SP/PIC2204_SP.CV",
                "Unità di misura": "mmH2O"
            }
        ],
        "Cloruro Ferrico-Ferroso Pot.le": [
            {
                "Nome": "s-904d",
                "nodo UA": "ns=2;s=0:800LI904D/AI1/PV.CV",
                "Nome strumento": "LI904D",
                "DV_path": "STOCCAGGI/STOCCAGGI-AI/800LI904D/AI1/PV",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "135",
                "min max": "5%-95%",
                "Prodotto": "Cloruro Ferrico 40%",
                "densità [kg/m3]": "1440",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "OK"
            },
            {
                "Nome": "s-904e",
                "nodo UA": "ns=2;s=0:800LI904E/AI1/PV.CV",
                "Nome strumento": "r",
                "DV_path": "STOCCAGGI/STOCCAGGI-AI/800LI904E/AI1/PV",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "135",
                "min max": "5%-95%",
                "Prodotto": "Cloruro Ferrico 40%",
                "densità [kg/m3]": "1440",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "OK"
            },
            {
                "Nome": "s-954a",
                "nodo UA": "ns=2;s=0:800LI954A/AI1/PV.CV",
                "Nome strumento": "LI954A",
                "DV_path": "STOCCAGGI/STOCCAGGI-AI/800LI954A/AI1/PV",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "50",
                "min max": "5%-95%",
                "Prodotto": "Cloruro Ferroso 30%",
                "densità [kg/m3]": "1400",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "OK"
            },
            {
                "Nome": "s-954b",
                "nodo UA": "ns=2;s=0:800LI954B/AI1/PV.CV",
                "Nome strumento": "LI954B",
                "DV_path": "STOCCAGGI/STOCCAGGI-AI/800LI954B/AI1/PV",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "50",
                "min max": "5%-95%",
                "Prodotto": "Cloruro Ferroso 30%",
                "densità [kg/m3]": "1400",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "OK"
            },
            {
                "Nome": "s-901",
                "Nome strumento": "LI901",
                "funzione": "inidcazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "50",
                "min max": "5%-95%",
                "Prodotto": "Acido esausto",
                "densità [kg/m3]": "1150",
                "destinazione": "M.P.",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "manca indirizzo OPCUA"
            },
            {
                "Nome": "S 910 A",
                "Nome strumento": "LI910A",
                "funzione": "inidcazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "135",
                "min max": "5%-95%",
                "Prodotto": "Acido esausto",
                "densità [kg/m3]": "1150",
                "destinazione": "M.P.",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "strumento da configurare, manca indirizzo OPCUA"
            },
            {
                "Nome": "c980",
                "nodo UA": "ns=2;s=0:900FIC986/PID1/PV.CV",
                "Nome strumento": "900FIC986",
                "DV_path": "FERRICO/FE-LOOP/900FIC986/PID1/PV",
                "funzione": "indicazione e regolazione portata",
                "Unità di misura": "Nm3/h",
                "min max": "0-300 (0 - 40 ton/g di FeCl2+FeCl3)",
                "densità [kg/m3]": "3 kg/Nm3",
                "Sorgente": "DCS Emerson"
            },
            {
                "Nome": "c980",
                "nodo UA": "ns=2;s=0:900FIC986/PID1/SP.CV",
                "Nome strumento": "900FIC986",
                "DV_path": "FERRICO/FE-LOOP/900FIC986/PID1/SP.CV"
            },
            {
                "Nome": "c980",
                "nodo UA": "ns=2;s=0:OPC_SP/900FIC986_SP.CV",
                "Nome strumento": "900FIC986"
            },
            {
                "Nome": "c-910",
                "Nome strumento": "FIC912",
                "funzione": "indicazione e regolazione portata",
                "Unità di misura": "Nm3/h",
                "min max": "0-150",
                "VERIFICA LETTURA DA UNIFI": "NON ANCORA INSTALLATO, DA INSERIRE INDIRIZZO OPCUA"
            },
            {
                "Nome": "portata acido esausto",
                "nodo UA": "ns=2;s=0:900-FIC901/PID1/PV.CV",
                "Nome strumento": "900-FIC901",
                "DV_path": "900-FERRICO/900-LOOP/900-FIC901/PID1/PV.CV",
                "funzione": "indicazione e regolazione portata",
                "Unità di misura": "l/h",
                "min max": "0-5000",
                "VERIFICA LETTURA DA UNIFI": "DA CONFIGURARE DA UNIFI, ACQUISIRE ANCHE SET POINT MODULO"
            },
            {
                "Nome": "SP portata acido esausto",
                "nodo UA": "ns=2;s=0:900-FIC901/PID1/SP.CV",
                "Nome strumento": "900-FIC901",
                "DV_path": "901-FERRICO/900-LOOP/900-FIC901/PID1/SP.CV"
            },
            {
                "Nome": "Scrittura SP",
                "nodo UA": "ns=2;s=0:OPC_SP/900-FIC901_SP.CV",
                "Nome strumento": "900-FIC901"
            },
            {
                "Sorgente": "DCS Emerson"
            },
            {
                "Nome": "p904b",
                "nodo UA": "ns=2;s=0:800FI904B/AI1/PV.CV\r\nns=2;s=0:800FQI904B/TOT.CV",
                "Nome strumento": "FI904B",
                "DV_path": "CARICHI/800FI904B/AI1/PV  CARICHI/CAR_FECL3P/800FQI904B/TOT",
                "funzione": "misura portata e totalizzazione",
                "Unità di misura": "m3",
                "Prodotto": "Cloruro Ferrico potabile",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "OK"
            },
            {
                "Nome": "a1ul3",
                "nodo UA": "ns=2;s=0:800FI954/AI1/PV.CV\r\nns=2;s=0:800FQI954/TOT.CV",
                "Nome strumento": "FI954",
                "DV_path": "CARICHI/800FI954/AI1/PV   CARICHI/CAR_FECL2P/800FQI954/TOT",
                "funzione": "misura portata e totalizzazione",
                "Unità di misura": "m3",
                "Prodotto": "Cloruro Ferroso",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "OK"
            },
            {
                "Nome": "Quantità ordinata a vendita",
                "Nome strumento": "AS400",
                "Unità di misura": "kg",
                "Sorgente": "AS400"
            },
            {
                "Nome": "s982",
                "nodo UA": "N/A",
                "Nome strumento": "DI982-1",
                "DV_path": "na",
                "funzione": "misura densità cloruro ferrico",
                "Unità di misura": "kg/m3",
                "min max": "1330 - 1380",
                "Sorgente": "DCS Emerson"
            },
            {
                "Nome": "s982",
                "nodo UA": "ns=2;s=0:900AI982/AI1/PV.CV",
                "Nome strumento": "AI982",
                "DV_path": "FERRICO/FE-AI/900AI982/AI1/PV",
                "funzione": "misura potenziale redox Cloruro ferrico",
                "Unità di misura": "mV",
                "min max": "650 - 750",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "OK"
            },
            {
                "Nome": "c980",
                "nodo UA": "ns=2;s=0:900PI980_2/AI1/PV.CV",
                "Nome strumento": "PI980/2",
                "DV_path": "FERRICO/FE-AI/900PI980_2/AI1/PV",
                "funzione": "misura pressione fondo colonna C980",
                "Unità di misura": "mmH2O",
                "min max": " -200 - 0",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "OK"
            }
        ],
        "Cloruro Ferrico std": [
            {
                "Nome": "s-904a",
                "nodo UA": "ns=2;s=0:800LI904A/AI1/PV.CV",
                "Nome strumento": "LI904A",
                "DV_path": "STOCCAGGI/STOCCAGGI-AI/800LI904A/AI1/PV",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "135",
                "min max": "10%-95%",
                "Prodotto": "Cloruro Ferrico 40%",
                "densità [kg/m3]": "1440",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "OK"
            },
            {
                "Nome": "s-904b",
                "nodo UA": "ns=2;s=0:800LI904B/AI1/PV.CV",
                "Nome strumento": "LI904B",
                "DV_path": "STOCCAGGI/STOCCAGGI-AI/800LI904B/AI1/PV",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "135",
                "min max": "20%-95%",
                "Prodotto": "Cloruro Ferrico 40% non filtrato/fuori specifica",
                "densità [kg/m3]": "1440",
                "destinazione": "da filtrare/recuperare",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "OK"
            },
            {
                "Nome": "s-904c",
                "nodo UA": "ns=2;s=0:800LI904C/AI1/PV.CV",
                "Nome strumento": "LI904C",
                "DV_path": "STOCCAGGI/STOCCAGGI-AI/800LI904C/AI1/PV",
                "funzione": "indicazione livello",
                "Unità di misura": "%",
                "Volume [m3]": "135",
                "min max": "10%-95%",
                "Prodotto": "Cloruro Ferrico 40%",
                "densità [kg/m3]": "1440",
                "destinazione": "vendita",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "OK"
            },
            {
                "Nome": "ul44",
                "nodo UA": "ns=2;s=0:900-FIC253_4/PID1/PV.CV",
                "Nome strumento": "900-FIC253-4",
                "DV_path": "900-FERRICO/900-LOOP/900-FIC253_4/PID1/PV",
                "funzione": "indicazione e regolazione portata",
                "Unità di misura": "Nm3/h",
                "min max": "0-300",
                "Prodotto": "Cloro",
                "densità [kg/m3]": "3",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "OK"
            },
            {
                "Nome": "ul44",
                "nodo UA": "ns=2;s=0:900-FIC253_4/PID1/SP.CV",
                "Nome strumento": "900-FIC253_4",
                "DV_path": "900-FERRICO/900-LOOP/900-FIC253_4/PID1/SP.CV"
            },
            {
                "Nome": "ul44",
                "nodo UA": "ns=2;s=0:OPC_SP/900-FIC253_4_SP.CV",
                "Nome strumento": "900-FIC253_4"
            },
            {
                "Nome": "ul45",
                "nodo UA": "ns=2;s=0:900-FIC909-2/PID1/PV.CV",
                "Nome strumento": "900-FIC909-2",
                "DV_path": "900-FERRICO/900-LOOP/900-FIC909-2/PID1/PV",
                "funzione": "indicazione e regolazione portata",
                "Unità di misura": "lt/h",
                "min max": "1000 - 3000 (40 - 90 ton/g di FeCl3)",
                "Prodotto": "Cloruro ferroso base",
                "densità [kg/m3]": "1400",
                "Sorgente": "DCS Emerson"
            },
            {
                "Nome": "ul45",
                "nodo UA": "ns=2;s=0:900-FIC909-2/PID1/SP.CV",
                "Nome strumento": "900-FIC909-2",
                "DV_path": "900-FERRICO/900-LOOP/900-FIC909-2/PID1/SP.CV"
            },
            {
                "Nome": "ul45",
                "nodo UA": "ns=2;s=0:OPC_SP/900-FIC909-2_SP.CV",
                "Nome strumento": "900-FIC909-2"
            },
            {
                "Nome": "ul19",
                "nodo UA": "ns=2;s=0:900FIC980/PID1/PV.CV",
                "Nome strumento": "900FIC980",
                "DV_path": "FERRICO/FE-LOOP/900FIC980/PID1/PV.CV",
                "Unità di misura": "m3/h (email pierno del 15/10/2020)",
                "VERIFICA LETTURA DA UNIFI": "nuovo"
            },
            {
                "Nome": "ul19",
                "nodo UA": "ns=2;s=0:900FIC980/PID1/SP.CV",
                "Nome strumento": "900FIC980",
                "DV_path": "FERRICO/FE-LOOP/900FIC980/PID1/SP.CV",
                "Unità di misura": "m3/h (email pierno del 15/10/2020)"
            },
            {
                "Nome": "ul19",
                "nodo UA": "ns=2;s=0:OPC_SP/900FIC980_SP.CV",
                "Nome strumento": "900FIC980",
                "Unità di misura": "m3/h (email pierno del 15/10/2020)"
            },
            {
                "Sorgente": "DCS Emerson"
            },
            {
                "Nome": "p904a",
                "nodo UA": "ns=2;s=0:800FI900/AI1/PV.CV\r\nns=2;s=0:800FQI900/TOT.CV",
                "Nome strumento": "FI900",
                "DV_path": "CARICHI/800FI900/AI1/PV   CARICHI/CAR_FECL3/800FQI900",
                "funzione": "misura portata e totalizzazione",
                "Unità di misura": "m3",
                "Prodotto": "Cloruro Ferrico",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "OK"
            },
            {
                "Nome": "Quantità ordinata a vendita",
                "Nome strumento": "AS400",
                "Unità di misura": "kg",
                "Sorgente": "AS400"
            },
            {
                "Nome": "Redox FeCl3 Pot",
                "nodo UA": "ns=2;s=0:900-RH900/AI1/OUT.CV",
                "Nome strumento": "RH900",
                "DV_path": "900-FERRICO/900-AI/900-RH900/AI1/OUT",
                "funzione": "misura potenziale redox Cloruro ferrico",
                "Unità di misura": "mV",
                "min max": "650 - 750",
                "Prodotto": "Cloruro Ferrico",
                "Sorgente": "DCS Emerson"
            },
            {
                "Nome": "c-909",
                "nodo UA": "ns=2;s=0:900-PI909-2/AI1/OUT.CV",
                "Nome strumento": "PI909/2",
                "DV_path": "900-FERRICO/900-AI/900-PI909-2/AI1/OUT",
                "funzione": "misura pressione fondo colonna C909",
                "Unità di misura": "mmH2O",
                "min max": " -200 - 0",
                "Sorgente": "DCS Emerson",
                "VERIFICA LETTURA DA UNIFI": "OK"
            }
        ]
    }

    for key_impianto in json:
        try:
            for object in json[key_impianto]:
                for key in object:
                    if(key == 'Nome'):
                      #  print('<https://saref.etsi.org/saref4bldg/'+object[key]+'>  a       owl:NamedIndividual , <https://saref.etsi.org/saref4bldg/PhysicalObject> .')
                        pass
                    if(key == 'nodo UA'):
                        print('<https://saref.etsi.org/saref4bldg/'+object['Nome'].replace(" ", "")+'> <http://www.disit.org/saref4bldg-ext/nodoUA> "'+object[key]+'" .')
                    if(key == 'UA data type'):
                        pass
                    if(key == 'Nome strumento'):
                        pass
                    if(key == 'DV_path'):
                        print('<https://saref.etsi.org/saref4bldg/' + object[
                            'Nome'].replace(" ", "") + '> <http://www.disit.org/saref4bldg-ext/DVpath> "' + object[key] + '" .')
                    if(key == 'funzione'):
                        print('<https://saref.etsi.org/saref4bldg/' + object[
                            'Nome'].replace(" ", "") + '> <http://www.disit.org/saref4bldg-ext/funzione> "' + object[key] + '" .')
                    if(key == 'Unità di misura'):
                        print('<https://saref.etsi.org/saref4bldg/' + object[
                            'Nome'].replace(" ", "") + '> <http://www.disit.org/saref4bldg-ext/unita-di-misura> "' + object[key] + '" .')
                    if(key == 'min max'):
                        print('<https://saref.etsi.org/saref4bldg/' + object[
                            'Nome'].replace(" ", "") + '> <http://www.disit.org/saref4bldg-ext/min-max> "' + object[key] + '" .')
                    if(key == 'Prodotto'):
                        print('<https://saref.etsi.org/saref4bldg/' + object[
                            'Nome'].replace(" ", "") + '> <http://www.disit.org/saref4bldg-ext/prodotto> "' + object[key] + '" .')

                    if('densi' in key  ):
                        print('<https://saref.etsi.org/saref4bldg/' + object[
                            'Nome'].replace(" ", "") + '> <http://www.disit.org/saref4bldg-ext/densita> "' + object[key] + '" .')

                    if(key == 'destinazione'):
                        print('<https://saref.etsi.org/saref4bldg/' + object[
                            'Nome'].replace(" ", "") + '> <http://www.disit.org/saref4bldg-ext/destinazione> "' + object[key] + '" .')
                    if(key == 'Sorgente'):
                        print('<https://saref.etsi.org/saref4bldg/' + object[
                            'Nome'].replace(" ", "") + '> <http://www.disit.org/saref4bldg-ext/sorgente> "' + object[key] + '" .')
                    if(key == 'note'):
                        print('<https://saref.etsi.org/saref4bldg/' + object[
                            'Nome'].replace(" ", "") + '> <http://www.disit.org/saref4bldg-ext/note> "' + object[key] + '" .')
                    if('VERIFICA' in key):
                        print('<https://saref.etsi.org/saref4bldg/' + object[
                            'Nome'].replace(" ", "") + '> <http://www.disit.org/saref4bldg-ext/verifica-lettura-da-unifi> "' + object[key] + '" .')
        except Exception as ex:
            continue


        # for object in impianto:
        #     for key in object:




