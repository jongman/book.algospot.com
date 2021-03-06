## 서문: 프로그래밍은 어렵다

프로그래밍은 참으로 어렵습니다. 양질의 컴퓨터 교육을 수년 간 받고 학교를
졸업한 뒤에도 프로그래밍이라면 자신 없어 하는 학생들이 수두룩하고, 유수의
대학에서 컴퓨터를 전공하고도 코드 한 줄 못 짜는 사람들에 대한 소프트웨어
기업들의 불평이 얼마나 많은지 물릴 정도입니다. 이것이 프로그래밍이 아니라
대학 교육의 문제라고 가정한다고 해도, “잘하는 사람과 못 하는 사람의 생산성 차이가 스무 배”라는 말[^1]이 진지하게 나올 수 있는 분야가 많지는 않을 것입
니다.

이런 현상의 가장 근본적인 이유는 대부분 컴퓨터 과학 교육 과정이 프로그래밍의 기술과 지식을 가르칠 뿐, 그것을 스스로 응용할 수 있는 능력을 주지 못하기 때문입니다. 이런 교육 과정만을 이수한 사람은 마치 문법책과 사전만으로 외국어를 배운 사람과 다를 바가 없습니다. 글을 기계적으로 해석할 수는 있어도,
시를 감상하거나 좋은 글을 직접 쓰지는 못하지요. 알고리즘을 배운 뒤 연습 문제를 풀 수는 있어도, 문제를 해결하기 위한 새로운 무언가를 고안할 수는 없는 개발자가 되는 것입니다.

이런 비극이 일어나는 가장 큰 원인은 현대의 컴퓨터 과학 교육이 실제 학문이 발전하는 방향의 반대 순서로 이루어져 있기 때문입니다. 처음부터 완전한
체계를 갖추고 발전하는 학문은 없으므로, 발전 과정에서 학자들은 모두 어둠
속에서 직관에 의존해 헤매게 됩니다(흔히 ‘삽질한다’고 하지요). 시행착오에
의한 직관과 경험이 하나씩 쌓여 학문의 기초를 이루고 나면, 학자들은 자연스럽게 학문의 뼈대가 되는 공리들과 법칙들을 만들고 학문의 체계를 정리해 나가게 됩니다. 반면 대부분의 교과서에서는 발전 과정의 최종 결과물인 복잡한
개념과 도구를 먼저 제시하고, 그 개념의 이론에 대해 설명한 뒤, 곧장 연습 문제를 풀도록 합니다. 이 과정에서 이론을 만들기 위해 필요했던 직관이나 경험적 요소는 완전히 배제되지요. 예를 들면 다음과 같은 식입니다.

> 그래프의 최단거리 알고리즘은 크게 한 정점에서부터 모든 정점까지의 최단거리를
구하는 단일 시작점 알고리즘과 모든 정점 쌍 간의 최단거리를 구하는 모든 쌍 최단 경로 알고리즘으로 나뉜다. 단일 시작점 알고리즘의 대표적인 것으로 다익스트라 알고리즘이 있다. 의사 코드는 이렇다. 이 그래프에 대해서 알고리즘을 실행해 보자. 이 간선, 이 간선, 이 간선 순으로 완화가 이루어지므로 최단 거리는 이렇게 된다. 자, 이제 시간 복잡도를 분석해 보자.

이 수업에서 대체 어떤 학생이 다익스트라 알고리즘이 생겨난 배경과 이 알고리즘을 설계하는 데 필요했던 결정적 통찰을 얻을 수 있을까요? 이런 교육형태는 학문 발전의 결과물에 대한 체계적인 지식을 학생에게 주입하는 데는 좋을지 몰라도, 문제의 답을 스스로 고안할 수 있는 학생을 기르기에는 턱없이 부족합니다. 지식을 진정 자신의 것으로 만들어 활용할 수 있기 위해서는 학문이 발전하는 과정에서 일어난 발견과 깨달음을 학생 자신이 되짚어갈 수 있어야 합니다.

이런 경험과 깨달음을 얻기 위한 좋은 통로가 바로 프로그래밍 대회입니다.
프로그래밍 대회들은 컴퓨터 과학 전반에 걸쳐 널리 쓰이는 각종 알고리즘과
자료 구조들을 이용해 주어진 문제들을 해결하고 구현하는 능력을 겨루는 대회입니다. 잘 알려진 알고리즘들을 베껴 쓰기만 하면 해결할 수 있는 문제만 있는 것이 아니라 알고리즘에 사용된 원칙들을 이해하고 변형해야 풀 수 있는 문제들이 많이 출제되기 때문에 이런 주제들을 깊이 이해하는 데 큰 도움이 됩니다.
공정하고 즉각적인 피드백이 주어지기 때문에 혼자서도 훨씬 재미있게 공부할 수 있습니다.

이 책은 프로그래밍 대회 문제를 풀며 각종 알고리즘 설계 기법과 자료 구조를 직관적으로 이해하고, 나아가 알고리즘 문제 해결 능력을 키울 수 있도록 구성했습니다. 이를 위해 각 기법이 생겨난 배경과 이유, 그리고 기법을 만들기
위해 필요한 과정을 자세히 다루었습니다. 연습 문제는 실제 프로그래밍 대회
문제로 구성되어 있으며, 해당 장에서 배운 기법을 직접적으로 적용하거나 변형해 보면서 이들에 대한 직관을 얻을 수 있도록 설계했습니다. 여러 문제를(어렵게) 풀어 가는 과정에서 다양한 개념과 구조들을 경험적으로 이해할 수 있도록 하는 것이 이 책의 목표입니다.

프로그래밍은 어려운 만큼 재미있는 작업이기도 합니다. 문제를 푸는 것도
그렇습니다. 문제가 풀리지 않을 때의 괴로움은 문제가 풀렸을 때의 기쁨과 그
과정에서 얻은 통찰을 자신의 것으로 만들었을 때 느끼는 뿌듯함에 비하면 아무것도 아닙니다. 그렇게 즐겁게 이 책을 읽어나갈 수 있기를 기대합니다.


[^1]: 이 말은 Thinking in Java 등의 교과서로 유명한 브루스 에켈(Bruce Eckel)이 한 대학교의 졸업 축사에서 한 말입니다.

