def findPoisonedDuration(timeSeries: list[int], duration: int) -> int:
  if(duration == 0 or len(timeSeries)==0):
      return 0
  result = 0

  for i in range(len(timeSeries)-1):
      if(timeSeries[i+1] - timeSeries[i]) >= duration:
          result += duration
      else:
          result += timeSeries[i+1] - timeSeries[i]
  result += duration
  return result

timeSeries = [1,4]
duration = 2
print(findPoisonedDuration(timeSeries,duration))
