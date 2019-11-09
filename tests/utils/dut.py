import logging
import munch


class DuT(object):
    """ Represents a Device under Test

    This object fakes an DuT that is more complicated to get into a specific operating state. It
    provides methods to control the state.
    """

    def __init__(self):
        self._init = True
        self.params = munch.Munch()
        self._state = None
        self._log = logging.getLogger("dut")

    def say_hello(self):
        print("Hello")

    def reset_state(self):
        self._log.info("State has been messed up")
        self._state = None

    def ensure_state(self, state_name):
        if self._state != state_name:
            self._log.info("Reboot to state {0}".format(state_name))
            self._state = state_name
        else:
            self._log.info("Already in state {0}".format(state_name))

    def get_state(self):
        return self._state
