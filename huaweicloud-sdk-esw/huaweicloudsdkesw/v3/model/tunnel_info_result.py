# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TunnelInfoResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpc_id': 'str',
        'virsubnet_id': 'str',
        'tunnel_ip': 'str',
        'tunnel_port': 'int',
        'tunnel_type': 'str'
    }

    attribute_map = {
        'vpc_id': 'vpc_id',
        'virsubnet_id': 'virsubnet_id',
        'tunnel_ip': 'tunnel_ip',
        'tunnel_port': 'tunnel_port',
        'tunnel_type': 'tunnel_type'
    }

    def __init__(self, vpc_id=None, virsubnet_id=None, tunnel_ip=None, tunnel_port=None, tunnel_type=None):
        r"""TunnelInfoResult

        The model defined in huaweicloud sdk

        :param vpc_id: - 参数解释：ESW所在VPC资源ID。 - 约束限制：   - 需要使用本租户下可操作的VPC资源的ID。   - 带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type vpc_id: str
        :param virsubnet_id: - 参数解释：ESW所在隧道子网ID。 - 约束限制：   - 需要使用本租户下可操作的子网资源的ID；此值即为子网详情中的“网络ID”参数值。   - 带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type virsubnet_id: str
        :param tunnel_ip: - 参数解释：ESW实例的本端隧道IP。 - 约束限制：不能与已存在的子网IP冲突。 - 取值范围：标准的IPv4格式，例：192.168.1.1。 - 默认取值：不涉及。
        :type tunnel_ip: str
        :param tunnel_port: - 参数解释：ESW实例的隧道端口。 - 约束限制：不涉及。 - 取值范围：4789。 - 默认取值：不涉及。
        :type tunnel_port: int
        :param tunnel_type: - 参数解释：ESW实例的隧道协议类型。 - 约束限制：不涉及。 - 取值范围：vxlan。 - 默认取值：不涉及。
        :type tunnel_type: str
        """
        
        

        self._vpc_id = None
        self._virsubnet_id = None
        self._tunnel_ip = None
        self._tunnel_port = None
        self._tunnel_type = None
        self.discriminator = None

        self.vpc_id = vpc_id
        self.virsubnet_id = virsubnet_id
        self.tunnel_ip = tunnel_ip
        self.tunnel_port = tunnel_port
        self.tunnel_type = tunnel_type

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this TunnelInfoResult.

        - 参数解释：ESW所在VPC资源ID。 - 约束限制：   - 需要使用本租户下可操作的VPC资源的ID。   - 带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The vpc_id of this TunnelInfoResult.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this TunnelInfoResult.

        - 参数解释：ESW所在VPC资源ID。 - 约束限制：   - 需要使用本租户下可操作的VPC资源的ID。   - 带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param vpc_id: The vpc_id of this TunnelInfoResult.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def virsubnet_id(self):
        r"""Gets the virsubnet_id of this TunnelInfoResult.

        - 参数解释：ESW所在隧道子网ID。 - 约束限制：   - 需要使用本租户下可操作的子网资源的ID；此值即为子网详情中的“网络ID”参数值。   - 带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The virsubnet_id of this TunnelInfoResult.
        :rtype: str
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        r"""Sets the virsubnet_id of this TunnelInfoResult.

        - 参数解释：ESW所在隧道子网ID。 - 约束限制：   - 需要使用本租户下可操作的子网资源的ID；此值即为子网详情中的“网络ID”参数值。   - 带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param virsubnet_id: The virsubnet_id of this TunnelInfoResult.
        :type virsubnet_id: str
        """
        self._virsubnet_id = virsubnet_id

    @property
    def tunnel_ip(self):
        r"""Gets the tunnel_ip of this TunnelInfoResult.

        - 参数解释：ESW实例的本端隧道IP。 - 约束限制：不能与已存在的子网IP冲突。 - 取值范围：标准的IPv4格式，例：192.168.1.1。 - 默认取值：不涉及。

        :return: The tunnel_ip of this TunnelInfoResult.
        :rtype: str
        """
        return self._tunnel_ip

    @tunnel_ip.setter
    def tunnel_ip(self, tunnel_ip):
        r"""Sets the tunnel_ip of this TunnelInfoResult.

        - 参数解释：ESW实例的本端隧道IP。 - 约束限制：不能与已存在的子网IP冲突。 - 取值范围：标准的IPv4格式，例：192.168.1.1。 - 默认取值：不涉及。

        :param tunnel_ip: The tunnel_ip of this TunnelInfoResult.
        :type tunnel_ip: str
        """
        self._tunnel_ip = tunnel_ip

    @property
    def tunnel_port(self):
        r"""Gets the tunnel_port of this TunnelInfoResult.

        - 参数解释：ESW实例的隧道端口。 - 约束限制：不涉及。 - 取值范围：4789。 - 默认取值：不涉及。

        :return: The tunnel_port of this TunnelInfoResult.
        :rtype: int
        """
        return self._tunnel_port

    @tunnel_port.setter
    def tunnel_port(self, tunnel_port):
        r"""Sets the tunnel_port of this TunnelInfoResult.

        - 参数解释：ESW实例的隧道端口。 - 约束限制：不涉及。 - 取值范围：4789。 - 默认取值：不涉及。

        :param tunnel_port: The tunnel_port of this TunnelInfoResult.
        :type tunnel_port: int
        """
        self._tunnel_port = tunnel_port

    @property
    def tunnel_type(self):
        r"""Gets the tunnel_type of this TunnelInfoResult.

        - 参数解释：ESW实例的隧道协议类型。 - 约束限制：不涉及。 - 取值范围：vxlan。 - 默认取值：不涉及。

        :return: The tunnel_type of this TunnelInfoResult.
        :rtype: str
        """
        return self._tunnel_type

    @tunnel_type.setter
    def tunnel_type(self, tunnel_type):
        r"""Sets the tunnel_type of this TunnelInfoResult.

        - 参数解释：ESW实例的隧道协议类型。 - 约束限制：不涉及。 - 取值范围：vxlan。 - 默认取值：不涉及。

        :param tunnel_type: The tunnel_type of this TunnelInfoResult.
        :type tunnel_type: str
        """
        self._tunnel_type = tunnel_type

    def to_dict(self):
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
        if not isinstance(other, TunnelInfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
