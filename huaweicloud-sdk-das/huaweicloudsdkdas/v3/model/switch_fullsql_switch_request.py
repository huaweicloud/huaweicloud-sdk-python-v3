# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchFullsqlSwitchRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'engine_type': 'str',
        'instance_id': 'str'
    }

    attribute_map = {
        'engine_type': 'engine_type',
        'instance_id': 'instance_id'
    }

    def __init__(self, engine_type=None, instance_id=None):
        r"""SwitchFullsqlSwitchRequest

        The model defined in huaweicloud sdk

        :param engine_type: 引擎类型
        :type engine_type: str
        :param instance_id: 实例ID
        :type instance_id: str
        """
        
        

        self._engine_type = None
        self._instance_id = None
        self.discriminator = None

        if engine_type is not None:
            self.engine_type = engine_type
        if instance_id is not None:
            self.instance_id = instance_id

    @property
    def engine_type(self):
        r"""Gets the engine_type of this SwitchFullsqlSwitchRequest.

        引擎类型

        :return: The engine_type of this SwitchFullsqlSwitchRequest.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this SwitchFullsqlSwitchRequest.

        引擎类型

        :param engine_type: The engine_type of this SwitchFullsqlSwitchRequest.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def instance_id(self):
        r"""Gets the instance_id of this SwitchFullsqlSwitchRequest.

        实例ID

        :return: The instance_id of this SwitchFullsqlSwitchRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this SwitchFullsqlSwitchRequest.

        实例ID

        :param instance_id: The instance_id of this SwitchFullsqlSwitchRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

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
        if not isinstance(other, SwitchFullsqlSwitchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
