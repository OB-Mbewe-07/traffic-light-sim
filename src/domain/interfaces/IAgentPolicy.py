from abc import ABC, abstractmethod


class IAgentPolicy(ABC):
    """Contract for anything that decides traffic light phase changes."""

    @abstractmethod
    def decide_phase_change(
        self,
        state : "IntersectionState", # type: ignore
    ) -> dict[str, bool]:
        """
        Given the current state of the intersection, decide which traffic light phases should be green.
        Returns a dictionary mapping lane directions to boolean values indicating whether they should be green.
        """
        raise NotImplementedError