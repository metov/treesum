def rsync_to_paths(rsync_lines):
    paths = []

    for s in rsync_lines:
        if s == '':
            continue

        # Remove the transfer type indicators
        _, p = s.split(' ', maxsplit=1)
        paths.append(p)

    return paths
