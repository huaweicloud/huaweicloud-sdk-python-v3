# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeFullDeadLockSwitchRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'switch_on': 'bool',
        'engine_type': 'str'
    }

    attribute_map = {
        'switch_on': 'switch_on',
        'engine_type': 'engine_type'
    }

    def __init__(self, switch_on=None, engine_type=None):
        r"""ChangeFullDeadLockSwitchRequestBody

        The model defined in huaweicloud sdk

        :param switch_on: 开关
        :type switch_on: bool
        :param engine_type: 引擎
        :type engine_type: str
        """
        
        

        self._switch_on = None
        self._engine_type = None
        self.discriminator = None

        self.switch_on = switch_on
        self.engine_type = engine_type

    @property
    def switch_on(self):
        r"""Gets the switch_on of this ChangeFullDeadLockSwitchRequestBody.

        开关

        :return: The switch_on of this ChangeFullDeadLockSwitchRequestBody.
        :rtype: bool
        """
        return self._switch_on

    @switch_on.setter
    def switch_on(self, switch_on):
        r"""Sets the switch_on of this ChangeFullDeadLockSwitchRequestBody.

        开关

        :param switch_on: The switch_on of this ChangeFullDeadLockSwitchRequestBody.
        :type switch_on: bool
        """
        self._switch_on = switch_on

    @property
    def engine_type(self):
        r"""Gets the engine_type of this ChangeFullDeadLockSwitchRequestBody.

        引擎

        :return: The engine_type of this ChangeFullDeadLockSwitchRequestBody.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this ChangeFullDeadLockSwitchRequestBody.

        引擎

        :param engine_type: The engine_type of this ChangeFullDeadLockSwitchRequestBody.
        :type engine_type: str
        """
        self._engine_type = engine_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ChangeFullDeadLockSwitchRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
