# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PropertiesDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'correlation_data': 'str',
        'response_topic': 'str',
        'user_properties': 'list[UserPropDTO]'
    }

    attribute_map = {
        'correlation_data': 'correlation_data',
        'response_topic': 'response_topic',
        'user_properties': 'user_properties'
    }

    def __init__(self, correlation_data=None, response_topic=None, user_properties=None):
        """PropertiesDTO

        The model defined in huaweicloud sdk

        :param correlation_data: **参数说明**：MQTT 5.0版本请求和响应模式中的相关数据，可选。用户可以通过该参数配置MQTT协议请求和响应模式中的相关数据。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。
        :type correlation_data: str
        :param response_topic: **参数说明**：MQTT 5.0版本请求和响应模式中的响应主题，可选。用户可以通过该参数配置MQTT协议请求和响应模式中的响应主题。 **取值范围**：长度不超过128, 只允许字母、数字、以及_-?&#x3D;$#+/等字符的组合。
        :type response_topic: str
        :param user_properties: **参数说明**：用户自定义属性，可选。用户可以通过该参数配置用户自定义属性。可以配置的最大自定义属性数量为20。
        :type user_properties: list[:class:`huaweicloudsdkiotda.v5.UserPropDTO`]
        """
        
        

        self._correlation_data = None
        self._response_topic = None
        self._user_properties = None
        self.discriminator = None

        if correlation_data is not None:
            self.correlation_data = correlation_data
        if response_topic is not None:
            self.response_topic = response_topic
        if user_properties is not None:
            self.user_properties = user_properties

    @property
    def correlation_data(self):
        """Gets the correlation_data of this PropertiesDTO.

        **参数说明**：MQTT 5.0版本请求和响应模式中的相关数据，可选。用户可以通过该参数配置MQTT协议请求和响应模式中的相关数据。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :return: The correlation_data of this PropertiesDTO.
        :rtype: str
        """
        return self._correlation_data

    @correlation_data.setter
    def correlation_data(self, correlation_data):
        """Sets the correlation_data of this PropertiesDTO.

        **参数说明**：MQTT 5.0版本请求和响应模式中的相关数据，可选。用户可以通过该参数配置MQTT协议请求和响应模式中的相关数据。 **取值范围**：长度不超过128，只允许字母、数字、下划线（_）、连接符（-）的组合。

        :param correlation_data: The correlation_data of this PropertiesDTO.
        :type correlation_data: str
        """
        self._correlation_data = correlation_data

    @property
    def response_topic(self):
        """Gets the response_topic of this PropertiesDTO.

        **参数说明**：MQTT 5.0版本请求和响应模式中的响应主题，可选。用户可以通过该参数配置MQTT协议请求和响应模式中的响应主题。 **取值范围**：长度不超过128, 只允许字母、数字、以及_-?=$#+/等字符的组合。

        :return: The response_topic of this PropertiesDTO.
        :rtype: str
        """
        return self._response_topic

    @response_topic.setter
    def response_topic(self, response_topic):
        """Sets the response_topic of this PropertiesDTO.

        **参数说明**：MQTT 5.0版本请求和响应模式中的响应主题，可选。用户可以通过该参数配置MQTT协议请求和响应模式中的响应主题。 **取值范围**：长度不超过128, 只允许字母、数字、以及_-?=$#+/等字符的组合。

        :param response_topic: The response_topic of this PropertiesDTO.
        :type response_topic: str
        """
        self._response_topic = response_topic

    @property
    def user_properties(self):
        """Gets the user_properties of this PropertiesDTO.

        **参数说明**：用户自定义属性，可选。用户可以通过该参数配置用户自定义属性。可以配置的最大自定义属性数量为20。

        :return: The user_properties of this PropertiesDTO.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.UserPropDTO`]
        """
        return self._user_properties

    @user_properties.setter
    def user_properties(self, user_properties):
        """Sets the user_properties of this PropertiesDTO.

        **参数说明**：用户自定义属性，可选。用户可以通过该参数配置用户自定义属性。可以配置的最大自定义属性数量为20。

        :param user_properties: The user_properties of this PropertiesDTO.
        :type user_properties: list[:class:`huaweicloudsdkiotda.v5.UserPropDTO`]
        """
        self._user_properties = user_properties

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
        if not isinstance(other, PropertiesDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
