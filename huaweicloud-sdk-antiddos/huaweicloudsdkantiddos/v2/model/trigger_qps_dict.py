# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TriggerQpsDict:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'http_request_pos_id': 'int',
        'http_packet_per_second': 'int'
    }

    attribute_map = {
        'http_request_pos_id': 'http_request_pos_id',
        'http_packet_per_second': 'http_packet_per_second'
    }

    def __init__(self, http_request_pos_id=None, http_packet_per_second=None):
        r"""TriggerQpsDict

        The model defined in huaweicloud sdk

        :param http_request_pos_id: HTTP请求数分段ID，固定值为1
        :type http_request_pos_id: int
        :param http_packet_per_second: 每秒HTTP请求数（个/s）阈值
        :type http_packet_per_second: int
        """
        
        

        self._http_request_pos_id = None
        self._http_packet_per_second = None
        self.discriminator = None

        self.http_request_pos_id = http_request_pos_id
        self.http_packet_per_second = http_packet_per_second

    @property
    def http_request_pos_id(self):
        r"""Gets the http_request_pos_id of this TriggerQpsDict.

        HTTP请求数分段ID，固定值为1

        :return: The http_request_pos_id of this TriggerQpsDict.
        :rtype: int
        """
        return self._http_request_pos_id

    @http_request_pos_id.setter
    def http_request_pos_id(self, http_request_pos_id):
        r"""Sets the http_request_pos_id of this TriggerQpsDict.

        HTTP请求数分段ID，固定值为1

        :param http_request_pos_id: The http_request_pos_id of this TriggerQpsDict.
        :type http_request_pos_id: int
        """
        self._http_request_pos_id = http_request_pos_id

    @property
    def http_packet_per_second(self):
        r"""Gets the http_packet_per_second of this TriggerQpsDict.

        每秒HTTP请求数（个/s）阈值

        :return: The http_packet_per_second of this TriggerQpsDict.
        :rtype: int
        """
        return self._http_packet_per_second

    @http_packet_per_second.setter
    def http_packet_per_second(self, http_packet_per_second):
        r"""Sets the http_packet_per_second of this TriggerQpsDict.

        每秒HTTP请求数（个/s）阈值

        :param http_packet_per_second: The http_packet_per_second of this TriggerQpsDict.
        :type http_packet_per_second: int
        """
        self._http_packet_per_second = http_packet_per_second

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
        if not isinstance(other, TriggerQpsDict):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
