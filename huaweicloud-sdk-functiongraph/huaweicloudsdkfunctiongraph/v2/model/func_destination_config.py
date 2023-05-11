# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FuncDestinationConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'destination': 'str',
        'param': 'str'
    }

    attribute_map = {
        'destination': 'destination',
        'param': 'param'
    }

    def __init__(self, destination=None, param=None):
        """FuncDestinationConfig

        The model defined in huaweicloud sdk

        :param destination: 目标类型。  - OBS：通知到OBS服务。 - SMN：通知到SMN服务。 - DIS：通知到DIS服务。 - FunctionGraph： 通知到函数服务。
        :type destination: str
        :param param: 通知目标服务对应参数,json字符串。  - OBS：包含bucket桶，对象目录前缀prefix，对象默认expires过期时间[0~365]天，0默认不过期。 - SMN：包含smn 主题topic_urn。 - DIS：包含DIS 通道名stream_name。 - FunctionGraph：包含func_urn，函数urn
        :type param: str
        """
        
        

        self._destination = None
        self._param = None
        self.discriminator = None

        if destination is not None:
            self.destination = destination
        if param is not None:
            self.param = param

    @property
    def destination(self):
        """Gets the destination of this FuncDestinationConfig.

        目标类型。  - OBS：通知到OBS服务。 - SMN：通知到SMN服务。 - DIS：通知到DIS服务。 - FunctionGraph： 通知到函数服务。

        :return: The destination of this FuncDestinationConfig.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this FuncDestinationConfig.

        目标类型。  - OBS：通知到OBS服务。 - SMN：通知到SMN服务。 - DIS：通知到DIS服务。 - FunctionGraph： 通知到函数服务。

        :param destination: The destination of this FuncDestinationConfig.
        :type destination: str
        """
        self._destination = destination

    @property
    def param(self):
        """Gets the param of this FuncDestinationConfig.

        通知目标服务对应参数,json字符串。  - OBS：包含bucket桶，对象目录前缀prefix，对象默认expires过期时间[0~365]天，0默认不过期。 - SMN：包含smn 主题topic_urn。 - DIS：包含DIS 通道名stream_name。 - FunctionGraph：包含func_urn，函数urn

        :return: The param of this FuncDestinationConfig.
        :rtype: str
        """
        return self._param

    @param.setter
    def param(self, param):
        """Sets the param of this FuncDestinationConfig.

        通知目标服务对应参数,json字符串。  - OBS：包含bucket桶，对象目录前缀prefix，对象默认expires过期时间[0~365]天，0默认不过期。 - SMN：包含smn 主题topic_urn。 - DIS：包含DIS 通道名stream_name。 - FunctionGraph：包含func_urn，函数urn

        :param param: The param of this FuncDestinationConfig.
        :type param: str
        """
        self._param = param

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
        if not isinstance(other, FuncDestinationConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
