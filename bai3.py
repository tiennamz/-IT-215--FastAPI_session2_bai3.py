from fastapi import FastAPI

app = FastAPI()


students = [
    {"id": 1, "name": "An", "status": "active"},
    {"id": 2, "name": "Binh", "status": "inactive"},
    {"id": 3, "name": "Cuong", "status": "active"},
    {"id": 4, "name": "Dung", "status": "pending"}
]

@app.get('/students/active')
def get_students_active():
    list_active = []
    for stu in students:
        if stu['status'] == 'active':
            list_active.append(stu)
    
    if not list_active:
        return {
            "message": "Không có sinh viên đang học",
            "data": []
                }
        
    return {"message": "Danh sách sinh viên đang học", 'data': list_active}


'''
- Input của bài toán là gì? Không
- Output mong muốn là gì? data Theo đúng định dạng JSON 
- Điều kiện nào dùng để xác định sinh viên đang học? status == active

'''
