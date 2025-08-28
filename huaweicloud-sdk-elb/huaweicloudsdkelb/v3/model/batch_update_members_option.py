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
        'availability_zone': 'str',
        'admin_state_up': 'bool',
        'name': 'str',
        'protocol_port': 'int',
        'weight': 'int'
    }

    attribute_map = {
        'id': 'id',
        'availability_zone': 'availability_zone',
        'admin_state_up': 'admin_state_up',
        'name': 'name',
        'protocol_port': 'protocol_port',
        'weight': 'weight'
    }

    def __init__(self, id=None, availability_zone=None, admin_state_up=None, name=None, protocol_port=None, weight=None):
        r"""BatchUpdateMembersOption

        The model defined in huaweicloud sdk

        :param id: **参数解释**：后端服务器ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  &gt;此处并非ECS服务器的ID，而是ELB为绑定的后端服务器自动生成的member ID。
        :type id: str
        :param availability_zone: **参数解释**：后端服务器的可用区。  **约束限制**：仅支持IP类型后端服务器设置该字段。且后端服务器组开启可用区亲和时，IP类型后端服务器必须配置该字段为有效非空值。  **取值范围**：本region中ECS可选择的可用区。  **默认取值**：不涉及
        :type availability_zone: str
        :param admin_state_up: **参数解释**：后端服务器的管理状态。取值：true、false。  **约束限制**：虽然创建、更新请求支持该字段，但实际取值决定于后端服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。  **取值范围**：不涉及  **默认取值**：不涉及  请勿传入该字段。
        :type admin_state_up: bool
        :param name: **参数解释**：后端服务器名称。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及
        :type name: str
        :param protocol_port: **参数解释**：后端服务器端口。  **约束限制**： - 在开启端口透传的pool下的member，该字段无法更新。 [- 网关型LB，即pool协议为IP时，protocol_port必须设置为0。](tag:hws_eu)  **取值范围**：1-65535  **默认取值**：不涉及
        :type protocol_port: int
        :param weight: **参数解释**：后端服务器的权重，请求按权重在同一后端服务器组下的后端服务器间分发。权重为0的后端不再接受新的请求。  **约束限制**：当后端服务器所在的后端服务器组的lb_algorithm的取值为SOURCE_IP时，该字段无效。  **取值范围**：0-100  **默认取值**：不涉及
        :type weight: int
        """
        
        

        self._id = None
        self._availability_zone = None
        self._admin_state_up = None
        self._name = None
        self._protocol_port = None
        self._weight = None
        self.discriminator = None

        self.id = id
        if availability_zone is not None:
            self.availability_zone = availability_zone
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
        r"""Gets the id of this BatchUpdateMembersOption.

        **参数解释**：后端服务器ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  >此处并非ECS服务器的ID，而是ELB为绑定的后端服务器自动生成的member ID。

        :return: The id of this BatchUpdateMembersOption.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BatchUpdateMembersOption.

        **参数解释**：后端服务器ID。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及  >此处并非ECS服务器的ID，而是ELB为绑定的后端服务器自动生成的member ID。

        :param id: The id of this BatchUpdateMembersOption.
        :type id: str
        """
        self._id = id

    @property
    def availability_zone(self):
        r"""Gets the availability_zone of this BatchUpdateMembersOption.

        **参数解释**：后端服务器的可用区。  **约束限制**：仅支持IP类型后端服务器设置该字段。且后端服务器组开启可用区亲和时，IP类型后端服务器必须配置该字段为有效非空值。  **取值范围**：本region中ECS可选择的可用区。  **默认取值**：不涉及

        :return: The availability_zone of this BatchUpdateMembersOption.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        r"""Sets the availability_zone of this BatchUpdateMembersOption.

        **参数解释**：后端服务器的可用区。  **约束限制**：仅支持IP类型后端服务器设置该字段。且后端服务器组开启可用区亲和时，IP类型后端服务器必须配置该字段为有效非空值。  **取值范围**：本region中ECS可选择的可用区。  **默认取值**：不涉及

        :param availability_zone: The availability_zone of this BatchUpdateMembersOption.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

    @property
    def admin_state_up(self):
        r"""Gets the admin_state_up of this BatchUpdateMembersOption.

        **参数解释**：后端服务器的管理状态。取值：true、false。  **约束限制**：虽然创建、更新请求支持该字段，但实际取值决定于后端服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。  **取值范围**：不涉及  **默认取值**：不涉及  请勿传入该字段。

        :return: The admin_state_up of this BatchUpdateMembersOption.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        r"""Sets the admin_state_up of this BatchUpdateMembersOption.

        **参数解释**：后端服务器的管理状态。取值：true、false。  **约束限制**：虽然创建、更新请求支持该字段，但实际取值决定于后端服务器对应的弹性云服务器是否存在。若存在，该值为true，否则，该值为false。  **取值范围**：不涉及  **默认取值**：不涉及  请勿传入该字段。

        :param admin_state_up: The admin_state_up of this BatchUpdateMembersOption.
        :type admin_state_up: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def name(self):
        r"""Gets the name of this BatchUpdateMembersOption.

        **参数解释**：后端服务器名称。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :return: The name of this BatchUpdateMembersOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BatchUpdateMembersOption.

        **参数解释**：后端服务器名称。  **约束限制**：不涉及  **取值范围**：不涉及  **默认取值**：不涉及

        :param name: The name of this BatchUpdateMembersOption.
        :type name: str
        """
        self._name = name

    @property
    def protocol_port(self):
        r"""Gets the protocol_port of this BatchUpdateMembersOption.

        **参数解释**：后端服务器端口。  **约束限制**： - 在开启端口透传的pool下的member，该字段无法更新。 [- 网关型LB，即pool协议为IP时，protocol_port必须设置为0。](tag:hws_eu)  **取值范围**：1-65535  **默认取值**：不涉及

        :return: The protocol_port of this BatchUpdateMembersOption.
        :rtype: int
        """
        return self._protocol_port

    @protocol_port.setter
    def protocol_port(self, protocol_port):
        r"""Sets the protocol_port of this BatchUpdateMembersOption.

        **参数解释**：后端服务器端口。  **约束限制**： - 在开启端口透传的pool下的member，该字段无法更新。 [- 网关型LB，即pool协议为IP时，protocol_port必须设置为0。](tag:hws_eu)  **取值范围**：1-65535  **默认取值**：不涉及

        :param protocol_port: The protocol_port of this BatchUpdateMembersOption.
        :type protocol_port: int
        """
        self._protocol_port = protocol_port

    @property
    def weight(self):
        r"""Gets the weight of this BatchUpdateMembersOption.

        **参数解释**：后端服务器的权重，请求按权重在同一后端服务器组下的后端服务器间分发。权重为0的后端不再接受新的请求。  **约束限制**：当后端服务器所在的后端服务器组的lb_algorithm的取值为SOURCE_IP时，该字段无效。  **取值范围**：0-100  **默认取值**：不涉及

        :return: The weight of this BatchUpdateMembersOption.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        r"""Sets the weight of this BatchUpdateMembersOption.

        **参数解释**：后端服务器的权重，请求按权重在同一后端服务器组下的后端服务器间分发。权重为0的后端不再接受新的请求。  **约束限制**：当后端服务器所在的后端服务器组的lb_algorithm的取值为SOURCE_IP时，该字段无效。  **取值范围**：0-100  **默认取值**：不涉及

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
