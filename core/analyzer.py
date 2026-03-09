def count_by_field(logs, field):
    count = {}
    for log in logs:
        value = log[field]
        if value in count:
            count[value] += 1
        else:
            count[value] = 1
    return count  # O(n)


def count_by_service(logs):
    return count_by_field(logs, "service")


def count_by_level(logs):
    return count_by_field(logs, "level")