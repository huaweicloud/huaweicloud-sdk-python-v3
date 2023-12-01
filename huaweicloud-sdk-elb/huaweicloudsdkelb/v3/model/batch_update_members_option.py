# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdateMembersOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'admin_state_up': 'bool',
        'name': 'str',
        'protocol_port': 'int',
        'weight': 'int'
    }

    attribute_map = {
        'id': 'id',
        'admin_state_up': 'admin_state_up',
        'name': 'name',
        'protocol_port': 'protocol_port',
        'weight': 'weight'
    }

    def __init__(self, id=None, admin_state_up=None, name=None, protocol_port=None, weight=None):
        """BatchUpdateMembersOption

        The model defined in huaweicloud sdk

        :param id: 后端服务器ID。 &gt;此处并非ECS服务器的ID，而是ELB为绑定的后端服务器自动生成的member ID。
        :type id: str
        :param admin_state_up: 后端云服务器的管理状态。取值：true、false。  虽然创建、更新请求支持该字段，但实际取值决定于后端云服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。  请勿传入该字段。
        :type admin_state_up: bool
        :param name: 后端服务器名称。
        :type name: str
        :param protocol_port: 后端服务器端口号。
        :type protocol_port: int
        :param weight: 后端云服务器的权重，请求按权重在同一后端云服务器组下的后端云服务器间分发。权重为0的后端不再接受新的请求。当后端云服务器所在的后端云服务器组的lb_algorithm的取值为SOURCE_IP时，该字段无效。
        :type weight: int
        """
        
        

        self._id = None
        self._admin_state_up = None
        self._name = None
        self._protocol_port = None
        self._weight = None
        self.discriminator = None

        self.id = id
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if name is not None:
            self.name = name
        if protocol_port is not None:
            self.protocol_port = protocol_port
        if weight is not None:
            self.weight = weight

    @property
    def id(self):
        """Gets the id of this BatchUpdateMembersOption.

        后端服务器ID。 >此处并非ECS服务器的ID，而是ELB为绑定的后端服务器自动生成的member ID。

        :return: The id of this BatchUpdateMembersOption.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BatchUpdateMembersOption.

        后端服务器ID。 >此处并非ECS服务器的ID，而是ELB为绑定的后端服务器自动生成的member ID。

        :param id: The id of this BatchUpdateMembersOption.
        :type id: str
        """
        self._id = id

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this BatchUpdateMembersOption.

        后端云服务器的管理状态。取值：true、false。  虽然创建、更新请求支持该字段，但实际取值决定于后端云服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。  请勿传入该字段。

        :return: The admin_state_up of this BatchUpdateMembersOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this BatchUpdateMembersOption.

        后端云服务器的管理状态。取值：true、false。  虽然创建、更新请求支持该字段，但实际取值决定于后端云服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。  请勿传入该字段。

        :param admin_state_up: The admin_state_up of this BatchUpdateMembersOption.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def name(self):
        """Gets the name of this BatchUpdateMembersOption.

        后端服务器名称。

        :return: The name of this BatchUpdateMembersOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BatchUpdateMembersOption.

        后端服务器名称。

        :param name: The name of this BatchUpdateMembersOption.
        :type name: str
        """
        self._name = name

    @property
    def protocol_port(self):
        """Gets the protocol_port of this BatchUpdateMembersOption.

        后端服务器端口号。

        :return: The protocol_port of this BatchUpdateMembersOption.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        """Sets the protocol_port of this BatchUpdateMembersOption.

        后端服务器端口号。

        :param protocol_port: The protocol_port of this BatchUpdateMembersOption.
        :type protocol_port: int
        """
        self._protocol_port = protocol_port

    @property
    def weight(self):
        """Gets the weight of this BatchUpdateMembersOption.

        后端云服务器的权重，请求按权重在同一后端云服务器组下的后端云服务器间分发。权重为0的后端不再接受新的请求。当后端云服务器所在的后端云服务器组的lb_algorithm的取值为SOURCE_IP时，该字段无效。

        :return: The weight of this BatchUpdateMembersOption.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this BatchUpdateMembersOption.

        后端云服务器的权重，请求按权重在同一后端云服务器组下的后端云服务器间分发。权重为0的后端不再接受新的请求。当后端云服务器所在的后端云服务器组的lb_algorithm的取值为SOURCE_IP时，该字段无效。

        :param weight: The weight of this BatchUpdateMembersOption.
        :type weight: int
        """
        self._weight = weight

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
        if not isinstance(other, BatchUpdateMembersOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
