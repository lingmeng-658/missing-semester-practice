import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s:%(name)s:%(message)s",
)

logger = logging.getLogger(__name__)


def average(scores: list[int]) -> float:
    logger.debug("average scores = %s", scores)

    if not scores:
        logger.error("scores is empty")
        raise ValueError("scores cannot be empty")

    total = sum(scores)
    logger.debug("total = %s, count = %s", total, len(scores))

    return total / len(scores)


def main():
    print(average([80, 90, 100]))
    print(average([]))


if __name__ == "__main__":
    main()