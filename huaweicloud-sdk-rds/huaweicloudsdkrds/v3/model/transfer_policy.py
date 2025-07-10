# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TransferPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'setting_id': 'str',
        'instance_id': 'str',
        'period': 'str',
        'backup_type': 'str',
        'destination': 'str',
        'prefix': 'str'
    }

    attribute_map = {
        'setting_id': 'setting_id',
        'instance_id': 'instance_id',
        'period': 'period',
        'backup_type': 'backup_type',
        'destination': 'destination',
        'prefix': 'prefix'
    }

    def __init__(self, setting_id=None, instance_id=None, period=None, backup_type=None, destination=None, prefix=None):
        r"""TransferPolicy

        The model defined in huaweicloud sdk

        :param setting_id: 策略id
        :type setting_id: str
        :param instance_id: 实例id
        :type instance_id: str
        :param period: 转储策略周期
        :type period: str
        :param backup_type: 转储备份类型
        :type backup_type: str
        :param destination: 目标存储
        :type destination: str
        :param prefix: 转储目标前缀
        :type prefix: str
        """
        
        

        self._setting_id = None
        self._instance_id = None
        self._period = None
        self._backup_type = None
        self._destination = None
        self._prefix = None
        self.discriminator = None

        if setting_id is not None:
            self.setting_id = setting_id
        if instance_id is not None:
            self.instance_id = instance_id
        if period is not None:
            self.period = period
        if backup_type is not None:
            self.backup_type = backup_type
        if destination is not None:
            self.destination = destination
        if prefix is not None:
            self.prefix = prefix

    @property
    def setting_id(self):
        r"""Gets the setting_id of this TransferPolicy.

        策略id

        :return: The setting_id of this TransferPolicy.
        :rtype: str
        """
        return self._setting_id

    @setting_id.setter
    def setting_id(self, setting_id):
        r"""Sets the setting_id of this TransferPolicy.

        策略id

        :param setting_id: The setting_id of this TransferPolicy.
        :type setting_id: str
        """
        self._setting_id = setting_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this TransferPolicy.

        实例id

        :return: The instance_id of this TransferPolicy.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this TransferPolicy.

        实例id

        :param instance_id: The instance_id of this TransferPolicy.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def period(self):
        r"""Gets the period of this TransferPolicy.

        转储策略周期

        :return: The period of this TransferPolicy.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this TransferPolicy.

        转储策略周期

        :param period: The period of this TransferPolicy.
        :type period: str
        """
        self._period = period

    @property
    def backup_type(self):
        r"""Gets the backup_type of this TransferPolicy.

        转储备份类型

        :return: The backup_type of this TransferPolicy.
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        r"""Sets the backup_type of this TransferPolicy.

        转储备份类型

        :param backup_type: The backup_type of this TransferPolicy.
        :type backup_type: str
        """
        self._backup_type = backup_type

    @property
    def destination(self):
        r"""Gets the destination of this TransferPolicy.

        目标存储

        :return: The destination of this TransferPolicy.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        r"""Sets the destination of this TransferPolicy.

        目标存储

        :param destination: The destination of this TransferPolicy.
        :type destination: str
        """
        self._destination = destination

    @property
    def prefix(self):
        r"""Gets the prefix of this TransferPolicy.

        转储目标前缀

        :return: The prefix of this TransferPolicy.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        r"""Sets the prefix of this TransferPolicy.

        转储目标前缀

        :param prefix: The prefix of this TransferPolicy.
        :type prefix: str
        """
        self._prefix = prefix

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
        if not isinstance(other, TransferPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
