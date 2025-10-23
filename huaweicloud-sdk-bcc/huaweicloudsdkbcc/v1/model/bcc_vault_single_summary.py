# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BccVaultSingleSummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vault_object_type': 'str',
        'vault_count': 'int',
        'vault_sum_size': 'int',
        'vault_used_size': 'int',
        'vault_utilization_rate': 'float'
    }

    attribute_map = {
        'vault_object_type': 'vault_object_type',
        'vault_count': 'vault_count',
        'vault_sum_size': 'vault_sum_size',
        'vault_used_size': 'vault_used_size',
        'vault_utilization_rate': 'vault_utilization_rate'
    }

    def __init__(self, vault_object_type=None, vault_count=None, vault_sum_size=None, vault_used_size=None, vault_utilization_rate=None):
        r"""BccVaultSingleSummary

        The model defined in huaweicloud sdk

        :param vault_object_type: vault的类型
        :type vault_object_type: str
        :param vault_count: vault的数量
        :type vault_count: int
        :param vault_sum_size: vault的大小
        :type vault_sum_size: int
        :param vault_used_size: vault的使用大小
        :type vault_used_size: int
        :param vault_utilization_rate: vault的使用率
        :type vault_utilization_rate: float
        """
        
        

        self._vault_object_type = None
        self._vault_count = None
        self._vault_sum_size = None
        self._vault_used_size = None
        self._vault_utilization_rate = None
        self.discriminator = None

        if vault_object_type is not None:
            self.vault_object_type = vault_object_type
        if vault_count is not None:
            self.vault_count = vault_count
        if vault_sum_size is not None:
            self.vault_sum_size = vault_sum_size
        if vault_used_size is not None:
            self.vault_used_size = vault_used_size
        if vault_utilization_rate is not None:
            self.vault_utilization_rate = vault_utilization_rate

    @property
    def vault_object_type(self):
        r"""Gets the vault_object_type of this BccVaultSingleSummary.

        vault的类型

        :return: The vault_object_type of this BccVaultSingleSummary.
        :rtype: str
        """
        return self._vault_object_type

    @vault_object_type.setter
    def vault_object_type(self, vault_object_type):
        r"""Sets the vault_object_type of this BccVaultSingleSummary.

        vault的类型

        :param vault_object_type: The vault_object_type of this BccVaultSingleSummary.
        :type vault_object_type: str
        """
        self._vault_object_type = vault_object_type

    @property
    def vault_count(self):
        r"""Gets the vault_count of this BccVaultSingleSummary.

        vault的数量

        :return: The vault_count of this BccVaultSingleSummary.
        :rtype: int
        """
        return self._vault_count

    @vault_count.setter
    def vault_count(self, vault_count):
        r"""Sets the vault_count of this BccVaultSingleSummary.

        vault的数量

        :param vault_count: The vault_count of this BccVaultSingleSummary.
        :type vault_count: int
        """
        self._vault_count = vault_count

    @property
    def vault_sum_size(self):
        r"""Gets the vault_sum_size of this BccVaultSingleSummary.

        vault的大小

        :return: The vault_sum_size of this BccVaultSingleSummary.
        :rtype: int
        """
        return self._vault_sum_size

    @vault_sum_size.setter
    def vault_sum_size(self, vault_sum_size):
        r"""Sets the vault_sum_size of this BccVaultSingleSummary.

        vault的大小

        :param vault_sum_size: The vault_sum_size of this BccVaultSingleSummary.
        :type vault_sum_size: int
        """
        self._vault_sum_size = vault_sum_size

    @property
    def vault_used_size(self):
        r"""Gets the vault_used_size of this BccVaultSingleSummary.

        vault的使用大小

        :return: The vault_used_size of this BccVaultSingleSummary.
        :rtype: int
        """
        return self._vault_used_size

    @vault_used_size.setter
    def vault_used_size(self, vault_used_size):
        r"""Sets the vault_used_size of this BccVaultSingleSummary.

        vault的使用大小

        :param vault_used_size: The vault_used_size of this BccVaultSingleSummary.
        :type vault_used_size: int
        """
        self._vault_used_size = vault_used_size

    @property
    def vault_utilization_rate(self):
        r"""Gets the vault_utilization_rate of this BccVaultSingleSummary.

        vault的使用率

        :return: The vault_utilization_rate of this BccVaultSingleSummary.
        :rtype: float
        """
        return self._vault_utilization_rate

    @vault_utilization_rate.setter
    def vault_utilization_rate(self, vault_utilization_rate):
        r"""Sets the vault_utilization_rate of this BccVaultSingleSummary.

        vault的使用率

        :param vault_utilization_rate: The vault_utilization_rate of this BccVaultSingleSummary.
        :type vault_utilization_rate: float
        """
        self._vault_utilization_rate = vault_utilization_rate

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
        if not isinstance(other, BccVaultSingleSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
