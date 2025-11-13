# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CollectPublicationMonitorResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'worst_latency': 'int',
        'best_latency': 'int',
        'average_latency': 'int',
        'last_dist_sync': 'str',
        'replicated_transactions': 'int',
        'replication_rate_trans': 'float'
    }

    attribute_map = {
        'status': 'status',
        'worst_latency': 'worst_latency',
        'best_latency': 'best_latency',
        'average_latency': 'average_latency',
        'last_dist_sync': 'last_dist_sync',
        'replicated_transactions': 'replicated_transactions',
        'replication_rate_trans': 'replication_rate_trans'
    }

    def __init__(self, status=None, worst_latency=None, best_latency=None, average_latency=None, last_dist_sync=None, replicated_transactions=None, replication_rate_trans=None):
        r"""CollectPublicationMonitorResponse

        The model defined in huaweicloud sdk

        :param status: 发布关联的快照代理的运行状态。取值如下:  started:已启动。 succeeded:成功。 in_progress:正在运行。 idle:空闲。 retrying:重试中。 failed:失败。
        :type status: str
        :param worst_latency: 数据更改的最长延迟时间（以秒为单位）。
        :type worst_latency: int
        :param best_latency: 数据更改的最短延迟时间（以秒为单位）。
        :type best_latency: int
        :param average_latency: 数据更改的平均延迟时间（以秒为单位）。
        :type average_latency: int
        :param last_dist_sync: 上一次分发代理运行时间。格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type last_dist_sync: str
        :param replicated_transactions: 等待传送到分发数据库的事务数。
        :type replicated_transactions: int
        :param replication_rate_trans: 平均每秒传送到分发数据库的事务数。
        :type replication_rate_trans: float
        """
        
        super().__init__()

        self._status = None
        self._worst_latency = None
        self._best_latency = None
        self._average_latency = None
        self._last_dist_sync = None
        self._replicated_transactions = None
        self._replication_rate_trans = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if worst_latency is not None:
            self.worst_latency = worst_latency
        if best_latency is not None:
            self.best_latency = best_latency
        if average_latency is not None:
            self.average_latency = average_latency
        if last_dist_sync is not None:
            self.last_dist_sync = last_dist_sync
        if replicated_transactions is not None:
            self.replicated_transactions = replicated_transactions
        if replication_rate_trans is not None:
            self.replication_rate_trans = replication_rate_trans

    @property
    def status(self):
        r"""Gets the status of this CollectPublicationMonitorResponse.

        发布关联的快照代理的运行状态。取值如下:  started:已启动。 succeeded:成功。 in_progress:正在运行。 idle:空闲。 retrying:重试中。 failed:失败。

        :return: The status of this CollectPublicationMonitorResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CollectPublicationMonitorResponse.

        发布关联的快照代理的运行状态。取值如下:  started:已启动。 succeeded:成功。 in_progress:正在运行。 idle:空闲。 retrying:重试中。 failed:失败。

        :param status: The status of this CollectPublicationMonitorResponse.
        :type status: str
        """
        self._status = status

    @property
    def worst_latency(self):
        r"""Gets the worst_latency of this CollectPublicationMonitorResponse.

        数据更改的最长延迟时间（以秒为单位）。

        :return: The worst_latency of this CollectPublicationMonitorResponse.
        :rtype: int
        """
        return self._worst_latency

    @worst_latency.setter
    def worst_latency(self, worst_latency):
        r"""Sets the worst_latency of this CollectPublicationMonitorResponse.

        数据更改的最长延迟时间（以秒为单位）。

        :param worst_latency: The worst_latency of this CollectPublicationMonitorResponse.
        :type worst_latency: int
        """
        self._worst_latency = worst_latency

    @property
    def best_latency(self):
        r"""Gets the best_latency of this CollectPublicationMonitorResponse.

        数据更改的最短延迟时间（以秒为单位）。

        :return: The best_latency of this CollectPublicationMonitorResponse.
        :rtype: int
        """
        return self._best_latency

    @best_latency.setter
    def best_latency(self, best_latency):
        r"""Sets the best_latency of this CollectPublicationMonitorResponse.

        数据更改的最短延迟时间（以秒为单位）。

        :param best_latency: The best_latency of this CollectPublicationMonitorResponse.
        :type best_latency: int
        """
        self._best_latency = best_latency

    @property
    def average_latency(self):
        r"""Gets the average_latency of this CollectPublicationMonitorResponse.

        数据更改的平均延迟时间（以秒为单位）。

        :return: The average_latency of this CollectPublicationMonitorResponse.
        :rtype: int
        """
        return self._average_latency

    @average_latency.setter
    def average_latency(self, average_latency):
        r"""Sets the average_latency of this CollectPublicationMonitorResponse.

        数据更改的平均延迟时间（以秒为单位）。

        :param average_latency: The average_latency of this CollectPublicationMonitorResponse.
        :type average_latency: int
        """
        self._average_latency = average_latency

    @property
    def last_dist_sync(self):
        r"""Gets the last_dist_sync of this CollectPublicationMonitorResponse.

        上一次分发代理运行时间。格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The last_dist_sync of this CollectPublicationMonitorResponse.
        :rtype: str
        """
        return self._last_dist_sync

    @last_dist_sync.setter
    def last_dist_sync(self, last_dist_sync):
        r"""Sets the last_dist_sync of this CollectPublicationMonitorResponse.

        上一次分发代理运行时间。格式为“yyyy-mm-ddThh:mm:ssZ”。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param last_dist_sync: The last_dist_sync of this CollectPublicationMonitorResponse.
        :type last_dist_sync: str
        """
        self._last_dist_sync = last_dist_sync

    @property
    def replicated_transactions(self):
        r"""Gets the replicated_transactions of this CollectPublicationMonitorResponse.

        等待传送到分发数据库的事务数。

        :return: The replicated_transactions of this CollectPublicationMonitorResponse.
        :rtype: int
        """
        return self._replicated_transactions

    @replicated_transactions.setter
    def replicated_transactions(self, replicated_transactions):
        r"""Sets the replicated_transactions of this CollectPublicationMonitorResponse.

        等待传送到分发数据库的事务数。

        :param replicated_transactions: The replicated_transactions of this CollectPublicationMonitorResponse.
        :type replicated_transactions: int
        """
        self._replicated_transactions = replicated_transactions

    @property
    def replication_rate_trans(self):
        r"""Gets the replication_rate_trans of this CollectPublicationMonitorResponse.

        平均每秒传送到分发数据库的事务数。

        :return: The replication_rate_trans of this CollectPublicationMonitorResponse.
        :rtype: float
        """
        return self._replication_rate_trans

    @replication_rate_trans.setter
    def replication_rate_trans(self, replication_rate_trans):
        r"""Sets the replication_rate_trans of this CollectPublicationMonitorResponse.

        平均每秒传送到分发数据库的事务数。

        :param replication_rate_trans: The replication_rate_trans of this CollectPublicationMonitorResponse.
        :type replication_rate_trans: float
        """
        self._replication_rate_trans = replication_rate_trans

    def to_dict(self):
        import warnings
        warnings.warn("CollectPublicationMonitorResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, CollectPublicationMonitorResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
