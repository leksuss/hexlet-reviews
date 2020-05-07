# BEGIN
def sort_deps(deps):
    visited = set()
    sorted_deps = []

    def get_deps_of(dep):
        visited.add(dep)
        for neighbor in deps.get(dep, []):
            if neighbor not in visited:
                get_deps_of(neighbor)
        sorted_deps.append(dep)

    for dep in deps:
        if dep not in sorted_deps:
            get_deps_of(dep)
    return sorted_deps
# END
