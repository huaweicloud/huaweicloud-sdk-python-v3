# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryInstanceResponseBody:

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
        'name': 'str',
        'vpc_id': 'str',
        'network_interfaces': 'list[NetworkInterface]',
        'tags': 'list[Tag]',
        'image': 'Image',
        'description': 'str',
        'state': 'InstanceState',
        'metadata': 'dict(str, str)',
        'user_data': 'str',
        'server_id': 'str',
        'created_at': 'str',
        'updated_at': 'str',
        'launched_at': 'str',
        'error': 'ErrorStatus'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'vpc_id': 'vpc_id',
        'network_interfaces': 'network_interfaces',
        'tags': 'tags',
        'image': 'image',
        'description': 'description',
        'state': 'state',
        'metadata': 'metadata',
        'user_data': 'user_data',
        'server_id': 'server_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'launched_at': 'launched_at',
        'error': 'error'
    }

    def __init__(self, id=None, name=None, vpc_id=None, network_interfaces=None, tags=None, image=None, description=None, state=None, metadata=None, user_data=None, server_id=None, created_at=None, updated_at=None, launched_at=None, error=None):
        r"""QueryInstanceResponseBody

        The model defined in huaweicloud sdk

        :param id: UUID（Universally Unique Identifier）是一个 128 位的数字，通常以 32 个十六进制数字的形式表示，分为 5 组，用连字符分隔。具体格式如下：  xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx 其中：  每个 x 是一个十六进制数字（0-9 或 a-f）。 5 组的长度分别是：8 位、4 位、4 位、4 位 和 12 位。 为了匹配这种格式的 UUID，可以使用以下正则表达式：  regex ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
        :type id: str
        :param name: instance name
        :type name: str
        :param vpc_id: VPC ID
        :type vpc_id: str
        :param network_interfaces: 指定裸机实例的网卡信息。  约束：  一个裸机实例最多挂载2个网卡，参数中第一个网卡会作为裸机实例的主网卡。若用户指定了多组网卡参数，需保证各组参数都属于同一VPC。
        :type network_interfaces: list[:class:`huaweicloudsdkclouddc.v1.NetworkInterface`]
        :param tags: 标签
        :type tags: list[:class:`huaweicloudsdkclouddc.v1.Tag`]
        :param image: 
        :type image: :class:`huaweicloudsdkclouddc.v1.Image`
        :param description: 云服务器描述信息，默认为空字符串。
        :type description: str
        :param state: 
        :type state: :class:`huaweicloudsdkclouddc.v1.InstanceState`
        :param metadata: 创建裸机实例的元数据。  可以通过元数据自定义键值对。   说明： 如果元数据中包含了敏感数据，您应当采取适当的措施来保护敏感数据，比如限制访问范围、加密等。 最多可注入10对键值（Key/Value）。 主键（Key）只能由大写字母（A-Z）、小写字母（a-z）、数字（0-9）、中划线（-）、下划线（_）、冒号（:）、空格（ ）和小数点（.）组成，长度为[1-255]个字符。     值（value）最大长度为255个字符。
        :type metadata: dict(str, str)
        :param user_data: 创建实例过程中待注入实例自定义数据。支持注入文本、文本文件。   说明： user_data的值为base64编码之后的内容。 注入内容（编码之前的内容）最大长度为32K。
        :type user_data: str
        :param server_id: UUID（Universally Unique Identifier）是一个 128 位的数字，通常以 32 个十六进制数字的形式表示，分为 5 组，用连字符分隔。具体格式如下：  xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx 其中：  每个 x 是一个十六进制数字（0-9 或 a-f）。 5 组的长度分别是：8 位、4 位、4 位、4 位 和 12 位。 为了匹配这种格式的 UUID，可以使用以下正则表达式：  regex ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$
        :type server_id: str
        :param created_at: 创建时间
        :type created_at: str
        :param updated_at: 更新时间
        :type updated_at: str
        :param launched_at: 启动时间
        :type launched_at: str
        :param error: 
        :type error: :class:`huaweicloudsdkclouddc.v1.ErrorStatus`
        """
        
        

        self._id = None
        self._name = None
        self._vpc_id = None
        self._network_interfaces = None
        self._tags = None
        self._image = None
        self._description = None
        self._state = None
        self._metadata = None
        self._user_data = None
        self._server_id = None
        self._created_at = None
        self._updated_at = None
        self._launched_at = None
        self._error = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.vpc_id = vpc_id
        if network_interfaces is not None:
            self.network_interfaces = network_interfaces
        self.tags = tags
        self.image = image
        if description is not None:
            self.description = description
        self.state = state
        if metadata is not None:
            self.metadata = metadata
        if user_data is not None:
            self.user_data = user_data
        self.server_id = server_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.launched_at = launched_at
        if error is not None:
            self.error = error

    @property
    def id(self):
        r"""Gets the id of this QueryInstanceResponseBody.

        UUID（Universally Unique Identifier）是一个 128 位的数字，通常以 32 个十六进制数字的形式表示，分为 5 组，用连字符分隔。具体格式如下：  xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx 其中：  每个 x 是一个十六进制数字（0-9 或 a-f）。 5 组的长度分别是：8 位、4 位、4 位、4 位 和 12 位。 为了匹配这种格式的 UUID，可以使用以下正则表达式：  regex ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$

        :return: The id of this QueryInstanceResponseBody.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this QueryInstanceResponseBody.

        UUID（Universally Unique Identifier）是一个 128 位的数字，通常以 32 个十六进制数字的形式表示，分为 5 组，用连字符分隔。具体格式如下：  xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx 其中：  每个 x 是一个十六进制数字（0-9 或 a-f）。 5 组的长度分别是：8 位、4 位、4 位、4 位 和 12 位。 为了匹配这种格式的 UUID，可以使用以下正则表达式：  regex ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$

        :param id: The id of this QueryInstanceResponseBody.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this QueryInstanceResponseBody.

        instance name

        :return: The name of this QueryInstanceResponseBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this QueryInstanceResponseBody.

        instance name

        :param name: The name of this QueryInstanceResponseBody.
        :type name: str
        """
        self._name = name

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this QueryInstanceResponseBody.

        VPC ID

        :return: The vpc_id of this QueryInstanceResponseBody.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this QueryInstanceResponseBody.

        VPC ID

        :param vpc_id: The vpc_id of this QueryInstanceResponseBody.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def network_interfaces(self):
        r"""Gets the network_interfaces of this QueryInstanceResponseBody.

        指定裸机实例的网卡信息。  约束：  一个裸机实例最多挂载2个网卡，参数中第一个网卡会作为裸机实例的主网卡。若用户指定了多组网卡参数，需保证各组参数都属于同一VPC。

        :return: The network_interfaces of this QueryInstanceResponseBody.
        :rtype: list[:class:`huaweicloudsdkclouddc.v1.NetworkInterface`]
        """
        return self._network_interfaces

    @network_interfaces.setter
    def network_interfaces(self, network_interfaces):
        r"""Sets the network_interfaces of this QueryInstanceResponseBody.

        指定裸机实例的网卡信息。  约束：  一个裸机实例最多挂载2个网卡，参数中第一个网卡会作为裸机实例的主网卡。若用户指定了多组网卡参数，需保证各组参数都属于同一VPC。

        :param network_interfaces: The network_interfaces of this QueryInstanceResponseBody.
        :type network_interfaces: list[:class:`huaweicloudsdkclouddc.v1.NetworkInterface`]
        """
        self._network_interfaces = network_interfaces

    @property
    def tags(self):
        r"""Gets the tags of this QueryInstanceResponseBody.

        标签

        :return: The tags of this QueryInstanceResponseBody.
        :rtype: list[:class:`huaweicloudsdkclouddc.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this QueryInstanceResponseBody.

        标签

        :param tags: The tags of this QueryInstanceResponseBody.
        :type tags: list[:class:`huaweicloudsdkclouddc.v1.Tag`]
        """
        self._tags = tags

    @property
    def image(self):
        r"""Gets the image of this QueryInstanceResponseBody.

        :return: The image of this QueryInstanceResponseBody.
        :rtype: :class:`huaweicloudsdkclouddc.v1.Image`
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this QueryInstanceResponseBody.

        :param image: The image of this QueryInstanceResponseBody.
        :type image: :class:`huaweicloudsdkclouddc.v1.Image`
        """
        self._image = image

    @property
    def description(self):
        r"""Gets the description of this QueryInstanceResponseBody.

        云服务器描述信息，默认为空字符串。

        :return: The description of this QueryInstanceResponseBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this QueryInstanceResponseBody.

        云服务器描述信息，默认为空字符串。

        :param description: The description of this QueryInstanceResponseBody.
        :type description: str
        """
        self._description = description

    @property
    def state(self):
        r"""Gets the state of this QueryInstanceResponseBody.

        :return: The state of this QueryInstanceResponseBody.
        :rtype: :class:`huaweicloudsdkclouddc.v1.InstanceState`
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this QueryInstanceResponseBody.

        :param state: The state of this QueryInstanceResponseBody.
        :type state: :class:`huaweicloudsdkclouddc.v1.InstanceState`
        """
        self._state = state

    @property
    def metadata(self):
        r"""Gets the metadata of this QueryInstanceResponseBody.

        创建裸机实例的元数据。  可以通过元数据自定义键值对。   说明： 如果元数据中包含了敏感数据，您应当采取适当的措施来保护敏感数据，比如限制访问范围、加密等。 最多可注入10对键值（Key/Value）。 主键（Key）只能由大写字母（A-Z）、小写字母（a-z）、数字（0-9）、中划线（-）、下划线（_）、冒号（:）、空格（ ）和小数点（.）组成，长度为[1-255]个字符。     值（value）最大长度为255个字符。

        :return: The metadata of this QueryInstanceResponseBody.
        :rtype: dict(str, str)
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this QueryInstanceResponseBody.

        创建裸机实例的元数据。  可以通过元数据自定义键值对。   说明： 如果元数据中包含了敏感数据，您应当采取适当的措施来保护敏感数据，比如限制访问范围、加密等。 最多可注入10对键值（Key/Value）。 主键（Key）只能由大写字母（A-Z）、小写字母（a-z）、数字（0-9）、中划线（-）、下划线（_）、冒号（:）、空格（ ）和小数点（.）组成，长度为[1-255]个字符。     值（value）最大长度为255个字符。

        :param metadata: The metadata of this QueryInstanceResponseBody.
        :type metadata: dict(str, str)
        """
        self._metadata = metadata

    @property
    def user_data(self):
        r"""Gets the user_data of this QueryInstanceResponseBody.

        创建实例过程中待注入实例自定义数据。支持注入文本、文本文件。   说明： user_data的值为base64编码之后的内容。 注入内容（编码之前的内容）最大长度为32K。

        :return: The user_data of this QueryInstanceResponseBody.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        r"""Sets the user_data of this QueryInstanceResponseBody.

        创建实例过程中待注入实例自定义数据。支持注入文本、文本文件。   说明： user_data的值为base64编码之后的内容。 注入内容（编码之前的内容）最大长度为32K。

        :param user_data: The user_data of this QueryInstanceResponseBody.
        :type user_data: str
        """
        self._user_data = user_data

    @property
    def server_id(self):
        r"""Gets the server_id of this QueryInstanceResponseBody.

        UUID（Universally Unique Identifier）是一个 128 位的数字，通常以 32 个十六进制数字的形式表示，分为 5 组，用连字符分隔。具体格式如下：  xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx 其中：  每个 x 是一个十六进制数字（0-9 或 a-f）。 5 组的长度分别是：8 位、4 位、4 位、4 位 和 12 位。 为了匹配这种格式的 UUID，可以使用以下正则表达式：  regex ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$

        :return: The server_id of this QueryInstanceResponseBody.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this QueryInstanceResponseBody.

        UUID（Universally Unique Identifier）是一个 128 位的数字，通常以 32 个十六进制数字的形式表示，分为 5 组，用连字符分隔。具体格式如下：  xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx 其中：  每个 x 是一个十六进制数字（0-9 或 a-f）。 5 组的长度分别是：8 位、4 位、4 位、4 位 和 12 位。 为了匹配这种格式的 UUID，可以使用以下正则表达式：  regex ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$

        :param server_id: The server_id of this QueryInstanceResponseBody.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def created_at(self):
        r"""Gets the created_at of this QueryInstanceResponseBody.

        创建时间

        :return: The created_at of this QueryInstanceResponseBody.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this QueryInstanceResponseBody.

        创建时间

        :param created_at: The created_at of this QueryInstanceResponseBody.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this QueryInstanceResponseBody.

        更新时间

        :return: The updated_at of this QueryInstanceResponseBody.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this QueryInstanceResponseBody.

        更新时间

        :param updated_at: The updated_at of this QueryInstanceResponseBody.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def launched_at(self):
        r"""Gets the launched_at of this QueryInstanceResponseBody.

        启动时间

        :return: The launched_at of this QueryInstanceResponseBody.
        :rtype: str
        """
        return self._launched_at

    @launched_at.setter
    def launched_at(self, launched_at):
        r"""Sets the launched_at of this QueryInstanceResponseBody.

        启动时间

        :param launched_at: The launched_at of this QueryInstanceResponseBody.
        :type launched_at: str
        """
        self._launched_at = launched_at

    @property
    def error(self):
        r"""Gets the error of this QueryInstanceResponseBody.

        :return: The error of this QueryInstanceResponseBody.
        :rtype: :class:`huaweicloudsdkclouddc.v1.ErrorStatus`
        """
        return self._error

    @error.setter
    def error(self, error):
        r"""Sets the error of this QueryInstanceResponseBody.

        :param error: The error of this QueryInstanceResponseBody.
        :type error: :class:`huaweicloudsdkclouddc.v1.ErrorStatus`
        """
        self._error = error

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
        if not isinstance(other, QueryInstanceResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
