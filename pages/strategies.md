## 2.3 문제 해결 전략

자신이 알고 있는 기술을 직접적으로 적용할 수 있는 단순한 문제의 경우에는 상관 없지만 어려운 문제일수록 다양한 방법을 시도해 보면서 답안을 찾아야 합니다. 여기에서는 우리가 사용할 수 있는 가장 일반적인 전략들을 몇 가지 소개하고 이들의 사용 예를 들어 보도록 하겠습니다. 이 기술들은 이 책의 연습 문제 풀이에 적극적으로 사용되고 있으므로, 답안을 읽을 때 어떤 방식으로 접근했는지를 눈여겨 보면 좋습니다.

#### 직관과 체계적인 접근

문제 해결 전략에서 가장 먼저 강조해야 할 것은 문제와 답의 구조에 대한 직관의 중요성입니다. 직관은 해당 문제를 해결하는 알고리즘이 대략적으로 어떤 형태를 가질지를 짐작할 수 있게 해 줍니다. 이와 같이 답안의 전체적인 얼개를 머릿 속에 그릴 수 있으면 문제를 반쯤 해결한 것이나 마찬가지입니다.

물론 어떤 문제건 보자마자 어떻게 풀어야 할지 감을 잡을 수 있다면 애초에 이 책을 읽고 있을 이유가 없습니다. 직관 또한 시간이 지나면서 발달하는 것이고, 직관을 발달시키기 위해서는 결국 얼핏 보기엔 막막한 문제들을 해결하며 차곡차곡 경험을 쌓아 나가야 합니다.

그럼 막막한 문제는 어떻게 해결할까요? 그냥 아이디어가 떠오르길 기대하면서 멍하니 앉아 있을 수도 있지만, 좀더 체계적인 방법을 선택할 수도 있습니다. 체계적인 방법이란 백지에서부터 시작해 문제를 해결하기 위한 기반을 차근차근 쌓아올리면서 점진적으로 전진하는 것을 의미합니다.

이 절에서 소개하는 질문들은 막막한 문제에 접근할 수 있는 여러 방법을 제공해 줍니다. 이들은 문제의 해법으로 직접 연결될 수도 있고 문제를 푸는 데 필수적인 직관을 제공할 수도 있습니다. 물론 이런 질문들로 모든 문제를 해결할 수 있는 것은 아닙니다만, 많은 경우 이 질문들은 문제 해결의 좋은 시작점 역할을 해 줍니다.

#### 체계적인 접근을 위한 질문들

다음은 문제를 해결할 때 유용한 질문들의 목록으로, 많은 문제에 적용될 수 있는 강력한 질문들부터 그 사용처가 제한되는 질문들의 순서대로 배열되어 있습니다.

#### 비슷한 문제를 풀어본 적이 있던가?

형태가 비슷하거나 관련된 문제를 풀어 본 적이 있다면 이전에 적용했던 방법과 비슷한 접근 방법을 사용할 거라고 예측할 수 있습니다. 프로그래밍 대회를 준비할 때 많은 문제를 풀어 보는 것이 중요한 이유가 바로 이것이지요.

물론 단순히 문제만 많이 푼다고 해서 그것이 다 경험이 되는 것은 아닙니다.  풀어 본 문제와 완전히 같은 문제를 대회에서 만날 확률은 별로 없기 때문입니 다. 따라서 기존에 접했던 문제가 온전히 경험이 되려면 그 원리를 완전히 이해하고 변형할 수 있어야 합니다.

예를 들어 철도망 위에서 두 도시를 잇는 가장 짧은 경로를 찾는 문제를 풀었다고 합시다. 최단 경로 문제는 굉장히 잘 알려진 문제이고, 이 문제를 해결하는 수많은 표준 알고리즘이 있지요. 따라서 해당 코드를 외우고 나면 이제 최단 거리 문제들을 다 풀 수 있을 거라고 생각하기 쉽습니다. 하지만 다음과 같은 변형 문제들은 어떨까요?

