# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDDoSConnectionNumberRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'str',
        'end_time': 'str',
        'instance_id': 'str',
        'ip': 'str'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'instance_id': 'instance_id',
        'ip': 'ip'
    }

    def __init__(self, start_time=None, end_time=None, instance_id=None, ip=None):
        r"""ListDDoSConnectionNumberRequest

        The model defined in huaweicloud sdk

        :param start_time: 开始时间（毫秒时间戳）
        :type start_time: str
        :param end_time: 结束时间（毫秒时间戳）
        :type end_time: str
        :param instance_id: 实例id
        :type instance_id: str
        :param ip: 高防ip
        :type ip: str
        """
        
        

        self._start_time = None
        self._end_time = None
        self._instance_id = None
        self._ip = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        self.instance_id = instance_id
        self.ip = ip

    @property
    def start_time(self):
        r"""Gets the start_time of this ListDDoSConnectionNumberRequest.

        开始时间（毫秒时间戳）

        :return: The start_time of this ListDDoSConnectionNumberRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListDDoSConnectionNumberRequest.

        开始时间（毫秒时间戳）

        :param start_time: The start_time of this ListDDoSConnectionNumberRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListDDoSConnectionNumberRequest.

        结束时间（毫秒时间戳）

        :return: The end_time of this ListDDoSConnectionNumberRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListDDoSConnectionNumberRequest.

        结束时间（毫秒时间戳）

        :param end_time: The end_time of this ListDDoSConnectionNumberRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListDDoSConnectionNumberRequest.

        实例id

        :return: The instance_id of this ListDDoSConnectionNumberRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListDDoSConnectionNumberRequest.

        实例id

        :param instance_id: The instance_id of this ListDDoSConnectionNumberRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def ip(self):
        r"""Gets the ip of this ListDDoSConnectionNumberRequest.

        高防ip

        :return: The ip of this ListDDoSConnectionNumberRequest.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this ListDDoSConnectionNumberRequest.

        高防ip

        :param ip: The ip of this ListDDoSConnectionNumberRequest.
        :type ip: str
        """
        self._ip = ip

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
        if not isinstance(other, ListDDoSConnectionNumberRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
