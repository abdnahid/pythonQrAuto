def calc_fee(capacity:float)->int:
  if capacity <= 5:
    return 100;
  elif capacity <= 50:
    return 200;
  elif capacity <= 500:
    return 300;
  elif capacity <= 2000:
    return 500;
  elif capacity <= 5000:
    return 1000;
  elif capacity <= 20000:
    return 1500;
  elif capacity <= 50000:
    return 2000;
  else:
    return 1000