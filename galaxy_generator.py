import matplotlib.cm

from galaxies.globular_cluster import GlobularCluster
import matplotlib.pyplot as plt


def main():
    radius = 10
    num_stars = 100

    globular_cluster = GlobularCluster()
    globular_cluster.generate_stars(radius, num_stars)
    for star_system in globular_cluster.star_system:
        print(star_system)

    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    for star_system in globular_cluster.star_system:
        norm = matplotlib.colors.Normalize(vmin=0.0, vmax=1.0, clip=True)
        color = matplotlib.cm.ScalarMappable(norm=norm, cmap=matplotlib.colormaps["jet"]).to_rgba(star_system.security)
        ax.scatter(star_system.galactic_x, star_system.galactic_y, star_system.galactic_z, marker='.', color=color)

    plt.show()

if __name__ == "__main__":
    main()