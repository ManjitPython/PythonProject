x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label='Sine', color='blue', linestyle='--', linewidth=2)
plt.plot(x, y2, label='Cosine', color='red', marker='o', markersize=4, linestyle='-', linewidth=2)

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Customized Plot Example')

plt.legend()
plt.show()
