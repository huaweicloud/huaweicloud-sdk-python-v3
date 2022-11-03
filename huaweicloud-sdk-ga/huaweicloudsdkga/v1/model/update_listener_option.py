# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateListenerOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'port_ranges': 'list[PortRange]',
        'client_affinity': 'ClientAffinity'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'port_ranges': 'port_ranges',
        'client_affinity': 'client_affinity'
    }

    def __init__(self, name=None, description=None, port_ranges=None, client_affinity=None):
        """UpdateListenerOption

        The model defined in huaweicloud sdk

        :param name: 监听器名称，取值范围：1~64个字符之间，只能由数字、字母、中划线和中文组成。
        :type name: str
        :param description: 监听器的描述信息，取值范围：0~255个字符之间，禁止输入字符：&lt;&gt;。
        :type description: str
        :param port_ranges: 监听端口范围列表。
        :type port_ranges: list[:class:`huaweicloudsdkga.v1.PortRange`]
        :param client_affinity: 
        :type client_affinity: :class:`huaweicloudsdkga.v1.ClientAffinity`
        """
        
        

        self._name = None
        self._description = None
        self._port_ranges = None
        self._client_affinity = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if port_ranges is not None:
            self.port_ranges = port_ranges
        if client_affinity is not None:
            self.client_affinity = client_affinity

    @property
    def name(self):
        """Gets the name of this UpdateListenerOption.

        监听器名称，取值范围：1~64个字符之间，只能由数字、字母、中划线和中文组成。

        :return: The name of this UpdateListenerOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateListenerOption.

        监听器名称，取值范围：1~64个字符之间，只能由数字、字母、中划线和中文组成。

        :param name: The name of this UpdateListenerOption.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateListenerOption.

        监听器的描述信息，取值范围：0~255个字符之间，禁止输入字符：<>。

        :return: The description of this UpdateListenerOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateListenerOption.

        监听器的描述信息，取值范围：0~255个字符之间，禁止输入字符：<>。

        :param description: The description of this UpdateListenerOption.
        :type description: str
        """
        self._description = description

    @property
    def port_ranges(self):
        """Gets the port_ranges of this UpdateListenerOption.

        监听端口范围列表。

        :return: The port_ranges of this UpdateListenerOption.
        :rtype: list[:class:`huaweicloudsdkga.v1.PortRange`]
        """
        return self._port_ranges

    @port_ranges.setter
    def port_ranges(self, port_ranges):
        """Sets the port_ranges of this UpdateListenerOption.

        监听端口范围列表。

        :param port_ranges: The port_ranges of this UpdateListenerOption.
        :type port_ranges: list[:class:`huaweicloudsdkga.v1.PortRange`]
        """
        self._port_ranges = port_ranges

    @property
    def client_affinity(self):
        """Gets the client_affinity of this UpdateListenerOption.


        :return: The client_affinity of this UpdateListenerOption.
        :rtype: :class:`huaweicloudsdkga.v1.ClientAffinity`
        """
        return self._client_affinity

    @client_affinity.setter
    def client_affinity(self, client_affinity):
        """Sets the client_affinity of this UpdateListenerOption.


        :param client_affinity: The client_affinity of this UpdateListenerOption.
        :type client_affinity: :class:`huaweicloudsdkga.v1.ClientAffinity`
        """
        self._client_affinity = client_affinity

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
        if not isinstance(other, UpdateListenerOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
