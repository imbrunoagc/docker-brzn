import os
import pandas as pd


output_dir = "/app/data" # CONSIDERANDO FILESYSTEM DO CONTAINER 
output_file = os.path.join(output_dir, "iss_position.csv")

print(pd.read_csv(output_file))


### comando:
### criação da imagem: docker build -t iss-data-reader . 
### execução da imagem em container: docker run --name iss-data-reader -v path_local:/app/data name_image