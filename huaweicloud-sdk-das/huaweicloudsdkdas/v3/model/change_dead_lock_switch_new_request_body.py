# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeDeadLockSwitchNewRequestBody:

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
        'switch_on': 'bool',
        'instance_id': 'str',
        'retention_hours': 'int'
    }

    attribute_map = {
        'engine_type': 'engine_type',
        'switch_on': 'switch_on',
        'instance_id': 'instance_id',
        'retention_hours': 'retention_hours'
    }

    def __init__(self, engine_type=None, switch_on=None, instance_id=None, retention_hours=None):
        r"""ChangeDeadLockSwitchNewRequestBody

        The model defined in huaweicloud sdk

        :param engine_type: 数据库引擎类型，取值范围：mysql
        :type engine_type: str
        :param switch_on: 开关状态，取值范围：false（关闭）、true（开启）
        :type switch_on: bool
        :param instance_id: 实例ID，实例的唯一标识
        :type instance_id: str
        :param retention_hours: 保存时长
        :type retention_hours: int
        """
        
        

        self._engine_type = None
        self._switch_on = None
        self._instance_id = None
        self._retention_hours = None
        self.discriminator = None

        self.engine_type = engine_type
        self.switch_on = switch_on
        self.instance_id = instance_id
        self.retention_hours = retention_hours

    @property
    def engine_type(self):
        r"""Gets the engine_type of this ChangeDeadLockSwitchNewRequestBody.

        数据库引擎类型，取值范围：mysql

        :return: The engine_type of this ChangeDeadLockSwitchNewRequestBody.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this ChangeDeadLockSwitchNewRequestBody.

        数据库引擎类型，取值范围：mysql

        :param engine_type: The engine_type of this ChangeDeadLockSwitchNewRequestBody.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def switch_on(self):
        r"""Gets the switch_on of this ChangeDeadLockSwitchNewRequestBody.

        开关状态，取值范围：false（关闭）、true（开启）

        :return: The switch_on of this ChangeDeadLockSwitchNewRequestBody.
        :rtype: bool
        """
        return self._switch_on

    @switch_on.setter
    def switch_on(self, switch_on):
        r"""Sets the switch_on of this ChangeDeadLockSwitchNewRequestBody.

        开关状态，取值范围：false（关闭）、true（开启）

        :param switch_on: The switch_on of this ChangeDeadLockSwitchNewRequestBody.
        :type switch_on: bool
        """
        self._switch_on = switch_on

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ChangeDeadLockSwitchNewRequestBody.

        实例ID，实例的唯一标识

        :return: The instance_id of this ChangeDeadLockSwitchNewRequestBody.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ChangeDeadLockSwitchNewRequestBody.

        实例ID，实例的唯一标识

        :param instance_id: The instance_id of this ChangeDeadLockSwitchNewRequestBody.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def retention_hours(self):
        r"""Gets the retention_hours of this ChangeDeadLockSwitchNewRequestBody.

        保存时长

        :return: The retention_hours of this ChangeDeadLockSwitchNewRequestBody.
        :rtype: int
        """
        return self._retention_hours

    @retention_hours.setter
    def retention_hours(self, retention_hours):
        r"""Sets the retention_hours of this ChangeDeadLockSwitchNewRequestBody.

        保存时长

        :param retention_hours: The retention_hours of this ChangeDeadLockSwitchNewRequestBody.
        :type retention_hours: int
        """
        self._retention_hours = retention_hours

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
        if not isinstance(other, ChangeDeadLockSwitchNewRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
