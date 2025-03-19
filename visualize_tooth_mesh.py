import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os
from scipy.spatial import Delaunay
import argparse

def visualize_tooth_mesh(file_path):
    """
    NPY 파일에서 치아 버텍스 정보를 불러와 3D 시각화합니다.
    
    Args:
        file_path (str): 치아 버텍스 정보가 담긴 NPY 파일 경로
    """
    # 파일 존재 확인
    if not os.path.exists(file_path):
        print(f"파일이 존재하지 않습니다: {file_path}")
        return
    
    # NPY 파일 로드
    points = np.load(file_path)
    
    # 데이터 형태 확인
    print("데이터 형태:", points.shape)
    print("데이터 타입:", points.dtype)
    print(f"포인트 개수: {len(points)}")
    print(f"X 범위: {points[:, 0].min():.4f} ~ {points[:, 0].max():.4f}")
    print(f"Y 범위: {points[:, 1].min():.4f} ~ {points[:, 1].max():.4f}")
    print(f"Z 범위: {points[:, 2].min():.4f} ~ {points[:, 2].max():.4f}")
    
    # 3D 점 시각화 (포인트 클라우드 + 메시)
    fig = plt.figure(figsize=(15, 10))
    
    # 포인트 클라우드 시각화
    ax1 = fig.add_subplot(121, projection='3d')
    ax1.scatter(points[:, 0], points[:, 1], points[:, 2], c='b', marker='.', s=1)
    ax1.set_title('포인트 클라우드')
    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')
    
    # 축 비율 동일하게 설정
    max_range = np.array([
        points[:, 0].max() - points[:, 0].min(),
        points[:, 1].max() - points[:, 1].min(),
        points[:, 2].max() - points[:, 2].min()
    ]).max() / 2.0
    
    mid_x = (points[:, 0].max() + points[:, 0].min()) / 2
    mid_y = (points[:, 1].max() + points[:, 1].min()) / 2
    mid_z = (points[:, 2].max() + points[:, 2].min()) / 2
    
    ax1.set_xlim(mid_x - max_range, mid_x + max_range)
    ax1.set_ylim(mid_y - max_range, mid_y + max_range)
    ax1.set_zlim(mid_z - max_range, mid_z + max_range)
    
    # 메시 시각화 (2D 투영 후 Delaunay 삼각화)
    ax2 = fig.add_subplot(122, projection='3d')
    
    # 간단한 메시 생성을 위해 XY 평면에 투영하여 Delaunay 삼각화
    try:
        # 2D 투영 (XY 평면)
        points_2d = points[:, :2]
        tri = Delaunay(points_2d)
        
        # 메시 그리기
        ax2.plot_trisurf(points[:, 0], points[:, 1], points[:, 2], 
                        triangles=tri.simplices, cmap='viridis', alpha=0.7)
        ax2.set_title('간단한 메시 시각화 (XY 투영)')
    except Exception as e:
        print(f"메시 생성 중 오류 발생: {e}")
        ax2.scatter(points[:, 0], points[:, 1], points[:, 2], c='r', marker='.', s=1)
        ax2.set_title('메시 생성 실패 - 포인트 클라우드')
    
    ax2.set_xlabel('X')
    ax2.set_ylabel('Y')
    ax2.set_zlabel('Z')
    
    # 두 번째 그래프도 같은 비율로 설정
    ax2.set_xlim(mid_x - max_range, mid_x + max_range)
    ax2.set_ylim(mid_y - max_range, mid_y + max_range)
    ax2.set_zlim(mid_z - max_range, mid_z + max_range)
    
    plt.suptitle(f'치아 메시 시각화: {os.path.basename(file_path)}', fontsize=16)
    plt.tight_layout()
    plt.show()

def main(file_path):
    
    # 시각화 실행
    visualize_tooth_mesh(file_path)

if __name__ == "__main__":
    file_path = "ssm/eigValVec/meanAlignedPG_11.npy"
    main(file_path)