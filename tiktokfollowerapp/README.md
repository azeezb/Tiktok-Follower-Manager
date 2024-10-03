# Summary of Architecture:
## Front-End (React/Vite):

- Fetches sorted data from the back-end.
- Displays the data efficiently using pagination or lazy loading.
- Handles user interactions like search, filter, and loading states.
- Back-End (Node.js/Express):

# Fetches follower counts from the TikTok API in batches.
- Handles API rate limits and caching to reduce redundant requests.
- Sorts the usernames by follower count and serves them to the front-end.
- Implements a caching layer (Redis) to prevent repeated API calls for the same usernames.