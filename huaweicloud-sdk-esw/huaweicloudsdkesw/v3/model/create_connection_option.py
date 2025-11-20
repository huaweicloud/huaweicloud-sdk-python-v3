# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateConnectionOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fixed_ips': 'list[str]',
        'name': 'str',
        'remote_infos': 'list[RemoteInfosOption]',
        'virsubnet_id': 'str',
        'vpc_id': 'str'
    }

    attribute_map = {
        'fixed_ips': 'fixed_ips',
        'name': 'name',
        'remote_infos': 'remote_infos',
        'virsubnet_id': 'virsubnet_id',
        'vpc_id': 'vpc_id'
    }

    def __init__(self, fixed_ips=None, name=None, remote_infos=None, virsubnet_id=None, vpc_id=None):
        r"""CreateConnectionOption

        The model defined in huaweicloud sdk

        :param fixed_ips: - 参数解释：下联面网口主备IP；ESW实例在本端二层子网中占用的主备接口IP。 - 约束限制：字符串列表，只能设置两个字符串，且每个字符串内容应该是标准IPv4格式；IP必须在二层子网网段范围内。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type fixed_ips: list[str]
        :param name: - 参数解释：二层连接的名称。 - 约束限制：   - 长度范围为1~64个字符。   - 名称由中文、英文字母、数字、下划线（_）、中划线（-）、点（.）组成。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type name: str
        :param remote_infos: - 参数解释：远端隧道信息。 - 约束限制：不涉及。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type remote_infos: list[:class:`huaweicloudsdkesw.v3.RemoteInfosOption`]
        :param virsubnet_id: - 参数解释：二层连接关联的二层子网ID。 - 约束限制：   - 需要使用本租户下可操作的子网资源的ID；此值即为子网详情中的“网络ID”参数值。   - 带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type virsubnet_id: str
        :param vpc_id: - 参数解释：ESW所在VPC资源ID。 - 约束限制：   - 需要使用本租户下可操作的VPC资源的ID。   - 带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type vpc_id: str
        """
        
        

        self._fixed_ips = None
        self._name = None
        self._remote_infos = None
        self._virsubnet_id = None
        self._vpc_id = None
        self.discriminator = None

        if fixed_ips is not None:
            self.fixed_ips = fixed_ips
        self.name = name
        self.remote_infos = remote_infos
        self.virsubnet_id = virsubnet_id
        self.vpc_id = vpc_id

    @property
    def fixed_ips(self):
        r"""Gets the fixed_ips of this CreateConnectionOption.

        - 参数解释：下联面网口主备IP；ESW实例在本端二层子网中占用的主备接口IP。 - 约束限制：字符串列表，只能设置两个字符串，且每个字符串内容应该是标准IPv4格式；IP必须在二层子网网段范围内。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The fixed_ips of this CreateConnectionOption.
        :rtype: list[str]
        """
        return self._fixed_ips

    @fixed_ips.setter
    def fixed_ips(self, fixed_ips):
        r"""Sets the fixed_ips of this CreateConnectionOption.

        - 参数解释：下联面网口主备IP；ESW实例在本端二层子网中占用的主备接口IP。 - 约束限制：字符串列表，只能设置两个字符串，且每个字符串内容应该是标准IPv4格式；IP必须在二层子网网段范围内。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param fixed_ips: The fixed_ips of this CreateConnectionOption.
        :type fixed_ips: list[str]
        """
        self._fixed_ips = fixed_ips

    @property
    def name(self):
        r"""Gets the name of this CreateConnectionOption.

        - 参数解释：二层连接的名称。 - 约束限制：   - 长度范围为1~64个字符。   - 名称由中文、英文字母、数字、下划线（_）、中划线（-）、点（.）组成。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The name of this CreateConnectionOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateConnectionOption.

        - 参数解释：二层连接的名称。 - 约束限制：   - 长度范围为1~64个字符。   - 名称由中文、英文字母、数字、下划线（_）、中划线（-）、点（.）组成。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param name: The name of this CreateConnectionOption.
        :type name: str
        """
        self._name = name

    @property
    def remote_infos(self):
        r"""Gets the remote_infos of this CreateConnectionOption.

        - 参数解释：远端隧道信息。 - 约束限制：不涉及。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The remote_infos of this CreateConnectionOption.
        :rtype: list[:class:`huaweicloudsdkesw.v3.RemoteInfosOption`]
        """
        return self._remote_infos

    @remote_infos.setter
    def remote_infos(self, remote_infos):
        r"""Sets the remote_infos of this CreateConnectionOption.

        - 参数解释：远端隧道信息。 - 约束限制：不涉及。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param remote_infos: The remote_infos of this CreateConnectionOption.
        :type remote_infos: list[:class:`huaweicloudsdkesw.v3.RemoteInfosOption`]
        """
        self._remote_infos = remote_infos

    @property
    def virsubnet_id(self):
        r"""Gets the virsubnet_id of this CreateConnectionOption.

        - 参数解释：二层连接关联的二层子网ID。 - 约束限制：   - 需要使用本租户下可操作的子网资源的ID；此值即为子网详情中的“网络ID”参数值。   - 带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The virsubnet_id of this CreateConnectionOption.
        :rtype: str
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        r"""Sets the virsubnet_id of this CreateConnectionOption.

        - 参数解释：二层连接关联的二层子网ID。 - 约束限制：   - 需要使用本租户下可操作的子网资源的ID；此值即为子网详情中的“网络ID”参数值。   - 带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param virsubnet_id: The virsubnet_id of this CreateConnectionOption.
        :type virsubnet_id: str
        """
        self._virsubnet_id = virsubnet_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CreateConnectionOption.

        - 参数解释：ESW所在VPC资源ID。 - 约束限制：   - 需要使用本租户下可操作的VPC资源的ID。   - 带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The vpc_id of this CreateConnectionOption.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CreateConnectionOption.

        - 参数解释：ESW所在VPC资源ID。 - 约束限制：   - 需要使用本租户下可操作的VPC资源的ID。   - 带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param vpc_id: The vpc_id of this CreateConnectionOption.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

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
        if not isinstance(other, CreateConnectionOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