* ᆞ한 도시를 두 번 방문하지 않으면서 가장 긴 경로를 찾는 문제
* ᆞ기차를 네 번 이하로 갈아타면서 가장 짧은 경로를 찾는 문제
* ᆞ역간 운행 거리 중 가장 긴 구간이 가장 짧은 경로를 찾는 문제
* ᆞ역간 운행 거리 중 가장 짧은 구간이 가장 긴 경로를 찾는 문제
* ᆞ가장 긴 구간과 가장 짧은 구간의 길이 차이가 가장 적은 경로를 찾는 문제

이 문제들 중에는 최단 경로 문제를 응용해 풀 수 있는 것도 있고, 그럴 수 없는 것도 있습니다. 이들을 구분하려면 최단 경로 알고리즘을 단순히 알고 있는 것에 멈추지 않고 그 동작 과정과 원리를 완전히 이해하고 있어야 합니다.

꼭 형태가 비슷하지 않더라도 문제의 목표가 같은 경우 또한 이런 사례에 속합니다. 예를 들어 어떤 사건의 발생 확률이나 경우의 수를 계산하는 문제들은 십중팔구 동적 계획법으로 해결(8.11절)할 수 있지요. 문제의 목적을 보고 적절한 접근 방법을 선택하기 위해서는 어떤 문제가 최적화 문제인지, 경우의 수를 구하는 문제인지, 검색 문제인지 등을 분류하는 방법을 익히고, 각 알고리즘들이 어느 경우에 사용될 수 있는지 체계적으로 공부해야 합니다.

이 질문은 각 장의 연습 문제 풀이에서도 답을 찾아내는 데 중요한 역할을 합니다. 다음과 같은 문제들의 풀이가 예가 될 수 있을 겁니다.

* ᆞ합친 LIS (문제 ID: JLIS, 8장 연습 문제)
* ᆞ신호 라우팅 (문제 ID: ROUTING, 30장 연습 문제)
* ᆞ음주 운전 단속 (문제 ID: DRUNKEN, 30장 연습 문제)
* ᆞ선거 공약 (문제 ID: PROMISES, 30장 연습 문제)

#### 단순한 방법에서 시작할 수 있을까?

비슷한 문제를 본 적이 없거나, 비슷한 문제의 해법이 곧장 적용되지 않는다면 어디서부터 시작해야 할까요? 이 책의 많은 연습 문제 풀이는 “무식하게 풀 수 있을까?”라는 질문으로 시작합니다. 다시 말해 일단 시간과 공간 제약을 생각하지 않고 문제를 해결할 수 있는 가장 단순한 알고리즘을 만들어 보는 것입니다. 이 전략의 일차적 목표는 간단하게 풀 수 있는 문제를 너무 복잡하게 생각해서 어렵게 푸는 실수를 예방하는 것입니다. 컴퓨터는 사람보다 훨씬 빠르므로, 언뜻 우리가 느끼기에는 엄청나게 오래 걸릴 것 같은 일도 시간 안에 수행할 수 있는 경우가 많습니다. 복잡한 알고리즘을 고생고생해서 작성한 뒤에야 간단하고 느린 알고리즘으로도 충분하다는 것을 깨닫는 순간의 슬픔은 겪어보지 않으면 모릅니다.

물론 단순한 방법으로 모든 문제가 풀릴 리는 없습니다. 이 방법이 유용한 진짜 이유는 효율적인 알고리즘이라도 단순한 알고리즘을 기반으로 구성된 경우가 많기 때문입니다. 이런 경우 좀더 효율적인 자료 구조를 사용하거나, 계산 과정에서 같은 정보를 두 번 중복으로 계산하지 않는 등의 최적화를 적용해서 충분히 빨라질 때까지 알고리즘을 개선하는 식으로 문제를 풀 수 있습니다. 이 문제 해결 방법은 굉장히 강력하면서도 사고 과정의 큰 도약이 필요하지 않으므로, 어려운 문제를 접했을 때 한번쯤 시도해 볼 만합니다.

