from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

def board_image_path(instance, filename):
    return f'boards/{instance.pk}/images/{filename}'
    
# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    image =ProcessedImageField(
        upload_to=board_image_path,            #저장위치
        processors=[ResizeToFill(200, 300)],  # 처리할 작업목록
        format='JPEG',                        # 저장 포멧
        options={'quality': 90},              # 옵션
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.id}: {self.title}"
        
class Comment(models.Model):
# 1. on_delete 
#  참조하는 부모객체가 사라졌을 때, 부모에 딸려있는 자식 객체들을 어떻게 처리할지 정의한다.
#  - 속성값
#   1. CASCADE : 부모객체가 삭제됏을때 이를 참조하는 객체도 삭제한다.
#   2. PROJECT : 참조가 되어있는 경우 삭제 오류 발생 (댓 달리면 삭제안됨)
#   3. SET_NULL : 부모 객체가 삭제 됏을 때 참조하는 모든 값을 NULL로 치환 (NOT NULL 조건시 불가능)
#   4. SET_DEFAULT : 모든 값이 DEFAULT로 치환. (디폴트 세팅이 필요)
#   5. SET() : 특정 함수 호출.
#   6. DO_NOTHING : 아무것도 하지 않음.(부모 게시글만 삭제되고 자식들만 남아있음) 
#       - 다만 SQL에서는 on_delete 직접 설정해줘야함.
# 2. 데이터베이스 무결성
# 1) 개체 무결성: PK / NOT NULL / UNIQUE
# -식별자는 NULL일수없고 중복일 수 없다.
# 2) 참조 무결성: FK / 모든 외래 키의 값은 2가지 상태 가운데 하나에만 속함을 규정
# 3) 범위/ 도메인무결성: 컬럼은 지정된 형식을 반드시 만족해야된다.(CHAR, TEXT)

    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content