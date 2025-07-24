# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Instance:

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
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'vpc_id': 'vpc_id',
        'network_interfaces': 'network_interfaces',
        'tags': 'tags',
        'image': 'image',
        'description': 'description'
    }

    def __init__(self, id=None, name=None, vpc_id=None, network_interfaces=None, tags=None, image=None, description=None):
        r"""Instance

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
        """
        
        

        self._id = None
        self._name = None
        self._vpc_id = None
        self._network_interfaces = None
        self._tags = None
        self._image = None
        self._description = None
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

    @property
    def id(self):
        r"""Gets the id of this Instance.

        UUID（Universally Unique Identifier）是一个 128 位的数字，通常以 32 个十六进制数字的形式表示，分为 5 组，用连字符分隔。具体格式如下：  xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx 其中：  每个 x 是一个十六进制数字（0-9 或 a-f）。 5 组的长度分别是：8 位、4 位、4 位、4 位 和 12 位。 为了匹配这种格式的 UUID，可以使用以下正则表达式：  regex ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$

        :return: The id of this Instance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Instance.

        UUID（Universally Unique Identifier）是一个 128 位的数字，通常以 32 个十六进制数字的形式表示，分为 5 组，用连字符分隔。具体格式如下：  xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx 其中：  每个 x 是一个十六进制数字（0-9 或 a-f）。 5 组的长度分别是：8 位、4 位、4 位、4 位 和 12 位。 为了匹配这种格式的 UUID，可以使用以下正则表达式：  regex ^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$

        :param id: The id of this Instance.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this Instance.

        instance name

        :return: The name of this Instance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Instance.

        instance name

        :param name: The name of this Instance.
        :type name: str
        """
        self._name = name

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this Instance.

        VPC ID

        :return: The vpc_id of this Instance.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this Instance.

        VPC ID

        :param vpc_id: The vpc_id of this Instance.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def network_interfaces(self):
        r"""Gets the network_interfaces of this Instance.

        指定裸机实例的网卡信息。  约束：  一个裸机实例最多挂载2个网卡，参数中第一个网卡会作为裸机实例的主网卡。若用户指定了多组网卡参数，需保证各组参数都属于同一VPC。

        :return: The network_interfaces of this Instance.
        :rtype: list[:class:`huaweicloudsdkclouddc.v1.NetworkInterface`]
        """
        return self._network_interfaces

    @network_interfaces.setter
    def network_interfaces(self, network_interfaces):
        r"""Sets the network_interfaces of this Instance.

        指定裸机实例的网卡信息。  约束：  一个裸机实例最多挂载2个网卡，参数中第一个网卡会作为裸机实例的主网卡。若用户指定了多组网卡参数，需保证各组参数都属于同一VPC。

        :param network_interfaces: The network_interfaces of this Instance.
        :type network_interfaces: list[:class:`huaweicloudsdkclouddc.v1.NetworkInterface`]
        """
        self._network_interfaces = network_interfaces

    @property
    def tags(self):
        r"""Gets the tags of this Instance.

        标签

        :return: The tags of this Instance.
        :rtype: list[:class:`huaweicloudsdkclouddc.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this Instance.

        标签

        :param tags: The tags of this Instance.
        :type tags: list[:class:`huaweicloudsdkclouddc.v1.Tag`]
        """
        self._tags = tags

    @property
    def image(self):
        r"""Gets the image of this Instance.

        :return: The image of this Instance.
        :rtype: :class:`huaweicloudsdkclouddc.v1.Image`
        """
        return self._image

    @image.setter
    def image(self, image):
        r"""Sets the image of this Instance.

        :param image: The image of this Instance.
        :type image: :class:`huaweicloudsdkclouddc.v1.Image`
        """
        self._image = image

    @property
    def description(self):
        r"""Gets the description of this Instance.

        云服务器描述信息，默认为空字符串。

        :return: The description of this Instance.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Instance.

        云服务器描述信息，默认为空字符串。

        :param description: The description of this Instance.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, Instance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
