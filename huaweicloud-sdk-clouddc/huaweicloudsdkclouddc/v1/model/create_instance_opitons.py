# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstanceOpitons:

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
        'image_id': 'str',
        'vpc_id': 'str',
        'network_interfaces': 'list[NetworkInterface]',
        'password': 'str',
        'metadata': 'dict(str, str)',
        'description': 'str',
        'placement': 'CreateInstanceOpitonsPlacement'
    }

    attribute_map = {
        'name': 'name',
        'image_id': 'image_id',
        'vpc_id': 'vpc_id',
        'network_interfaces': 'network_interfaces',
        'password': 'password',
        'metadata': 'metadata',
        'description': 'description',
        'placement': 'placement'
    }

    def __init__(self, name=None, image_id=None, vpc_id=None, network_interfaces=None, password=None, metadata=None, description=None, placement=None):
        r"""CreateInstanceOpitons

        The model defined in huaweicloud sdk

        :param name: 设置实例主机名称。取值范围：只能由中文字符、英文字母（a~z，A~Z）、数字（0~9）、下划线（_）、中划线（-）、点（.）组成，且长度为[1-63]个字符。
        :type name: str
        :param image_id: 镜像ID
        :type image_id: str
        :param vpc_id: 创建网卡所属的 VPC ID，可通过 VPC API 查询：https://support.huaweicloud.com/api-vpc/vpc_api01_0003.html。
        :type vpc_id: str
        :param network_interfaces: 指定裸机实例的网卡信息。  约束： 一个裸机实例最多挂载2个网卡，参数中第一个网卡会作为裸机实例的主网卡。若用户指定了多组网卡参数，需保证各组参数都属于同一VPC。
        :type network_interfaces: list[:class:`huaweicloudsdkclouddc.v1.NetworkInterface`]
        :param password: 设置实例的管理员账户初始登录密码，其中，Linux管理员账户为root，Windows管理员账户为Administrator。
        :type password: str
        :param metadata: 创建裸机实例的元数据。  可以通过元数据自定义键值对。   说明： 如果元数据中包含了敏感数据，您应当采取适当的措施来保护敏感数据，比如限制访问范围、加密等。 最多可注入10对键值（Key/Value）。 主键（Key）只能由大写字母（A-Z）、小写字母（a-z）、数字（0-9）、中划线（-）、下划线（_）、冒号（:）、空格（ ）和小数点（.）组成，长度为[1-255]个字符。     值（value）最大长度为255个字符。
        :type metadata: dict(str, str)
        :param description: 裸机实例的描述信息，默认为空字符串。
        :type description: str
        :param placement: 
        :type placement: :class:`huaweicloudsdkclouddc.v1.CreateInstanceOpitonsPlacement`
        """
        
        

        self._name = None
        self._image_id = None
        self._vpc_id = None
        self._network_interfaces = None
        self._password = None
        self._metadata = None
        self._description = None
        self._placement = None
        self.discriminator = None

        self.name = name
        self.image_id = image_id
        self.vpc_id = vpc_id
        self.network_interfaces = network_interfaces
        self.password = password
        if metadata is not None:
            self.metadata = metadata
        if description is not None:
            self.description = description
        if placement is not None:
            self.placement = placement

    @property
    def name(self):
        r"""Gets the name of this CreateInstanceOpitons.

        设置实例主机名称。取值范围：只能由中文字符、英文字母（a~z，A~Z）、数字（0~9）、下划线（_）、中划线（-）、点（.）组成，且长度为[1-63]个字符。

        :return: The name of this CreateInstanceOpitons.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateInstanceOpitons.

        设置实例主机名称。取值范围：只能由中文字符、英文字母（a~z，A~Z）、数字（0~9）、下划线（_）、中划线（-）、点（.）组成，且长度为[1-63]个字符。

        :param name: The name of this CreateInstanceOpitons.
        :type name: str
        """
        self._name = name

    @property
    def image_id(self):
        r"""Gets the image_id of this CreateInstanceOpitons.

        镜像ID

        :return: The image_id of this CreateInstanceOpitons.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this CreateInstanceOpitons.

        镜像ID

        :param image_id: The image_id of this CreateInstanceOpitons.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this CreateInstanceOpitons.

        创建网卡所属的 VPC ID，可通过 VPC API 查询：https://support.huaweicloud.com/api-vpc/vpc_api01_0003.html。

        :return: The vpc_id of this CreateInstanceOpitons.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this CreateInstanceOpitons.

        创建网卡所属的 VPC ID，可通过 VPC API 查询：https://support.huaweicloud.com/api-vpc/vpc_api01_0003.html。

        :param vpc_id: The vpc_id of this CreateInstanceOpitons.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def network_interfaces(self):
        r"""Gets the network_interfaces of this CreateInstanceOpitons.

        指定裸机实例的网卡信息。  约束： 一个裸机实例最多挂载2个网卡，参数中第一个网卡会作为裸机实例的主网卡。若用户指定了多组网卡参数，需保证各组参数都属于同一VPC。

        :return: The network_interfaces of this CreateInstanceOpitons.
        :rtype: list[:class:`huaweicloudsdkclouddc.v1.NetworkInterface`]
        """
        return self._network_interfaces

    @network_interfaces.setter
    def network_interfaces(self, network_interfaces):
        r"""Sets the network_interfaces of this CreateInstanceOpitons.

        指定裸机实例的网卡信息。  约束： 一个裸机实例最多挂载2个网卡，参数中第一个网卡会作为裸机实例的主网卡。若用户指定了多组网卡参数，需保证各组参数都属于同一VPC。

        :param network_interfaces: The network_interfaces of this CreateInstanceOpitons.
        :type network_interfaces: list[:class:`huaweicloudsdkclouddc.v1.NetworkInterface`]
        """
        self._network_interfaces = network_interfaces

    @property
    def password(self):
        r"""Gets the password of this CreateInstanceOpitons.

        设置实例的管理员账户初始登录密码，其中，Linux管理员账户为root，Windows管理员账户为Administrator。

        :return: The password of this CreateInstanceOpitons.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this CreateInstanceOpitons.

        设置实例的管理员账户初始登录密码，其中，Linux管理员账户为root，Windows管理员账户为Administrator。

        :param password: The password of this CreateInstanceOpitons.
        :type password: str
        """
        self._password = password

    @property
    def metadata(self):
        r"""Gets the metadata of this CreateInstanceOpitons.

        创建裸机实例的元数据。  可以通过元数据自定义键值对。   说明： 如果元数据中包含了敏感数据，您应当采取适当的措施来保护敏感数据，比如限制访问范围、加密等。 最多可注入10对键值（Key/Value）。 主键（Key）只能由大写字母（A-Z）、小写字母（a-z）、数字（0-9）、中划线（-）、下划线（_）、冒号（:）、空格（ ）和小数点（.）组成，长度为[1-255]个字符。     值（value）最大长度为255个字符。

        :return: The metadata of this CreateInstanceOpitons.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this CreateInstanceOpitons.

        创建裸机实例的元数据。  可以通过元数据自定义键值对。   说明： 如果元数据中包含了敏感数据，您应当采取适当的措施来保护敏感数据，比如限制访问范围、加密等。 最多可注入10对键值（Key/Value）。 主键（Key）只能由大写字母（A-Z）、小写字母（a-z）、数字（0-9）、中划线（-）、下划线（_）、冒号（:）、空格（ ）和小数点（.）组成，长度为[1-255]个字符。     值（value）最大长度为255个字符。

        :param metadata: The metadata of this CreateInstanceOpitons.
        :type metadata: dict(str, str)
        """
        self._metadata = metadata

    @property
    def description(self):
        r"""Gets the description of this CreateInstanceOpitons.

        裸机实例的描述信息，默认为空字符串。

        :return: The description of this CreateInstanceOpitons.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateInstanceOpitons.

        裸机实例的描述信息，默认为空字符串。

        :param description: The description of this CreateInstanceOpitons.
        :type description: str
        """
        self._description = description

    @property
    def placement(self):
        r"""Gets the placement of this CreateInstanceOpitons.

        :return: The placement of this CreateInstanceOpitons.
        :rtype: :class:`huaweicloudsdkclouddc.v1.CreateInstanceOpitonsPlacement`
        """
        return self._placement

    @placement.setter
    def placement(self, placement):
        r"""Sets the placement of this CreateInstanceOpitons.

        :param placement: The placement of this CreateInstanceOpitons.
        :type placement: :class:`huaweicloudsdkclouddc.v1.CreateInstanceOpitonsPlacement`
        """
        self._placement = placement

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
        if not isinstance(other, CreateInstanceOpitons):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
