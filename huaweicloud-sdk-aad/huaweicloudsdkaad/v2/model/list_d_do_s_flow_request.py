# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDDoSFlowRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'ip': 'str',
        'type': 'str',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'ip': 'ip',
        'type': 'type',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, instance_id=None, ip=None, type=None, start_time=None, end_time=None):
        r"""ListDDoSFlowRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param ip: 高防IP
        :type ip: str
        :param type: 请求类型 pps、bps
        :type type: str
        :param start_time: 开始时间（毫秒时间戳）
        :type start_time: str
        :param end_time: 结束时间（毫秒时间戳）
        :type end_time: str
        """
        
        

        self._instance_id = None
        self._ip = None
        self._type = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.instance_id = instance_id
        self.ip = ip
        self.type = type
        self.start_time = start_time
        self.end_time = end_time

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListDDoSFlowRequest.

        实例ID

        :return: The instance_id of this ListDDoSFlowRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListDDoSFlowRequest.

        实例ID

        :param instance_id: The instance_id of this ListDDoSFlowRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def ip(self):
        r"""Gets the ip of this ListDDoSFlowRequest.

        高防IP

        :return: The ip of this ListDDoSFlowRequest.
        :rtype: str
        """
        return self._ip

    @ip.setter
    def ip(self, ip):
        r"""Sets the ip of this ListDDoSFlowRequest.

        高防IP

        :param ip: The ip of this ListDDoSFlowRequest.
        :type ip: str
        """
        self._ip = ip

    @property
    def type(self):
        r"""Gets the type of this ListDDoSFlowRequest.

        请求类型 pps、bps

        :return: The type of this ListDDoSFlowRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListDDoSFlowRequest.

        请求类型 pps、bps

        :param type: The type of this ListDDoSFlowRequest.
        :type type: str
        """
        self._type = type

    @property
    def start_time(self):
        r"""Gets the start_time of this ListDDoSFlowRequest.

        开始时间（毫秒时间戳）

        :return: The start_time of this ListDDoSFlowRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListDDoSFlowRequest.

        开始时间（毫秒时间戳）

        :param start_time: The start_time of this ListDDoSFlowRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListDDoSFlowRequest.

        结束时间（毫秒时间戳）

        :return: The end_time of this ListDDoSFlowRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListDDoSFlowRequest.

        结束时间（毫秒时间戳）

        :param end_time: The end_time of this ListDDoSFlowRequest.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, ListDDoSFlowRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
