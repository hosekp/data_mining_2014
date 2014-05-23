import rdkit.Chem as rd
import numpy,scipy,math
import sklearn as scikit
import json

from datamining import *

#chembljson=r"""[{"smiles": "Oc1ccc(cc1)B2345B678B9%10%11B%12%13%14B9%15%16B%12%17%18B%13%19%20B6%10%14C27%19B3%17%20C4%15%18B58%11%16", "pIC": -2.258633205464863, "id": "CHEMBL219763"}, {"smiles": "CC1=C(C(=O)c2ccc(O)cc12)c3ccc(O)cc3", "pIC": -1.791759469228055, "id": "CHEMBL370037"}, {"smiles": "C[C@@H](COc1ccc(cc1)[C@@H]2Oc3ccc(O)cc3S[C@@H]2c4ccc(O)cc4)N5CCCC5", "pIC": -0.26236426446749106, "id": "CHEMBL180300"}, {"smiles": "OCC1CCN(CCOc2ccc(cc2)[C@@H]3Oc4ccc(O)cc4S[C@@H]3c5ccc(O)cc5)CC1", "pIC": -0.7884573603642703, "id": "CHEMBL184431"}, {"smiles": "Oc1ccc(cc1)[C@H]2Sc3cc(O)ccc3S[C@H]2c4ccc(OCCN5CCCCC5)c(Br)c4", "pIC": -1.6094379124341003, "id": "CHEMBL124482"}, {"smiles": "CCc1c(O)ccc2S[C@H]([C@H](Oc12)c3ccc(OCCN4CCCCC4)cc3)c5ccc(O)cc5", "pIC": -1.547562508716013, "id": "CHEMBL420068"}, {"smiles": "Cc1cc(O)cc2O[C@@H]([C@@H](Sc12)c3ccc(O)cc3)c4ccc(OCCN5CCCCC5)cc4", "pIC": -1.7047480922384253, "id": "CHEMBL93793"}, {"smiles": "Oc1ccc(cc1)c2oc3c(Cl)cc(O)cc3c2", "pIC": -1.916922612182061, "id": "CHEMBL184448"}, {"smiles": "C[C@H]1CCN(CCOc2ccc(cc2)[C@@H]3Oc4ccc(O)cc4S[C@@H]3c5ccc(O)cc5)C1", "pIC": -0.0, "id": "CHEMBL183049"}, {"smiles": "CC[C@@H](CN1CCCC1)Oc2ccc(cc2)[C@@H]3Oc4ccc(O)cc4S[C@@H]3c5ccc(O)cc5", "pIC": 0.2231435513142097, "id": "CHEMBL183092"}, {"smiles": "CC\\C(=C(\\CC)/c1ccc(O)cc1)\\c2ccc(O)cc2", "pIC": 0.2613647641344075, "id": "CHEMBL411"}, {"smiles": "Oc1ccc(cc1)[C@H]2Sc3cc(O)ccc3S[C@H]2c4ccc(OCCN5CCCC5)c(Br)c4", "pIC": -1.3862943611198906, "id": "CHEMBL123025"}, {"smiles": "Oc1ccc(cc1)[C@@H]2Sc3c(F)c(O)ccc3O[C@@H]2c4ccc(OCCN5CCCCC5)cc4", "pIC": -0.9162907318741551, "id": "CHEMBL328716"}, {"smiles": "Oc1ccc2O[C@H]([C@@H](CC3CCCC3)Sc2c1)c4ccc(OCCN5CCCCC5)cc4", "pIC": -1.0986122886681098, "id": "CHEMBL315271"}, {"smiles": "Oc1ccc2C3=C(CCOc2c1)c4ccc(O)cc4OC3c5ccc(OCCN6CCCCC6)cc5", "pIC": -2.0794415416798357, "id": "CHEMBL1087419"}, {"smiles": "OCC1=Nc2cc3CCC(N(CC#C)c4ccc(cc4)C(=O)N[C@@H](CCC(=O)N[C@H](CCC(=O)O)C(=O)O)C(=O)O)c3cc2C(=O)N1", "pIC": -0.0, "id": "CHEMBL1253498"}, {"smiles": "OC1CCN(CCOc2ccc(cc2)[C@@H]3Oc4ccc(O)cc4S[C@@H]3c5ccc(O)cc5)CC1", "pIC": -0.5877866649021191, "id": "CHEMBL184372"}, {"smiles": "CN(C)CCOc1ccc(cc1)[C@H]2Oc3cc(O)ccc3C4=C2c5ccc(O)cc5OCC4", "pIC": -1.1939224684724346, "id": "CHEMBL1083186"}, {"smiles": "CCN(CC)CCOc1ccc(cc1)[C@H]2Oc3ccccc3C4=C2c5ccc(O)cc5OCC4", "pIC": -1.6094379124341003, "id": "CHEMBL1084128"}, {"smiles": "Oc1ccc(cc1)[C@H]2Sc3cc(O)ccc3O[C@H]2c4ccc(CCCN5CCCCC5)cc4", "pIC": -0.3364722366212129, "id": "CHEMBL124474"}, {"smiles": "Oc1ccc2C3=C(CCOc2c1)c4ccc(O)cc4O[C@@H]3c5ccc(OCCN6CCOCC6)cc5", "pIC": -0.47000362924573563, "id": "CHEMBL1087811"}, {"smiles": "Oc1ccc(cc1)c2sc3cc(O)ccc3c2C(=O)c4ccc(cc4)N5CCN(CC5)C(=O)c6ccccc6O", "pIC": -1.1151415906193203, "id": "CHEMBL427496"}, {"smiles": "Oc1ccc(cc1)C2345B678B9%10%11B%12%13%14B9%15%16B%12%17%18B%13%19%20B6%10%14B27%19C3%17%20B4%15%18B58%11%16", "pIC": -1.0473189942805592, "id": "CHEMBL219003"}, {"smiles": "CN(C)CCOc1ccc(cc1)[C@@H]2Oc3ccc(O)cc3S[C@@H]2c4cccc(O)c4", "pIC": -0.8329091229351039, "id": "CHEMBL329902"}, {"smiles": "Oc1ccc2C3=C(CCOc2c1)c4ccc(F)cc4O[C@@H]3c5ccc(OCCN6CCCCCC6)cc5", "pIC": -1.1939224684724346, "id": "CHEMBL1082224"}, {"smiles": "Oc1ccc2C3=C(CCOc2c1)c4ccc(O)cc4O[C@@H]3c5ccc(OCCN6C(=O)CCC6=O)cc5", "pIC": -1.5686159179138452, "id": "CHEMBL1083194"}, {"smiles": "Oc1ccc(cc1)[C@H]2Sc3cc(O)ccc3O[C@H]2c4ccc(OCCN5CC6CC7CC(C6)CC5C7)cc4", "pIC": 0.5108256237659907, "id": "CHEMBL184371"}, {"smiles": "Oc1ccc2O[C@H]([C@H](Sc2c1)C3CCCC3)c4ccc(OCCN5CCCCC5)cc4", "pIC": -0.9162907318741551, "id": "CHEMBL431611"}, {"smiles": "COc1ccc2C3=C(CCOc2c1)c4ccc(O)cc4O[C@H]3c5ccc(OCCN6CCCCC6)cc5", "pIC": -1.4350845252893227, "id": "CHEMBL1088344"}, {"smiles": "OC[C@@H]1CCCN1CCOc2ccc(cc2)[C@@H]3Oc4ccc(O)cc4S[C@@H]3c5ccc(O)cc5", "pIC": -1.3609765531356006, "id": "CHEMBL359774"}, {"smiles": "Oc1ccc(cc1)C2=C(c3ccc(OCCN4CCC4)cc3)c5ccccc5OCC2", "pIC": -0.6418538861723947, "id": "CHEMBL470993"}, {"smiles": "COc1ccc2C(=C(CCOc2c1)c3ccc(O)cc3)c4ccc(OCCN5CCC5)cc4", "pIC": -1.9021075263969205, "id": "CHEMBL511269"}, {"smiles": "Oc1ccc2C3=C([C@H](Oc2c1)c4ccc(OCCN5CCCCC5)cc4)c6ccccc6OCC3", "pIC": -2.302585092994046, "id": "CHEMBL1087289"}, {"smiles": "Oc1ccc2C3=C(CCOc2c1)c4ccc(O)cc4O[C@H]3c5ccc(OCCN6CCCC6)cc5", "pIC": -0.9162907318741551, "id": "CHEMBL1086776"}, {"smiles": "O[C@@H]1CCN(CCOc2ccc(cc2)[C@@H]3Oc4ccc(O)cc4S[C@@H]3c5ccc(O)cc5)C1", "pIC": -0.5306282510621704, "id": "CHEMBL185114"}, {"smiles": "Oc1ccc2C(N(CCc2c1)c3ccc(\\C=C\\C(=O)N4CCOCC4)cc3)c5ccccc5", "pIC": -1.7749523509116738, "id": "CHEMBL93586"}, {"smiles": "CC1(N(CCc2cc(O)ccc12)c3cccc(O)c3)c4ccc(OCCN5CCCC5)cc4", "pIC": 0.5108256237659907, "id": "CHEMBL328388"}, {"smiles": "Oc1ccc(cc1)B2345B678B9%10%11B6%12%13B27%14B%12%15%16B3%14%17B4%18%19B589B%10%18%20C%11%13%15C%16%17%19%20", "pIC": -1.366091653802371, "id": "CHEMBL385993"}, {"smiles": "Oc1ccc2C(N(Cc3ccccc3)CCc2c1)c4ccc(OCCN5CCCC5)cc4", "pIC": -1.547562508716013, "id": "CHEMBL94280"}, {"smiles": "Oc1ccc(C[C@H]2Sc3cc(O)ccc3O[C@H]2c4ccc(OCCN5CCCCC5)cc4)cc1", "pIC": -0.9932517730102834, "id": "CHEMBL313941"}, {"smiles": "Oc1ccc2[C@H]([C@H](SCc2c1)c3ccccc3)c4ccc(OCCN5CCCC5)cc4", "pIC": 0.5108256237659907, "id": "CHEMBL183333"}, {"smiles": "Oc1ccc(cc1)[C@H]2Sc3cc(O)ccc3O[C@H]2c4ccc(OCCN5C[C@H]6CCCC[C@H]6C5)cc4", "pIC": -0.0, "id": "CHEMBL185231"}, {"smiles": "C[C@@H]1CCN(CCOc2ccc(Cn3c(c(C)c4cc(O)ccc34)c5ccc(O)cc5)cc2)C1", "pIC": 0.6931471805599453, "id": "CHEMBL198914"}, {"smiles": "C[C@@H](COc1ccc(Cn2c(c(C)c3cc(O)ccc23)c4ccc(O)cc4)cc1)N5CCCC5", "pIC": 0.916290731874155, "id": "CHEMBL372808"}, {"smiles": "C[C@@H](COc1ccc(cc1)[C@H]2[C@H](CCc3cc(O)ccc23)c4ccccc4)N5CCCC5", "pIC": 0.5108256237659907, "id": "CHEMBL197495"}, {"smiles": "CC(CCc1ccc(O)cc1)NC(=O)Cc2c([nH]c3ccccc23)c4ccccc4", "pIC": -0.0, "id": "CHEMBL241301"}, {"smiles": "C[C@H](NC(=O)Cc1c([nH]c2ccccc12)c3ccccc3)c4c(C)c5cc(O)ccc5n4Cc6ccc(OCCN7CC[C@H](C)C7)cc6", "pIC": -1.3862943611198906, "id": "CHEMBL437190"}, {"smiles": "CC1(N(CCc2cc(O)ccc12)c3ccc(F)cc3)c4ccc(OCCN5CCCCC5)cc4", "pIC": -0.6418538861723947, "id": "CHEMBL101083"}, {"smiles": "CC\\C(=C(/c1ccccc1)\\c2ccc(O)cc2)\\c3ccccc3", "pIC": -1.9459101490553132, "id": "CHEMBL50995"}, {"smiles": "C[C@@H](COc1ccc(cc1)[C@@H]2Oc3ccc(O)cc3S[C@@H]2c4ccc(O)cc4)N5CC[C@@H](C)C5", "pIC": -0.26236426446749106, "id": "CHEMBL182402"}, {"smiles": "Oc1ccc(cc1)[C@H]2Sc3cc(O)ccc3O[C@H]2c4ccc(OCCN5CC6CCC6C5)cc4", "pIC": 0.2231435513142097, "id": "CHEMBL184598"}, {"smiles": "C[C@@H](COc1ccc(cc1)[C@@H]2Oc3ccc(O)cc3[C@@H](C)[C@@H]2c4ccc(O)cc4)N5CCCC5", "pIC": -0.3364722366212129, "id": "CHEMBL360315"}, {"smiles": "Oc1cccc(c1)[C@H]2Sc3cc(O)ccc3O[C@H]2c4ccc(OCCNC5CCCCCC5)cc4", "pIC": -1.252762968495368, "id": "CHEMBL94225"}, {"smiles": "Oc1ccc(cc1)c2sc3cc(O)ccc3c2C(=O)c4ccc(cc4)N5CCN(CC5)C(=O)c6ccc(Cl)cc6", "pIC": 1.5141277326297755, "id": "CHEMBL180707"}, {"smiles": "C[C@@H]1CN(CCOc2ccc(cc2)[C@@H]3Oc4ccc(O)cc4S[C@@H]3c5ccc(O)cc5)C[C@@H]1C", "pIC": 0.35667494393873245, "id": "CHEMBL367574"}, {"smiles": "Oc1ccc(cc1)C2345B678B9%10%11B%12%13%14B%15%16%17B%18%19%20B69(B27%18B3%15%19B4%12%16B58%10%13)C%11%14%17%20", "pIC": 0.527632742082372, "id": "CHEMBL219004"}, {"smiles": "CC1(N(CCc2cc(O)ccc12)c3ccccc3)c4ccc(OCCN5CCCCC5)cc4", "pIC": -0.9555114450274363, "id": "CHEMBL101807"}, {"smiles": "C[C@@H]1CCN(CCOc2ccc(cc2)[C@@H]3Oc4ccc(O)cc4S[C@@H]3c5ccc(O)cc5)C1", "pIC": -1.0986122886681098, "id": "CHEMBL183584"}, {"smiles": "Oc1ccc(cc1)c2sc3cc(O)ccc3c2C(=O)c4ccc(cc4)N5CCN(CC5)C6CCCC6", "pIC": -0.0769610411361284, "id": "CHEMBL366928"}, {"smiles": "CC1(N(CCc2cc(O)ccc12)c3cccc(Cl)c3)c4ccc(OCCN5CCCCC5)cc4", "pIC": -1.5040773967762742, "id": "CHEMBL103305"}, {"smiles": "Cc1cc(C)nc(n1)N2CCN(CC2)c3ccc(cc3)C(=O)c4c(sc5cc(O)ccc45)c6ccc(O)cc6", "pIC": -0.7514160886839212, "id": "CHEMBL182237"}, {"smiles": "CC[C@H](CN1CCCC1)Oc2ccc(cc2)[C@@H]3Oc4ccc(O)cc4S[C@@H]3c5ccc(O)cc5", "pIC": -0.1823215567939546, "id": "CHEMBL183086"}, {"smiles": "Oc1ccc(cc1)[C@H]2Sc3cc(O)ccc3O[C@H]2c4ccc(OCCN5CCSCC5)cc4", "pIC": -0.4054651081081644, "id": "CHEMBL362718"}, {"smiles": "Oc1ccc(cc1)C2=C(Oc3ccc(O)cc3S2)c4ccc(OCCN5CCCCC5)cc4", "pIC": -0.47000362924573563, "id": "CHEMBL418327"}, {"smiles": "C[C@@H](COc1ccc(cc1)[C@@H]2Oc3ccc(O)c(F)c3[C@@H](C)[C@@H]2c4ccc(O)cc4)N5CCC[C@H]5C", "pIC": 0.35667494393873245, "id": "CHEMBL181248"}, {"smiles": "CC1(C)CCCN1CCOc2ccc(cc2)[C@@H]3Oc4ccc(O)cc4S[C@@H]3c5ccc(O)cc5", "pIC": 0.10536051565782628, "id": "CHEMBL183371"}, {"smiles": "CN1CCCN(CC1)c2ccc(cc2)[C@@H]3Oc4ccc(O)cc4S[C@@H]3c5ccc(O)cc5", "pIC": -1.2809338454620642, "id": "CHEMBL121879"}, {"smiles": "Oc1ccc(cc1)C2=C(c3ccccc3)c4cc(O)ccc4C2=O", "pIC": -2.302585092994046, "id": "CHEMBL373095"}, {"smiles": "C[C@H]1[C@@H]([C@@H](Oc2ccc(O)cc12)c3ccc(OCCN4CCCCC4)cc3)c5ccc(O)cc5", "pIC": -0.3364722366212129, "id": "CHEMBL178470"}, {"smiles": "Oc1ccc(cc1)[C@H]2Sc3cc(O)ccc3O[C@H]2c4ccc(OCCN5CCC6(CC5)OCCO6)cc4", "pIC": -0.6931471805599453, "id": "CHEMBL185480"}, {"smiles": "OC[C@H]1CCCN1CCOc2ccc(cc2)[C@@H]3Oc4ccc(O)cc4S[C@@H]3c5ccc(O)cc5", "pIC": -0.6931471805599453, "id": "CHEMBL360802"}, {"smiles": "Oc1ccc(cc1)[C@H]2Sc3cc(O)ccc3O[C@H]2c4ccc(cc4)N5CCNCC5", "pIC": -1.4816045409242156, "id": "CHEMBL332625"}, {"smiles": "Oc1ccc2O[C@@H]([C@@H](Sc2c1)c3ccccc3O)c4ccc(OCCN5CCCCC5)cc4", "pIC": -0.26236426446749106, "id": "CHEMBL91758"}, {"smiles": "Oc1ccc(cc1)[C@@H]2Sc3ccc(O)cc3O[C@@H]2c4ccc(OCCN5CCCCC5)cc4", "pIC": -0.47000362924573563, "id": "CHEMBL71584"}, {"smiles": "C[C@H]1CCN(CCOc2ccc(cc2)[C@@H]3Oc4ccc(O)cc4[C@@H](C)[C@@H]3c5ccc(O)cc5)C1", "pIC": -0.26236426446749106, "id": "CHEMBL433581"}, {"smiles": "CC1(N(CCc2cc(O)ccc12)c3cccc(O)c3)c4ccc(OCCN5CCCCC5)cc4", "pIC": 0.35667494393873245, "id": "CHEMBL100617"}, {"smiles": "C[C@@H](COc1ccc(cc1)[C@@H]2Oc3ccc(O)c(F)c3[C@@H](C)[C@@H]2c4ccc(O)cc4)N5CC[C@H](C)C5", "pIC": -0.9162907318741551, "id": "CHEMBL359671"}, {"smiles": "CC1CCCC(C)N1CCOc2ccc(cc2)[C@@H]3Oc4ccc(O)cc4S[C@@H]3c5cccc(O)c5", "pIC": -1.2237754316221157, "id": "CHEMBL90794"}, {"smiles": "Oc1ccc2C(N(CCc2c1)S(=O)(=O)c3ccccc3)c4ccc(OCCN5CCCC5)cc4", "pIC": -1.6486586255873816, "id": "CHEMBL420244"}, {"smiles": "Oc1ccc(cc1)c2sc3cc(O)ccc3c2C(=O)c4ccc(cc4)N5CCN(CC5)C(=O)c6cccc(O)c6", "pIC": -0.3293037471426003, "id": "CHEMBL441499"}, {"smiles": "Oc1ccc(cc1)[C@H]2Sc3cc(O)ccc3O[C@H]2c4ccc(OCCN5CCC(F)CC5)cc4", "pIC": -0.9162907318741551, "id": "CHEMBL183084"}, {"smiles": "C[C@H](CCc1ccc(O)cc1)NC(=O)Cc2c([nH]c3ccccc23)c4ccccc4", "pIC": -0.0, "id": "CHEMBL391910"}, {"smiles": "C[C@H](CCc1ccc(O)cc1)NC(=O)Cc2c([nH]c3cc(OCCN4CCCCC4)ccc23)c5ccccc5", "pIC": -2.0794415416798357, "id": "CHEMBL241303"}, {"smiles": "C[C@H]1[C@@H]([C@@H](Oc2cc(O)ccc12)c3ccc(OCCN4CCCCC4)cc3)c5ccc(O)cc5", "pIC": 0.4155154439616658, "id": "CHEMBL362428"}, {"smiles": "CC[C@@H](COc1ccc(cc1)[C@@H]2Oc3ccc(O)cc3S[C@@H]2c4ccc(O)cc4)N5CCCC5", "pIC": 0.6931471805599453, "id": "CHEMBL367350"}, {"smiles": "Oc1ccc(cc1)[C@H]2Sc3cc(O)ccc3O[C@H]2c4ccc(OCCN5CC6CC5CO6)cc4", "pIC": 0.35667494393873245, "id": "CHEMBL434525"}, {"smiles": "Oc1ccc(cc1)[C@H]2Sc3cc(O)ccc3O[C@H]2c4ccc(OCCN5CC[C@@H]6C[C@H]56)cc4", "pIC": 0.6931471805599453, "id": "CHEMBL181862"}, {"smiles": "Oc1ccc(cc1)[C@H]2Sc3cc(O)ccc3O[C@H]2c4ccc(OCCN5CC6CC6C5)cc4", "pIC": 0.35667494393873245, "id": "CHEMBL184202"}, {"smiles": "C[C@]12CC[C@H]3[C@@H]([C@H](CCCCCCCCC[S+]([O-])CCCC(F)(F)C(F)(F)F)Cc4cc(O)ccc34)[C@@H]1CC[C@@H]2O", "pIC": -1.3862943611198906, "id": "CHEMBL1358"}, {"smiles": "CC1(N(CCc2cc(O)ccc12)c3ccc(F)cc3)c4ccc(OCCN5CCCC5)cc4", "pIC": -0.47000362924573563, "id": "CHEMBL101997"}, {"smiles": "Oc1ccc(cc1)[C@H]2Sc3cc(O)ccc3O[C@H]2c4ccc(OCCN5CC6(CCC6)C5)cc4", "pIC": 0.916290731874155, "id": "CHEMBL185083"}, {"smiles": "Oc1ccc(cc1)[C@H]2Sc3cc(O)ccc3O[C@H]2c4ccc(OCCCN5CCCC5)cc4", "pIC": -0.5306282510621704, "id": "CHEMBL361751"}, {"smiles": "C[C@@H](COc1ccc(cc1)[C@@H]2Oc3ccc(O)c(F)c3[C@@H](C)[C@@H]2c4ccc(O)cc4)N5CCCC5", "pIC": 0.6931471805599453, "id": "CHEMBL359633"}, {"smiles": "Oc1ccc2C3=C(CCOc2c1)c4ccc(O)cc4O[C@@H]3c5ccc(OCCN6CCCCCC6)cc5", "pIC": -0.7884573603642703, "id": "CHEMBL1087545"}, {"smiles": "Oc1ccc2C3=C(CCOc2c1)c4ccccc4O[C@@H]3c5ccc(OCCN6CCCCC6)cc5", "pIC": -1.7578579175523736, "id": "CHEMBL1087298"}, {"smiles": "Oc1ccc2C3=C([C@@H](Oc2c1)c4ccc(OCCN5CCCCC5)cc4)c6ccccc6OCC3", "pIC": -1.840549633397487, "id": "CHEMBL1086652"}, {"smiles": "COc1ccc2C3=C(CCOc2c1)c4ccc(O)cc4O[C@@H]3c5ccc(OCCN6CCCCC6)cc5", "pIC": -1.7578579175523736, "id": "CHEMBL1088343"}, {"smiles": "C[C@]12CC[C@H]3[C@@H](CCc4cc(O)ccc34)[C@@H]1CC[C@@]2(O)C#C", "pIC": 0.8029620465671519, "id": "CHEMBL691"}, {"smiles": "CC1CCN(CCOc2ccc(cc2)[C@@H]3Oc4ccc(O)cc4S[C@@H]3c5cccc(O)c5)CC1", "pIC": -1.3862943611198906, "id": "CHEMBL92635"}, {"smiles": "C[C@@H](CN1CCCC1)Oc2ccc(cc2)[C@@H]3Oc4ccc(O)cc4S[C@@H]3c5ccc(O)cc5", "pIC": -0.9162907318741551, "id": "CHEMBL181944"}, {"smiles": "CC(C)C[C@H]1Sc2cc(O)ccc2O[C@H]1c3ccc(OCCN4CCCCC4)cc3", "pIC": -1.0986122886681098, "id": "CHEMBL85650"}, {"smiles": "CC[C@@H]1CCN(CCOc2ccc(cc2)[C@@H]3Oc4ccc(O)cc4S[C@@H]3c5ccc(O)cc5)C1", "pIC": 0.10536051565782628, "id": "CHEMBL183388"}, {"smiles": "Oc1ccc(cc1)C2=COc3cc(O)cc(O)c3C2=O", "pIC": -2.272125885509337, "id": "CHEMBL44"}, {"smiles": "Cc1cccc(c1)C(=O)N2CCN(CC2)c3ccc(cc3)C(=O)c4c(sc5cc(O)ccc45)c6ccc(O)cc6", "pIC": 1.3093333199837622, "id": "CHEMBL180873"}, {"smiles": "CC1(C)CCN(CCOc2ccc(cc2)[C@@H]3Oc4ccc(O)cc4S[C@@H]3c5ccc(O)cc5)C1", "pIC": -0.0, "id": "CHEMBL182887"}, {"smiles": "Oc1ccc(cc1)C2=Cc3cc(O)ccc3C24Cc5ccccc5C4", "pIC": -1.4586150226995167, "id": "CHEMBL281499"}, {"smiles": "Oc1ccc(cc1)C2345B678B9%10%11B6%12%13B9%14%15B%12%16%17B27%13B3%16%18B4%19%20B%10%14(B58%11%19)C%15%17%18%20", "pIC": -1.2809338454620642, "id": "CHEMBL386948"}, {"smiles": "CSC1=C(C(=O)c2ccc(O)cc12)c3ccc(O)cc3", "pIC": -1.1314021114911006, "id": "CHEMBL192765"}, {"smiles": "Oc1ccc(cc1)C2=C(CCOc3cc(F)ccc23)c4ccc(OCCN5CCCC5)cc4", "pIC": -1.7173950539391927, "id": "CHEMBL472468"}, {"smiles": "CN(C)CCOc1ccc(cc1)\\C(=C(\\CCN=[N+]=[N-])/c2ccccc2)\\c3ccc(O)cc3", "pIC": -0.0, "id": "CHEMBL203472"}, {"smiles": "Oc1ccc(cc1)C2=C(c3ccccc3)c4cc(O)cc(O)c4C2=O", "pIC": -1.0986122886681098, "id": "CHEMBL191836"}, {"smiles": "Oc1ccc2OC(C(Sc2c1)c3ccc(F)cc3)c4ccc(OCCN5CCCCC5)cc4", "pIC": -1.33500106673234, "id": "CHEMBL93546"}, {"smiles": "Oc1ccc2O[C@H]([C@@H](CC3CCCCC3)Sc2c1)c4ccc(OCCN5CCCCC5)cc4", "pIC": -1.3609765531356006, "id": "CHEMBL85881"}, {"smiles": "C[C@@H](COc1ccc(cc1)[C@@H]2Oc3ccc(O)cc3[C@@H](C)[C@@H]2c4ccc(O)cc4)N5CC[C@@H](C)C5", "pIC": -0.26236426446749106, "id": "CHEMBL368449"}, {"smiles": "Oc1ccc2C(N(Cc3ccc4OCOc4c3)CCc2c1)c5ccc(OCCN6CCCC6)cc5", "pIC": -2.2192034840549946, "id": "CHEMBL92900"}, {"smiles": "Oc1ccc(cc1)c2sc3cc(O)ccc3c2C(=O)c4ccc(cc4)N5CCN(CC5)C(=O)c6ccccc6[N+](=O)[O-]", "pIC": -1.275362800412609, "id": "CHEMBL360978"}, {"smiles": "CCCN(c1c(CC)cccc1CC)S(=O)(=O)c2ccc(O)c(C)c2", "pIC": -1.6094379124341003, "id": "CHEMBL202472"}, {"smiles": "Oc1ccc2O[C@H]([C@H](Sc2c1)c3cccc(O)c3)c4ccc(OCCN5CCCC5)cc4", "pIC": -0.0, "id": "CHEMBL327320"}, {"smiles": "Oc1ccc(cc1)c2sc3cc(O)ccc3c2C(=O)c4ccc(cc4)N5CCN(CC5)C(=O)c6ccccc6Cl", "pIC": -0.5423242908253617, "id": "CHEMBL180973"}, {"smiles": "Oc1ccc(cc1)[C@@H]2Cc3ccc(O)cc3O[C@@H]2c4ccc(OCCN5CCCCC5)cc4", "pIC": -1.9021075263969205, "id": "CHEMBL30439"}, {"smiles": "Oc1ccc(cc1)c2sc3cc(O)ccc3c2C(=O)c4ccc(OCCN5CCCCC5)cc4", "pIC": 0.7765287894989963, "id": "CHEMBL81"}, {"smiles": "Oc1cccc(c1)[C@H]2Sc3cc(O)ccc3O[C@H]2c4ccc(OCCN5CCCCC5)cc4", "pIC": -1.3862943611198906, "id": "CHEMBL93705"}, {"smiles": "Oc1ccc(cc1)c2sc3cc(O)ccc3c2C(=O)c4ccc(cc4)N5CCN(CC5)C(=O)c6ccccc6", "pIC": 0.15082288973458366, "id": "CHEMBL360498"}, {"smiles": "Oc1ccc2C3=C(CCOc2c1)c4ccc(F)cc4O[C@H]3c5ccc(OCCN6CCCCCC6)cc5", "pIC": -1.6094379124341003, "id": "CHEMBL1082528"}, {"smiles": "C[C@H]1[C@@H]([C@@H](Oc2ccc(O)c(F)c12)c3ccc(OCCN4CCCC4)cc3)c5ccc(O)cc5", "pIC": 0.10536051565782628, "id": "CHEMBL181369"}, {"smiles": "Oc1ccc(cc1)[C@@H]2Sc3c(Cl)c(O)ccc3O[C@@H]2c4ccc(OCCN5CCCCC5)cc4", "pIC": -0.0, "id": "CHEMBL92660"}, {"smiles": "C[C@]12CC[C@H]3[C@@H](CCc4cc(O)ccc34)[C@@H]1CC[C@@H]2O", "pIC": -0.26236426446749106, "id": "CHEMBL135"}, {"smiles": "Oc1ccc(cc1)[C@@H]2Sc3c(Cl)cc(O)cc3O[C@@H]2c4ccc(OCCN5CCCCC5)cc4", "pIC": -1.2237754316221157, "id": "CHEMBL94116"}, {"smiles": "Cc1c(c2ccc(O)cc2)n(Cc3ccc(OCCN4CCCCC4)cc3)c5ccc(O)cc15", "pIC": -0.4054651081081644, "id": "CHEMBL44426"}, {"smiles": "Oc1ccc(cc1)c2noc(c2c3ccccc3)C(F)(F)F", "pIC": -2.1400661634962708, "id": "CHEMBL200021"}, {"smiles": "Oc1ccc2O[C@H]([C@H](Sc2c1)C3CCCCCC3)c4ccc(OCCN5CCCCC5)cc4", "pIC": -2.0149030205422647, "id": "CHEMBL316132"}, {"smiles": "Oc1ccc(cc1)c2sc3cc(O)ccc3c2C(=O)c4ccc(cc4)N5CCN(CC5)C(=O)c6ccc(cc6)[N+](=O)[O-]", "pIC": -0.7654678421395714, "id": "CHEMBL362020"}, {"smiles": "Oc1ccc2c(c1)sc3c4cc(O)ccc4n(Cc5ccc(OCCN6CCCC6)cc5)c23", "pIC": -1.791759469228055, "id": "CHEMBL370849"}, {"smiles": "Oc1ccc(cc1)c2sc3cc(O)ccc3c2C(=O)c4ccc(cc4)N5CCN(CC5)c6ccc(Cl)cc6", "pIC": 1.5141277326297755, "id": "CHEMBL178679"}, {"smiles": "Oc1ccc2c(c1)sc3c4cc(O)ccc4n(Cc5ccc(OCCN6CCCCCC6)cc5)c23", "pIC": -1.205970806988609, "id": "CHEMBL264216"}, {"smiles": "CN1CCN(CC1)c2ccc(cc2)[C@@H]3Oc4ccc(O)cc4S[C@@H]3c5ccc(O)cc5", "pIC": -0.0, "id": "CHEMBL121978"}, {"smiles": "Oc1ccc(cc1)[C@H]2Sc3cc(O)ccc3O[C@H]2c4ccc(cc4)C5=CCNCC5", "pIC": -0.3364722366212129, "id": "CHEMBL334096"}, {"smiles": "Oc1ccc(cc1)[C@@H]2Sc3c(F)cc(O)cc3O[C@@H]2c4ccc(OCCN5CCCCC5)cc4", "pIC": -1.8082887711792655, "id": "CHEMBL94030"}, {"smiles": "C[C@H]1[C@@H]([C@@H](Oc2ccc(O)c(F)c12)c3ccc(OCCN4CCCCC4)cc3)c5ccc(O)cc5", "pIC": 0.2231435513142097, "id": "CHEMBL180146"}, {"smiles": "CN(C)CCOc1ccc(cc1)\\C(=C(\\CCCl)/c2ccccc2)\\c3ccc(O)cc3", "pIC": -1.3862943611198906, "id": "CHEMBL1402"}, {"smiles": "CSCCC\\C(=C(/c1ccc(O)cc1)\\c2ccc(OCCN(C)C)cc2)\\c3ccccc3", "pIC": -2.302585092994046, "id": "CHEMBL369935"}, {"smiles": "CCCN1CCN(CC1)c2ccc(cc2)C(=O)c3c(sc4cc(O)ccc34)c5ccc(O)cc5", "pIC": -0.3576744442718159, "id": "CHEMBL179518"}, {"smiles": "Oc1ccc2C3=C(CCOc2c1)c4ccc(O)cc4O[C@H]3c5ccc(OCCN6CCCCC6)cc5", "pIC": -1.2237754316221157, "id": "CHEMBL1088631"}, {"smiles": "CCN(CC)CCOc1ccc(cc1)[C@@H]2Oc3cc(F)ccc3C4=C2c5ccc(O)cc5OCC4", "pIC": -1.9459101490553132, "id": "CHEMBL1084120"}, {"smiles": "Oc1ccc2C3=C(CCOc2c1)c4ccc(O)cc4O[C@@H]3c5ccc(OCCN6CCCC6)cc5", "pIC": -0.1823215567939546, "id": "CHEMBL1086775"}, {"smiles": "C[C@H](CCc1ccc(O)cc1)NC(=O)Cc2c(c3ccccc3)n(Cc4ccc(OCCCN5CCCCC5)cc4)c6ccccc26", "pIC": -2.0541237336955462, "id": "CHEMBL238961"}, {"smiles": "Oc1ccc2O[C@H]([C@H](Sc2c1)C3CCCCC3)c4ccc(OCCN5CCCCC5)cc4", "pIC": -0.9555114450274363, "id": "CHEMBL85090"}, {"smiles": "Oc1ccc(cc1)[C@H]2Sc3cc(O)ccc3O[C@H]2c4ccc(OCCN5C6CCCC5CCC6)cc4", "pIC": 0.5108256237659907, "id": "CHEMBL184360"}, {"smiles": "Oc1ccc(cc1)c2sc3cc(O)ccc3c2C(=O)c4ccc(cc4)N5CCN(CC5)c6ccc(cc6)[N+](=O)[O-]", "pIC": 0.843970070294529, "id": "CHEMBL180176"}, {"smiles": "C[C@@H]1CCN(CCOc2ccc(cc2)[C@H]3[C@H](CCc4cc(O)ccc34)c5ccccc5)C1", "pIC": 0.6931471805599453, "id": "CHEMBL437695"}, {"smiles": "Cc1c(O)ccc2S[C@H]([C@H](Oc12)c3ccc(OCCN4CCCCC4)cc3)c5ccc(O)cc5", "pIC": -2.2300144001592104, "id": "CHEMBL329849"}, {"smiles": "C[C@@H]1CCCN1CCOc2ccc(cc2)[C@@H]3Oc4ccc(O)cc4S[C@@H]3c5ccc(O)cc5", "pIC": 0.35667494393873245, "id": "CHEMBL183489"}, {"smiles": "Cc1ccc(cc1)N2CCc3cc(O)ccc3C2(C)c4ccc(OCCN5CCCCC5)cc4", "pIC": -1.0647107369924282, "id": "CHEMBL174502"}, {"smiles": "Oc1ccc(cc1)[C@@H]2Sc3ccccc3O[C@@H]2c4ccc(OCCN5CCCCC5)cc4", "pIC": -2.302585092994046, "id": "CHEMBL68940"}, {"smiles": "CC(C)[C@@H]1CCN(CCOc2ccc(cc2)[C@@H]3Oc4ccc(O)cc4S[C@@H]3c5ccc(O)cc5)C1", "pIC": 0.916290731874155, "id": "CHEMBL361601"}, {"smiles": "CC1(N(CCc2cc(O)ccc12)c3ccccc3)c4ccc(OCCN5CCCCCC5)cc4", "pIC": -0.4054651081081644, "id": "CHEMBL328810"}, {"smiles": "C[C@H]1CCN(CCOc2ccc(cc2)[C@@H]3Oc4ccc(O)c(F)c4[C@@H](C)[C@@H]3c5ccc(O)cc5)C1", "pIC": 0.2231435513142097, "id": "CHEMBL181404"}, {"smiles": "Oc1ccc2[C@H]([C@H](CCc2c1)c3ccccc3)c4ccc(OCCN5CCCC5)cc4", "pIC": -0.3364722366212129, "id": "CHEMBL328190"}, {"smiles": "CSC1=C(C(=O)c2cc(O)cc(O)c12)c3ccc(O)cc3", "pIC": -0.6931471805599453, "id": "CHEMBL190038"}, {"smiles": "Oc1ccc(cc1)[C@H]2Sc3cc(O)ccc3O[C@H]2c4ccc(OCCN5CCCCC5)cc4", "pIC": 0.2231435513142097, "id": "CHEMBL304552"}, {"smiles": "CCCCN(C)C(=O)CCCCCCCCCCS[C@@H]1Cc2cc(O)ccc2[C@H]3CC[C@]4(C)[C@@H](O)CC[C@H]4[C@H]13", "pIC": -2.1972245773362196, "id": "CHEMBL1627354"}, {"smiles": "Oc1ccc2O[C@H]([C@@H](Cc3ccccc3)Sc2c1)c4ccc(OCCN5CCCCC5)cc4", "pIC": -2.0014800002101243, "id": "CHEMBL85536"}, {"smiles": "Oc1ccc(cc1)c2sc3cc(O)ccc3c2C(=O)c4ccc(cc4)N5CCN(CC5)C(=O)c6cccc(Cl)c6", "pIC": 0.7765287894989963, "id": "CHEMBL178665"}, {"smiles": "CCN(CC)CCOc1ccc(cc1)\\C(=C(\\Cl)/c2ccccc2)\\c3ccccc3", "pIC": -1.5173226235262947, "id": "CHEMBL954"}, {"smiles": "Oc1ccc(cc1)[C@H]2Sc3cc(O)ccc3O[C@H]2c4ccc(OCCN5CCC6(CCCC6)CC5)cc4", "pIC": -0.1823215567939546, "id": "CHEMBL184974"}, {"smiles": "Oc1ccc(cc1)B2345B678B9%10%11B%12%13%14B9%15%16B%12%17%18B2%15(B3%17%19B46%20B7%10%13C%14%18%19%20)C58%11%16", "pIC": -1.9286186519452522, "id": "CHEMBL373625"}, {"smiles": "Oc1ccc2c(c1)sc3c4cc(O)ccc4n(Cc5ccc(OCCN6CCCCC6)cc5)c23", "pIC": -1.0438040521731147, "id": "CHEMBL196131"}, {"smiles": "C[C@H]1CCCN1CCOc2ccc(cc2)[C@@H]3Oc4ccc(O)cc4S[C@@H]3c5ccc(O)cc5", "pIC": 0.2231435513142097, "id": "CHEMBL183344"}, {"smiles": "CC[C@H](COc1ccc(cc1)[C@@H]2Oc3ccc(O)cc3S[C@@H]2c4ccc(O)cc4)N5CCCC5", "pIC": 0.35667494393873245, "id": "CHEMBL369545"}, {"smiles": "Oc1ccc2c(noc2c1)c3cccc4c(O)cccc34", "pIC": -1.791759469228055, "id": "CHEMBL188051"}, {"smiles": "CCc1c(c2ccc(O)cc2)c3C=Cc4cccc1n34", "pIC": -2.2512917986064953, "id": "CHEMBL420017"}, {"smiles": "Oc1ccc(cc1)[C@H]2Sc3cc(O)ccc3O[C@H]2c4ccc(OCCN5C6CCCC5CC6)cc4", "pIC": 0.5108256237659907, "id": "CHEMBL184367"}, {"smiles": "Oc1ccc2c(c1)sc3c4cc(O)ccc4n(Cc5ccc(OCCN6CCOCC6)cc5)c23", "pIC": -2.302585092994046, "id": "CHEMBL370282"}, {"smiles": "Cc1ccc(cc1)C(=O)N2CCN(CC2)c3ccc(cc3)C(=O)c4c(sc5cc(O)ccc45)c6ccc(O)cc6", "pIC": -1.007957920399979, "id": "CHEMBL180702"}, {"smiles": "C[C@H]1[C@@H]([C@@H](Oc2ccc(O)cc12)c3ccc(OCCN4CCCC4)cc3)c5ccc(O)cc5", "pIC": -0.4054651081081644, "id": "CHEMBL181936"}, {"smiles": "Oc1ccc(cc1)c2oc3c(Br)cc(O)cc3c2", "pIC": -0.4054651081081644, "id": "CHEMBL183782"}, {"smiles": "CC(C)c1ccc(cc1)N2CCc3cc(O)ccc3C2(C)c4ccc(OCCN5CCCC5)cc4", "pIC": -0.9555114450274363, "id": "CHEMBL98470"}, {"smiles": "Oc1ccc(cc1)[C@H]2Sc3cc(O)ccc3O[C@H]2CCCN4CCCCC4", "pIC": 0.35667494393873245, "id": "CHEMBL122208"}, {"smiles": "Oc1ccc2C(N(CCc2c1)S(=O)(=O)c3cccc4ccccc34)c5ccc(OCCN6CCCC6)cc5", "pIC": -1.7227665977411035, "id": "CHEMBL93230"}, {"smiles": "Oc1ccc(cc1)[C@H]2Sc3cc(O)ccc3O[C@H]2c4ccc(cc4)N5CCCNCC5", "pIC": -1.2809338454620642, "id": "CHEMBL340606"}, {"smiles": "C[C@]12CC[C@H]3[C@@H](CCc4cc(O)ccc34)[C@@H]1C[C@@H](O)[C@@H]2O", "pIC": -0.5247285289349821, "id": "CHEMBL193482"}, {"smiles": "Oc1ccc(cc1)[C@@H]2Sc3cc(O)ccc3O[C@@H]2c4ccc(OCCN5CCCCC5)cc4", "pIC": -1.0986122886681098, "id": "CHEMBL539927"}, {"smiles": "Oc1cccc(c1)[C@H]2Sc3cc(O)ccc3S[C@H]2c4ccc(OCCN5CCCCC5)c(Br)c4", "pIC": -1.3862943611198906, "id": "CHEMBL125362"}, {"smiles": "Oc1ccc2C3=C(CCOc2c1)c4ccc(O)cc4O[C@@H]3c5ccc(OCCCN6C(=O)CCC6=O)cc5", "pIC": -0.9669838461896731, "id": "CHEMBL1087557"}, {"smiles": "Oc1ccc2C3=C(CCOc2c1)c4ccc(O)cc4O[C@H]3c5ccc(OCCN6CCOCC6)cc5", "pIC": -2.302585092994046, "id": "CHEMBL1087812"}, {"smiles": "Oc1ccc2C3=C(CCOc2c1)c4ccc(O)cc4O[C@@H]3c5ccc(OCCN6CCSCC6)cc5", "pIC": -0.1823215567939546, "id": "CHEMBL1083178"}, {"smiles": "Oc1ccc(cc1)C2=C(Br)c3cc(O)ccc3C2=O", "pIC": -1.6486586255873816, "id": "CHEMBL363872"}, {"smiles": "Oc1ccc(cc1)[C@H]2Sc3cc(O)ccc3O[C@H]2c4ccc(OCCN5CC[C@H]6C[C@@H]56)cc4", "pIC": 0.5108256237659907, "id": "CHEMBL184421"}, {"smiles": "Oc1ccc(cc1)[C@H]2Sc3cc(O)ccc3O[C@H]2c4ccc(OCCN5CCS(=O)(=O)CC5)cc4", "pIC": -0.6931471805599453, "id": "CHEMBL185383"}, {"smiles": "Oc1ccc(cc1)[C@H]2Sc3cc(O)ccc3O[C@H]2c4ccc(OCCN5CCCC5)cc4", "pIC": -0.9555114450274363, "id": "CHEMBL362623"}, {"smiles": "Oc1ccc(cc1)C2=C(c3ccc(OCCN4CCCCC4)cc3)c5ccc(F)cc5OCC2", "pIC": -1.8718021769015913, "id": "CHEMBL511971"}, {"smiles": "CC(C)N(CCOc1ccc(cc1)[C@H]2Oc3cc(O)ccc3C4=C2c5ccc(O)cc5OCC4)C(C)C", "pIC": -1.6863989535702288, "id": "CHEMBL1085669"}, {"smiles": "CC(C)N(CCOc1ccc(cc1)[C@@H]2Oc3cc(O)ccc3C4=C2c5ccc(O)cc5OCC4)C(C)C", "pIC": -1.7227665977411035, "id": "CHEMBL1085899"}, {"smiles": "Oc1cccc(c1)C2Sc3cc(O)ccc3OC2c4ccc(OCCN5CCCCC5)cc4", "pIC": -1.2809338454620642, "id": "CHEMBL91807"}, {"smiles": "C[C@H](CN1CCCC1)Oc2ccc(cc2)[C@@H]3Oc4ccc(O)cc4S[C@@H]3c5ccc(O)cc5", "pIC": -1.840549633397487, "id": "CHEMBL183044"}, {"smiles": "C[C@@H](COc1ccc(cc1)C(=O)c2c(sc3cc(O)ccc23)c4ccc(O)cc4)N5CCCC5", "pIC": 1.6094379124341003, "id": "CHEMBL198803"}, {"smiles": "Oc1ccc(cc1)[C@@H]2Sc3cc(O)c(Cl)cc3O[C@@H]2c4ccc(OCCN5CCCCC5)cc4", "pIC": -1.6863989535702288, "id": "CHEMBL90072"}, {"smiles": "NC(=O)C1CCN(CCOc2ccc(cc2)[C@@H]3Oc4ccc(O)cc4S[C@@H]3c5ccc(O)cc5)CC1", "pIC": -0.7884573603642703, "id": "CHEMBL184491"}, {"smiles": "C[C@H](CCc1ccc(O)cc1)NC(=O)Cc2c([nH]c3cc(OCCCN4CCCC4)ccc23)c5ccccc5", "pIC": -2.2082744135228043, "id": "CHEMBL393982"}, {"smiles": "C[C@H](NC(=O)Cc1c([nH]c2ccccc12)c3ccccc3)c4c(C)c5cc(O)ccc5n4Cc6ccc(OCCN7CCCCC7)cc6", "pIC": -0.6931471805599453, "id": "CHEMBL240438"}, {"smiles": "Oc1ccc(cc1)[C@H]2Sc3cc(O)ccc3O[C@H]2c4ccc(OCCN5C6CCC5CC6)cc4", "pIC": 0.10536051565782628, "id": "CHEMBL368688"}, {"smiles": "Oc1cccc(c1)[C@H]2Sc3cc(O)ccc3O[C@H]2c4ccc(OCCN5CCOCC5)cc4", "pIC": -1.547562508716013, "id": "CHEMBL92027"}, {"smiles": "Oc1ccc(cc1)[C@H]2Sc3cc(O)ccc3O[C@H]2c4ccc(cc4)C5CCNCC5", "pIC": -0.5306282510621704, "id": "CHEMBL125119"}, {"smiles": "Oc1ccc(c(Cl)c1)c2ccc3cc(O)ccc3c2", "pIC": -2.302585092994046, "id": "CHEMBL195311"}, {"smiles": "CC(C)n1nc(c2ccc(O)cc2)c3cccc(c13)C(F)(F)F", "pIC": -1.0986122886681098, "id": "CHEMBL386502"}, {"smiles": "Oc1ccc(cc1)[C@H]2Sc3cc(O)ccc3O[C@H]2c4ccc(OCCN5C[C@H]6CCC[C@H]6C5)cc4", "pIC": 1.2039728043259361, "id": "CHEMBL433769"}, {"smiles": "CC(C)(COc1ccc(cc1)[C@@H]2Oc3ccc(O)cc3S[C@@H]2c4ccc(O)cc4)N5CCCC5", "pIC": 0.35667494393873245, "id": "CHEMBL179852"}, {"smiles": "Cc1ccc(cc1)N2CCc3cc(O)ccc3C2(C)c4ccc(OCCN5CCCC5)cc4", "pIC": -1.252762968495368, "id": "CHEMBL327515"}, {"smiles": "Oc1ccc2C(Cc3ccccc3)N(CCc2c1)c4ccccc4", "pIC": -1.9021075263969205, "id": "CHEMBL315866"}, {"smiles": "C[C@H](COc1ccc(cc1)[C@@H]2Oc3ccc(O)cc3S[C@@H]2c4ccc(O)cc4)N5CCCC5", "pIC": -0.5306282510621704, "id": "CHEMBL180792"}, {"smiles": "C[C@@H]1CCN(CCOc2ccc(cc2)[C@@H]3Oc4ccc(O)cc4[C@@H](C)[C@@H]3c5ccc(O)cc5)C1", "pIC": -0.8754687373538999, "id": "CHEMBL369724"}, {"smiles": "CC(C)c1ccc(cc1)N2CCc3cc(O)ccc3C2(C)c4ccc(OCCN5CCCCC5)cc4", "pIC": -1.6486586255873816, "id": "CHEMBL100231"}, {"smiles": "Oc1ccc(cc1)[C@H]2Sc3cc(O)ccc3O[C@H]2c4ccc(OCCN5CC6CCC5CC6)cc4", "pIC": -0.26236426446749106, "id": "CHEMBL361056"}, {"smiles": "CC(C)[C@H]1Sc2cc(O)ccc2O[C@H]1c3ccc(OCCN4CCCCC4)cc3", "pIC": -1.9459101490553132, "id": "CHEMBL313825"}, {"smiles": "Oc1ccc2O[C@H]([C@H](Sc2c1)c3cccs3)c4ccc(OCCN5CCCCC5)cc4", "pIC": -2.174751721484161, "id": "CHEMBL83623"}, {"smiles": "CC(C)[C@@H](COc1ccc(cc1)[C@@H]2Oc3ccc(O)cc3S[C@@H]2c4ccc(O)cc4)N5CCCC5", "pIC": 0.35667494393873245, "id": "CHEMBL183263"}, {"smiles": "CC(C)N1CCN(CC1)c2ccc(cc2)C(=O)c3c(sc4cc(O)ccc34)c5ccc(O)cc5", "pIC": 1.2729656758128873, "id": "CHEMBL178334"}, {"smiles": "CC1(N(CCc2cc(O)ccc12)c3cccc(Cl)c3)c4ccc(OCCN5CCCC5)cc4", "pIC": -1.0647107369924282, "id": "CHEMBL319678"}, {"smiles": "Cc1ccccc1C(=O)N2CCN(CC2)c3ccc(cc3)C(=O)c4c(sc5cc(O)ccc45)c6ccc(O)cc6", "pIC": -1.3711807233098425, "id": "CHEMBL182157"}, {"smiles": "Oc1ccc(cc1)C2=Cc3cc(O)ccc3C24Cc5ccc(OCCN6CCCCC6)cc5C4", "pIC": -0.0, "id": "CHEMBL267385"}, {"smiles": "CC\\C(=C(/c1ccc(O)cc1)\\c2ccc(OCCN(C)C)cc2)\\c3ccccc3", "pIC": -0.6931471805599453, "id": "CHEMBL489"}, {"smiles": "C[C@@H]1CN(CCOc2ccc(cc2)[C@@H]3Oc4ccc(O)cc4S[C@@H]3c5ccc(O)cc5)C[C@H]1C", "pIC": 0.916290731874155, "id": "CHEMBL183467"}, {"smiles": "Oc1ccc(cc1)[C@H]2Sc3c(F)c(O)ccc3O[C@H]2c4ccc(OCCN5CCCCC5)cc4", "pIC": -0.0, "id": "CHEMBL329892"}, {"smiles": "Oc1ccc2C3=C(COc2c1)c4ccc(O)cc4O[C@H]3c5ccc(OCCN6CCCCC6)cc5", "pIC": 0.4942963218147801, "id": "CHEMBL207324"}, {"smiles": "Oc1ccc(cc1)C2=C(c3ccc(OCCN4CCCC4)cc3)c5ccc(O)cc5OCC2", "pIC": -2.128231705849268, "id": "CHEMBL469511"}, {"smiles": "Oc1ccc2C3=C(CCOc2c1)c4ccc(O)cc4O[C@H]3c5ccc(OCCN6CCCCCC6)cc5", "pIC": -0.8754687373538999, "id": "CHEMBL1086774"}, {"smiles": "Oc1ccc2C3=C(CCOc2c1)c4ccc(O)cc4O[C@H]3c5ccc(OCCN6C(=O)CCC6=O)cc5", "pIC": -1.824549292051046, "id": "CHEMBL1088337"}, {"smiles": "CCN(CC)CCOc1ccc(cc1)[C@H]2Oc3cc(F)ccc3C4=C2c5ccc(O)cc5OCC4", "pIC": -1.6094379124341003, "id": "CHEMBL1088629"}, {"smiles": "COc1ccc2C3=C([C@H](Oc2c1)c4ccc(OCCN5CCCCC5)cc4)c6ccc(O)cc6OCC3", "pIC": -2.1972245773362196, "id": "CHEMBL1088483"}, {"smiles": "Oc1ccc(cc1)C2=C(c3ccccc3)c4ccc(O)cc4C2=O", "pIC": -2.1972245773362196, "id": "CHEMBL192586"}, {"smiles": "CN1CCN(CCOc2ccc(cc2)[C@H]3Oc4cc(O)ccc4C5=C3c6ccc(O)cc6OCC5)CC1", "pIC": -2.163323025660538, "id": "CHEMBL1084922"}, {"smiles": "C[C@@H]1CCN(CCOc2ccc(cc2)C(=O)c3c(sc4cc(O)ccc34)c5ccc(O)cc5)C1", "pIC": 0.5108256237659907, "id": "CHEMBL372337"}, {"smiles": "C[C@@H](COc1ccc(cc1)[C@@H]2Oc3ccc(O)c(F)c3[C@@H](C)[C@@H]2c4ccc(O)cc4)N5CC[C@@H](C)C5", "pIC": 0.10536051565782628, "id": "CHEMBL180995"}, {"smiles": "CCSC1=C(C(=O)c2cc(O)ccc12)c3ccc(O)cc3", "pIC": -2.302585092994046, "id": "CHEMBL193108"}, {"smiles": "CC(C)[C@H](COc1ccc(cc1)[C@@H]2Oc3ccc(O)cc3S[C@@H]2c4ccc(O)cc4)N5CCCC5", "pIC": 0.6931471805599453, "id": "CHEMBL182794"}, {"smiles": "Cc1c(c2ccc(O)cc2)n(Cc3ccc(OCCN4CCCCCC4)cc3)c5ccc(O)cc15", "pIC": 0.5108256237659907, "id": "CHEMBL46740"}, {"smiles": "Oc1ccc(cc1)[C@@H]2Sc3cc(O)cc(Cl)c3O[C@@H]2c4ccc(OCCN5CCCCC5)cc4", "pIC": -1.667706820558076, "id": "CHEMBL441457"}, {"smiles": "CN(C)C(=O)\\C=C\\c1ccc(cc1)N2CCc3cc(O)ccc3C2c4ccccc4", "pIC": -2.0794415416798357, "id": "CHEMBL93391"}, {"smiles": "Oc1ccc(cc1)[C@H]2Sc3cc(O)ccc3O[C@H]2c4ccc(COCCN5CCCCC5)cc4", "pIC": -0.8329091229351039, "id": "CHEMBL122237"}, {"smiles": "C[C@@H]1CCN(CCOc2ccc(cc2)[C@@H]3Oc4ccc(O)c(F)c4[C@@H](C)[C@@H]3c5ccc(O)cc5)C1", "pIC": 0.2231435513142097, "id": "CHEMBL361005"}, {"smiles": "Oc1ccc(cc1)[C@H]2Sc3cc(O)ccc3O[C@H]2c4ccc(OCCN5CC[C@@H](F)C5)cc4", "pIC": 0.6931471805599453, "id": "CHEMBL184679"}, {"smiles": "Oc1ccc2c(noc2c1)c3ccc4cc(O)ccc4c3", "pIC": -2.0794415416798357, "id": "CHEMBL187105"}, {"smiles": "C[C@]12CC[C@H]3[C@@H](CCc4cc(O)ccc34)[C@@H]1CCC2=O", "pIC": -2.0347056478384444, "id": "CHEMBL1405"}, {"smiles": "CC1(N(CCc2cc(O)ccc12)c3ccccc3)c4ccc(OCCN5CCCC5)cc4", "pIC": -0.5877866649021191, "id": "CHEMBL98558"}, {"smiles": "C[C@H]1[C@@H]([C@@H](Oc2ccc(O)c(F)c12)c3ccc(OCCN4CCCCCC4)cc3)c5ccc(O)cc5", "pIC": 1.2039728043259361, "id": "CHEMBL181368"}, {"smiles": "CC1(N(CCc2cc(O)ccc12)c3ccc(Cl)cc3)c4ccc(OCCN5CCCCC5)cc4", "pIC": -1.1314021114911006, "id": "CHEMBL103294"}, {"smiles": "Cc1cc(O)cc2S[C@H]([C@H](Oc12)c3ccc(OCCN4CCCCC4)cc3)c5ccc(O)cc5", "pIC": -1.667706820558076, "id": "CHEMBL327471"}, {"smiles": "Oc1ccc2O[C@@H]([C@@H](Sc2c1)c3ccccc3)c4ccc(OCCN5CCCCC5)cc4", "pIC": -1.824549292051046, "id": "CHEMBL71585"}, {"smiles": "CC1(N(CCc2cc(O)ccc12)c3ccc(Cl)cc3)c4ccc(OCCN5CCCC5)cc4", "pIC": -1.1939224684724346, "id": "CHEMBL100763"}, {"smiles": "OCCC1CCN(CCOc2ccc(cc2)[C@@H]3Oc4ccc(O)cc4S[C@@H]3c5ccc(O)cc5)CC1", "pIC": -1.9878743481543455, "id": "CHEMBL365484"}, {"smiles": "Oc1ccc(cc1)c2sc3cc(O)ccc3c2C(=O)c4ccc(cc4)N5CCN(CC5)C(=O)c6occc6", "pIC": -0.9745596399981308, "id": "CHEMBL178857"}, {"smiles": "C[C@H]1CN(CCOc2ccc(cc2)[C@@H]3Oc4ccc(O)cc4S[C@@H]3c5ccc(O)cc5)C[C@@H]1C", "pIC": 0.6931471805599453, "id": "CHEMBL182980"}, {"smiles": "CC1(N(CCc2cc(O)ccc12)c3cccc(F)c3)c4ccc(OCCN5CCCC5)cc4", "pIC": -1.0986122886681098, "id": "CHEMBL319211"}, {"smiles": "Oc1ccc2[C@H]([C@H](OCc2c1)c3ccccc3)c4ccc(OCCN5CCCC5)cc4", "pIC": -0.8754687373538999, "id": "CHEMBL183162"}, {"smiles": "CC(C)[C@H]1CCN(CCOc2ccc(cc2)[C@@H]3Oc4ccc(O)cc4S[C@@H]3c5ccc(O)cc5)C1", "pIC": 1.2039728043259361, "id": "CHEMBL427324"}, {"smiles": "Oc1ccc2C3=C([C@@H](Oc2c1)c4ccc(OCCN5CCCCCC5)cc4)c6ccccc6OCC3", "pIC": -1.3862943611198906, "id": "CHEMBL1087418"}, {"smiles": "Oc1ccc2C3=C(CCOc2c1)c4ccccc4O[C@H]3c5ccc(OCCN6CCCCCC6)cc5", "pIC": -1.5040773967762742, "id": "CHEMBL1087297"}, {"smiles": "Oc1ccc2C3=C(CCOc2c1)c4ccccc4O[C@H]3c5ccc(OCCN6CCCCC6)cc5", "pIC": -1.4350845252893227, "id": "CHEMBL1087426"}, {"smiles": "Oc1ccc2C3=C(CCOc2c1)c4ccc(O)cc4O[C@@H]3c5ccc(OCCN6CCCCC6)cc5", "pIC": -0.09531017980432493, "id": "CHEMBL1088485"}, {"smiles": "COC(=O)COc1ccc(cc1)C2Oc3cc(O)ccc3C4=C2c5ccc(O)cc5OCC4", "pIC": -1.5686159179138452, "id": "CHEMBL1085161"}, {"smiles": "COc1ccc2C3=C([C@@H](Oc2c1)c4ccc(OCCN5CCCCC5)cc4)c6ccc(O)cc6OCC3", "pIC": -1.840549633397487, "id": "CHEMBL1082864"}, {"smiles": "C[C@H](CCc1ccc(O)cc1)NC(=O)Cc2c([nH]c3ccc(OCCCCCN4CCCCC4)cc23)c5ccccc5", "pIC": -1.8870696490323797, "id": "CHEMBL241256"}, {"smiles": "C[C@H](CCc1ccc(O)cc1)NC(=O)Cc2c(c3ccccc3)n(Cc4ccc(OCCCCN5CCCCC5)cc4)c6ccccc26", "pIC": -1.589235205116581, "id": "CHEMBL396119"}, {"smiles": "CCN(CC)CCOc1ccc(cc1)[C@@H]2Oc3ccccc3C4=C2c5ccc(O)cc5OCC4", "pIC": -2.1972245773362196, "id": "CHEMBL1084129"}, {"smiles": "Oc1ccc2C(C(CCc2c1)c3ccccc3)c4ccc(OCCN5CCCC5)cc4", "pIC": 0.6931471805599453, "id": "CHEMBL92748"}, {"smiles": "Oc1ccc(cc1)c2sc3cc(O)ccc3c2Oc4ccc(OCCN5CCCCC5)cc4", "pIC": -2.0541237336955462, "id": "CHEMBL226268"}, {"smiles": "CCCN(c1c(C)cccc1CC)S(=O)(=O)c2ccc(O)c(C)c2", "pIC": -1.9459101490553132, "id": "CHEMBL371637"}, {"smiles": "Oc1ccc(cc1)C(=C(CC(F)(F)F)c2ccccc2)c3ccc(O)cc3", "pIC": -2.1972245773362196, "id": "CHEMBL357283"}, {"smiles": "C(CN1CCC1)Oc2ccc(cc2)C3=C(CCOc4ccccc34)c5ccccc5", "pIC": -2.1713368063840917, "id": "CHEMBL513397"}, {"smiles": "CCN1CCN(CC1)c2ccc(cc2)[C@@H]3Oc4ccc(O)cc4S[C@@H]3c5ccc(O)cc5", "pIC": -0.0, "id": "CHEMBL121720"}, {"smiles": "Cn1cc(NC(=O)c2cc(NC(=O)CCS(=O)(=O)C)cn2C)cc1C(=O)NCCCC(=O)NCCCCCC[C@@H]3Cc4cc(O)ccc4[C@H]5CC[C@]6(C)[C@@H](O)CC[C@H]6[C@H]35", "pIC": -0.10436001532424286, "id": "CHEMBL1818254"}, {"smiles": "C[C@H](COc1ccc(cc1)C(=O)c2c(sc3cc(O)ccc23)c4ccc(O)cc4)N5CCCC5", "pIC": 1.6094379124341003, "id": "CHEMBL2024377"}, {"smiles": "C[C@H]1CCN(CCOc2ccc(cc2)C(=O)c3c(sc4cc(O)ccc34)c5ccc(O)cc5)C1", "pIC": 0.5108256237659907, "id": "CHEMBL2024376"}, {"smiles": "C[C@H](CN1CCCC1)Oc2ccc(cc2)[C@@H]3Oc4ccc(O)cc4[C@@H](C)[C@@H]3c5ccc(O)cc5", "pIC": -0.4054651081081644, "id": "CHEMBL2113002"}, {"smiles": "Oc1ccc(cc1)[C@@H]2Sc3cc(O)ccc3O[C@H]2c4ccc(OCCN5CCCCC5)cc4", "pIC": -1.0986122886681098, "id": "CHEMBL2111532"}, {"smiles": "CC[C@H]1CCN(CCOc2ccc(cc2)[C@@H]3Oc4ccc(O)cc4S[C@@H]3c5ccc(O)cc5)C1", "pIC": -0.09531017980432493, "id": "CHEMBL2113027"}, {"smiles": "Oc1ccc(cc1)c2sc3cc(O)ccc3c2C(=O)c4ccc(cc4)N5CCN(Cc6ccccc6)CC5", "pIC": 0.030459207484708574, "id": "CHEMBL2113001"}, {"smiles": "CCCC(CCC)(c1ccc(O)c(C)c1)c2ccc(O)c(C)c2", "pIC": -1.589235205116581, "id": "CHEMBL2403356"}]"""

