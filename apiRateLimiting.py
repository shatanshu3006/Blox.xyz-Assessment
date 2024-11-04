class RateLimiter:
    constructor(limit, interval, penaltyTime):
        set this.limit to limit  // Number of allowed calls per user
        set this.interval to interval  // Time interval in milliseconds
        set this.penaltyTime to penaltyTime  // Penalty time for exceeding limit
        initialize a dictionary userCalls to store call counts and timestamps for each user

    method callAPI(userID, input):
        currentTime = getCurrentTime()  // Get current timestamp
        if userID not in userCalls:
            initialize userCalls[userID] to an empty list

        // Remove expired calls from the list
        for each call in userCalls[userID]:
            if call.timestamp + interval < currentTime:
                remove call from userCalls[userID]

        // Check current call count
        if size of userCalls[userID] >= limit:
            // Apply penalty if limit is exceeded
            if (currentTime < userCalls[userID][0].timestamp + interval + penaltyTime):
                print "User is penalized. Cannot make calls until penalty time expires."
                return "Rate limit exceeded. Try again later."

        // Proceed with API call
        callResult = callMe(input)  // Simulate API call
        add currentTime to userCalls[userID]  // Record the call
        print "API called successfully for user:", userID
        return callResult

    method callMe(input):
        simulate API call with a delay (e.g., sleep for 1 second)
        print "Calling API with input: input"
        return "Response for input"


// Example usage
create instance of RateLimiter with 15 calls per minute and a penalty of 1 minute

for i from 1 to 20:
    result = callAPI("User123", "Input i")
    if result contains "Rate limit exceeded":
        break  // Stop trying if rate limit is exceeded

// Allow time for processing before ending
wait for sufficient time