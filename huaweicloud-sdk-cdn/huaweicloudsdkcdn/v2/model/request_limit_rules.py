# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RequestLimitRules:

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
        'type': 'str',
        'limit_rate_after': 'int',
        'limit_rate_value': 'int'
    }

    attribute_map = {
        'status': 'status',
        'type': 'type',
        'limit_rate_after': 'limit_rate_after',
        'limit_rate_value': 'limit_rate_value'
    }

    def __init__(self, status=None, type=None, limit_rate_after=None, limit_rate_value=None):
        """RequestLimitRules

        The model defined in huaweicloud sdk

        :param status: 状态, on：开启，off：关闭。
        :type status: str
        :param type: 限速方式，目前只支持按传送流量限速，当单个HTTP请求流量达到设定的值，开始限制访问速度。  &gt; size:按传送流量限速。
        :type type: str
        :param limit_rate_after: 限速条件,type&#x3D;size,limit_rate_after&#x3D;50表示从传输传输50个字节后开始限速且限速值为limit_rate_value，  &gt; 单位byte，取值范围：0-1073741824。
        :type limit_rate_after: int
        :param limit_rate_value: 限速值,设置开始限速后的最大访问速度。  &gt; 单位Bps，取值范围 0-104857600
        :type limit_rate_value: int
        """
        
        

        self._status = None
        self._type = None
        self._limit_rate_after = None
        self._limit_rate_value = None
        self.discriminator = None

        self.status = status
        self.type = type
        if limit_rate_after is not None:
            self.limit_rate_after = limit_rate_after
        if limit_rate_value is not None:
            self.limit_rate_value = limit_rate_value

    @property
    def status(self):
        """Gets the status of this RequestLimitRules.

        状态, on：开启，off：关闭。

        :return: The status of this RequestLimitRules.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this RequestLimitRules.

        状态, on：开启，off：关闭。

        :param status: The status of this RequestLimitRules.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this RequestLimitRules.

        限速方式，目前只支持按传送流量限速，当单个HTTP请求流量达到设定的值，开始限制访问速度。  > size:按传送流量限速。

        :return: The type of this RequestLimitRules.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RequestLimitRules.

        限速方式，目前只支持按传送流量限速，当单个HTTP请求流量达到设定的值，开始限制访问速度。  > size:按传送流量限速。

        :param type: The type of this RequestLimitRules.
        :type type: str
        """
        self._type = type

    @property
    def limit_rate_after(self):
        """Gets the limit_rate_after of this RequestLimitRules.

        限速条件,type=size,limit_rate_after=50表示从传输传输50个字节后开始限速且限速值为limit_rate_value，  > 单位byte，取值范围：0-1073741824。

        :return: The limit_rate_after of this RequestLimitRules.
        :rtype: int
        """
        return self._limit_rate_after

    @limit_rate_after.setter
    def limit_rate_after(self, limit_rate_after):
        """Sets the limit_rate_after of this RequestLimitRules.

        限速条件,type=size,limit_rate_after=50表示从传输传输50个字节后开始限速且限速值为limit_rate_value，  > 单位byte，取值范围：0-1073741824。

        :param limit_rate_after: The limit_rate_after of this RequestLimitRules.
        :type limit_rate_after: int
        """
        self._limit_rate_after = limit_rate_after

    @property
    def limit_rate_value(self):
        """Gets the limit_rate_value of this RequestLimitRules.

        限速值,设置开始限速后的最大访问速度。  > 单位Bps，取值范围 0-104857600

        :return: The limit_rate_value of this RequestLimitRules.
        :rtype: int
        """
        return self._limit_rate_value

    @limit_rate_value.setter
    def limit_rate_value(self, limit_rate_value):
        """Sets the limit_rate_value of this RequestLimitRules.

        限速值,设置开始限速后的最大访问速度。  > 单位Bps，取值范围 0-104857600

        :param limit_rate_value: The limit_rate_value of this RequestLimitRules.
        :type limit_rate_value: int
        """
        self._limit_rate_value = limit_rate_value

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
        if not isinstance(other, RequestLimitRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
