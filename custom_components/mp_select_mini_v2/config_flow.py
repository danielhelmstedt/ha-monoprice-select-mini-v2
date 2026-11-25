import probatio
from homeassistant import config_entries
from homeassistant.const import CONF_HOST, CONF_NAME

from .const import DOMAIN


class MPSelectMiniV2ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            host = user_input[CONF_HOST]
            name = user_input[CONF_NAME]

            # Create entry with the provided data
            return self.async_create_entry(
                title=name,
                data={
                    CONF_HOST: host,
                    CONF_NAME: name,
                    "manufacturer": "Monoprice",
                    "model": "Select Mini V2",
                },
            )

        data_schema = probatio.Schema({
            probatio.Required(CONF_HOST): str,
            probatio.Required(CONF_NAME): str,
        })

        return self.async_show_form(
            step_id="user", data_schema=data_schema, errors=errors
        )