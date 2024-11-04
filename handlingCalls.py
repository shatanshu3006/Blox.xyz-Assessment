class RateLimiter:
    constructor(limit, interval):
        set this.limit to limit  // Number of allowed calls
        set this.interval to interval  // Time interval in milliseconds
        set this.callsMade to 0  // Count of calls made in the current interval
        set this.queue to an empty queue  // Queue to hold pending API calls
        start a processing thread that runs processQueue()

    method callAPI(input):
        lock queueMutex
        add input to queue
        notify processing thread to process the queue
        unlock queueMutex

    method callMe(input):
        simulate API call with a delay (e.g., sleep for 1 second)
        print "Calling API with input: input"
        print "Response for input"

    method processQueue():
        while not stopProcessing:
            wait for a notification to process the queue
            if stopProcessing then break
            
            if isThrottled is false:
                set isThrottled to true
                // Process calls within the limit
                while queue is not empty and callsMade < limit:
                    get nextInput from the front of the queue
                    unlock queueMutex
                    call callMe(nextInput)  // Execute API call
                    lock queueMutex
                    increment callsMade by 1

                // Handle excess calls
                if queue is not empty:
                    // Space out remaining calls over multiple intervals
                    while queue is not empty:
                        wait for interval milliseconds  // Wait for the next interval
                        reset callsMade to 0  // Reset call count
                        // Process remaining calls in the next interval
                        for i from 0 to limit:
                            if queue is not empty:
                                get nextInput from the front of the queue
                                unlock queueMutex
                                call callMe(nextInput)  // Execute API call
                                lock queueMutex
                                increment callsMade by 1
                        
                set isThrottled to false

// Example usage
create instance of RateLimiter with 15 calls per minute
for i from 1 to 20:
    call callAPI with "Input i"

// Allow time for processing before ending
wait for sufficient time