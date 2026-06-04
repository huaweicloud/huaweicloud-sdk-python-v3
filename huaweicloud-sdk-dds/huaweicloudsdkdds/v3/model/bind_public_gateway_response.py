# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BindPublicGatewayResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'instance_name': 'str',
        'node_id': 'str',
        'node_name': 'str',
        'nat_gateway_id': 'str',
        'public_ip_id': 'str',
        'external_service_port': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'node_id': 'node_id',
        'node_name': 'node_name',
        'nat_gateway_id': 'nat_gateway_id',
        'public_ip_id': 'public_ip_id',
        'external_service_port': 'external_service_port'
    }

    def __init__(self, instance_id=None, instance_name=None, node_id=None, node_name=None, nat_gateway_id=None, public_ip_id=None, external_service_port=None):
        r"""BindPublicGatewayResponse

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释：** 实例ID。 **取值范围：** 不涉及。
        :type instance_id: str
        :param instance_name: **参数解释：** 实例名称。 **取值范围：** 不涉及。
        :type instance_name: str
        :param node_id: **参数解释：** 节点ID。 **取值范围：** 不涉及。
        :type node_id: str
        :param node_name: **参数解释：** 节点名称。 **取值范围：** 不涉及。
        :type node_name: str
        :param nat_gateway_id: **参数解释：** 公网NAT网关实例的ID。 **取值范围：** 不涉及。
        :type nat_gateway_id: str
        :param public_ip_id: **参数解释：** 弹性公网IP的ID。 **取值范围：** 不涉及。
        :type public_ip_id: str
        :param external_service_port: **参数解释：** 弹性公网IP对外提供服务的端口号。 **取值范围：** 1~65535。
        :type external_service_port: int
        """
        
        super().__init__()

        self._instance_id = None
        self._instance_name = None
        self._node_id = None
        self._node_name = None
        self._nat_gateway_id = None
        self._public_ip_id = None
        self._external_service_port = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if node_id is not None:
            self.node_id = node_id
        if node_name is not None:
            self.node_name = node_name
        if nat_gateway_id is not None:
            self.nat_gateway_id = nat_gateway_id
        if public_ip_id is not None:
            self.public_ip_id = public_ip_id
        if external_service_port is not None:
            self.external_service_port = external_service_port

    @property
    def instance_id(self):
        r"""Gets the instance_id of this BindPublicGatewayResponse.

        **参数解释：** 实例ID。 **取值范围：** 不涉及。

        :return: The instance_id of this BindPublicGatewayResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this BindPublicGatewayResponse.

        **参数解释：** 实例ID。 **取值范围：** 不涉及。

        :param instance_id: The instance_id of this BindPublicGatewayResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this BindPublicGatewayResponse.

        **参数解释：** 实例名称。 **取值范围：** 不涉及。

        :return: The instance_name of this BindPublicGatewayResponse.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this BindPublicGatewayResponse.

        **参数解释：** 实例名称。 **取值范围：** 不涉及。

        :param instance_name: The instance_name of this BindPublicGatewayResponse.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def node_id(self):
        r"""Gets the node_id of this BindPublicGatewayResponse.

        **参数解释：** 节点ID。 **取值范围：** 不涉及。

        :return: The node_id of this BindPublicGatewayResponse.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this BindPublicGatewayResponse.

        **参数解释：** 节点ID。 **取值范围：** 不涉及。

        :param node_id: The node_id of this BindPublicGatewayResponse.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def node_name(self):
        r"""Gets the node_name of this BindPublicGatewayResponse.

        **参数解释：** 节点名称。 **取值范围：** 不涉及。

        :return: The node_name of this BindPublicGatewayResponse.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this BindPublicGatewayResponse.

        **参数解释：** 节点名称。 **取值范围：** 不涉及。

        :param node_name: The node_name of this BindPublicGatewayResponse.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def nat_gateway_id(self):
        r"""Gets the nat_gateway_id of this BindPublicGatewayResponse.

        **参数解释：** 公网NAT网关实例的ID。 **取值范围：** 不涉及。

        :return: The nat_gateway_id of this BindPublicGatewayResponse.
        :rtype: str
        """
        return self._nat_gateway_id

    @nat_gateway_id.setter
    def nat_gateway_id(self, nat_gateway_id):
        r"""Sets the nat_gateway_id of this BindPublicGatewayResponse.

        **参数解释：** 公网NAT网关实例的ID。 **取值范围：** 不涉及。

        :param nat_gateway_id: The nat_gateway_id of this BindPublicGatewayResponse.
        :type nat_gateway_id: str
        """
        self._nat_gateway_id = nat_gateway_id

    @property
    def public_ip_id(self):
        r"""Gets the public_ip_id of this BindPublicGatewayResponse.

        **参数解释：** 弹性公网IP的ID。 **取值范围：** 不涉及。

        :return: The public_ip_id of this BindPublicGatewayResponse.
        :rtype: str
        """
        return self._public_ip_id

    @public_ip_id.setter
    def public_ip_id(self, public_ip_id):
        r"""Sets the public_ip_id of this BindPublicGatewayResponse.

        **参数解释：** 弹性公网IP的ID。 **取值范围：** 不涉及。

        :param public_ip_id: The public_ip_id of this BindPublicGatewayResponse.
        :type public_ip_id: str
        """
        self._public_ip_id = public_ip_id

    @property
    def external_service_port(self):
        r"""Gets the external_service_port of this BindPublicGatewayResponse.

        **参数解释：** 弹性公网IP对外提供服务的端口号。 **取值范围：** 1~65535。

        :return: The external_service_port of this BindPublicGatewayResponse.
        :rtype: int
        """
        return self._external_service_port

    @external_service_port.setter
    def external_service_port(self, external_service_port):
        r"""Sets the external_service_port of this BindPublicGatewayResponse.

        **参数解释：** 弹性公网IP对外提供服务的端口号。 **取值范围：** 1~65535。

        :param external_service_port: The external_service_port of this BindPublicGatewayResponse.
        :type external_service_port: int
        """
        self._external_service_port = external_service_port

    def to_dict(self):
        import warnings
        warnings.warn("BindPublicGatewayResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BindPublicGatewayResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
