# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TransferPolicyParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'prefix': 'str',
        'destination': 'str',
        'period': 'str',
        'backup_type': 'str'
    }

    attribute_map = {
        'prefix': 'prefix',
        'destination': 'destination',
        'period': 'period',
        'backup_type': 'backup_type'
    }

    def __init__(self, prefix=None, destination=None, period=None, backup_type=None):
        r"""TransferPolicyParam

        The model defined in huaweicloud sdk

        :param prefix: 转储目标前缀
        :type prefix: str
        :param destination: 转储目标桶
        :type destination: str
        :param period: 自动转储周期
        :type period: str
        :param backup_type: 转储备份类型， db:自动备份 log:增量备份, snapshot:手动备份 snapshot:手动备份 db:自动备份 log:日志备份
        :type backup_type: str
        """
        
        

        self._prefix = None
        self._destination = None
        self._period = None
        self._backup_type = None
        self.discriminator = None

        if prefix is not None:
            self.prefix = prefix
        self.destination = destination
        self.period = period
        self.backup_type = backup_type

    @property
    def prefix(self):
        r"""Gets the prefix of this TransferPolicyParam.

        转储目标前缀

        :return: The prefix of this TransferPolicyParam.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        r"""Sets the prefix of this TransferPolicyParam.

        转储目标前缀

        :param prefix: The prefix of this TransferPolicyParam.
        :type prefix: str
        """
        self._prefix = prefix

    @property
    def destination(self):
        r"""Gets the destination of this TransferPolicyParam.

        转储目标桶

        :return: The destination of this TransferPolicyParam.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        r"""Sets the destination of this TransferPolicyParam.

        转储目标桶

        :param destination: The destination of this TransferPolicyParam.
        :type destination: str
        """
        self._destination = destination

    @property
    def period(self):
        r"""Gets the period of this TransferPolicyParam.

        自动转储周期

        :return: The period of this TransferPolicyParam.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        r"""Sets the period of this TransferPolicyParam.

        自动转储周期

        :param period: The period of this TransferPolicyParam.
        :type period: str
        """
        self._period = period

    @property
    def backup_type(self):
        r"""Gets the backup_type of this TransferPolicyParam.

        转储备份类型， db:自动备份 log:增量备份, snapshot:手动备份 snapshot:手动备份 db:自动备份 log:日志备份

        :return: The backup_type of this TransferPolicyParam.
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        r"""Sets the backup_type of this TransferPolicyParam.

        转储备份类型， db:自动备份 log:增量备份, snapshot:手动备份 snapshot:手动备份 db:自动备份 log:日志备份

        :param backup_type: The backup_type of this TransferPolicyParam.
        :type backup_type: str
        """
        self._backup_type = backup_type

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
        if not isinstance(other, TransferPolicyParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
