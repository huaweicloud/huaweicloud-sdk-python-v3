# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BigKeyHotKeySwitchReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'engine_type': 'str'
    }

    attribute_map = {
        'action': 'action',
        'engine_type': 'engine_type'
    }

    def __init__(self, action=None, engine_type=None):
        r"""BigKeyHotKeySwitchReq

        The model defined in huaweicloud sdk

        :param action: 操作类型。enable-开启，disable-关闭
        :type action: str
        :param engine_type: 引擎类型（小写），如geminidb-redis
        :type engine_type: str
        """
        
        

        self._action = None
        self._engine_type = None
        self.discriminator = None

        self.action = action
        self.engine_type = engine_type

    @property
    def action(self):
        r"""Gets the action of this BigKeyHotKeySwitchReq.

        操作类型。enable-开启，disable-关闭

        :return: The action of this BigKeyHotKeySwitchReq.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this BigKeyHotKeySwitchReq.

        操作类型。enable-开启，disable-关闭

        :param action: The action of this BigKeyHotKeySwitchReq.
        :type action: str
        """
        self._action = action

    @property
    def engine_type(self):
        r"""Gets the engine_type of this BigKeyHotKeySwitchReq.

        引擎类型（小写），如geminidb-redis

        :return: The engine_type of this BigKeyHotKeySwitchReq.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this BigKeyHotKeySwitchReq.

        引擎类型（小写），如geminidb-redis

        :param engine_type: The engine_type of this BigKeyHotKeySwitchReq.
        :type engine_type: str
        """
        self._engine_type = engine_type

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
        if not isinstance(other, BigKeyHotKeySwitchReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
