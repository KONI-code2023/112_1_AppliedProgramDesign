month_sum = (6, 7, 8, 9)                                                        #夏季 (6 ~ 9)
kwh = (120, 330, 500, 700, 1000)                                                #用電度數分段
fee_sum = (1.63, 2.38, 3.52, 4.80, 5.66, 6.41)                                  #夏季電費
fee_not_sum = (1.63, 2.10, 2.89, 3.94, 4.60, 5.03)                              #非夏季電費
soc = 0
fee = 0

def func(x, y, z):
  fee = 0
  if x in month_sum:
    fee = fee_calc(y, fee_sum)
  else:
    fee = fee_calc(y, fee_not_sum)
  soc = func2(x, y, z) - y
  soc = final_ver(x, soc + y, z)
  print(f'電費{round(fee, 2)}元 尚可用{round(soc-y, 2)}度')
  
def func2(x, y, z):
  fee = 0
  if x in month_sum:
    while True:
      fee = fee_calc(y, fee_sum)
      if fee >= z:
        return y 
      y += 0.01
  else:
    while True:
      fee = fee_calc(y, fee_not_sum)
      if fee >= z:
        return y
      y += 0.01

def final_ver(x, soc, z):
  fee = 0
  if x in month_sum:
    fee = fee_calc(soc, fee_sum)
  else:
    fee = fee_calc(soc, fee_not_sum)
  if fee > z:
    return soc-0.01
  else: 
    return soc

def fee_calc(y, fee):
  if 0 <= y < kwh[0]+1:
    return y * fee[0]
  
  if kwh[0]+1 <= y < kwh[1]+1:
    return kwh[0] * fee[0] + \
          (y - kwh[0]) * fee[1]
  
  if kwh[1]+1 <= y < kwh[2]+1:
    return kwh[0] * fee[0] + \
          (kwh[1] - kwh[0]) * fee[1] + \
          (y - kwh[1]) * fee[2]
  
  if kwh[2]+1 <= y < kwh[3]+1:
    return kwh[0] * fee[0] + \
          (kwh[1] - kwh[0]) * fee[1] + \
          (kwh[2] - kwh[1]) * fee[2] + \
          (y - kwh[2]) * fee[3]

  if kwh[3]+1 <= y < kwh[4]+1:
    return kwh[0] * fee[0] + \
          (kwh[1] - kwh[0]) * fee[1] + \
          (kwh[2] - kwh[1]) * fee[2] + \
          (kwh[3] - kwh[2]) * fee[3] + \
          (y - kwh[3]) * fee[4]
  
  if kwh[4]+1 <= y:
    return kwh[0] * fee[0] + \
          (kwh[1] - kwh[0]) * fee[1] + \
          (kwh[2] - kwh[1]) * fee[2] + \
          (kwh[3] - kwh[2]) * fee[3] + \
          (kwh[4] - kwh[3]) * fee[4] + \
          ((y) - kwh[4]) * fee[5]
      
def main():
  x = int(input("月份："))                                                      #用電月份
  y = float(input("目前使用度數："))                                            #用電度數
  z = int(input("本月預算："))                                                  #電費預算
  func(x, y, z)

if __name__ == "__main__":
  try:
    main()
  except:
    pass