점진적인 개선을 통해 문제를 풀 수 없더라도 단순한 방법을 생각해 보는 것에는 나름의 의미가 있습니다. 단순한 방법은 알고리즘 효율성의 기준선을 정해 주는 효과가 있기 때문입니다. 우선 어느 정도 시간에 동작하는 알고리즘을 알고 있어야 다른 알고리즘이 그에 비해 얼마나 개선되었는지 잴 수 있습니다.

예제 문제를 하나 풀면서 점진적인 개선을 어떻게 적용할 수 있나 살펴봅시다. $N (N \le 30)$개의 사탕을 세 명의 어린이에게 가능한 공평하게 나눠 주려고 합니다. 공평함의 기준은 받는 사탕의 총 무게가 가장 무거운 어린이와 가장 가벼운 어린이 간의 차이로 합시다. 사탕의 무게는 모두 20 이하의 정수입니다. 가능한 최소 차이는 얼마일까요?

이 문제를 푸는 가장 단순한 방법은 사탕을 나눠 주는 모든 방법을 하나씩 만들어 보는 것입니다. 각 사탕마다 셋 중 어느 어린이에게 줄지를 결정한다고 하면 $3^N$, 최대 205조 개의 경우의 수가 있습니다. 이는 죽기 전에 다 세어볼 수 있을까 엄두가 나지 않는 큰 수이지만, 사실 이때 우리는 엄청나게 많은 수를 중복으로 세고 있습니다. 모든 사탕의 무게가 같은 단순한 입력이 있다고 가정해 보면 이를 쉽게 실감할 수 있습니다. 무게가 같은 두 개의 사탕을 두 어린이가 서로 바꾼다고 해도 더 공평해지는 것은 아니지요. 좀더 생각해 보면 중요한 것은 사탕이 어떻게 분배되었느냐가 아니라 각 어린이가 받은 사탕 무게의 총 합임을 알 수 있습니다. 205조 개의 경우의 수 중 각 어린이의 사탕 총량이 같은 경우를 하나로 합치면 경우의 수는 $(N \times 20) \cdot 3 = 600^{3}$으로 최댓값은 대략 2억이 됩니다.

이 상태 공간을 너비 우선 탐색(29장)으로 탐색하면 답을 찾을 수 있겠지만, 답을 찾기에는 아직 경우의 수가 너무 큽니다. 2억 개의 경우의 수를 메모리에 저장할 수 없기 때문입니다. 이 방법을 더 최적화하는 방법은 이 문제의 답이 최대 얼마일지 생각해 보는 것입니다. 사탕 총량의 최대치와 최소치가 20 이상 차이난다고 가정해 봅시다. 사탕의 최대 무게는 20이므로, 이때 사탕을 가장 많이 받은 어린이가 가장 적게 받은 어린이에게 사탕을 하나 준다고 해도 사탕의 총량이 역전되지 않습니다. 그러면 최대치와 최소치의 차이는 항상 감소하며, 따라서 차이가 20 이상인 경우는 최적의 답이 될 수 없다는 것을 알 수 있지요.  따라서 넉넉잡아도 사탕을 가장 많이 받은 어린이가 220 넘게 사탕을 받는 경우는 무시해도 됩니다. 이렇게 하면 경우의 수는 $220^3$ , 대략 1000만으로 줄어듭니다.

