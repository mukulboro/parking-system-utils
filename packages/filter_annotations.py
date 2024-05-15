def filter_annotations(anno:list)->list:
    filtered_annos = []
    for a in anno:
        labels = []
        image_name = a["image"].split("/")[-1].split("-")[-1]
        w, h = a["label"][0]["original_width"], a["label"][0]["original_height"]
        for l in a["label"]:
            true_x = float((l["x"]/100)*w)
            true_y = float((l["y"]/100)*h)
            true_bb_h = float((l["height"]/100)*h)
            true_bb_w = float((l["width"]/100)*w)
            
            labels.append({
                "label": l["rectanglelabels"][0],
                # "x_max": true_x,
                # "y_max": true_y,
                # "x_min": true_x+true_bb_w,
                # "y_min": true_y+true_bb_h,
                # "bb_h": true_bb_h,
                # "bb_w": true_bb_w,
                "n_x_max": (true_x)/w,
                "n_y_max": (true_y)/h,
                "n_x_min": (true_x+true_bb_w)/w,
                "n_y_min": (true_y+true_bb_h)/h,
                "n_bb_h": true_bb_h/h,
                "n_bb_w": true_bb_w/w,
            })
        filtered_annos.append({
            "img_name": image_name,
            # "width": w,
            # "height": h,
            "annotations": labels
        })
    return filtered_annos
