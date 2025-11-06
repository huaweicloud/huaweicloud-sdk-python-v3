# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BccVaultDaySummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'time_stamp': 'int',
        'vault_summary_list': 'list[BccVaultSingleSummary]',
        'vault_summary_count': 'int',
        'vault_summary_size': 'int',
        'vault_summary_used': 'int',
        'vault_average_utilization_rate': 'float'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'time_stamp': 'time_stamp',
        'vault_summary_list': 'vault_summary_list',
        'vault_summary_count': 'vault_summary_count',
        'vault_summary_size': 'vault_summary_size',
        'vault_summary_used': 'vault_summary_used',
        'vault_average_utilization_rate': 'vault_average_utilization_rate'
    }

    def __init__(self, domain_id=None, time_stamp=None, vault_summary_list=None, vault_summary_count=None, vault_summary_size=None, vault_summary_used=None, vault_average_utilization_rate=None):
        r"""BccVaultDaySummary

        The model defined in huaweicloud sdk

        :param domain_id: 账号ID
        :type domain_id: str
        :param time_stamp: 时间戳
        :type time_stamp: int
        :param vault_summary_list: vault的summary列表
        :type vault_summary_list: list[:class:`huaweicloudsdkbcc.v1.BccVaultSingleSummary`]
        :param vault_summary_count: 存储库summary数量
        :type vault_summary_count: int
        :param vault_summary_size: 存储库summary全部容量大小，单位GB。
        :type vault_summary_size: int
        :param vault_summary_used: 存储库summary已用容量大小，单位MB。
        :type vault_summary_used: int
        :param vault_average_utilization_rate: 存储库summary容量使用率
        :type vault_average_utilization_rate: float
        """
        
        

        self._domain_id = None
        self._time_stamp = None
        self._vault_summary_list = None
        self._vault_summary_count = None
        self._vault_summary_size = None
        self._vault_summary_used = None
        self._vault_average_utilization_rate = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if time_stamp is not None:
            self.time_stamp = time_stamp
        if vault_summary_list is not None:
            self.vault_summary_list = vault_summary_list
        if vault_summary_count is not None:
            self.vault_summary_count = vault_summary_count
        if vault_summary_size is not None:
            self.vault_summary_size = vault_summary_size
        if vault_summary_used is not None:
            self.vault_summary_used = vault_summary_used
        if vault_average_utilization_rate is not None:
            self.vault_average_utilization_rate = vault_average_utilization_rate

    @property
    def domain_id(self):
        r"""Gets the domain_id of this BccVaultDaySummary.

        账号ID

        :return: The domain_id of this BccVaultDaySummary.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this BccVaultDaySummary.

        账号ID

        :param domain_id: The domain_id of this BccVaultDaySummary.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def time_stamp(self):
        r"""Gets the time_stamp of this BccVaultDaySummary.

        时间戳

        :return: The time_stamp of this BccVaultDaySummary.
        :rtype: int
        """
        return self._time_stamp

    @time_stamp.setter
    def time_stamp(self, time_stamp):
        r"""Sets the time_stamp of this BccVaultDaySummary.

        时间戳

        :param time_stamp: The time_stamp of this BccVaultDaySummary.
        :type time_stamp: int
        """
        self._time_stamp = time_stamp

    @property
    def vault_summary_list(self):
        r"""Gets the vault_summary_list of this BccVaultDaySummary.

        vault的summary列表

        :return: The vault_summary_list of this BccVaultDaySummary.
        :rtype: list[:class:`huaweicloudsdkbcc.v1.BccVaultSingleSummary`]
        """
        return self._vault_summary_list

    @vault_summary_list.setter
    def vault_summary_list(self, vault_summary_list):
        r"""Sets the vault_summary_list of this BccVaultDaySummary.

        vault的summary列表

        :param vault_summary_list: The vault_summary_list of this BccVaultDaySummary.
        :type vault_summary_list: list[:class:`huaweicloudsdkbcc.v1.BccVaultSingleSummary`]
        """
        self._vault_summary_list = vault_summary_list

    @property
    def vault_summary_count(self):
        r"""Gets the vault_summary_count of this BccVaultDaySummary.

        存储库summary数量

        :return: The vault_summary_count of this BccVaultDaySummary.
        :rtype: int
        """
        return self._vault_summary_count

    @vault_summary_count.setter
    def vault_summary_count(self, vault_summary_count):
        r"""Sets the vault_summary_count of this BccVaultDaySummary.

        存储库summary数量

        :param vault_summary_count: The vault_summary_count of this BccVaultDaySummary.
        :type vault_summary_count: int
        """
        self._vault_summary_count = vault_summary_count

    @property
    def vault_summary_size(self):
        r"""Gets the vault_summary_size of this BccVaultDaySummary.

        存储库summary全部容量大小，单位GB。

        :return: The vault_summary_size of this BccVaultDaySummary.
        :rtype: int
        """
        return self._vault_summary_size

    @vault_summary_size.setter
    def vault_summary_size(self, vault_summary_size):
        r"""Sets the vault_summary_size of this BccVaultDaySummary.

        存储库summary全部容量大小，单位GB。

        :param vault_summary_size: The vault_summary_size of this BccVaultDaySummary.
        :type vault_summary_size: int
        """
        self._vault_summary_size = vault_summary_size

    @property
    def vault_summary_used(self):
        r"""Gets the vault_summary_used of this BccVaultDaySummary.

        存储库summary已用容量大小，单位MB。

        :return: The vault_summary_used of this BccVaultDaySummary.
        :rtype: int
        """
        return self._vault_summary_used

    @vault_summary_used.setter
    def vault_summary_used(self, vault_summary_used):
        r"""Sets the vault_summary_used of this BccVaultDaySummary.

        存储库summary已用容量大小，单位MB。

        :param vault_summary_used: The vault_summary_used of this BccVaultDaySummary.
        :type vault_summary_used: int
        """
        self._vault_summary_used = vault_summary_used

    @property
    def vault_average_utilization_rate(self):
        r"""Gets the vault_average_utilization_rate of this BccVaultDaySummary.

        存储库summary容量使用率

        :return: The vault_average_utilization_rate of this BccVaultDaySummary.
        :rtype: float
        """
        return self._vault_average_utilization_rate

    @vault_average_utilization_rate.setter
    def vault_average_utilization_rate(self, vault_average_utilization_rate):
        r"""Sets the vault_average_utilization_rate of this BccVaultDaySummary.

        存储库summary容量使用率

        :param vault_average_utilization_rate: The vault_average_utilization_rate of this BccVaultDaySummary.
        :type vault_average_utilization_rate: float
        """
        self._vault_average_utilization_rate = vault_average_utilization_rate

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
        if not isinstance(other, BccVaultDaySummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
