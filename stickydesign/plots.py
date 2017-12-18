import numpy as np
from matplotlib import pylab

from .stickydesign import energy_array_uniform


def hist_multi(all_ends,
               all_energetics,
               energetics_names=None,
               title="", **kwargs):
    fig = pylab.figure(figsize=(10, 15))
    a, b, c = fig.subplots(3, 1)
    a.hist(
        [
            np.concatenate(tuple(en.matching_uniform(y) for y in all_ends))
            for en in all_energetics
        ],
        bins=50,
        label=energetics_names,
        **kwargs)
    if energetics_names:
        a.legend()
    a.set_xlabel("$ΔG_{se}$ (kcal/mol)")
    a.set_ylabel("# of interactions")
    a.set_title("Matching ends")

    b.hist(
        [
            np.concatenate(
                tuple(
                    np.ravel(energy_array_uniform(y, en)) for y in all_ends))
            for en in all_energetics
        ],
        bins=100,
        label=energetics_names, **kwargs)
    b.set_xlabel("$ΔG_{se}$ (kcal/mol)")
    b.set_ylabel("# of interactions")
    b.set_title("All ends")
    bins = np.linspace(2.5, 9.0, 100)

    c.hist(
        [
            np.concatenate(
                tuple(
                    np.ravel(energy_array_uniform(y, en)) for y in all_ends))
            for en in all_energetics
        ],
        bins=bins,
        label=energetics_names, **kwargs)
    c.set_xlim(2.5, 9.0)
    c.set_xlabel("$ΔG_{se}$ (kcal/mol)")
    c.set_ylabel("# of interactions")
    c.set_title("All ends (zoomed)")
    if title:
        fig.suptitle(title)
    fig.tight_layout(rect=[0, 0.3, 1, 0.97])
    return fig


def heatmap(ends, energetics, title="", **kwargs):
    fig = pylab.figure()

    heat = energy_array_uniform(ends, energetics)

    pylab.imshow(heat)
    pylab.colorbar()
    pylab.title(title)

    return fig
