from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # Step 1: Count frequency of each word
        freq = Counter(words)

        # Step 2: Use a min-heap of size k
        heap = []
        for word, count in freq.items():
            # Push (-count, word) so that highest freq comes first
            heapq.heappush(heap, (-count, word))

        # Step 3: Pop k times from heap
        result = [heapq.heappop(heap)[1] for _ in range(k)]
        return result
