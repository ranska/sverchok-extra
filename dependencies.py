
class Dependency(object):
    def __init__(self, package, url,  module=None, message=None):
        self.package = package
        self.module = module
        self.message = message
        self.url = url
        self.pip_installable = False

dependencies = dict()

sverchok_d = dependencies["sverchok"] = Dependency(None, "https://github.com/nortikin/sverchok")
try:
    import sverchok
    from sverchok.utils.logging import info, error, debug
    sverchok_d.module = sverchok
    sverchok_d.message =  "Sverchok addon is available"
except ImportError:
    sverchok_d.message =  "Sverchok addon is not available. Sverchok-Extra will not work."
    print(sverchok_d.message)
    sverchok = None

pip_d = dependencies["pip"] = Dependency("pip", "https://pypi.org/project/pip/")
try:
    import pip
    pip_d.message = "PIP is available"
    pip_d.module = pip
except ImportError:
    pip_d.message = "PIP is not installed"
    debug(pip_d.message)
    pip = None

if pip is None:
    try:
        import ensurepip
    except ImportError:
        ensurepip = None
        info("Ensurepip module is not available, user will not be able to install PIP automatically")
else:
    ensurepip = None
    debug("PIP is already installed, no need to call ensurepip")

scipy_d = dependencies["scipy"] = Dependency("scipy", "https://www.scipy.org/")
try:
    import scipy
    scipy_d.message = "SciPy is available"
    scipy_d.module = scipy
except ImportError:
    scipy_d.message = "SciPy package is not available. Voronoi nodes and RBF-based nodes will not be available."
    scipy_d.pip_installable = True
    info(scipy_d.message)
    scipy = None

geomdl_d = dependencies["geomdl"] = Dependency("geomdl", "https://github.com/orbingol/NURBS-Python/tree/master/geomdl")
try:
    import geomdl
    geomdl_d.message = "geomdl package is available"
    geomdl_d.module = geomdl
except ImportError:
    geomdl_d.message = "geomdl package is not available, NURBS / BSpline related nodes will not be available"
    info(geomdl_d.message)
    geomdl = None

skimage_d = dependencies["skimage"] = Dependency("scikit-image", "https://scikit-image.org/")
try:
    import skimage
    skimage_d.message = "SciKit-Image package is available"
    skimage_d.module = skimage
except ImportError:
    skimage_d.message = "SciKit-Image package is not available; SciKit-based implementation of Marching Cubes and Marching Squares will not be available"
    skimage_d.pip_installable = True
    info(skimage_d.message)
    skimage = None

mcubes_d = dependencies["mcubes"] = Dependency("mcubes", "https://github.com/pmneila/PyMCubes")
try:
    import mcubes
    mcubes_d.message = "PyMCubes package is available"
    mcubes_d.module = mcubes
except ImportError:
    mcubes_d.message = "PyMCubes package is not available. PyMCubes-based implementation of Marching Cubes will not be available"
    info(mcubes_d.message)
    mcubes = None

pygalmesh_d = dependencies["pygalmesh"] = Dependency("pygalmesh", "https://github.com/nschloe/pygalmesh")
try:
    import pygalmesh
    pygalmesh_d.message = "Pygalmesh package is available"
    pygalmesh_d.module = pygalmesh
except ImportError:
    pygalmesh_d.message = "Pygalmesh package is not available. Corresponding nodes will not be available"
    info(pygalmesh_d.message)
    pygalmesh = None

circlify_d = dependencies["circlify"] = Dependency("circlify", "https://github.com/elmotec/circlify")
try:
    import circlify
    circlify_d.message = "Circlify package is available"
    circlify_d.module = circlify
except ImportError:
    circlify_d.message = "Circlify package is not available. Circlify node will not be available"
    circlify_d.pip_installable = True
    info(circlify_d.message)
    circlify = None

good_names = [d.package for d in dependencies.values() if d.module is not None and d.package is not None]
if good_names:
    info("Dependencies available: %s.", ", ".join(good_names))
else:
    info("No dependencies are available.")

