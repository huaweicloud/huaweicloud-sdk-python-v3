# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConversionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'measure_type': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'measure_type': 'measure_type'
    }

    def __init__(self, x_language=None, measure_type=None):
        r"""ListConversionsRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言，字段预留。默认zh_CN，枚举：zh_CN：中文 en_US：英文
        :type x_language: str
        :param measure_type: 度量类型。1：货币 2：时长 3：流量 4：数量 7：容量 9：行数 10：周期 11：频率 12：个数 16：带宽速率 19：带宽速率（1000进制） 20：性能测试用量 27：核数*时长 28：内存*时长 29：IOPS*时长 30：吞吐量*时长 31：个/时长 40：流量（1000进制） 41：1K Tokens 108：数量*时长。此参数不携带或携带值为空或携带值为null时，不作为筛选条件；不支持携带值为空串。
        :type measure_type: int
        """
        
        

        self._x_language = None
        self._measure_type = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if measure_type is not None:
            self.measure_type = measure_type

    @property
    def x_language(self):
        r"""Gets the x_language of this ListConversionsRequest.

        语言，字段预留。默认zh_CN，枚举：zh_CN：中文 en_US：英文

        :return: The x_language of this ListConversionsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListConversionsRequest.

        语言，字段预留。默认zh_CN，枚举：zh_CN：中文 en_US：英文

        :param x_language: The x_language of this ListConversionsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def measure_type(self):
        r"""Gets the measure_type of this ListConversionsRequest.

        度量类型。1：货币 2：时长 3：流量 4：数量 7：容量 9：行数 10：周期 11：频率 12：个数 16：带宽速率 19：带宽速率（1000进制） 20：性能测试用量 27：核数*时长 28：内存*时长 29：IOPS*时长 30：吞吐量*时长 31：个/时长 40：流量（1000进制） 41：1K Tokens 108：数量*时长。此参数不携带或携带值为空或携带值为null时，不作为筛选条件；不支持携带值为空串。

        :return: The measure_type of this ListConversionsRequest.
        :rtype: int
        """
        return self._measure_type

    @measure_type.setter
    def measure_type(self, measure_type):
        r"""Sets the measure_type of this ListConversionsRequest.

        度量类型。1：货币 2：时长 3：流量 4：数量 7：容量 9：行数 10：周期 11：频率 12：个数 16：带宽速率 19：带宽速率（1000进制） 20：性能测试用量 27：核数*时长 28：内存*时长 29：IOPS*时长 30：吞吐量*时长 31：个/时长 40：流量（1000进制） 41：1K Tokens 108：数量*时长。此参数不携带或携带值为空或携带值为null时，不作为筛选条件；不支持携带值为空串。

        :param measure_type: The measure_type of this ListConversionsRequest.
        :type measure_type: int
        """
        self._measure_type = measure_type

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
        if not isinstance(other, ListConversionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
