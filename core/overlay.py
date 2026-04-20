def get_overlay_filter(cta1=None, cta2=None, pos1="top-right", pos2="bottom-left"):
    def pos_to_xy(pos):
        mapping = {
            "top-left": "10:10",
            "top-right": "main_w-overlay_w-10:10",
            "bottom-left": "10:main_h-overlay_h-10",
            "bottom-right": "main_w-overlay_w-10:main_h-overlay_h-10",
            "center": "(main_w-overlay_w)/2:(main_h-overlay_h)/2"
        }
        return mapping.get(pos, "10:10")

    filters = []

    if cta1:
        filters.append(f"movie={cta1}[c1];[in][c1]overlay={pos_to_xy(pos1)}[v1]")
    if cta2:
        base = "[v1]" if cta1 else "[in]"
        filters.append(f"movie={cta2}[c2];{base}[c2]overlay={pos_to_xy(pos2)}")

    return ";".join(filters)
