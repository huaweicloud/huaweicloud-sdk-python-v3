# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeviceShadowProperties:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'properties': 'object',
        'event_time': 'str'
    }

    attribute_map = {
        'properties': 'properties',
        'event_time': 'event_time'
    }

    def __init__(self, properties=None, event_time=None):
        r"""DeviceShadowProperties

        The model defined in huaweicloud sdk

        :param properties: 设备影子的属性数据，Json格式，里面是一个个键值对，每个键都是产品模型中属性的参数名(property_name)，目前如样例所示只支持一层结构。 **注意**：JSON结构的key当前不支持特殊字符：点(.)、dollar符号($)、空char(十六进制的ASCII码为00),key为以上特殊字符无法正常刷新设备影子
        :type properties: object
        :param event_time: 事件操作时间，格式：yyyyMMdd&#39;T&#39;HHmmss&#39;Z&#39;，如20151212T121212Z。
        :type event_time: str
        """
        
        

        self._properties = None
        self._event_time = None
        self.discriminator = None

        if properties is not None:
            self.properties = properties
        if event_time is not None:
            self.event_time = event_time

    @property
    def properties(self):
        r"""Gets the properties of this DeviceShadowProperties.

        设备影子的属性数据，Json格式，里面是一个个键值对，每个键都是产品模型中属性的参数名(property_name)，目前如样例所示只支持一层结构。 **注意**：JSON结构的key当前不支持特殊字符：点(.)、dollar符号($)、空char(十六进制的ASCII码为00),key为以上特殊字符无法正常刷新设备影子

        :return: The properties of this DeviceShadowProperties.
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this DeviceShadowProperties.

        设备影子的属性数据，Json格式，里面是一个个键值对，每个键都是产品模型中属性的参数名(property_name)，目前如样例所示只支持一层结构。 **注意**：JSON结构的key当前不支持特殊字符：点(.)、dollar符号($)、空char(十六进制的ASCII码为00),key为以上特殊字符无法正常刷新设备影子

        :param properties: The properties of this DeviceShadowProperties.
        :type properties: object
        """
        self._properties = properties

    @property
    def event_time(self):
        r"""Gets the event_time of this DeviceShadowProperties.

        事件操作时间，格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :return: The event_time of this DeviceShadowProperties.
        :rtype: str
        """
        return self._event_time

    @event_time.setter
    def event_time(self, event_time):
        r"""Sets the event_time of this DeviceShadowProperties.

        事件操作时间，格式：yyyyMMdd'T'HHmmss'Z'，如20151212T121212Z。

        :param event_time: The event_time of this DeviceShadowProperties.
        :type event_time: str
        """
        self._event_time = event_time

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
        if not isinstance(other, DeviceShadowProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
