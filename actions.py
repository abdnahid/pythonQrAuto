import math

def calc_fee_ws(capacity:float)->int:
  if capacity <= 50:
    return 200;
  elif capacity <= 250:
    return 500;
  elif capacity <= 1000:
    return 600;
  elif capacity <= 5000:
    return 1000;
  elif capacity <= 10000:
    return 2000;
  elif capacity <= 20000:
    return 3000;
  elif capacity <= 50000:
    return 8000;
  else:
    base_fee = 8000
    ten_fraction = math.ceil(capacity/8000)
    return base_fee+ten_fraction*800
  
def calc_fee_lm(capacity:float)->int:
  match capacity:
    case 0.001:
      return 10
    case 0.05:
      return 10
    case 0.1:
      return  20
    case 0.5:
      return 20
    case 1:
      return 40
    case 2:
      return 50
    case 5:
      return 100
    case 10:
      return 200
    case 20:
      return 300
    case 50:
      return 400
    case 100:
      return 500
    case _:
      return 0
    
def calc_fee_ms(capacity:float)->int:
  if capacity <= 1:
    return 200;
  elif capacity <= 10:
    return 300;
  elif capacity <= 20:
    return 500;
  elif capacity <= 50:
    return 800;
  elif capacity <= 100:
    return 1200;
  else:
    return 1600
    
def calc_fee(scale_type:str,capacity:int)->int:
  match scale_type:
    case "dw":
      return calc_fee_ws(capacity=capacity)
    case "lm":
      return calc_fee_lm(capacity=capacity)
    case "ms":
      return calc_fee_ms(capacity=capacity)
    
def get_scale_type(scale_type:str)->str:
  match scale_type:
    case "dw":
      return "Digital Weight Scale"
    case "lm":
      return "Liter Measures"
    case "ms":
      return "Meter Scale"
    case "wb":
      return "Electronic Weighbridge Scale"
    
def get_scale_type_bn(scale_type:str)->str:
  match scale_type:
    case "dw":
      return "ডিজিটাল ওয়েট স্কেল"
    case "lm":
      return "লিটার মেজার্স"
    case "ms":
      return "মিটার স্কেল"
    case "wb":
      return "ইলেকট্রনিক ওয়েব্রীজ স্কেল"