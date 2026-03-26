# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetLockBlockingSwitchReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'switch_on': 'bool',
        'engine_type': 'str',
        'retention_hours': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'switch_on': 'switch_on',
        'engine_type': 'engine_type',
        'retention_hours': 'retention_hours'
    }

    def __init__(self, instance_id=None, switch_on=None, engine_type=None, retention_hours=None):
        r"""SetLockBlockingSwitchReq

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param switch_on: 开关
        :type switch_on: bool
        :param engine_type: 引擎
        :type engine_type: str
        :param retention_hours: 保存时长
        :type retention_hours: int
        """
        
        

        self._instance_id = None
        self._switch_on = None
        self._engine_type = None
        self._retention_hours = None
        self.discriminator = None

        self.instance_id = instance_id
        self.switch_on = switch_on
        self.engine_type = engine_type
        if retention_hours is not None:
            self.retention_hours = retention_hours

    @property
    def instance_id(self):
        r"""Gets the instance_id of this SetLockBlockingSwitchReq.

        实例ID

        :return: The instance_id of this SetLockBlockingSwitchReq.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this SetLockBlockingSwitchReq.

        实例ID

        :param instance_id: The instance_id of this SetLockBlockingSwitchReq.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def switch_on(self):
        r"""Gets the switch_on of this SetLockBlockingSwitchReq.

        开关

        :return: The switch_on of this SetLockBlockingSwitchReq.
        :rtype: bool
        """
        return self._switch_on

    @switch_on.setter
    def switch_on(self, switch_on):
        r"""Sets the switch_on of this SetLockBlockingSwitchReq.

        开关

        :param switch_on: The switch_on of this SetLockBlockingSwitchReq.
        :type switch_on: bool
        """
        self._switch_on = switch_on

    @property
    def engine_type(self):
        r"""Gets the engine_type of this SetLockBlockingSwitchReq.

        引擎

        :return: The engine_type of this SetLockBlockingSwitchReq.
        :rtype: str
        """
        return self._engine_type

    @engine_type.setter
    def engine_type(self, engine_type):
        r"""Sets the engine_type of this SetLockBlockingSwitchReq.

        引擎

        :param engine_type: The engine_type of this SetLockBlockingSwitchReq.
        :type engine_type: str
        """
        self._engine_type = engine_type

    @property
    def retention_hours(self):
        r"""Gets the retention_hours of this SetLockBlockingSwitchReq.

        保存时长

        :return: The retention_hours of this SetLockBlockingSwitchReq.
        :rtype: int
        """
        return self._retention_hours

    @retention_hours.setter
    def retention_hours(self, retention_hours):
        r"""Sets the retention_hours of this SetLockBlockingSwitchReq.

        保存时长

        :param retention_hours: The retention_hours of this SetLockBlockingSwitchReq.
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
        if not isinstance(other, SetLockBlockingSwitchReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
