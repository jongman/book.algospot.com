## ITES 문제 예제 답안의 오류 (1쇄, 2쇄)

'외계 신호 분석' 문제의 예제 답안(19.7절)에 오류가 있습니다. 오류는 코드 19.3(오프라인 버전)과 코드 19.4(온라인 버전)에 모두 존재합니다. 온라인 채점 사이트에 있는 채점 데이터는 현재 이 오류를 잡지 못합니다. (이 점은 향후 개선될 예정입니다)

두 코드 모두, 합이 K인 부분 수열이 입력 데이터의 처음부터 시작될 경우 이를 찾지 못한다는 오류를 갖고 있습니다.

### 코드 19.3의 문제

**오류**: 코드 19.3은 $psum[head]$와 $psum[tail]$의 차이가 $k$인지를 확인합니다. 이 때 $psum[i]$는 $A[0]+A[1]+\cdots+A[i]$이므로, $psum[tail]-psum[head] = A[head+1]+\cdots+A[tail]$ 입니다. 따라서 우리가 원하는 답이 $A[0]$부터 시작한다면 이를 찾지 못하게 되지요. 

**해결책**: $[head, tail]$ 구간의 합을 코드 17.1에 나오는 $rangeSum()$ 함수를 이용해 구합니다. 이 때 코드 19.3은 다음과 같이 변합니다.

	// 코드 17.1을 참조
	long long rangeSum(const vector<long long>& psum, int a, int b) { 
	  if(a == 0) return psum[b];
	  return psum[b] - psum[a-1];
	} 
	  
	int offline(const vector<int>& signals, int k) {
	  vector<long long> psum(signals.size());
	  // signals 를 부분 합으로 바꾸자
	  psum[0] = signals[0];
	  for(int i = 1; i < signals.size(); i++)
		psum[i] = signals[i] + psum[i-1];
		
	  int ret = 0, tail = 0;
	  for(int head = 0; head < psum.size(); ++head) {
		// [head, tail] 구간합이 k 미만인 동안 tail을 뒤로 옮긴다
		while(tail+1 < psum.size() && rangeSum(psum, head, tail) < k)
		  ++tail;
		// 답이 되는 구간을 찾았나?
		if(rangeSum(psum, head, tail) == k)
		  ++ret;
	  }
	  return ret;
	} 

### 코드 19.4의 문제

**문제**: 코드 19.4에서도 위와 같은 문제가 있습니다. 이 코드는 구간의 합을 구하기 위해 $psum - psums.front()$를 사용합니다. 만약 $A[0]=k$라고 하면, $A[0]$만 구간 내에 들어가 있을 때 $psum = psums.front() = A[0]$이기 때문에 답을 찾을 수 없습니다.

**해결책**: 가장 쉬운 해결책은 숫자 0을 맨 처음 큐에 넣어 두는 것입니다. 0개의 숫자에 대한 구간합은 0이라는 것을 나타내는 것으로, 이 경우 위의 문제가 해결됨을 알 수 있습니다. 따라서 이 경우 코드 19.4는 다음과 같이 바뀝니다.

	int countPartialSums(int k, int n) {
	  RNG rng;
	  int ret = 0;
	  long long psum = 0;
	  queue<long long> psums;
      psums.push(0); // 추가된 부분
	  for(int i = 0; i < n; i++) {
		// 구간에 숫자를 추가한다
		psum += rng.next();
		psums.push(psum);

		// 현재 구간의 합이 k미만인 동안 구간에서 숫자를 뺀다
		while(psum - psums.front() < k)
		  psums.pop();

		// 답을 하나 찾은 경우
		if(psums.front() + k == psum)
		  ++ret;
	  }
	  return ret;
	}

### 19.7절 다시 쓰기

이 문제를 해결하기 위해 사실 부분 합은 반드시 필요한 도구가 아니며, 이  경우 부분 합을 사용함으로 인해 오히려 설명이 불필요하게 복잡해지는 효과를 얻게 되었습니다. 따라서 3쇄 이하에서는 19.7절 전체가 다음과 같이 바뀌게 됩니다.

[새로 작성된 19.7절 읽기](19-7.html)