이 정도면 충분히 문제를 풀 수 있을 것 같지만, 문제를 푸는 더 빠른 방법이 있습니다. 세 어린이 중 누가 가장 사탕을 적게 받고, 누가 가장 많이 받는지는 중요하지 않기 때문입니다. 세 어린이의 사탕의 총량이 (180, 190, 200)이건 (200, 190, 180)이건 우리의 답은 변하지 않지요. 따라서 세 어린이의 사탕의 총량이 항상 오름차순으로 정렬되어 있는 경우만을 탐색하도록 합시다. 서로 다른 세 수를 여섯 가지의 방법으로 나열할 수 있으므로, 이렇게 하면 경우의 수는 다시 대략 $\frac{1}{6}$ 로 줄어듭니다. 결과적으로 대략 200만개 이하의 경우의 수만을 탐색해 문제를 해결할 수 있지요. 이 과정에서 천재만이 떠올릴 수 있는 번뜩이는 영감은 필요없었지만, 처음에 생각했던 방법에 비해 검사해야 할 상태의 수
가 1억분의 1로 줄어들었음을 알 수 있습니다.

이런 기법을 사용하는 풀이의 예로 쿼드 트리 뒤집기(문제 ID: QUADTREE, 7장 연습 문제)를 들 수 있습니다. 이 책에서 가장 중요한 알고리즘 설계 패러다임 중 하나인 동적 계획법(8장) 또한 이 기법과 같은 맥락에서 설명합니다. 따라서 모든 동적 계획법 연습 문제들 또한 이 기법의 적용 예라고 할 수 있지요.

#### 내가 문제를 푸는 과정을 수식화할 수 있을까?

물론 점진적인 접근 방식이 만능은 아닙니다. 공부를 하다 보면 처음에 생각한 것과 완전히 다른, 새로운 방향에서 접근해야 풀리는 문제들도 만나게 됩니다.  이렇게 번뜩이는 영감이 필요한 문제를 만났을 때 시도할 수 있는 한 가지 방법은 손으로 여러 간단한 입력, 예를 들어 문제에 주어진 예제 입력을 직접 해결해 보는 것입니다. 자신이 문제를 해결한 과정을 공식화해서 답을 만드는 알고리즘을 만들 수 있는 경우가 흔히 있고, 그렇지 못하더라도 이 과정에서 알고리즘이 어떤 점을 고려해야 하는지를 알게 되기 때문입니다.

손으로 문제를 풀어 보는 습관은 어떻게 문제를 풀어야 할지 감이 올 때도 유용합니다. 프로그램을 작성하기 전에 알고리즘에 간과한 점이 없는지 미리 확인할 수 있기 때문입니다. 물론 대회 중에는 조급해서 그럴 여유를 찾기가 쉽지 않습니다. 그러나 프로그램을 전부 작성하고, 예제 입력을 수행해 보고, 오랜 디버깅을 거쳐서야 알고리즘에 문제가 있다는 것을 깨닫는 비극 또한 자주 마주치게 되므로, 급할수록 돌아갑시다.

다음 문제들에 대해 이 방법을 연습해 볼 수 있습니다.

* ᆞQuantization (문제 ID: QUANTIZE, 8장 연습 문제)
* ᆞ두니발 박사의 탈옥 (문제 ID: NUMB3RS, 8장 연습 문제)
* ᆞ실험 데이터 복구하기 (문제 ID: RESTORE, 9장 연습 문제)
* ᆞ출전 순서 정하기 (문제 ID: MATCHORDER, 10장 예제 문제)
* ᆞ마법의 약 (문제 ID: POTION, 14장 연습 문제)
* ᆞ함정 설치 (문제 ID: TRAPCARD, 32장 연습 문제)

<div class="well">
이상은 2.3절의 첫 일부분입니다. ^^ 나머지는 책을 구입해서 봐주세요~
</div>

#### 문제를 단순화할 수 없을까?

#### 그림으로 그려볼 수 있을까?

#### 문제를 분해할 수 있을까?

#### 뒤에서부터 생각해서 문제를 풀 수 있을까?

#### 순서를 강제할 수 있을까?

#### 특정 형태의 답만을 고려할 수 있을까?