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
        """ListConversionsRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言。zh_CN：中文en_US：英文缺省为zh_CN。
        :type x_language: str
        :param measure_type: 度量类型。1：货币2：时长3：流量4：数量7：容量9：行数10：周期11：频率12：个数16：带宽速率17：容量时长18：查询速率19：带宽速率（1000进制）20：性能测试用量21：面积22：视频23：吞吐量26：通用资源包抵扣单位此参数不携带或携带值为空或携带值为null时，不作为筛选条件。
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
        """Gets the x_language of this ListConversionsRequest.

        语言。zh_CN：中文en_US：英文缺省为zh_CN。

        :return: The x_language of this ListConversionsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this ListConversionsRequest.

        语言。zh_CN：中文en_US：英文缺省为zh_CN。

        :param x_language: The x_language of this ListConversionsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def measure_type(self):
        """Gets the measure_type of this ListConversionsRequest.

        度量类型。1：货币2：时长3：流量4：数量7：容量9：行数10：周期11：频率12：个数16：带宽速率17：容量时长18：查询速率19：带宽速率（1000进制）20：性能测试用量21：面积22：视频23：吞吐量26：通用资源包抵扣单位此参数不携带或携带值为空或携带值为null时，不作为筛选条件。

        :return: The measure_type of this ListConversionsRequest.
        :rtype: int
        """
        return self._measure_type

    @measure_type.setter
    def measure_type(self, measure_type):
        """Sets the measure_type of this ListConversionsRequest.

        度量类型。1：货币2：时长3：流量4：数量7：容量9：行数10：周期11：频率12：个数16：带宽速率17：容量时长18：查询速率19：带宽速率（1000进制）20：性能测试用量21：面积22：视频23：吞吐量26：通用资源包抵扣单位此参数不携带或携带值为空或携带值为null时，不作为筛选条件。

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
