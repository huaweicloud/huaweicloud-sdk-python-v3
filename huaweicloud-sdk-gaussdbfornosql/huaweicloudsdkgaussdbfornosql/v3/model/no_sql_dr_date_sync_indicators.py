# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NoSQLDrDateSyncIndicators:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rsync_ops': 'int',
        'rsync_wal_size': 'int',
        'rsync_push_cost': 'int',
        'rsync_send_cost': 'int',
        'rsync_max_push_cost': 'int',
        'rsync_max_send_cost': 'int',
        'rsync_status': 'int'
    }

    attribute_map = {
        'rsync_ops': 'rsync_ops',
        'rsync_wal_size': 'rsync_wal_size',
        'rsync_push_cost': 'rsync_push_cost',
        'rsync_send_cost': 'rsync_send_cost',
        'rsync_max_push_cost': 'rsync_max_push_cost',
        'rsync_max_send_cost': 'rsync_max_send_cost',
        'rsync_status': 'rsync_status'
    }

    def __init__(self, rsync_ops=None, rsync_wal_size=None, rsync_push_cost=None, rsync_send_cost=None, rsync_max_push_cost=None, rsync_max_send_cost=None, rsync_status=None):
        """NoSQLDrDateSyncIndicators

        The model defined in huaweicloud sdk

        :param rsync_ops: 节点内同步命令的执行速率,每秒多少条数据；
        :type rsync_ops: int
        :param rsync_wal_size: 节点内的同步WAL堆积大小,单位MB；
        :type rsync_wal_size: int
        :param rsync_push_cost: 同步消息从放入消息队列，直到收到对端响应的平均耗时，单位us；
        :type rsync_push_cost: int
        :param rsync_send_cost: 同步消息从消息队列取出，直到收到对端响应的平均耗时，单位us；
        :type rsync_send_cost: int
        :param rsync_max_push_cost: 采集周期内rsync的同步推送耗时最大值，单位us;
        :type rsync_max_push_cost: int
        :param rsync_max_send_cost: 采集周期内rsync的同步发送耗时最大值，单位us;
        :type rsync_max_send_cost: int
        :param rsync_status: rsync的同步状态，1表示正在同步，0表示没有同步;
        :type rsync_status: int
        """
        
        

        self._rsync_ops = None
        self._rsync_wal_size = None
        self._rsync_push_cost = None
        self._rsync_send_cost = None
        self._rsync_max_push_cost = None
        self._rsync_max_send_cost = None
        self._rsync_status = None
        self.discriminator = None

        if rsync_ops is not None:
            self.rsync_ops = rsync_ops
        if rsync_wal_size is not None:
            self.rsync_wal_size = rsync_wal_size
        if rsync_push_cost is not None:
            self.rsync_push_cost = rsync_push_cost
        if rsync_send_cost is not None:
            self.rsync_send_cost = rsync_send_cost
        if rsync_max_push_cost is not None:
            self.rsync_max_push_cost = rsync_max_push_cost
        if rsync_max_send_cost is not None:
            self.rsync_max_send_cost = rsync_max_send_cost
        if rsync_status is not None:
            self.rsync_status = rsync_status

    @property
    def rsync_ops(self):
        """Gets the rsync_ops of this NoSQLDrDateSyncIndicators.

        节点内同步命令的执行速率,每秒多少条数据；

        :return: The rsync_ops of this NoSQLDrDateSyncIndicators.
        :rtype: int
        """
        return self._rsync_ops

    @rsync_ops.setter
    def rsync_ops(self, rsync_ops):
        """Sets the rsync_ops of this NoSQLDrDateSyncIndicators.

        节点内同步命令的执行速率,每秒多少条数据；

        :param rsync_ops: The rsync_ops of this NoSQLDrDateSyncIndicators.
        :type rsync_ops: int
        """
        self._rsync_ops = rsync_ops

    @property
    def rsync_wal_size(self):
        """Gets the rsync_wal_size of this NoSQLDrDateSyncIndicators.

        节点内的同步WAL堆积大小,单位MB；

        :return: The rsync_wal_size of this NoSQLDrDateSyncIndicators.
        :rtype: int
        """
        return self._rsync_wal_size

    @rsync_wal_size.setter
    def rsync_wal_size(self, rsync_wal_size):
        """Sets the rsync_wal_size of this NoSQLDrDateSyncIndicators.

        节点内的同步WAL堆积大小,单位MB；

        :param rsync_wal_size: The rsync_wal_size of this NoSQLDrDateSyncIndicators.
        :type rsync_wal_size: int
        """
        self._rsync_wal_size = rsync_wal_size

    @property
    def rsync_push_cost(self):
        """Gets the rsync_push_cost of this NoSQLDrDateSyncIndicators.

        同步消息从放入消息队列，直到收到对端响应的平均耗时，单位us；

        :return: The rsync_push_cost of this NoSQLDrDateSyncIndicators.
        :rtype: int
        """
        return self._rsync_push_cost

    @rsync_push_cost.setter
    def rsync_push_cost(self, rsync_push_cost):
        """Sets the rsync_push_cost of this NoSQLDrDateSyncIndicators.

        同步消息从放入消息队列，直到收到对端响应的平均耗时，单位us；

        :param rsync_push_cost: The rsync_push_cost of this NoSQLDrDateSyncIndicators.
        :type rsync_push_cost: int
        """
        self._rsync_push_cost = rsync_push_cost

    @property
    def rsync_send_cost(self):
        """Gets the rsync_send_cost of this NoSQLDrDateSyncIndicators.

        同步消息从消息队列取出，直到收到对端响应的平均耗时，单位us；

        :return: The rsync_send_cost of this NoSQLDrDateSyncIndicators.
        :rtype: int
        """
        return self._rsync_send_cost

    @rsync_send_cost.setter
    def rsync_send_cost(self, rsync_send_cost):
        """Sets the rsync_send_cost of this NoSQLDrDateSyncIndicators.

        同步消息从消息队列取出，直到收到对端响应的平均耗时，单位us；

        :param rsync_send_cost: The rsync_send_cost of this NoSQLDrDateSyncIndicators.
        :type rsync_send_cost: int
        """
        self._rsync_send_cost = rsync_send_cost

    @property
    def rsync_max_push_cost(self):
        """Gets the rsync_max_push_cost of this NoSQLDrDateSyncIndicators.

        采集周期内rsync的同步推送耗时最大值，单位us;

        :return: The rsync_max_push_cost of this NoSQLDrDateSyncIndicators.
        :rtype: int
        """
        return self._rsync_max_push_cost

    @rsync_max_push_cost.setter
    def rsync_max_push_cost(self, rsync_max_push_cost):
        """Sets the rsync_max_push_cost of this NoSQLDrDateSyncIndicators.

        采集周期内rsync的同步推送耗时最大值，单位us;

        :param rsync_max_push_cost: The rsync_max_push_cost of this NoSQLDrDateSyncIndicators.
        :type rsync_max_push_cost: int
        """
        self._rsync_max_push_cost = rsync_max_push_cost

    @property
    def rsync_max_send_cost(self):
        """Gets the rsync_max_send_cost of this NoSQLDrDateSyncIndicators.

        采集周期内rsync的同步发送耗时最大值，单位us;

        :return: The rsync_max_send_cost of this NoSQLDrDateSyncIndicators.
        :rtype: int
        """
        return self._rsync_max_send_cost

    @rsync_max_send_cost.setter
    def rsync_max_send_cost(self, rsync_max_send_cost):
        """Sets the rsync_max_send_cost of this NoSQLDrDateSyncIndicators.

        采集周期内rsync的同步发送耗时最大值，单位us;

        :param rsync_max_send_cost: The rsync_max_send_cost of this NoSQLDrDateSyncIndicators.
        :type rsync_max_send_cost: int
        """
        self._rsync_max_send_cost = rsync_max_send_cost

    @property
    def rsync_status(self):
        """Gets the rsync_status of this NoSQLDrDateSyncIndicators.

        rsync的同步状态，1表示正在同步，0表示没有同步;

        :return: The rsync_status of this NoSQLDrDateSyncIndicators.
        :rtype: int
        """
        return self._rsync_status

    @rsync_status.setter
    def rsync_status(self, rsync_status):
        """Sets the rsync_status of this NoSQLDrDateSyncIndicators.

        rsync的同步状态，1表示正在同步，0表示没有同步;

        :param rsync_status: The rsync_status of this NoSQLDrDateSyncIndicators.
        :type rsync_status: int
        """
        self._rsync_status = rsync_status

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
        if not isinstance(other, NoSQLDrDateSyncIndicators):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
