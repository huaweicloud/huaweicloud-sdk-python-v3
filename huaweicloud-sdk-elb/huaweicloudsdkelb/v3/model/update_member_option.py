# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateMemberOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'admin_state_up': 'bool',
        'name': 'str',
        'weight': 'int',
        'protocol_port': 'int'
    }

    attribute_map = {
        'admin_state_up': 'admin_state_up',
        'name': 'name',
        'weight': 'weight',
        'protocol_port': 'protocol_port'
    }

    def __init__(self, admin_state_up=None, name=None, weight=None, protocol_port=None):
        """UpdateMemberOption

        The model defined in huaweicloud sdk

        :param admin_state_up: 后端云服务器的管理状态。  取值：true、false。  虽然创建、更新请求支持该字段，但实际取值决定于后端云服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。  请勿传入该字段。
        :type admin_state_up: bool
        :param name: 后端云服务器名称。注意：该名称并非ECS名称，若不传则返回为空。
        :type name: str
        :param weight: 后端云服务器的权重，请求将根据pool配置的负载均衡算法和后端云服务器的权重进行负载分发。 权重值越大，分发的请求越多。权重为0的后端不再接受新的请求。  取值：0-100，默认1。  使用说明：若所在pool的lb_algorithm取值为SOURCE_IP，该字段无效。
        :type weight: int
        :param protocol_port: 后端服务器端口。 &gt; 在开启端口透传的pool下的member，该字段无法更新。
        :type protocol_port: int
        """
        
        

        self._admin_state_up = None
        self._name = None
        self._weight = None
        self._protocol_port = None
        self.discriminator = None

        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if name is not None:
            self.name = name
        if weight is not None:
            self.weight = weight
        if protocol_port is not None:
            self.protocol_port = protocol_port

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this UpdateMemberOption.

        后端云服务器的管理状态。  取值：true、false。  虽然创建、更新请求支持该字段，但实际取值决定于后端云服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。  请勿传入该字段。

        :return: The admin_state_up of this UpdateMemberOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this UpdateMemberOption.

        后端云服务器的管理状态。  取值：true、false。  虽然创建、更新请求支持该字段，但实际取值决定于后端云服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。  请勿传入该字段。

        :param admin_state_up: The admin_state_up of this UpdateMemberOption.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def name(self):
        """Gets the name of this UpdateMemberOption.

        后端云服务器名称。注意：该名称并非ECS名称，若不传则返回为空。

        :return: The name of this UpdateMemberOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateMemberOption.

        后端云服务器名称。注意：该名称并非ECS名称，若不传则返回为空。

        :param name: The name of this UpdateMemberOption.
        :type name: str
        """
        self._name = name

    @property
    def weight(self):
        """Gets the weight of this UpdateMemberOption.

        后端云服务器的权重，请求将根据pool配置的负载均衡算法和后端云服务器的权重进行负载分发。 权重值越大，分发的请求越多。权重为0的后端不再接受新的请求。  取值：0-100，默认1。  使用说明：若所在pool的lb_algorithm取值为SOURCE_IP，该字段无效。

        :return: The weight of this UpdateMemberOption.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this UpdateMemberOption.

        后端云服务器的权重，请求将根据pool配置的负载均衡算法和后端云服务器的权重进行负载分发。 权重值越大，分发的请求越多。权重为0的后端不再接受新的请求。  取值：0-100，默认1。  使用说明：若所在pool的lb_algorithm取值为SOURCE_IP，该字段无效。

        :param weight: The weight of this UpdateMemberOption.
        :type weight: int
        """
        self._weight = weight

    @property
    def protocol_port(self):
        """Gets the protocol_port of this UpdateMemberOption.

        后端服务器端口。 > 在开启端口透传的pool下的member，该字段无法更新。

        :return: The protocol_port of this UpdateMemberOption.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        """Sets the protocol_port of this UpdateMemberOption.

        后端服务器端口。 > 在开启端口透传的pool下的member，该字段无法更新。

        :param protocol_port: The protocol_port of this UpdateMemberOption.
        :type protocol_port: int
        """
        self._protocol_port = protocol_port

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
        if not isinstance(other, UpdateMemberOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
