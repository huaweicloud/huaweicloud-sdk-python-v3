# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TrafficInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'rxmegabytes': 'float',
        'time': 'str',
        'txmegabytes': 'float'
    }

    attribute_map = {
        'id': 'id',
        'rxmegabytes': 'rxmegabytes',
        'time': 'time',
        'txmegabytes': 'txmegabytes'
    }

    def __init__(self, id=None, rxmegabytes=None, time=None, txmegabytes=None):
        r"""TrafficInfo

        The model defined in huaweicloud sdk

        :param id: 记录ID
        :type id: str
        :param rxmegabytes: 每秒钟接收字节数
        :type rxmegabytes: float
        :param time: 记录时间
        :type time: str
        :param txmegabytes: 每秒钟发送字节数
        :type txmegabytes: float
        """
        
        

        self._id = None
        self._rxmegabytes = None
        self._time = None
        self._txmegabytes = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if rxmegabytes is not None:
            self.rxmegabytes = rxmegabytes
        if time is not None:
            self.time = time
        if txmegabytes is not None:
            self.txmegabytes = txmegabytes

    @property
    def id(self):
        r"""Gets the id of this TrafficInfo.

        记录ID

        :return: The id of this TrafficInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this TrafficInfo.

        记录ID

        :param id: The id of this TrafficInfo.
        :type id: str
        """
        self._id = id

    @property
    def rxmegabytes(self):
        r"""Gets the rxmegabytes of this TrafficInfo.

        每秒钟接收字节数

        :return: The rxmegabytes of this TrafficInfo.
        :rtype: float
        """
        return self._rxmegabytes

    @rxmegabytes.setter
    def rxmegabytes(self, rxmegabytes):
        r"""Sets the rxmegabytes of this TrafficInfo.

        每秒钟接收字节数

        :param rxmegabytes: The rxmegabytes of this TrafficInfo.
        :type rxmegabytes: float
        """
        self._rxmegabytes = rxmegabytes

    @property
    def time(self):
        r"""Gets the time of this TrafficInfo.

        记录时间

        :return: The time of this TrafficInfo.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this TrafficInfo.

        记录时间

        :param time: The time of this TrafficInfo.
        :type time: str
        """
        self._time = time

    @property
    def txmegabytes(self):
        r"""Gets the txmegabytes of this TrafficInfo.

        每秒钟发送字节数

        :return: The txmegabytes of this TrafficInfo.
        :rtype: float
        """
        return self._txmegabytes

    @txmegabytes.setter
    def txmegabytes(self, txmegabytes):
        r"""Sets the txmegabytes of this TrafficInfo.

        每秒钟发送字节数

        :param txmegabytes: The txmegabytes of this TrafficInfo.
        :type txmegabytes: float
        """
        self._txmegabytes = txmegabytes

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
        if not isinstance(other, TrafficInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
