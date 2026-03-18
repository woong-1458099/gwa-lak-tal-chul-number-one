a, c, b, d, a, b, c, a, b, d, c, d

c, c, c, d, d, c, c, d, b, b, c, c



document.querySelector(selector) : CSS 선택자와 일치하는 첫 번 째 요소 하나를 반환

document.querySelectorAll(selector) : CSS 선택자와 일치하는 모든 요소를 NodeList 형태로 반환



const를 기본으로 사용하여 의도치 않은 재할당을 막는다

이게 이제 const는 재할당이 안되고 let은 재할당이 가능하고 둘다 블록 스코프고 var은 재선언/재할당 둘다 가능하고 함수 스코프 이다.

setAttribute() 사용하여 지정된 요소의 '속성' 값을 설정하거나 갱신

getAttribute() 사용하여 해당 요소에 지정된 값을 반환(조회)

textContent 는 HTML 태그를 제외한 순수한 텍스트 데이터만 가져오거나 설정



d, d, b, c, a, c, b, a, b, d

c, c, b, b, a, c, d, c, c, b



원시 자료형 : Number, String, Boolean(True 와 False를 나타내는 논리 자료형 ), null, undefined, 데이터가 불변

참조 자료형 : Objects(Object, Array, Function), 데이터가 가변

type of null 의 결과는 'object'

for... in 은 객체의 열거 가능한 속성(키)에 대해 반복하는 데 사용 , 배열에는 부적합

for... of 는 배열과 같은 반복 가능한 객체의 각 요소(값)를 순회하는데 사용 ( while : 조건문이 참이면 문장을 계속해서 수행 )

함수 선언식은 호이스팅되어 선언 전에 호출 가능하지만, 함수 표현식은 그렇지 않다

함수 선언식 : function funcName() {} , 함수 표현식 const funcName - functino () {}

화살표 함수 이거 할 떄 본문이 한줄의 표현식이면 중괄호 { } 임마랑 return 둘다 생략 ㄱㄴ

=== -> 값과 타입이 모두 같은지 비교 == -> '암묵적 타입 변환'을 통해 타입을 일치시킨 후 같은 값인지 비교 임마들이 비교연산자

논리 연산자 : \&\& (and) , ! (not) , ||(or)



a, a, d, c, a, d, a, c a, a, b, a

c, a, c, b, d, b, b, c, a, a, b, c



this 는 함수를 호출하는 방법에 따라 결정된다 , 메서드 호출할땐 해당 메서드를 호출한 객체를 가리킨다.

**JSON.stringify() -> JavaScript 값이나 객체를 JSON 문자열로 변환 , JSON.parse() 는 JSON 문자열을 JavaScript 객체로 반환**

push() 배열 끝에 요소 추가, pop() 배열 끝 요소 제거 shift 배열 앞 요소 제거, 제거한 요소 반환 unshift() 배열 앞 요소 추가

**추가      제거**

**unshift shift 앞**

**push    pop 끝**

콜백 함수 : 다른 함수의 인자로 전달되는 함수

forEach() 임마 이거는 항상 undefined 를 반환 즉 아무것도 반환하지 않는 거다

map() 배열의 모든 요소에 함수를 적용한 결과로 새로운 배열을 만드는 메서드

Object(객체) : 키 와 값으로 구성된 속성들의 집합을 저장하는 자료형

Optional CHaining (?.) : 중첩된 객체의 속성을 에러 없이 안전하게 접근할 때 사용



d, b, b, c, c, a, b, c, a, c

c, d, b, b, a, b, c, b, a, b



이벤트(event) : 웹 페이지에서 일어나는 신호 또는 사건

이벤트 핸들러 (event handler ): 특정 이벤트 발생 시 실행되는 콜백 함수

**addEvenetListener : DOM 요소에 특정 이벤트가 발생했을 때 실행할 이벤트 핸들러를 등록하는 메서드**

**이벤트 버블링 : 한 요소에 이벤트가 발생하면, 해당 요소의 핸들러가 동작한 후 이어서 부모 요소의 핸들러가 동작하는데 가장 최상단의 조상 요소를 만날 때까지 계속 함 임마랑 반대대는게 캡처링 : 최상위 조상에서 타겟 요소까지 하위로 전파**

event. target : 실제 이벤트가 시작된 요소

event.currentTarget : 핸들러가 연결된 요소 , this와 동일한 대상

preventDefault : 요소의 기본 동작을 막는 메서드

버블링을 잘 사용하려면 , 상위 요소에 핸들러 하나만 등록해서 여러 하위 요소의 이벤트를 공통 상위 요소에서 한 번에 처리하여 효율성을 높일 수 있다.



챕터 확인해보기 정답

1	다크 모드 버튼 눌렀을 때 화면이 어두워지는 원리 :	   body.classList.toggle('dark-mode')

2	장바구니 총액 + 무료 배송 구현:	                                   for…of로 합산 후 조건문 적용

3	여러 사람의 데이터는 어떻게 관리해야 하나?:                 객체 배열로 구조화, map 활용

4	target vs currentTarget 차이	 	                                   target=실제 클릭 요소, currentTarget=리스너 요소



### view.py 에서

@api\_view(\['GET', 'PUT', 'DELETE'])

def article\_detail(request, article\_pk):

    article = get\_object\_or\_404(Article, pk=article\_pk)

문제 2 GET 

@api\_view(\['GET', 'POST'])

def article\_list(request):

  if request.method == 'GET':

     article = Article.objects.all()

      serializer = ArticleListSerializer(article, many=True)

      return Response(serializer.data)

  elif request.method == 'POST':

------------------------------------------------------------------------------------------------------------------ 밑에 정답

      serializer = ArticleListSerializer(data=request.data)

     if serializer.is\_valid():

         serializer.save()

         return Response(serializer.data, status=status.HTTP\_201\_CREATED)

      return Response(serializer.errors, status=status.HTTP\_400\_BAD\_REQUEST)



문제 3 POST

    if request.method == 'GET':

        serializer = ArticleSerializer(article)

        return Response(serializer.data)

    elif request.method == 'PUT':

------------------------------------------------------------------------------------------------------------------밑에 정답

        **serializer = ArticleListSerializer(article, data=request.data)**

         **if serializer.is\_valid():
             serializer.save()
             return Response(serializer.data)
         return Response(serializer.errors, status=status.HTTP\_400\_BAD\_REQUEST)**





문제 4 DELETE article.delete() 부터 끝까지

    elif request.method == 'DELETE':

------------------------------------------------------------------------------------------------------------------밑에 정답

        **article.delete()**

         **data = {
             'msg' : f'{article\_pk}번 파일 삭제',
         }
         return Response(data, status=status.HTTP\_400\_BAD\_REQUEST)\*\***





### serializers.py 에서

문제 1번 fields = ('id', 'title',) 로 바꿈

class ArticleListSerializer(serializers.ModelSerializer):

    class Meta:

        model = Article

        fields **= ('id', 'title',)**



**문제 5 서술형**

**Serializer 에서 many=True를 설정해, 여러 객체를 리스트 형태로 직렬화 하기 위함**