#readMolecules("data/er_antagonist_decoys.mol2", decoy)    # temporal
#readMolecules("data/er_antagonist_ligands.mol2", active)    # temporal
#print chembl["bioactivities"][0]
#print getPossibles(chembl["bioactivities"],u'units')
nodenetwork={
    1:Node("loadChembl",loader.loadMoleculesFromChEMBL,params="CHEMBL206"),
    2:Node("filterByActivity",filters.filterByActivity,need=[1]),
    7:Node("addActivityChEMBL",utils.addValue,params={"activity":1},need=[2]),
    11:Node("filterKeysChEMBL",filters.filterKeys,params=["id","pIC","activity"],need=[7]),
    12:Node("getRDMolFromChEMBL",loader.getRDMolFromChEMBL,need=[11]),
    
    3:Node("readMoleculesLigands",loader.readMoleculesFromMol2,params="data/er_antagonist_ligands.mol2"),
    13:Node("createMoleculesLigands",filters.createMolecules,need=[3]),
    5:Node("addActivityLigands",utils.addValue,params={"activity":1,"pIC":6},need=[13]),
    4:Node("readMoleculesDecoys",loader.readMoleculesFromMol2,params="data/er_antagonist_decoys.mol2"),
    14:Node("createMoleculesDecoys",filters.createMolecules,need=[4]),
    6:Node("addActivityDecoys",utils.addValue,params={"activity":0,"pIC":0},need=[14]),
    8:Node("concatLigandsDecoys",utils.concatenate,need=[5,6]),
    
    9:Node("concatLigandsDecoysChEMBL",utils.concatenate,need=[12,8]),
    15:Node("postCatCheckPoint",filters.checkPoint,need=[9],params=["RDMol","pIC","activity","id"]),
    16:Node("fingerprints",processor.fingerPrints,need=[15],params={"fingerprint":"topological","radius":2}),
    18:Node("prePickerSplit",utils.spitter,need=[16],params={"key":"activity","value":1}),
    17:Node("divPickerLigands",processor.DiversePicker,need=[18],needpos=[0],params={"size":30}),
    19:Node("divPickerDecoys",processor.DiversePicker,need=[18],needpos=[1],params={"size":30}),
    20:Node("postPickCat",utils.concatenate,need=[17,19]),
    
    100:Node("",lambda x:x)
             }
def main():
    nodenetwork[18].invalidate()
    #chembl=loadMoleculesFromChEMBL("CHEMBL206")
    #filtrate=filterByActivity(chembl["bioactivities"])
    #print "filtrated"
    #exit()
    #arr1=processor.execute(nodenetwork, 7)
    #arr2=processor.execute(nodenetwork, 8)
    arr=executor.execute(nodenetwork, 20)
    #print("len arr1="+str(len(arr1)))
    #print("len arr2="+str(len(arr2)))
    print("len arr="+str(len(arr)))
    print([elem.activity for elem in arr])
main()


