# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunInstancesOptions:

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
        'network_interfaces': 'list[RunInstancesOptionsNetworkInterfaces]',
        'password': 'str',
        'metadata': 'dict(str, str)',
        'description': 'str',
        'placement': 'RunInstancesOptionsPlacement',
        'min_count': 'int',
        'max_count': 'int'
    }

    attribute_map = {
        'name': 'name',
        'image_id': 'image_id',
        'vpc_id': 'vpc_id',
        'network_interfaces': 'network_interfaces',
        'password': 'password',
        'metadata': 'metadata',
        'description': 'description',
        'placement': 'placement',
        'min_count': 'min_count',
        'max_count': 'max_count'
    }

    def __init__(self, name=None, image_id=None, vpc_id=None, network_interfaces=None, password=None, metadata=None, description=None, placement=None, min_count=None, max_count=None):
        r"""RunInstancesOptions

        The model defined in huaweicloud sdk

        :param name: 设置实例主机名称。取值范围：只能由中文字符、英文字母（a~z，A~Z）、数字（0~9）、下划线（_）、中划线（-）、点（.）组成，且长度为[1-63]个字符。
        :type name: str
        :param image_id: 镜像ID
        :type image_id: str
        :param vpc_id: 创建网卡所属的 VPC ID，可通过 VPC API 查询：https://support.huaweicloud.com/api-vpc/vpc_api01_0003.html。
        :type vpc_id: str
        :param network_interfaces: 指定裸机实例的网卡信息。  约束： 一个裸机实例最多挂载2个网卡，参数中第一个网卡会作为裸机实例的主网卡。若用户指定了多组网卡参数，需保证各组参数都属于同一VPC。
        :type network_interfaces: list[:class:`huaweicloudsdkclouddc.v1.RunInstancesOptionsNetworkInterfaces`]
        :param password: 设置实例的管理员账户初始登录密码，其中，Linux管理员账户为root，Windows管理员账户为Administrator。
        :type password: str
        :param metadata: 创建裸机实例的元数据。  可以通过元数据自定义键值对。   说明： 如果元数据中包含了敏感数据，您应当采取适当的措施来保护敏感数据，比如限制访问范围、加密等。 最多可注入10对键值（Key/Value）。 主键（Key）只能由大写字母（A-Z）、小写字母（a-z）、数字（0-9）、中划线（-）、下划线（_）、冒号（:）、空格（ ）和小数点（.）组成，长度为[1-255]个字符。     值（value）最大长度为255个字符。
        :type metadata: dict(str, str)
        :param description: 裸机实例的描述信息，默认为空字符串。
        :type description: str
        :param placement: 
        :type placement: :class:`huaweicloudsdkclouddc.v1.RunInstancesOptionsPlacement`
        :param min_count: 必须成功启动的最小实例数量。如果无法满足此数量，整个请求失败（不会启动任何实例）。
        :type min_count: int
        :param max_count: 允许启动的最大实例数量。尝试启动最多该数量的实例，但实际启动数可能介于 min_count 和 max_count 之间
        :type max_count: int
        """
        
        

        self._name = None
        self._image_id = None
        self._vpc_id = None
        self._network_interfaces = None
        self._password = None
        self._metadata = None
        self._description = None
        self._placement = None
        self._min_count = None
        self._max_count = None
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
        if min_count is not None:
            self.min_count = min_count
        if max_count is not None:
            self.max_count = max_count

    @property
    def name(self):
        r"""Gets the name of this RunInstancesOptions.

        设置实例主机名称。取值范围：只能由中文字符、英文字母（a~z，A~Z）、数字（0~9）、下划线（_）、中划线（-）、点（.）组成，且长度为[1-63]个字符。

        :return: The name of this RunInstancesOptions.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RunInstancesOptions.

        设置实例主机名称。取值范围：只能由中文字符、英文字母（a~z，A~Z）、数字（0~9）、下划线（_）、中划线（-）、点（.）组成，且长度为[1-63]个字符。

        :param name: The name of this RunInstancesOptions.
        :type name: str
        """
        self._name = name

    @property
    def image_id(self):
        r"""Gets the image_id of this RunInstancesOptions.

        镜像ID

        :return: The image_id of this RunInstancesOptions.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this RunInstancesOptions.

        镜像ID

        :param image_id: The image_id of this RunInstancesOptions.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this RunInstancesOptions.

        创建网卡所属的 VPC ID，可通过 VPC API 查询：https://support.huaweicloud.com/api-vpc/vpc_api01_0003.html。

        :return: The vpc_id of this RunInstancesOptions.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this RunInstancesOptions.

        创建网卡所属的 VPC ID，可通过 VPC API 查询：https://support.huaweicloud.com/api-vpc/vpc_api01_0003.html。

        :param vpc_id: The vpc_id of this RunInstancesOptions.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def network_interfaces(self):
        r"""Gets the network_interfaces of this RunInstancesOptions.

        指定裸机实例的网卡信息。  约束： 一个裸机实例最多挂载2个网卡，参数中第一个网卡会作为裸机实例的主网卡。若用户指定了多组网卡参数，需保证各组参数都属于同一VPC。

        :return: The network_interfaces of this RunInstancesOptions.
        :rtype: list[:class:`huaweicloudsdkclouddc.v1.RunInstancesOptionsNetworkInterfaces`]
        """
        return self._network_interfaces

    @network_interfaces.setter
    def network_interfaces(self, network_interfaces):
        r"""Sets the network_interfaces of this RunInstancesOptions.

        指定裸机实例的网卡信息。  约束： 一个裸机实例最多挂载2个网卡，参数中第一个网卡会作为裸机实例的主网卡。若用户指定了多组网卡参数，需保证各组参数都属于同一VPC。

        :param network_interfaces: The network_interfaces of this RunInstancesOptions.
        :type network_interfaces: list[:class:`huaweicloudsdkclouddc.v1.RunInstancesOptionsNetworkInterfaces`]
        """
        self._network_interfaces = network_interfaces

    @property
    def password(self):
        r"""Gets the password of this RunInstancesOptions.

        设置实例的管理员账户初始登录密码，其中，Linux管理员账户为root，Windows管理员账户为Administrator。

        :return: The password of this RunInstancesOptions.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        r"""Sets the password of this RunInstancesOptions.

        设置实例的管理员账户初始登录密码，其中，Linux管理员账户为root，Windows管理员账户为Administrator。

        :param password: The password of this RunInstancesOptions.
        :type password: str
        """
        self._password = password

    @property
    def metadata(self):
        r"""Gets the metadata of this RunInstancesOptions.

        创建裸机实例的元数据。  可以通过元数据自定义键值对。   说明： 如果元数据中包含了敏感数据，您应当采取适当的措施来保护敏感数据，比如限制访问范围、加密等。 最多可注入10对键值（Key/Value）。 主键（Key）只能由大写字母（A-Z）、小写字母（a-z）、数字（0-9）、中划线（-）、下划线（_）、冒号（:）、空格（ ）和小数点（.）组成，长度为[1-255]个字符。     值（value）最大长度为255个字符。

        :return: The metadata of this RunInstancesOptions.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this RunInstancesOptions.

        创建裸机实例的元数据。  可以通过元数据自定义键值对。   说明： 如果元数据中包含了敏感数据，您应当采取适当的措施来保护敏感数据，比如限制访问范围、加密等。 最多可注入10对键值（Key/Value）。 主键（Key）只能由大写字母（A-Z）、小写字母（a-z）、数字（0-9）、中划线（-）、下划线（_）、冒号（:）、空格（ ）和小数点（.）组成，长度为[1-255]个字符。     值（value）最大长度为255个字符。

        :param metadata: The metadata of this RunInstancesOptions.
        :type metadata: dict(str, str)
        """
        self._metadata = metadata

    @property
    def description(self):
        r"""Gets the description of this RunInstancesOptions.

        裸机实例的描述信息，默认为空字符串。

        :return: The description of this RunInstancesOptions.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this RunInstancesOptions.

        裸机实例的描述信息，默认为空字符串。

        :param description: The description of this RunInstancesOptions.
        :type description: str
        """
        self._description = description

    @property
    def placement(self):
        r"""Gets the placement of this RunInstancesOptions.

        :return: The placement of this RunInstancesOptions.
        :rtype: :class:`huaweicloudsdkclouddc.v1.RunInstancesOptionsPlacement`
        """
        return self._placement

    @placement.setter
    def placement(self, placement):
        r"""Sets the placement of this RunInstancesOptions.

        :param placement: The placement of this RunInstancesOptions.
        :type placement: :class:`huaweicloudsdkclouddc.v1.RunInstancesOptionsPlacement`
        """
        self._placement = placement

    @property
    def min_count(self):
        r"""Gets the min_count of this RunInstancesOptions.

        必须成功启动的最小实例数量。如果无法满足此数量，整个请求失败（不会启动任何实例）。

        :return: The min_count of this RunInstancesOptions.
        :rtype: int
        """
        return self._min_count

    @min_count.setter
    def min_count(self, min_count):
        r"""Sets the min_count of this RunInstancesOptions.

        必须成功启动的最小实例数量。如果无法满足此数量，整个请求失败（不会启动任何实例）。

        :param min_count: The min_count of this RunInstancesOptions.
        :type min_count: int
        """
        self._min_count = min_count

    @property
    def max_count(self):
        r"""Gets the max_count of this RunInstancesOptions.

        允许启动的最大实例数量。尝试启动最多该数量的实例，但实际启动数可能介于 min_count 和 max_count 之间

        :return: The max_count of this RunInstancesOptions.
        :rtype: int
        """
        return self._max_count

    @max_count.setter
    def max_count(self, max_count):
        r"""Sets the max_count of this RunInstancesOptions.

        允许启动的最大实例数量。尝试启动最多该数量的实例，但实际启动数可能介于 min_count 和 max_count 之间

        :param max_count: The max_count of this RunInstancesOptions.
        :type max_count: int
        """
        self._max_count = max_count

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
        if not isinstance(other, RunInstancesOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
