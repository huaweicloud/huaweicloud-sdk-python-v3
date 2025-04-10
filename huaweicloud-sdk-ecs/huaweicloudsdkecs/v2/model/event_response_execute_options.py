# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EventResponseExecuteOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'device': 'str',
        'wwn': 'str',
        'serial_number': 'str',
        'resize_target_flavor_id': 'str',
        'migrate_policy': 'str',
        'executor': 'str'
    }

    attribute_map = {
        'device': 'device',
        'wwn': 'wwn',
        'serial_number': 'serial_number',
        'resize_target_flavor_id': 'resize_target_flavor_id',
        'migrate_policy': 'migrate_policy',
        'executor': 'executor'
    }

    def __init__(self, device=None, wwn=None, serial_number=None, resize_target_flavor_id=None, migrate_policy=None, executor=None):
        r"""EventResponseExecuteOptions

        The model defined in huaweicloud sdk

        :param device: 本地盘设备名
        :type device: str
        :param wwn: 本地盘挂载唯一标识
        :type wwn: str
        :param serial_number: 本地盘序列号
        :type serial_number: str
        :param resize_target_flavor_id: flavorID
        :type resize_target_flavor_id: str
        :param migrate_policy: 实例迁移策略
        :type migrate_policy: str
        :param executor: 执行器
        :type executor: str
        """
        
        

        self._device = None
        self._wwn = None
        self._serial_number = None
        self._resize_target_flavor_id = None
        self._migrate_policy = None
        self._executor = None
        self.discriminator = None

        if device is not None:
            self.device = device
        if wwn is not None:
            self.wwn = wwn
        if serial_number is not None:
            self.serial_number = serial_number
        if resize_target_flavor_id is not None:
            self.resize_target_flavor_id = resize_target_flavor_id
        if migrate_policy is not None:
            self.migrate_policy = migrate_policy
        if executor is not None:
            self.executor = executor

    @property
    def device(self):
        r"""Gets the device of this EventResponseExecuteOptions.

        本地盘设备名

        :return: The device of this EventResponseExecuteOptions.
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        r"""Sets the device of this EventResponseExecuteOptions.

        本地盘设备名

        :param device: The device of this EventResponseExecuteOptions.
        :type device: str
        """
        self._device = device

    @property
    def wwn(self):
        r"""Gets the wwn of this EventResponseExecuteOptions.

        本地盘挂载唯一标识

        :return: The wwn of this EventResponseExecuteOptions.
        :rtype: str
        """
        return self._wwn

    @wwn.setter
    def wwn(self, wwn):
        r"""Sets the wwn of this EventResponseExecuteOptions.

        本地盘挂载唯一标识

        :param wwn: The wwn of this EventResponseExecuteOptions.
        :type wwn: str
        """
        self._wwn = wwn

    @property
    def serial_number(self):
        r"""Gets the serial_number of this EventResponseExecuteOptions.

        本地盘序列号

        :return: The serial_number of this EventResponseExecuteOptions.
        :rtype: str
        """
        return self._serial_number

    @serial_number.setter
    def serial_number(self, serial_number):
        r"""Sets the serial_number of this EventResponseExecuteOptions.

        本地盘序列号

        :param serial_number: The serial_number of this EventResponseExecuteOptions.
        :type serial_number: str
        """
        self._serial_number = serial_number

    @property
    def resize_target_flavor_id(self):
        r"""Gets the resize_target_flavor_id of this EventResponseExecuteOptions.

        flavorID

        :return: The resize_target_flavor_id of this EventResponseExecuteOptions.
        :rtype: str
        """
        return self._resize_target_flavor_id

    @resize_target_flavor_id.setter
    def resize_target_flavor_id(self, resize_target_flavor_id):
        r"""Sets the resize_target_flavor_id of this EventResponseExecuteOptions.

        flavorID

        :param resize_target_flavor_id: The resize_target_flavor_id of this EventResponseExecuteOptions.
        :type resize_target_flavor_id: str
        """
        self._resize_target_flavor_id = resize_target_flavor_id

    @property
    def migrate_policy(self):
        r"""Gets the migrate_policy of this EventResponseExecuteOptions.

        实例迁移策略

        :return: The migrate_policy of this EventResponseExecuteOptions.
        :rtype: str
        """
        return self._migrate_policy

    @migrate_policy.setter
    def migrate_policy(self, migrate_policy):
        r"""Sets the migrate_policy of this EventResponseExecuteOptions.

        实例迁移策略

        :param migrate_policy: The migrate_policy of this EventResponseExecuteOptions.
        :type migrate_policy: str
        """
        self._migrate_policy = migrate_policy

    @property
    def executor(self):
        r"""Gets the executor of this EventResponseExecuteOptions.

        执行器

        :return: The executor of this EventResponseExecuteOptions.
        :rtype: str
        """
        return self._executor

    @executor.setter
    def executor(self, executor):
        r"""Sets the executor of this EventResponseExecuteOptions.

        执行器

        :param executor: The executor of this EventResponseExecuteOptions.
        :type executor: str
        """
        self._executor = executor

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
        if not isinstance(other, EventResponseExecuteOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
