import unittest

import numpy as np
import pandas
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

import categorization
from unsupervised_GraphSAGE import UnsupervisedGraphSAGE


class MyTestCase(unittest.TestCase):
    def test_plot_embedding_scatter_Wave2Vec(self):
        """
        this just tests the plotting capabilities of the scatter plot
        :return:
        """
        # data is a tuple of node embeddings
        data = ([3.3330023, 3.561639, 6.589698, -4.7265286,
                 4.6781564, 7.5142694, 13.688438, 1.6063952,
                 1.6049043, 0.99830973, -5.1681557, -2.8908863,
                 6.616754, 4.3329587, -4.6663914, -7.155874,
                 -8.143685, 12.824974, -8.706427, 1.4858488,
                 10.79331, 13.497556, 10.599396, 2.2197173,
                 -5.8614397, 12.994918, -5.179164, -6.4388843,
                 1.6111507, 1.9861838, -2.5384903, -7.0952477,
                 -8.151745, -1.4109113, 5.3046136, -10.546682,
                 -7.6875415, -8.937828, -8.273917, -9.224861,
                 2.2334068, -9.657032, 7.7591615, -9.333963,
                 -5.92966, 8.534093, 5.1510878, 8.651328,
                 -7.3117037, 2.7587047, 9.582241, -4.2645245,
                 -7.478939, -5.2008576, 5.985793, 2.1845245,
                 -12.478377, 2.2541199, -4.7357154, 0.28910792,
                 -3.0990472, -7.0446734, -11.112159, 2.9855592,
                 1.8955754, -9.074958, 12.416974, 6.5503855,
                 13.17812, -6.226892, -8.629497, 3.15222,
                 1.9645569, 8.160886, 4.7919855, 2.4043567,
                 -7.356034, 0.7346413, 10.088229, 6.53879,
                 -2.272885, -2.3223534, 8.454225, 8.946386,
                 8.496465, 10.665854, -6.653851, -7.4484677,
                 6.196666, -10.221012, 15.29435, 12.169046,
                 6.6013293, 10.780287, -8.755308, -0.12431898,
                 -4.958663, -5.9132085, -8.412387, -6.6441536,
                 3.1370554, 1.7728003, 2.5329967, 2.2806988,
                 -2.785771, 10.815036, -9.869041, 4.5192204,
                 14.005128, -7.04065, -8.588685, 6.6239076,
                 -2.7480736, 2.0489569, 0.5678261, 6.889491,
                 0.57787424, 8.258528, -8.207662, 8.739309,
                 -8.248929, -2.0384245, 13.935599, -6.3898077,
                 -5.4391932, -2.0310755, 8.6778, -9.025752,
                 0.5487672, -5.436681, -6.3838477, 12.766224,
                 -5.0082283, -2.1081932, -6.1716805, -2.133484,
                 -8.14314, -0.8298971, 7.914728, -0.86433285,
                 -7.961184, -11.141721, -11.1754875, 2.9895449,
                 -10.60271, -9.3643055, -9.301046, -10.613032,
                 -9.308895, -10.612444, -8.628873, 2.259551,
                 8.622112, 4.7206, -7.7048755, -8.575613,
                 12.504288, -11.115827, 12.747194, 2.9750195,
                 9.003617, 1.9931946, 3.4287405, 9.980693,
                 3.348549, -7.9884586, 4.72738, 1.9322176,
                 -7.631189, 2.2726133, 1.9942912, 3.1720004,
                 12.485455, 3.1956654, 3.2534168, 10.004798,
                 8.971912, 4.1352606, 4.065838, 4.160985,
                 13.665642, 10.565811, -6.780044, 10.499268,
                 10.37164, 10.514878, -7.552678, -7.430113,
                 -7.484017, -7.543199, 11.496784, 13.653475,
                 3.0131574, -6.0814247, -6.0612745, 12.654954,
                 11.443334, -8.220683, 2.8585677, -5.48574,
                 3.105116, 2.5055635, 2.5075428, 2.8216121,
                 -8.591517, 11.491183, 0.7807467, 0.7220218,
                 0.63013273, 0.710047, 1.955293, 1.911164,
                 1.934232, -2.6445053],
                [-9.52122879e+00, 1.41339331e+01, 1.16807652e+01, 8.12396812e+00,
                 3.03958011e+00, 5.47326756e+00, 5.11692858e+00, -7.84784555e+00,
                 -2.89390755e+00, 4.00634909e+00, -3.91111541e+00, 4.05510712e+00,
                 1.63558369e+01, -6.00553322e+00, -1.77845490e+00, 2.43216586e+00,
                 3.25563699e-01, 3.69582725e+00, -1.14620104e+01, 1.15860205e+01,
                 1.25639415e+00, 4.02110577e+00, 1.96482718e+00, -6.15506315e+00,
                 -1.29780588e+01, 2.73607135e+00, 2.58618474e+00, 7.82249451e+00,
                 1.77526796e+00, -5.42587805e+00, -1.34694319e+01, -1.40644956e+00,
                 8.60217953e+00, -4.20303631e+00, 1.78341424e+00, -1.11672516e+01,
                 6.46091890e+00, -1.30060940e+01, -5.53108931e-01, -1.39896739e+00,
                 1.20629292e+01, -1.39754047e+01, 1.31780701e+01, -1.32966483e+00,
                 3.70125222e+00, 4.16510630e+00, 1.26726522e+01, 3.46439600e+00,
                 5.82224274e+00, 4.43696594e+00, 7.91867542e+00, 3.48006225e+00,
                 -2.24920297e+00, 4.95375824e+00, -3.51618695e+00, 5.52011609e-01,
                 -1.23999777e+01, -3.83375454e+00, 8.07483137e-01, -4.72247791e+00,
                 -1.30194263e+01, -1.28306999e+01, -1.08002748e+01, 2.50088143e+00,
                 1.20428877e+01, -1.50254412e+01, 1.00296998e+00, 1.44698038e+01,
                 6.12533903e+00, 7.54419041e+00, -1.01848688e+01, 3.19500446e+00,
                 8.06824493e+00, 1.47407722e+01, -4.40929937e+00, 3.15531659e+00,
                 -1.40514183e+01, 9.85883236e+00, 6.42011976e+00, 1.43975811e+01,
                 -1.29329748e+01, -1.31440840e+01, 1.50548248e+01, 3.71237183e+00,
                 1.50109501e+01, 6.21717024e+00, -1.63062787e+00, -1.08861160e+01,
                 1.20624895e+01, -1.19874878e+01, 1.53570592e+00, 4.37573576e+00,
                 8.92479610e+00, 2.19660044e+00, -1.42143154e+01, -6.21739101e+00,
                 2.24880195e+00, 1.39704943e+00, -1.29194441e+01, 3.43198490e+00,
                 2.34972668e+00, -6.69748831e+00, 3.90418363e+00, 4.55770540e+00,
                 -1.29035416e+01, 8.68132472e-01, -1.42643003e+01, -5.97377825e+00,
                 5.32849550e+00, -1.41671629e+01, -9.85834312e+00, 1.35354719e+01,
                 -1.40945702e+01, 1.19563303e+01, 4.52541828e+00, 1.49566612e+01,
                 4.49114227e+00, 1.40122604e+01, -2.70931411e+00, 1.53837042e+01,
                 -2.74079394e+00, -4.04432583e+00, 5.31869555e+00, -2.66366768e+00,
                 6.96627760e+00, -3.96989083e+00, 1.39369326e+01, -1.48992300e+01,
                 3.58644795e+00, 6.97996426e+00, -2.67605162e+00, 6.72069311e+00,
                 5.22075987e+00, -4.21111012e+00, 7.47495747e+00, -4.18749619e+00,
                 6.87799597e+00, -6.09272814e+00, 1.33876448e+01, -6.09457970e+00,
                 7.30929327e+00, -1.26242342e+01, -1.26595097e+01, 1.09958467e+01,
                 -1.01537437e+01, -9.13594440e-02, 4.34213504e-02, -1.01318254e+01,
                 -7.46599166e-03, -1.01724920e+01, -1.04416142e+01, -4.05713606e+00,
                 1.37327909e+01, -4.42282438e+00, -2.78390050e+00, -1.39104724e-01,
                 1.35728669e+00, -1.26225748e+01, 6.71543360e+00, 1.09928780e+01,
                 3.95569658e+00, 1.02601423e+01, 4.66233969e+00, 5.93844366e+00,
                 4.74379730e+00, 7.26932955e+00, -4.41578484e+00, 1.77384734e+00,
                 -1.39139090e+01, -4.08130741e+00, 1.02864037e+01, 1.00004845e+01,
                 1.38511455e+00, 1.00681887e+01, 1.00475206e+01, 5.71215630e+00,
                 4.10878134e+00, 1.11654949e+01, 1.12080526e+01, 1.11703815e+01,
                 1.90453148e+00, 5.76119471e+00, -1.73437417e+00, 4.36361170e+00,
                 5.75279856e+00, 4.37836123e+00, 1.27077591e+00, 5.71543932e+00,
                 5.64711523e+00, 1.17151642e+00, 3.37900019e+00, 1.90624976e+00,
                 -7.25014257e+00, 1.50675249e+00, 1.49794519e+00, 2.31304789e+00,
                 3.37876940e+00, -1.25235443e+01, -7.13175344e+00, 3.20754385e+00,
                 -7.59521389e+00, -7.41059637e+00, -7.71671391e+00, -7.90414667e+00,
                 -1.36124907e+01, 3.31006122e+00, -5.95393181e+00, -6.01889038e+00,
                 -6.46378183e+00, -6.31541777e+00, 3.82641315e+00, 4.35973883e+00,
                 3.80683351e+00, -1.28344488e+01])
        # c is a category vector corresponding to the data
        c = [0, 2, 1, 0, 1, 1, 0, 0, 0, 4, 3, 0, 0, 1, 2, 0, 2, 5, 2, 1, 1, 1, 5, 0, 1, 1, 5, 2, 5, 0, 4, 0, 1, 3, 4, 2,
             5, 5, 5, 3, 1, 5, 2, 3, 1, 4, 1, 5, 1, 1, 1, 1, 3, 1, 0, 3, 3, 0, 2, 3, 4, 4, 2, 1, 2, 5, 5, 5, 2, 4, 0, 1,
             1, 0, 1, 1, 5, 1, 4, 2, 5, 4, 0, 2, 0, 5, 3, 0, 2, 2, 1, 2, 2, 5, 1, 3, 2, 2, 5, 0, 5, 0, 1, 5, 4, 3, 5, 2,
             4, 1, 5, 2, 3, 1, 0, 0, 1, 1, 3, 0, 3, 0, 5, 0, 4, 4, 4, 5, 5, 4, 0, 3, 5, 0, 4, 0, 2, 3, 2, 0, 0, 2, 1, 4,
             3, 0, 0, 4, 0, 0, 3, 0, 1, 4, 3, 0, 5, 4, 2, 5, 5, 4, 1, 4, 1, 2, 1, 5, 2, 0, 1, 5, 4, 0, 1, 5, 4, 2, 1, 0,
             4, 5, 3, 4, 2, 2, 0, 1, 0, 0, 2, 3, 0, 2, 2, 5, 1, 1, 2, 5, 2, 3, 5, 2, 1, 4, 3, 3, 3, 3, 1, 0, 1, 4]
        sage = UnsupervisedGraphSAGE()
        sage.classifier = categorization.TitleClassification()

        sage._plot_embedding_scatter(
            data, c, alpha=0.7, legend_alpha=0.5, legend_loc="lower left", title="some title", activate_title=False
        )
        return True  # dummy value

    def test_plot_embedding_scatter_GraphSAGE(self):
        """
        this generates the node-edge-node embedding scatter plot
        :return:
        """
        # data is a trained node edge node embedding
        data1 = {0: -14.010557, 1: -13.684941, 2: -13.737495, 3: -13.737495, 5: -13.737495, 4: -13.737495,
                 6: -13.684941,
                 7: -13.737495, 8: -13.684941, 9: -14.010558, 10: -13.988311, 11: -20.240625, 14: -19.552425,
                 12: -20.003801,
                 16: -18.98213, 26: -18.390192, 40: -19.597439, 15: -19.876295, 17: -19.61075, 13: -20.740652,
                 18: -19.876184,
                 19: -20.42714, 20: -20.740652, 21: -20.778292, 22: -20.740652, 23: -21.128113, 24: -20.740652,
                 25: -19.447628, 27: -18.001856, 37: -18.910849, 38: -19.214195, 39: -19.013372, 28: -18.900305,
                 29: -15.470122, 35: -14.84431, 36: -14.78618, 30: -15.04711, 31: -14.843392, 32: -14.848629,
                 33: -14.94306,
                 34: -14.893793, 42: -20.46191, 41: -20.005554, 43: -20.740652, 44: -20.003801, 45: -20.740652,
                 46: -20.740652, 47: -20.363338, 49: -20.740652, 50: -20.778292, 48: -20.740652, 51: 15.303169,
                 52: 16.330296,
                 59: 16.826487, 96: 14.25637, 78: 15.9765415, 83: 14.889483, 67: 16.764532, 63: 17.083557,
                 53: 16.807829,
                 64: 16.393574, 100: 16.59952, 99: 17.248425, 68: 16.814165, 66: 17.151423, 65: 17.320518, 54: 17.27053,
                 55: 16.362381, 56: 17.26397, 57: 17.262924, 58: 16.443848, 60: 16.259481, 61: 16.720316, 62: 16.251696,
                 97: 14.889483, 98: 14.265128, 69: 15.5438595, 70: 15.094415, 71: 14.487213, 72: 14.968222,
                 73: 14.495265,
                 74: 14.810708, 75: 14.292062, 77: 14.659895, 76: 15.507793, 79: 16.197012, 80: 16.193443,
                 81: 16.145357,
                 82: 16.22312, 84: 14.964097, 85: 15.260416, 86: 14.090759, 87: 14.073356, 88: 15.455146, 89: 14.073356,
                 90: 15.455146, 91: 14.820429, 92: 14.154349, 93: 14.692246, 94: 15.455146, 95: 15.455146,
                 101: 19.476782,
                 102: 18.572048, 103: 19.476782, 104: 19.476782, 105: 19.476782, 106: 19.476782, 107: 19.476782,
                 108: 19.476782, 109: 19.476782, 110: 19.476782, 111: 18.572048, 112: 18.756643, 113: 18.572048,
                 114: 19.476782, 115: 19.476782, 116: 19.476782, 117: 18.578444, 118: 19.261665, 119: 18.572048,
                 120: 19.476782, 121: 19.476782, 122: 19.476782, 123: 19.476782, 124: 19.476782, 125: -4.845193,
                 126: -3.5766244, 129: -3.3233776, 152: -4.5877504, 138: -6.2355237, 127: -4.193382, 128: -4.0120378,
                 154: -4.6825743, 153: -4.323672, 155: -4.699941, 156: -4.4643235, 140: -5.959018, 139: -5.9769564,
                 144: -7.202679, 141: -6.6452746, 142: -6.483201, 143: -6.413589, 146: -7.18799, 147: -7.18799,
                 145: -7.2005396, 148: -6.867885, 149: -7.128864, 150: -7.1575785, 151: -7.138513, 131: -2.8244743,
                 130: -2.2815793, 157: -2.8597944, 132: -2.7942119, 133: -2.3289008, 134: -1.0983781, 136: -1.0086858,
                 137: -1.1446743, 135: 0.99445873, 158: -2.8597944, 160: -2.8237364, 161: -2.8597944, 159: -2.8597944,
                 162: -2.8597944, 163: 0.964908, 164: 0.63959354, 165: 1.0170883, 166: 0.7595032, 167: 0.7552346,
                 168: 0.7593663, 169: 1.535783, 170: 1.4665813, 172: 1.9832193, 171: 2.044586, 180: 0.39603516,
                 173: 1.6028465, 174: 1.5567654, 175: 1.5590158, 176: 1.7435375, 177: 1.5836279, 179: 2.016728,
                 178: 2.0283234, 182: 7.466607, 181: 6.173501, 183: 6.5144615, 188: 6.5144615, 186: 7.2106905,
                 185: 6.8577123, 189: 6.038242, 190: 7.5158334, 191: 7.214475, 187: 7.448807, 184: 7.551359,
                 207: 7.6522665,
                 208: 7.889022, 209: 7.673614, 192: 5.7942705, 195: 6.829835, 194: 6.4562573, 193: 7.246451,
                 196: 6.5144615,
                 198: 6.5144615, 199: 6.5144615, 197: 7.0624957, 200: 6.5144615, 203: 6.5144615, 202: 6.5144615,
                 201: 6.5144615, 204: 6.4562573, 205: 6.5144615, 206: 6.5144615, 210: -18.708069, 211: -18.670187,
                 227: -19.027452, 235: -18.423159, 229: -18.10992, 230: -18.187029, 231: -17.956697, 232: -18.38494,
                 233: -17.560843, 234: -17.569092, 228: -18.831871, 236: -18.391273, 240: -17.549564, 239: -17.778563,
                 237: -17.84451, 238: -17.453371, 243: -18.071812, 241: -17.429983, 242: -17.442476, 212: -18.77941,
                 213: -18.740828, 219: -19.722275, 220: -19.407768, 214: -19.70109, 216: -18.958572, 215: -19.412273,
                 217: -18.855883, 218: -19.532019, 221: -19.465027, 222: -19.905327, 223: -19.430601, 224: -19.873835,
                 225: -19.904099, 226: -19.094194, 244: 0.36639252, 245: -0.39657256, 246: -0.67732644, 247: 0.36441883,
                 248: 0.36441883, 249: -0.068799965, 250: 0.36441883, 251: 0.36441883, 252: -0.28765494,
                 253: -0.064209454,
                 254: -0.5159919, 255: -0.2700025, 256: 0.1971471, 257: 0.028921517, 258: 0.333976, 259: -0.5029456,
                 260: -0.1389101, 261: -0.33492962, 262: -0.54400796, 263: 0.4439911, 264: -0.552248}
        data2 = {0: 10.096028, 1: 10.216452, 2: 10.711928, 3: 10.711928, 5: 10.711928, 6: 10.216452, 4: 10.711928,
                 7: 10.711928, 8: 10.216452, 9: 10.096029, 10: 10.011968, 11: 13.563768, 14: 12.035521, 12: 13.06399,
                 16: 11.99806, 26: 12.1454315, 40: 12.458533, 15: 13.485079, 17: 12.156017, 13: 12.5208845,
                 18: 13.485034,
                 19: 11.802431, 20: 12.5208845, 21: 13.447767, 22: 12.5208845, 23: 13.23875, 24: 12.5208845,
                 25: 12.009024,
                 27: 11.96955, 37: 12.264142, 38: 12.718708, 39: 12.753951, 28: 12.648784, 29: 10.97431, 35: 10.94005,
                 36: 10.960851, 30: 10.659238, 31: 10.580641, 32: 10.94327, 33: 10.591739, 34: 10.559989, 42: 13.548113,
                 41: 13.038464, 43: 12.5208845, 44: 13.06399, 45: 12.5208845, 46: 12.5208845, 47: 11.815783,
                 49: 12.5208845,
                 50: 13.447767, 48: 12.5208845, 51: 10.376444, 52: 14.258642, 59: 13.3335705, 96: 9.549722,
                 78: 12.030595,
                 83: 8.381416, 67: 14.561887, 63: 13.611288, 53: 13.96878, 64: 14.224276, 100: 14.674146, 99: 14.577798,
                 68: 14.831274, 66: 14.846392, 65: 14.462169, 54: 14.002012, 55: 14.310628, 56: 13.983636,
                 57: 13.981009,
                 58: 13.453687, 60: 13.643683, 61: 13.264961, 62: 13.665708, 97: 8.381416, 98: 8.576333, 69: 8.68673,
                 70: 8.078853, 71: 8.317778, 72: 9.688043, 73: 9.676279, 74: 9.055814, 75: 8.440211, 77: 9.712526,
                 76: 8.622643, 79: 12.647651, 80: 12.58784, 81: 12.457966, 82: 12.763093, 84: 9.693383, 85: 8.568997,
                 86: 9.266126, 87: 8.883429, 88: 9.266053, 89: 8.883429, 90: 9.266053, 91: 9.0028715, 92: 9.375784,
                 93: 8.9637375, 94: 9.266053, 95: 9.266053, 101: -6.9260488, 102: -6.520064, 103: -6.9260488,
                 104: -6.9260488,
                 105: -6.9260488, 106: -6.9260488, 107: -6.9260488, 108: -6.9260488, 109: -6.9260488, 110: -6.9260488,
                 111: -6.520064, 112: -7.551159, 113: -6.520064, 114: -6.9260488, 115: -6.9260488, 116: -6.9260488,
                 117: -7.3376827, 118: -5.9950533, 119: -6.520064, 120: -6.9260488, 121: -6.9260488, 122: -6.9260488,
                 123: -6.9260488, 124: -6.9260488, 125: -2.338032, 126: -2.6145756, 129: -2.3383014, 152: -2.5651276,
                 138: -2.1332467, 127: -2.1884766, 128: -2.5269399, 154: -2.2557554, 153: -2.4988918, 155: -2.4677129,
                 156: -2.2001514, 140: -2.350093, 139: -2.3662767, 144: -2.1990209, 141: -2.063125, 142: -2.5116239,
                 143: -2.489441, 146: -2.496244, 147: -2.496244, 145: -2.4829319, 148: -2.5873563, 149: -2.0321147,
                 150: -2.0860434, 151: -2.0500689, 131: -2.284363, 130: -2.554828, 157: -2.8842134, 132: -2.2334208,
                 133: -2.5290082, 134: -2.5780861, 136: -2.581492, 137: -2.5812762, 135: -2.845172, 158: -2.8842134,
                 160: -2.265671, 161: -2.8842134, 159: -2.8842134, 162: -2.8842134, 163: -2.8402839, 164: -2.692484,
                 165: -2.8486762, 166: -2.2438264, 167: -2.2437754, 168: -2.2382133, 169: -2.8447707, 170: -2.1144812,
                 172: -2.6878183, 171: -2.3331468, 180: -2.5777845, 173: -2.082146, 174: -2.8479002, 175: -2.0958502,
                 176: -2.8459408, 177: -2.0898366, 179: -2.6244917, 178: -2.263576, 182: -21.56731, 181: -20.3908,
                 183: -21.34737, 188: -21.34737, 186: -20.594044, 185: -20.234058, 189: -20.516972, 190: -21.446781,
                 191: -20.598343, 187: -20.949974, 184: -21.262522, 207: -20.867477, 208: -20.534216, 209: -20.169704,
                 192: -20.794765, 195: -20.21581, 194: -20.238588, 193: -21.870018, 196: -21.34737, 198: -21.34737,
                 199: -21.34737, 197: -20.216352, 200: -21.34737, 203: -21.34737, 202: -21.34737, 201: -21.34737,
                 204: -20.238588, 205: -21.34737, 206: -21.34737, 210: -16.0573, 211: -16.7697, 227: -16.36358,
                 235: -15.471284, 229: -16.309372, 230: -15.937956, 231: -15.630754, 232: -15.39079, 233: -16.120695,
                 234: -16.120014, 228: -16.450191, 236: -15.406499, 240: -15.230429, 239: -16.2146, 237: -15.132621,
                 238: -15.325632, 243: -15.180217, 241: -15.748171, 242: -15.709564, 212: -17.214909, 213: -17.164452,
                 219: -16.91512, 220: -17.45611, 214: -17.814842, 216: -17.62759, 215: -16.753445, 217: -17.46337,
                 218: -16.958866, 221: -16.763582, 222: -17.37012, 223: -17.936039, 224: -17.929115, 225: -17.357668,
                 226: -17.733904, 244: 13.0267, 245: 12.3295145, 246: 12.752336, 247: 12.418362, 248: 12.418362,
                 249: 12.144451, 250: 12.418362, 251: 12.418362, 252: 12.221635, 253: 12.144148, 254: 12.338394,
                 255: 12.94855, 256: 13.271459, 257: 13.265538, 258: 13.016825, 259: 13.174111, 260: 13.4623165,
                 261: 13.408754, 262: 12.72079, 263: 12.917996, 264: 12.978453}
        data = (
            [data1[k] for k in range(len(data1))],
            [data2[k] for k in range(len(data2))]
        )

        # classification results
        c = [1, 4, 4, 4, 5, 4, 4, 0, 0, 1, 3, 1, 0, 1, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0,
             3,
             0, 0, 4, 0, 0, 0, 0, 0, 1, 0, 1, 2, 4, 2, 1, 1, 5, 0, 1, 1, 1, 5, 5, 5, 5, 4, 4, 5, 3, 1, 3, 4, 3, 2, 4, 1,
             2,
             1, 2, 4, 4, 5, 5, 5, 4, 5, 2, 2, 4, 2, 2, 2, 5, 2, 2, 0, 2, 2, 2, 5, 4, 4, 0, 3, 1, 1, 1, 2, 2, 1, 0, 0, 5,
             1,
             1, 4, 1, 1, 5, 4, 1, 0, 2, 2, 0, 1, 1, 2, 1, 1, 0, 1, 0, 0, 0, 0, 0, 5, 1, 1, 0, 5, 1, 4, 4, 4, 2, 4, 2, 2,
             0,
             1, 0, 1, 5, 2, 5, 2, 0, 0, 2, 2, 2, 2, 2, 2, 3, 0, 0, 0, 0, 0, 3, 5, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 1, 4, 5,
             0,
             0, 5, 0, 5, 1, 0, 3, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 4, 1, 1, 1, 0, 2, 2, 3, 2, 2, 1, 4, 0, 0,
             0,
             0, 3, 2, 5, 3, 0, 4, 1, 2, 5, 5, 1, 5, 2, 4, 1, 1, 1, 5, 5, 5, 5, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 2,
             2,
             2, 1, 2, 2, 5, 4]

        sage = UnsupervisedGraphSAGE()
        sage.classifier = categorization.TitleClassification()

        sage._plot_embedding_scatter(
            data, c, alpha=0.7, legend_alpha=0.5, legend_loc="lower left", title="some title", activate_title=False,
            text_on_nodes=data1.keys()
        )
        return True  # dummy value

    def test_plot_calculate_neighborhoods(self):
        """
        this method calculates clusters in the graph and returns the list of nodes
        :return:
        """
        # data is a trained node edge node embedding
        data1 = {0: -14.010557, 1: -13.684941, 2: -13.737495, 3: -13.737495, 5: -13.737495, 4: -13.737495,
                 6: -13.684941,
                 7: -13.737495, 8: -13.684941, 9: -14.010558, 10: -13.988311, 11: -20.240625, 14: -19.552425,
                 12: -20.003801,
                 16: -18.98213, 26: -18.390192, 40: -19.597439, 15: -19.876295, 17: -19.61075, 13: -20.740652,
                 18: -19.876184,
                 19: -20.42714, 20: -20.740652, 21: -20.778292, 22: -20.740652, 23: -21.128113, 24: -20.740652,
                 25: -19.447628, 27: -18.001856, 37: -18.910849, 38: -19.214195, 39: -19.013372, 28: -18.900305,
                 29: -15.470122, 35: -14.84431, 36: -14.78618, 30: -15.04711, 31: -14.843392, 32: -14.848629,
                 33: -14.94306,
                 34: -14.893793, 42: -20.46191, 41: -20.005554, 43: -20.740652, 44: -20.003801, 45: -20.740652,
                 46: -20.740652, 47: -20.363338, 49: -20.740652, 50: -20.778292, 48: -20.740652, 51: 15.303169,
                 52: 16.330296,
                 59: 16.826487, 96: 14.25637, 78: 15.9765415, 83: 14.889483, 67: 16.764532, 63: 17.083557,
                 53: 16.807829,
                 64: 16.393574, 100: 16.59952, 99: 17.248425, 68: 16.814165, 66: 17.151423, 65: 17.320518, 54: 17.27053,
                 55: 16.362381, 56: 17.26397, 57: 17.262924, 58: 16.443848, 60: 16.259481, 61: 16.720316, 62: 16.251696,
                 97: 14.889483, 98: 14.265128, 69: 15.5438595, 70: 15.094415, 71: 14.487213, 72: 14.968222,
                 73: 14.495265,
                 74: 14.810708, 75: 14.292062, 77: 14.659895, 76: 15.507793, 79: 16.197012, 80: 16.193443,
                 81: 16.145357,
                 82: 16.22312, 84: 14.964097, 85: 15.260416, 86: 14.090759, 87: 14.073356, 88: 15.455146, 89: 14.073356,
                 90: 15.455146, 91: 14.820429, 92: 14.154349, 93: 14.692246, 94: 15.455146, 95: 15.455146,
                 101: 19.476782,
                 102: 18.572048, 103: 19.476782, 104: 19.476782, 105: 19.476782, 106: 19.476782, 107: 19.476782,
                 108: 19.476782, 109: 19.476782, 110: 19.476782, 111: 18.572048, 112: 18.756643, 113: 18.572048,
                 114: 19.476782, 115: 19.476782, 116: 19.476782, 117: 18.578444, 118: 19.261665, 119: 18.572048,
                 120: 19.476782, 121: 19.476782, 122: 19.476782, 123: 19.476782, 124: 19.476782, 125: -4.845193,
                 126: -3.5766244, 129: -3.3233776, 152: -4.5877504, 138: -6.2355237, 127: -4.193382, 128: -4.0120378,
                 154: -4.6825743, 153: -4.323672, 155: -4.699941, 156: -4.4643235, 140: -5.959018, 139: -5.9769564,
                 144: -7.202679, 141: -6.6452746, 142: -6.483201, 143: -6.413589, 146: -7.18799, 147: -7.18799,
                 145: -7.2005396, 148: -6.867885, 149: -7.128864, 150: -7.1575785, 151: -7.138513, 131: -2.8244743,
                 130: -2.2815793, 157: -2.8597944, 132: -2.7942119, 133: -2.3289008, 134: -1.0983781, 136: -1.0086858,
                 137: -1.1446743, 135: 0.99445873, 158: -2.8597944, 160: -2.8237364, 161: -2.8597944, 159: -2.8597944,
                 162: -2.8597944, 163: 0.964908, 164: 0.63959354, 165: 1.0170883, 166: 0.7595032, 167: 0.7552346,
                 168: 0.7593663, 169: 1.535783, 170: 1.4665813, 172: 1.9832193, 171: 2.044586, 180: 0.39603516,
                 173: 1.6028465, 174: 1.5567654, 175: 1.5590158, 176: 1.7435375, 177: 1.5836279, 179: 2.016728,
                 178: 2.0283234, 182: 7.466607, 181: 6.173501, 183: 6.5144615, 188: 6.5144615, 186: 7.2106905,
                 185: 6.8577123, 189: 6.038242, 190: 7.5158334, 191: 7.214475, 187: 7.448807, 184: 7.551359,
                 207: 7.6522665,
                 208: 7.889022, 209: 7.673614, 192: 5.7942705, 195: 6.829835, 194: 6.4562573, 193: 7.246451,
                 196: 6.5144615,
                 198: 6.5144615, 199: 6.5144615, 197: 7.0624957, 200: 6.5144615, 203: 6.5144615, 202: 6.5144615,
                 201: 6.5144615, 204: 6.4562573, 205: 6.5144615, 206: 6.5144615, 210: -18.708069, 211: -18.670187,
                 227: -19.027452, 235: -18.423159, 229: -18.10992, 230: -18.187029, 231: -17.956697, 232: -18.38494,
                 233: -17.560843, 234: -17.569092, 228: -18.831871, 236: -18.391273, 240: -17.549564, 239: -17.778563,
                 237: -17.84451, 238: -17.453371, 243: -18.071812, 241: -17.429983, 242: -17.442476, 212: -18.77941,
                 213: -18.740828, 219: -19.722275, 220: -19.407768, 214: -19.70109, 216: -18.958572, 215: -19.412273,
                 217: -18.855883, 218: -19.532019, 221: -19.465027, 222: -19.905327, 223: -19.430601, 224: -19.873835,
                 225: -19.904099, 226: -19.094194, 244: 0.36639252, 245: -0.39657256, 246: -0.67732644, 247: 0.36441883,
                 248: 0.36441883, 249: -0.068799965, 250: 0.36441883, 251: 0.36441883, 252: -0.28765494,
                 253: -0.064209454,
                 254: -0.5159919, 255: -0.2700025, 256: 0.1971471, 257: 0.028921517, 258: 0.333976, 259: -0.5029456,
                 260: -0.1389101, 261: -0.33492962, 262: -0.54400796, 263: 0.4439911, 264: -0.552248}
        data2 = {0: 10.096028, 1: 10.216452, 2: 10.711928, 3: 10.711928, 5: 10.711928, 6: 10.216452, 4: 10.711928,
                 7: 10.711928, 8: 10.216452, 9: 10.096029, 10: 10.011968, 11: 13.563768, 14: 12.035521, 12: 13.06399,
                 16: 11.99806, 26: 12.1454315, 40: 12.458533, 15: 13.485079, 17: 12.156017, 13: 12.5208845,
                 18: 13.485034,
                 19: 11.802431, 20: 12.5208845, 21: 13.447767, 22: 12.5208845, 23: 13.23875, 24: 12.5208845,
                 25: 12.009024,
                 27: 11.96955, 37: 12.264142, 38: 12.718708, 39: 12.753951, 28: 12.648784, 29: 10.97431, 35: 10.94005,
                 36: 10.960851, 30: 10.659238, 31: 10.580641, 32: 10.94327, 33: 10.591739, 34: 10.559989, 42: 13.548113,
                 41: 13.038464, 43: 12.5208845, 44: 13.06399, 45: 12.5208845, 46: 12.5208845, 47: 11.815783,
                 49: 12.5208845,
                 50: 13.447767, 48: 12.5208845, 51: 10.376444, 52: 14.258642, 59: 13.3335705, 96: 9.549722,
                 78: 12.030595,
                 83: 8.381416, 67: 14.561887, 63: 13.611288, 53: 13.96878, 64: 14.224276, 100: 14.674146, 99: 14.577798,
                 68: 14.831274, 66: 14.846392, 65: 14.462169, 54: 14.002012, 55: 14.310628, 56: 13.983636,
                 57: 13.981009,
                 58: 13.453687, 60: 13.643683, 61: 13.264961, 62: 13.665708, 97: 8.381416, 98: 8.576333, 69: 8.68673,
                 70: 8.078853, 71: 8.317778, 72: 9.688043, 73: 9.676279, 74: 9.055814, 75: 8.440211, 77: 9.712526,
                 76: 8.622643, 79: 12.647651, 80: 12.58784, 81: 12.457966, 82: 12.763093, 84: 9.693383, 85: 8.568997,
                 86: 9.266126, 87: 8.883429, 88: 9.266053, 89: 8.883429, 90: 9.266053, 91: 9.0028715, 92: 9.375784,
                 93: 8.9637375, 94: 9.266053, 95: 9.266053, 101: -6.9260488, 102: -6.520064, 103: -6.9260488,
                 104: -6.9260488,
                 105: -6.9260488, 106: -6.9260488, 107: -6.9260488, 108: -6.9260488, 109: -6.9260488, 110: -6.9260488,
                 111: -6.520064, 112: -7.551159, 113: -6.520064, 114: -6.9260488, 115: -6.9260488, 116: -6.9260488,
                 117: -7.3376827, 118: -5.9950533, 119: -6.520064, 120: -6.9260488, 121: -6.9260488, 122: -6.9260488,
                 123: -6.9260488, 124: -6.9260488, 125: -2.338032, 126: -2.6145756, 129: -2.3383014, 152: -2.5651276,
                 138: -2.1332467, 127: -2.1884766, 128: -2.5269399, 154: -2.2557554, 153: -2.4988918, 155: -2.4677129,
                 156: -2.2001514, 140: -2.350093, 139: -2.3662767, 144: -2.1990209, 141: -2.063125, 142: -2.5116239,
                 143: -2.489441, 146: -2.496244, 147: -2.496244, 145: -2.4829319, 148: -2.5873563, 149: -2.0321147,
                 150: -2.0860434, 151: -2.0500689, 131: -2.284363, 130: -2.554828, 157: -2.8842134, 132: -2.2334208,
                 133: -2.5290082, 134: -2.5780861, 136: -2.581492, 137: -2.5812762, 135: -2.845172, 158: -2.8842134,
                 160: -2.265671, 161: -2.8842134, 159: -2.8842134, 162: -2.8842134, 163: -2.8402839, 164: -2.692484,
                 165: -2.8486762, 166: -2.2438264, 167: -2.2437754, 168: -2.2382133, 169: -2.8447707, 170: -2.1144812,
                 172: -2.6878183, 171: -2.3331468, 180: -2.5777845, 173: -2.082146, 174: -2.8479002, 175: -2.0958502,
                 176: -2.8459408, 177: -2.0898366, 179: -2.6244917, 178: -2.263576, 182: -21.56731, 181: -20.3908,
                 183: -21.34737, 188: -21.34737, 186: -20.594044, 185: -20.234058, 189: -20.516972, 190: -21.446781,
                 191: -20.598343, 187: -20.949974, 184: -21.262522, 207: -20.867477, 208: -20.534216, 209: -20.169704,
                 192: -20.794765, 195: -20.21581, 194: -20.238588, 193: -21.870018, 196: -21.34737, 198: -21.34737,
                 199: -21.34737, 197: -20.216352, 200: -21.34737, 203: -21.34737, 202: -21.34737, 201: -21.34737,
                 204: -20.238588, 205: -21.34737, 206: -21.34737, 210: -16.0573, 211: -16.7697, 227: -16.36358,
                 235: -15.471284, 229: -16.309372, 230: -15.937956, 231: -15.630754, 232: -15.39079, 233: -16.120695,
                 234: -16.120014, 228: -16.450191, 236: -15.406499, 240: -15.230429, 239: -16.2146, 237: -15.132621,
                 238: -15.325632, 243: -15.180217, 241: -15.748171, 242: -15.709564, 212: -17.214909, 213: -17.164452,
                 219: -16.91512, 220: -17.45611, 214: -17.814842, 216: -17.62759, 215: -16.753445, 217: -17.46337,
                 218: -16.958866, 221: -16.763582, 222: -17.37012, 223: -17.936039, 224: -17.929115, 225: -17.357668,
                 226: -17.733904, 244: 13.0267, 245: 12.3295145, 246: 12.752336, 247: 12.418362, 248: 12.418362,
                 249: 12.144451, 250: 12.418362, 251: 12.418362, 252: 12.221635, 253: 12.144148, 254: 12.338394,
                 255: 12.94855, 256: 13.271459, 257: 13.265538, 258: 13.016825, 259: 13.174111, 260: 13.4623165,
                 261: 13.408754, 262: 12.72079, 263: 12.917996, 264: 12.978453}

        # classification results
        c = [1, 4, 4, 4, 5, 4, 4, 0, 0, 1, 3, 1, 0, 1, 0, 0, 0, 0, 0, 0, 2, 2, 2, 0, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0,
             3,
             0, 0, 4, 0, 0, 0, 0, 0, 1, 0, 1, 2, 4, 2, 1, 1, 5, 0, 1, 1, 1, 5, 5, 5, 5, 4, 4, 5, 3, 1, 3, 4, 3, 2, 4, 1,
             2,
             1, 2, 4, 4, 5, 5, 5, 4, 5, 2, 2, 4, 2, 2, 2, 5, 2, 2, 0, 2, 2, 2, 5, 4, 4, 0, 3, 1, 1, 1, 2, 2, 1, 0, 0, 5,
             1,
             1, 4, 1, 1, 5, 4, 1, 0, 2, 2, 0, 1, 1, 2, 1, 1, 0, 1, 0, 0, 0, 0, 0, 5, 1, 1, 0, 5, 1, 4, 4, 4, 2, 4, 2, 2,
             0,
             1, 0, 1, 5, 2, 5, 2, 0, 0, 2, 2, 2, 2, 2, 2, 3, 0, 0, 0, 0, 0, 3, 5, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 1, 4, 5,
             0,
             0, 5, 0, 5, 1, 0, 3, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 4, 1, 1, 1, 0, 2, 2, 3, 2, 2, 1, 4, 0, 0,
             0,
             0, 3, 2, 5, 3, 0, 4, 1, 2, 5, 5, 1, 5, 2, 4, 1, 1, 1, 5, 5, 5, 5, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 1, 2,
             2,
             2, 1, 2, 2, 5, 4]

        dataDict = {idx:{'x1': value,'x2': data2[idx]} for idx, value in data1.items()}

        data = pandas.DataFrame(
            dataDict
        ).transpose()

        data['l2_norm'] = np.sqrt(data['x1'] ** 2 + data['x2'] ** 2)

        # Perform K-means clustering on the L2 norms
        num_clusters = 10  # Adjust the number of clusters as needed
        kmeans = KMeans(n_clusters=num_clusters)
        data['cluster'] = kmeans.fit_predict(data[['l2_norm']])

        # Group node IDs by clusters
        clustered_indexes = data.groupby('cluster').apply(lambda x: x.index.tolist()).to_dict()

        # compute length of clusters
        cluster_length = {cl_id: len(value) for cl_id, value in clustered_indexes.items()}

        score = silhouette_score(data, c, metric='euclidean')

        print(score)

        data.head()

        return True  # dummy value

if __name__ == '__main__':
    unittest.main()