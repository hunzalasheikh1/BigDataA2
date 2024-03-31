# BigDataA2


1. Inverted Index Creation
Mapper: mapper_inverted_index.py
Purpose: Associates each word in the corpus with a list of documents in which it appears.
Input: Text data representing documents.
Output: Key-value pairs where the key is a word and the value is the document ID.
Reducer: reducer_inverted_index.py
Purpose: Aggregates the intermediate key-value pairs produced by the mapper to generate the inverted index.
Input: Key-value pairs where the key is a word and the value is a list of document IDs.
Output: Key-value pairs where the key is a word and the value is the list of document IDs where the word appears.
2. Query Processing
Mapper: query_mapper.py
Purpose: Processes user queries and prepares them for retrieval.
Input: User queries.
Output: Key-value pairs where the key is a unique identifier and the value is the processed query.
Reducer: query_reducer.py
Purpose: Performs the actual query processing by retrieving relevant documents based on the provided queries and the inverted index.
Input: Key-value pairs where the key is a unique identifier and the value is the processed query.
Output: Relevant documents for each query.
3. Ranking
Mapper: mapper_ranking.py
Purpose: Calculates relevance scores for documents based on various ranking algorithms such as TF-IDF, BM25, or PageRank.
Input: Relevant documents retrieved from query processing.
Output: Key-value pairs where the key is a document ID and the value is its relevance score.
Reducer: reducer_ranking.py
Purpose: Ranks the documents based on their relevance scores.
Input: Key-value pairs where the key is a document ID and the value is its relevance score.
Output: Ranked list of documents based on relevance scores.
4. Index Pruning
Mapper: mapper_pruning.py
Purpose: Identifies less relevant or infrequently accessed terms in the inverted index for removal.
Input: Inverted index data.
Output: Key-value pairs where the key is a term and the value is its relevance or access frequency.
Reducer: reducer_pruning.py
Purpose: Prunes the inverted index by removing less relevant or infrequently accessed terms.
Input: Key-value pairs where the key is a term and the value is its relevance or access frequency.
Output: Pruned inverted index data.
