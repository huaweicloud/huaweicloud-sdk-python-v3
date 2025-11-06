# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStatusClusterItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success_rate': 'float',
        'fail_rate': 'float',
        'success_count': 'int',
        'total_count': 'int',
        'average_value': 'float',
        'total_value': 'float',
        'limit': 'bool',
        'cluster_id': 'str',
        'cluster_name': 'str'
    }

    attribute_map = {
        'success_rate': 'success_rate',
        'fail_rate': 'fail_rate',
        'success_count': 'success_count',
        'total_count': 'total_count',
        'average_value': 'average_value',
        'total_value': 'total_value',
        'limit': 'limit',
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name'
    }

    def __init__(self, success_rate=None, fail_rate=None, success_count=None, total_count=None, average_value=None, total_value=None, limit=None, cluster_id=None, cluster_name=None):
        r"""ShowStatusClusterItem

        The model defined in huaweicloud sdk

        :param success_rate: 成功率
        :type success_rate: float
        :param fail_rate: 失败率
        :type fail_rate: float
        :param success_count: 成功次数
        :type success_count: int
        :param total_count: 总次数
        :type total_count: int
        :param average_value: 平均值
        :type average_value: float
        :param total_value: 总数
        :type total_value: float
        :param limit: 指标是否超出限制
        :type limit: bool
        :param cluster_id: 集群ID
        :type cluster_id: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        """
        
        

        self._success_rate = None
        self._fail_rate = None
        self._success_count = None
        self._total_count = None
        self._average_value = None
        self._total_value = None
        self._limit = None
        self._cluster_id = None
        self._cluster_name = None
        self.discriminator = None

        if success_rate is not None:
            self.success_rate = success_rate
        if fail_rate is not None:
            self.fail_rate = fail_rate
        if success_count is not None:
            self.success_count = success_count
        if total_count is not None:
            self.total_count = total_count
        if average_value is not None:
            self.average_value = average_value
        if total_value is not None:
            self.total_value = total_value
        if limit is not None:
            self.limit = limit
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name

    @property
    def success_rate(self):
        r"""Gets the success_rate of this ShowStatusClusterItem.

        成功率

        :return: The success_rate of this ShowStatusClusterItem.
        :rtype: float
        """
        return self._success_rate

    @success_rate.setter
    def success_rate(self, success_rate):
        r"""Sets the success_rate of this ShowStatusClusterItem.

        成功率

        :param success_rate: The success_rate of this ShowStatusClusterItem.
        :type success_rate: float
        """
        self._success_rate = success_rate

    @property
    def fail_rate(self):
        r"""Gets the fail_rate of this ShowStatusClusterItem.

        失败率

        :return: The fail_rate of this ShowStatusClusterItem.
        :rtype: float
        """
        return self._fail_rate

    @fail_rate.setter
    def fail_rate(self, fail_rate):
        r"""Sets the fail_rate of this ShowStatusClusterItem.

        失败率

        :param fail_rate: The fail_rate of this ShowStatusClusterItem.
        :type fail_rate: float
        """
        self._fail_rate = fail_rate

    @property
    def success_count(self):
        r"""Gets the success_count of this ShowStatusClusterItem.

        成功次数

        :return: The success_count of this ShowStatusClusterItem.
        :rtype: int
        """
        return self._success_count

    @success_count.setter
    def success_count(self, success_count):
        r"""Sets the success_count of this ShowStatusClusterItem.

        成功次数

        :param success_count: The success_count of this ShowStatusClusterItem.
        :type success_count: int
        """
        self._success_count = success_count

    @property
    def total_count(self):
        r"""Gets the total_count of this ShowStatusClusterItem.

        总次数

        :return: The total_count of this ShowStatusClusterItem.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ShowStatusClusterItem.

        总次数

        :param total_count: The total_count of this ShowStatusClusterItem.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def average_value(self):
        r"""Gets the average_value of this ShowStatusClusterItem.

        平均值

        :return: The average_value of this ShowStatusClusterItem.
        :rtype: float
        """
        return self._average_value

    @average_value.setter
    def average_value(self, average_value):
        r"""Sets the average_value of this ShowStatusClusterItem.

        平均值

        :param average_value: The average_value of this ShowStatusClusterItem.
        :type average_value: float
        """
        self._average_value = average_value

    @property
    def total_value(self):
        r"""Gets the total_value of this ShowStatusClusterItem.

        总数

        :return: The total_value of this ShowStatusClusterItem.
        :rtype: float
        """
        return self._total_value

    @total_value.setter
    def total_value(self, total_value):
        r"""Sets the total_value of this ShowStatusClusterItem.

        总数

        :param total_value: The total_value of this ShowStatusClusterItem.
        :type total_value: float
        """
        self._total_value = total_value

    @property
    def limit(self):
        r"""Gets the limit of this ShowStatusClusterItem.

        指标是否超出限制

        :return: The limit of this ShowStatusClusterItem.
        :rtype: bool
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowStatusClusterItem.

        指标是否超出限制

        :param limit: The limit of this ShowStatusClusterItem.
        :type limit: bool
        """
        self._limit = limit

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ShowStatusClusterItem.

        集群ID

        :return: The cluster_id of this ShowStatusClusterItem.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ShowStatusClusterItem.

        集群ID

        :param cluster_id: The cluster_id of this ShowStatusClusterItem.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ShowStatusClusterItem.

        集群名称

        :return: The cluster_name of this ShowStatusClusterItem.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ShowStatusClusterItem.

        集群名称

        :param cluster_name: The cluster_name of this ShowStatusClusterItem.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

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
        if not isinstance(other, ShowStatusClusterItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
