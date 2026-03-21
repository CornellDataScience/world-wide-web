import data
from typing import Any
class WebInteraction: 
    
    task: str
    website: str
    state_changes: list[data.StateChange]
    reward: float
    final_state: data.WebState

    #builds an instance of a WebInteraction from raw data
    def from_raw_data(cls, raw: dict[str, Any], reward): 
        raw_actions = raw.get("actions", [])
       
       #need to build WebState
        return cls(
            task = raw["task"],
            website = raw["website"],
            #state_changes = 
            reward = reward,
            #final_state = 
        )
