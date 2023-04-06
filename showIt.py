import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 定义图片列表
images = []



for i in range(0, 200,10):
   images.append('./rst/'+str(i)+'example.png')


# 定义更新图片的函数
def update_image(num):
    # 清空当前的图形
    plt.clf()
    # 读取当前帧的图片
    img = plt.imread(images[num])
    plt.axis('off')
    plt.gcf().patch.set_visible(False)
    # 显示当前帧的图片
    plt.imshow(img)

# 创建动画对象
ani = animation.FuncAnimation(plt.gcf(), update_image, frames=len(images), interval=1000)
ani.save('./rst/animation.gif', writer='imagemagick')

# 显示动画
plt.show()