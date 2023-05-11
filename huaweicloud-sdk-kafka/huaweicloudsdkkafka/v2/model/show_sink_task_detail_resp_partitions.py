# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSinkTaskDetailRespPartitions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'partition_id': 'str',
        'status': 'str',
        'last_transfer_offset': 'str',
        'log_end_offset': 'str',
        'lag': 'str'
    }

    attribute_map = {
        'partition_id': 'partition_id',
        'status': 'status',
        'last_transfer_offset': 'last_transfer_offset',
        'log_end_offset': 'log_end_offset',
        'lag': 'lag'
    }

    def __init__(self, partition_id=None, status=None, last_transfer_offset=None, log_end_offset=None, lag=None):
        """ShowSinkTaskDetailRespPartitions

        The model defined in huaweicloud sdk

        :param partition_id: 分区ID。
        :type partition_id: str
        :param status: 运行状态。
        :type status: str
        :param last_transfer_offset: 已转储的消息偏移量。
        :type last_transfer_offset: str
        :param log_end_offset: 消息偏移量。
        :type log_end_offset: str
        :param lag: 积压的消息数。
        :type lag: str
        """
        
        

        self._partition_id = None
        self._status = None
        self._last_transfer_offset = None
        self._log_end_offset = None
        self._lag = None
        self.discriminator = None

        if partition_id is not None:
            self.partition_id = partition_id
        if status is not None:
            self.status = status
        if last_transfer_offset is not None:
            self.last_transfer_offset = last_transfer_offset
        if log_end_offset is not None:
            self.log_end_offset = log_end_offset
        if lag is not None:
            self.lag = lag

    @property
    def partition_id(self):
        """Gets the partition_id of this ShowSinkTaskDetailRespPartitions.

        分区ID。

        :return: The partition_id of this ShowSinkTaskDetailRespPartitions.
        :rtype: str
        """
        return self._partition_id

    @partition_id.setter
    def partition_id(self, partition_id):
        """Sets the partition_id of this ShowSinkTaskDetailRespPartitions.

        分区ID。

        :param partition_id: The partition_id of this ShowSinkTaskDetailRespPartitions.
        :type partition_id: str
        """
        self._partition_id = partition_id

    @property
    def status(self):
        """Gets the status of this ShowSinkTaskDetailRespPartitions.

        运行状态。

        :return: The status of this ShowSinkTaskDetailRespPartitions.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowSinkTaskDetailRespPartitions.

        运行状态。

        :param status: The status of this ShowSinkTaskDetailRespPartitions.
        :type status: str
        """
        self._status = status

    @property
    def last_transfer_offset(self):
        """Gets the last_transfer_offset of this ShowSinkTaskDetailRespPartitions.

        已转储的消息偏移量。

        :return: The last_transfer_offset of this ShowSinkTaskDetailRespPartitions.
        :rtype: str
        """
        return self._last_transfer_offset

    @last_transfer_offset.setter
    def last_transfer_offset(self, last_transfer_offset):
        """Sets the last_transfer_offset of this ShowSinkTaskDetailRespPartitions.

        已转储的消息偏移量。

        :param last_transfer_offset: The last_transfer_offset of this ShowSinkTaskDetailRespPartitions.
        :type last_transfer_offset: str
        """
        self._last_transfer_offset = last_transfer_offset

    @property
    def log_end_offset(self):
        """Gets the log_end_offset of this ShowSinkTaskDetailRespPartitions.

        消息偏移量。

        :return: The log_end_offset of this ShowSinkTaskDetailRespPartitions.
        :rtype: str
        """
        return self._log_end_offset

    @log_end_offset.setter
    def log_end_offset(self, log_end_offset):
        """Sets the log_end_offset of this ShowSinkTaskDetailRespPartitions.

        消息偏移量。

        :param log_end_offset: The log_end_offset of this ShowSinkTaskDetailRespPartitions.
        :type log_end_offset: str
        """
        self._log_end_offset = log_end_offset

    @property
    def lag(self):
        """Gets the lag of this ShowSinkTaskDetailRespPartitions.

        积压的消息数。

        :return: The lag of this ShowSinkTaskDetailRespPartitions.
        :rtype: str
        """
        return self._lag

    @lag.setter
    def lag(self, lag):
        """Sets the lag of this ShowSinkTaskDetailRespPartitions.

        积压的消息数。

        :param lag: The lag of this ShowSinkTaskDetailRespPartitions.
        :type lag: str
        """
        self._lag = lag

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
        if not isinstance(other, ShowSinkTaskDetailRespPartitions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
