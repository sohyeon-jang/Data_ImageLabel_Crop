import json
import os 
import glob
from PIL import Image


# data_sample 주소 입력
path = '/content/drive/MyDrive/Colab Notebooks/labelme/data_sample' 

file_list1 = os.listdir(path)


i = 0

# file_list1 -> ['falldown_79_6255', 'falldown_324_8154', 'falldown_407_6980']
# file_list2[0] -> ['rgb']
# len(file_list1) -> 3


while i <= ((len(file_list1)) -1 ):
  second_path = f"{path}/{file_list1[i]}"
  file_list2 = os.listdir(second_path)

  rgb_path = f"{path}/{file_list1[i]}/{file_list2[0]}"
  # print(rgb_path)

  
  json_path = glob.glob(f"{rgb_path}/*.json", recursive=True)
  # print(json_path)


  # result 폴더 만들기
  result_folder = f'{second_path}/result'

  if not os.path.isdir(result_folder):
    os.mkdir(result_folder)


  
  # JSON 파일, PNG파일
  num = 1 # 파일이름위한변수(1.json~)

  while num <= (len(json_path)):

      with open(f"{rgb_path}/{num}.json" , "r", encoding="utf8") as f:
          contents = f.read()
          json_data = json.loads(contents) # JSON 파일


      image = Image.open(f"{rgb_path}/{num}.png") # PNG파일
      image.show()


      x = 0 # label 이름 출력 위한 변수

      while x < (len(json_data["shapes"])):

          labelname = json_data["shapes"][x]["label"] # Label 이름
          
          print(num,".json파일의", x+1, "번째 레이블 출력 : ", labelname)

          point1 = json_data["shapes"][x]["points"][0][0]
          point2 = json_data["shapes"][x]["points"][0][1]
          point3 = json_data["shapes"][x]["points"][1][0]
          point4 = json_data["shapes"][x]["points"][1][1]

          if (point1 > point3) & (point2 > point4):
            point1 = json_data["shapes"][x]["points"][1][0]
            point3 = json_data["shapes"][x]["points"][0][0]
            point2 = json_data["shapes"][x]["points"][1][1]
            point4 = json_data["shapes"][x]["points"][0][1]

          croppedImage=image.crop((
              point1, point2, point3, point4
          ))


          # Label 이름으로 디렉토리 생성
          label_folder = f'{result_folder}/{labelname}'

          if not os.path.isdir(label_folder):
            os.mkdir(label_folder)

          if labelname == {labelname}:
            label_folder = f'{label_folder}'

          # Label이름의 폴더로 사진 저장
          # 저장된 사진이름 : (사진이름)_(Label이름)_(레이블번호) ex)10_swoon3.PNG
          croppedImage.save(f'{label_folder}/{num}_{labelname}{x+1}.PNG')

          x += 1
              
      num += 1

  i += 1