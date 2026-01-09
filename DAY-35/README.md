AI 실습 특강
컴퓨터 비전 실습용 가상환경 설정
1. 현재 가상환경을 활성화 해 놨다면 비활성화
conda deacticate
2. conda 명령어로 필요 의존 패키지 설치
conda env create -f computer_vision.yaml -n computer_vision
3. 가상환경 활성화 확인
conda activate computer_vision

컴퓨터 비전
기계가 이미지/영상을 이해하고 분석하는 AI 기술 분야
- 자율주행, 의료 영상 정밀 진단, 지능형 보안 시스템 등

머신러닝 파이프라인
- 전처리 ( Preprocessing ) :  원시 데이터를 모델이 학습할 수 있게 변환
- 추론 (Inference) :  학습된 모델이 실제 입력에 대한 결과 생성
- 후처리 ( Postprooessing ) : 모델 출력 결과를 사용자나 서비스가 쓸 수 있게 다듬음

- 컴퓨터 비전 -> 전처리

기하학적 변환 ( Geometric Transformations )
- 이미지의 좌표계를 조작하여 형태, 크기, 위치를 변경하는 기술
- 딥러닝 모델은 고정되 크기의 입력 텐서 ( Input Tensor )를 요구하느 경우가 많음
- 다양한 원본 이미지를 모델의 규격에 맞추는 작업이 선행

비율 유지 패딩 ( Letterbox padding )
- 왜곡 문제를 해결하기 위해 '비율 유지 패딩'기법이 널리 사용됨
- 객체 탐지 ( Object Detection ) 모델인 TOLO ( You Only Look Once ) 시리즈 등에서 표준적으로 채택하는 전처리 방식

이미지 피라미드 ( Image Pyramid )
- 하나의 원본 이미지를 다양한 해상도로 변환하여 계층적 (Hierarchical) 으로 구성하는 기법
- 단일 해상도 입력만으로는 아주 작거나 아주 큰 객체를 동시에 효과적으로 탐지하기 어려운 문제를 해결

정규화 ( Normalization )
- 디지털 이미지는 통상 0에서 255사이의 정수 (Integer) 값을 가짐
- 신경망은 입력 데이터의 스케일에 매우 민감하며, 큰 값의 입력은 학습 과정에서 내부 공변량 변화 ( Internal Covariate Shift ) 를 유발하거나 최적화 과정을 불안정하게 만들 수 있음

- 컴퓨터 비전 -> 추론

추론 (Inference)
- 학습된 모델을 실전 ( Production )에 투입하여 새로운 데이터 ( Unseen Data 예측)

이미지 분류 (Image Classification)
- 입력된 이미지의 전체적인 시각 정보를 분석하여 미리 정의된 정답지 (Class)중 하나를 할당하는 작업
- 화면 꽉 차게 들어온 단일 피사체를 분석할 때 가장 유효

객체 탐지 ( Object Detection )
- 이미지 내에 존재하는 여러 객체를 종류 (Classification)를 식별함과 동시에,
각 객체의 위치(Localization) 를 바운딩 박스 형태로 찾아내는 복합적인 과제

이미지 분할 ( Image Segmentation )
- 이미지 내에 존재하는 여러 객체의 종류 ( Classification )를 식별함과 동시에 , 각 객체의 위치(Localization) 를 바운딩 박스 형태로 찾아내는 복합적인 과제

- 컴퓨터 비전 -> 추론
후처리 ( Post-processing )
- 모델이 출력한 원시적인 수치 데이터(Raw Output)를 인간이 이해할 수 있거나 시스템이 활용할 수 있는 형태로 정제하는 과정
- 서비스의 품질과 사용성을 결정짓는 마지막 관문

OCR 및 자연어 처리의 후처리 전략
- OCR 모델의 출력인 토큰 ID의 나열을 의미 있는 텍스트로 변환
- 디코딩 및 정규화
토큰 디코딩 : 모델의 출력 텐서를 단어 사전 (Vocabulary)을 이용해 문자열로 변혼 (,같은 특수 토큰 제거)
텍스트 정규화 : 결과의 품질을 높이기 위해 유니코드 정규화(NFC), 공백 정리, 불필요한 특수문자 제거 등을 수행
LLM을 활용한 지능형 후처리
- OCR이 인식한 텍스트에 오타나 문맥상 어색한 부분이 있을 경우, LLM을 통해 인식률을 비약적으로 높임


