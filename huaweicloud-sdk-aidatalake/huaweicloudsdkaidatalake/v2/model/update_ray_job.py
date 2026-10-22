# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRayJob:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'history_server_config': 'HistoryServerConfig'
    }

    attribute_map = {
        'type': 'type',
        'history_server_config': 'history_server_config'
    }

    def __init__(self, type=None, history_server_config=None):
        r"""UpdateRayJob

        The model defined in huaweicloud sdk

        :param type: **参数解释**：引擎类型。 **约束限制**：不涉及。 **取值范围**：RayJob。 **默认取值**：不涉及。 
        :type type: str
        :param history_server_config: 
        :type history_server_config: :class:`huaweicloudsdkaidatalake.v2.HistoryServerConfig`
        """
        
        

        self._type = None
        self._history_server_config = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if history_server_config is not None:
            self.history_server_config = history_server_config

    @property
    def type(self):
        r"""Gets the type of this UpdateRayJob.

        **参数解释**：引擎类型。 **约束限制**：不涉及。 **取值范围**：RayJob。 **默认取值**：不涉及。 

        :return: The type of this UpdateRayJob.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this UpdateRayJob.

        **参数解释**：引擎类型。 **约束限制**：不涉及。 **取值范围**：RayJob。 **默认取值**：不涉及。 

        :param type: The type of this UpdateRayJob.
        :type type: str
        """
        self._type = type

    @property
    def history_server_config(self):
        r"""Gets the history_server_config of this UpdateRayJob.

        :return: The history_server_config of this UpdateRayJob.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.HistoryServerConfig`
        """
        return self._history_server_config

    @history_server_config.setter
    def history_server_config(self, history_server_config):
        r"""Sets the history_server_config of this UpdateRayJob.

        :param history_server_config: The history_server_config of this UpdateRayJob.
        :type history_server_config: :class:`huaweicloudsdkaidatalake.v2.HistoryServerConfig`
        """
        self._history_server_config = history_server_config

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateRayJob):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
