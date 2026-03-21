from data import WebAction, WebState
class StateChange:
    #Records the result/change after an agent applied an action

    pre_state: WebState
    action: WebAction
    post_state: WebState

    def dom_change(self) -> bool:
        return self.pre_state.dom_to_string() != self.post_state.dom_to_string()