# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchSetSqlLimitingSwitchRequestBody:

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
        'engine_type': 'str',
        'switch_type': 'str',
        'instance_ids': 'list[str]'
    }

    attribute_map = {
        'switch_on': 'switch_on',
        'engine_type': 'engine_type',
        'switch_type': 'switch_type',
        'instance_ids': 'instance_ids'
    }

    def __init__(self, switch_on=None, engine_type=None, switch_type=None, instance_ids=None):
        r"""BatchSetSqlLimitingSwitchRequestBody

        The model defined in huaweicloud sdk

        :param switch_on: 开关状态
        :type switch_on: bool
        :param engine_type: 数据库引擎类型
        :type engine_type: str
        :param switch_type: 设置开关的类型
        :type switch_type: str
        :param instance_ids: 实例ID列表
        :type instance_ids: list[str]
        """
        
        

        self._switch_on = None
        self._engine_type = None
        self._switch_type = None
        self._instance_ids = None
        self.discriminator = None

        self.switch_on = switch_on
        self.engine_type = engine_type
        self.switch_type = switch_type
        self.instance_ids = instance_ids

    @property
    def switch_on(self):
        r"""Gets the switch_on of this BatchSetSqlLimitingSwitchRequestBody.

        开关状态

        :return: The switch_on of this BatchSetSqlLimitingSwitchRequestBody.
        :rtype: bool
        """
        return self._switch_on

    @switch_on.setter
    def switch_on(self, switch_on):
        r"""Sets the switch_on of this BatchSetSqlLimitingSwitchRequestBody.

        开关状态

        :param switch_on: The switch_on of this BatchSetSqlLimitingSwitchRequestBody.
        :type switch_on: bool
        """
        self._switch_on = switch_on

    @property
    def engine_type(self):
        r"""Gets the engine_type of this BatchSetSqlLimitingSwitchRequestBody.

        数据库引擎类型

        :return: The engine_type of this BatchSetSqlLimitingSwitchRequestBody.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this BatchSetSqlLimitingSwitchRequestBody.

        数据库引擎类型

        :param engine_type: The engine_type of this BatchSetSqlLimitingSwitchRequestBody.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def switch_type(self):
        r"""Gets the switch_type of this BatchSetSqlLimitingSwitchRequestBody.

        设置开关的类型

        :return: The switch_type of this BatchSetSqlLimitingSwitchRequestBody.
        :rtype: str
        """
        return self._switch_type

    @switch_type.setter
    def switch_type(self, switch_type):
        r"""Sets the switch_type of this BatchSetSqlLimitingSwitchRequestBody.

        设置开关的类型

        :param switch_type: The switch_type of this BatchSetSqlLimitingSwitchRequestBody.
        :type switch_type: str
        """
        self._switch_type = switch_type

    @property
    def instance_ids(self):
        r"""Gets the instance_ids of this BatchSetSqlLimitingSwitchRequestBody.

        实例ID列表

        :return: The instance_ids of this BatchSetSqlLimitingSwitchRequestBody.
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        r"""Sets the instance_ids of this BatchSetSqlLimitingSwitchRequestBody.

        实例ID列表

        :param instance_ids: The instance_ids of this BatchSetSqlLimitingSwitchRequestBody.
        :type instance_ids: list[str]
        """
        self._instance_ids = instance_ids

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
        if not isinstance(other, BatchSetSqlLimitingSwitchRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
