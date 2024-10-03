import matplotlib.pyplot as plt

times = [1, 2, 3, 4, 5]
request_rates = [100, 300, 500, 200, 100]

plt.plot(times, request_rates)
plt.xlabel('Time')
plt.ylabel('Request Rate')
plt.title('Request Rate Over Time')
plt.show()
