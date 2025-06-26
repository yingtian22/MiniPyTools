from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl
import matplotlib.cm as cm

def plot_3d_surface(image_path, save_path='3d_surface.png'):
    # 设置专业学术风格
    plt.rcParams.update({
        "font.family": "serif",
        "font.serif": ["Times New Roman"],
        "font.size": 12,
        "axes.labelsize": 14,
        "axes.titlesize": 16,
        "figure.dpi": 300,
        "figure.facecolor": "white",
        "savefig.facecolor": "white",
        "axes.facecolor": "white",
        "savefig.bbox": "tight",
        "axes.edgecolor": "#333333",
        "axes.linewidth": 1.5,
        "grid.color": "#dddddd"
    })
    
    # 打开图像文件
    with Image.open(image_path) as img:
        # 将图像转换为灰度图像
        if img.mode != 'L':
            img = img.convert('L')
        
        # 将图像数据转换为NumPy数组
        img_array = np.array(img)
        
        # 获取图像的宽度和高度
        width, height = img.size
        
        # 创建网格
        x = np.arange(width)
        y = np.arange(height)
        X, Y = np.meshgrid(x, y)
        
        # 创建图形和3D轴
        fig = plt.figure(figsize=(10, 8))
        ax = fig.add_subplot(111, projection='3d')
        
        # 设置视角
        ax.view_init(elev=30, azim=-60)
        
        # 创建自定义colormap - 从深蓝到浅蓝再到白色
        colors = mpl.colors.LinearSegmentedColormap.from_list("custom_blue", 
                                                             ["#003366", "#1e88e5", "#64b5f6", "#bbdefb", "#ffffff"])
        
        # 绘制三维表面图 - 使用平滑的渲染
        surf = ax.plot_surface(X, Y, img_array, cmap=colors, 
                              rstride=2, cstride=2,  # 降低采样密度提高性能
                              edgecolor='none', 
                              antialiased=True,
                              shade=True, 
                              alpha=0.9)
        
        # 添加颜色条
        cbar = fig.colorbar(surf, ax=ax, shrink=0.6, aspect=20, pad=0.1)
        cbar.set_label('Pixel Intensity', fontsize=12, labelpad=10)
        cbar.ax.tick_params(labelsize=10)
        
        # 设置轴标签
        ax.set_xlabel('X Coordinate', fontsize=14, labelpad=15)
        ax.set_ylabel('Y Coordinate', fontsize=14, labelpad=15)
        ax.set_zlabel('Intensity Value', fontsize=14, labelpad=15)
        
        # 设置轴刻度样式
        ax.tick_params(axis='both', which='major', labelsize=10, pad=8)
        ax.tick_params(axis='z', which='major', pad=15)
        
        # 设置网格样式
        ax.xaxis._axinfo["grid"].update({"linewidth": 0.5, "alpha": 0.2})
        ax.yaxis._axinfo["grid"].update({"linewidth": 0.5, "alpha": 0.2})
        ax.zaxis._axinfo["grid"].update({"linewidth": 0.5, "alpha": 0.2})
        
        # 添加标题（可选）
        # ax.set_title('3D Surface Representation of Image Intensities', 
        #              fontsize=16, pad=20, fontweight='bold')
        
        # 设置轴范围
        ax.set_xlim(0, width)
        ax.set_ylim(0, height)
        ax.set_zlim(img_array.min(), img_array.max())
        
        # 设置背景为白色
        ax.xaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
        ax.yaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
        ax.zaxis.set_pane_color((1.0, 1.0, 1.0, 1.0))
        
        # 保存高质量图像
        plt.tight_layout()
        plt.savefig(save_path, dpi=300)
        plt.close()
        print(f"专业级3D表面图已保存至：{save_path}")

# 使用函数
plot_3d_surface('my_img.png', 'surface_plot.png')