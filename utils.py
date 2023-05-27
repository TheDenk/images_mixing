from matplotlib import pyplot as plt


def show_image(image, figsize=(5, 5), cmap=None, title='', xlabel=None, ylabel=None, axis=False):
    plt.figure(figsize=figsize)
    plt.imshow(image, cmap=cmap)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.axis(axis)
    plt.show();


def show_images(images, n_rows=1, titles=None, figsize=(5, 5), cmap=None, xlabel=None, ylabel=None, axis=False):
    n_cols = len(images) // n_rows
    if n_rows == n_cols == 1:
        if isinstance(titles, str) or titles is None:
            title = titles
        if isinstance(titles, list):
            title = titles[0]
        show_image(images[0], title=title, figsize=figsize, cmap=cmap, xlabel=xlabel, ylabel=ylabel, axis=axis)
    else:
        titles = titles if isinstance(titles, list) else ['' for _ in range(len(images))]
        fig, axes = plt.subplots(n_rows, n_cols, figsize=figsize)
        fig.tight_layout(pad=0.0)
        axes = axes.flatten()
        for index, ax in enumerate(axes):
            ax.imshow(images[index], cmap=cmap)
            ax.set_title(titles[index])
            ax.set_xlabel(xlabel)
            ax.set_ylabel(ylabel)
            ax.axis(axis)
        plt.show();