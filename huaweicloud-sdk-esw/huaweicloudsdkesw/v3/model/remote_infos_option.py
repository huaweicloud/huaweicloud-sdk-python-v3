# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RemoteInfosOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'segmentation_id': 'int',
        'tunnel_ip': 'str',
        'tunnel_port': 'int'
    }

    attribute_map = {
        'segmentation_id': 'segmentation_id',
        'tunnel_ip': 'tunnel_ip',
        'tunnel_port': 'tunnel_port'
    }

    def __init__(self, segmentation_id=None, tunnel_ip=None, tunnel_port=None):
        r"""RemoteInfosOption

        The model defined in huaweicloud sdk

        :param segmentation_id: - 参数解释：二层连接的隧道号，对应VXLAN网络标识VNI。 - 约束限制：需与对端VXLAN设置的VNI保持一致。 - 取值范围：1-16777216。 - 默认取值：不涉及。
        :type segmentation_id: int
        :param tunnel_ip: - 参数解释：ESW实例的远端隧道IP。 - 约束限制：需与对端VXLAN设置的VTEP IP保持一致。 - 取值范围：标准的IPv4格式，例：192.168.1.1。 - 默认取值：不涉及。
        :type tunnel_ip: str
        :param tunnel_port: - 参数解释：二层连接的远端隧道端口。 - 约束限制：不涉及。 - 取值范围：4789。 - 默认取值：不涉及。
        :type tunnel_port: int
        """
        
        

        self._segmentation_id = None
        self._tunnel_ip = None
        self._tunnel_port = None
        self.discriminator = None

        self.segmentation_id = segmentation_id
        self.tunnel_ip = tunnel_ip
        if tunnel_port is not None:
            self.tunnel_port = tunnel_port

    @property
    def segmentation_id(self):
        r"""Gets the segmentation_id of this RemoteInfosOption.

        - 参数解释：二层连接的隧道号，对应VXLAN网络标识VNI。 - 约束限制：需与对端VXLAN设置的VNI保持一致。 - 取值范围：1-16777216。 - 默认取值：不涉及。

        :return: The segmentation_id of this RemoteInfosOption.
        :rtype: int
        """
        return self._segmentation_id

    @segmentation_id.setter
    def segmentation_id(self, segmentation_id):
        r"""Sets the segmentation_id of this RemoteInfosOption.

        - 参数解释：二层连接的隧道号，对应VXLAN网络标识VNI。 - 约束限制：需与对端VXLAN设置的VNI保持一致。 - 取值范围：1-16777216。 - 默认取值：不涉及。

        :param segmentation_id: The segmentation_id of this RemoteInfosOption.
        :type segmentation_id: int
        """
        self._segmentation_id = segmentation_id

    @property
    def tunnel_ip(self):
        r"""Gets the tunnel_ip of this RemoteInfosOption.

        - 参数解释：ESW实例的远端隧道IP。 - 约束限制：需与对端VXLAN设置的VTEP IP保持一致。 - 取值范围：标准的IPv4格式，例：192.168.1.1。 - 默认取值：不涉及。

        :return: The tunnel_ip of this RemoteInfosOption.
        :rtype: str
        """
        return self._tunnel_ip

    @tunnel_ip.setter
    def tunnel_ip(self, tunnel_ip):
        r"""Sets the tunnel_ip of this RemoteInfosOption.

        - 参数解释：ESW实例的远端隧道IP。 - 约束限制：需与对端VXLAN设置的VTEP IP保持一致。 - 取值范围：标准的IPv4格式，例：192.168.1.1。 - 默认取值：不涉及。

        :param tunnel_ip: The tunnel_ip of this RemoteInfosOption.
        :type tunnel_ip: str
        """
        self._tunnel_ip = tunnel_ip

    @property
    def tunnel_port(self):
        r"""Gets the tunnel_port of this RemoteInfosOption.

        - 参数解释：二层连接的远端隧道端口。 - 约束限制：不涉及。 - 取值范围：4789。 - 默认取值：不涉及。

        :return: The tunnel_port of this RemoteInfosOption.
        :rtype: int
        """
        return self._tunnel_port

    @tunnel_port.setter
    def tunnel_port(self, tunnel_port):
        r"""Sets the tunnel_port of this RemoteInfosOption.

        - 参数解释：二层连接的远端隧道端口。 - 约束限制：不涉及。 - 取值范围：4789。 - 默认取值：不涉及。

        :param tunnel_port: The tunnel_port of this RemoteInfosOption.
        :type tunnel_port: int
        """
        self._tunnel_port = tunnel_port

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
        if not isinstance(other, RemoteInfosOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
