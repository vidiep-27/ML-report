import pandas as pd

def clean_wine_data():
    print("Đang tiến hành tiền xử lý dữ liệu rượu...")
    
    # 1. Đọc dữ liệu từ thư mục data (lưu ý dấu phân cách ';' đặc trưng của file dữ liệu rượu)
    red_wine = pd.read_csv('data/winequality-red.csv', sep=';')
    white_wine = pd.read_csv('data/winequality-white.csv', sep=';')
    
    # 2. Tạo thêm cột để phân biệt loại rượu (1 là đỏ, 0 là trắng)
    red_wine['is_red'] = 1
    white_wine['is_red'] = 0
    
    # 3. Gộp 2 tập dữ liệu lại thành một DataFrame chung
    combined_df = pd.concat([red_wine, white_wine], ignore_index=True)
    
    # 4. Xóa bỏ các dòng dữ liệu bị trùng lặp (nếu có)
    combined_df.drop_duplicates(inplace=True)
    
    # 5. Xuất dữ liệu sạch ra thư mục output để sau này dùng huấn luyện mô hình
    combined_df.to_csv('output/wine_quality_clean.csv', index=False)
    
    print("-> Tiền xử lý hoàn tất! Đã lưu file sạch vào: output/wine_quality_clean.csv")
    return combined_df
