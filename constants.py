import os

TOP_LEVEL = "Dataset"
Emb_Dir = f"{TOP_LEVEL}/Embossed"
Pro_Dir = f"{TOP_LEVEL}/Province"
Reg_Dir = f"{TOP_LEVEL}/Regional"

emb = os.listdir(Emb_Dir)
pro = os.listdir(Pro_Dir)
reg = os.listdir(Reg_Dir)