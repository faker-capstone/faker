[TOC]
##Generator 사용법

####1. Landmark 추출

```
cd generator/landmark/
python test.py "input-img-name"
```
결과: input.txt에 landmark위치 저장

input.txt 파일과 img 파일 이동시키기
```
mv input.txt ../Face-Pose-Net/
mv "input-img-name" ../Face-Pose-Net/input_samples/
```

####2. Change Face Pose

```
python main_fpn.py input.txt

```
결과: ./output_render/1 폴더에 결과물 저장

```
mv ./output_render/1 ./face_renderer/input/
```

####3. augmentation 갯수 증가

* 제일 첫번째 이미지 선택

```
python demo.py ./input/1/1_rendered_aug_-00_00_10.jpg
```
결과: ./output/1 폴더에 결과물 저장
