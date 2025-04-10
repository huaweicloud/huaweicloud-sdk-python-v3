# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VpcAttachmentCreateRequest:

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
        'name': 'str',
        'virsubnet_id': 'str',
        'description': 'str',
        'auto_create_vpc_routes': 'bool',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'vpc_id': 'vpc_id',
        'name': 'name',
        'virsubnet_id': 'virsubnet_id',
        'description': 'description',
        'auto_create_vpc_routes': 'auto_create_vpc_routes',
        'tags': 'tags'
    }

    def __init__(self, vpc_id=None, name=None, virsubnet_id=None, description=None, auto_create_vpc_routes=None, tags=None):
        r"""VpcAttachmentCreateRequest

        The model defined in huaweicloud sdk

        :param vpc_id: VPC的id，取值范围：最大长度36字节，带“-”连字符的UUID格式
        :type vpc_id: str
        :param name: VPC连接名字，取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）
        :type name: str
        :param virsubnet_id: VPC子网id，取值范围：最大长度36字节，带“-”连字符的UUID格式
        :type virsubnet_id: str
        :param description: 描述信息，取值范围：0-255个字符，不能包含“&lt;”和“&gt;”
        :type description: str
        :param auto_create_vpc_routes: 默认为false，为true表示自动为vpc配置指向企业路由器的路由
        :type auto_create_vpc_routes: bool
        :param tags: 标签信息
        :type tags: list[:class:`huaweicloudsdker.v3.Tag`]
        """
        
        

        self._vpc_id = None
        self._name = None
        self._virsubnet_id = None
        self._description = None
        self._auto_create_vpc_routes = None
        self._tags = None
        self.discriminator = None

        self.vpc_id = vpc_id
        self.name = name
        self.virsubnet_id = virsubnet_id
        if description is not None:
            self.description = description
        if auto_create_vpc_routes is not None:
            self.auto_create_vpc_routes = auto_create_vpc_routes
        if tags is not None:
            self.tags = tags

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this VpcAttachmentCreateRequest.

        VPC的id，取值范围：最大长度36字节，带“-”连字符的UUID格式

        :return: The vpc_id of this VpcAttachmentCreateRequest.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this VpcAttachmentCreateRequest.

        VPC的id，取值范围：最大长度36字节，带“-”连字符的UUID格式

        :param vpc_id: The vpc_id of this VpcAttachmentCreateRequest.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def name(self):
        r"""Gets the name of this VpcAttachmentCreateRequest.

        VPC连接名字，取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :return: The name of this VpcAttachmentCreateRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this VpcAttachmentCreateRequest.

        VPC连接名字，取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）

        :param name: The name of this VpcAttachmentCreateRequest.
        :type name: str
        """
        self._name = name

    @property
    def virsubnet_id(self):
        r"""Gets the virsubnet_id of this VpcAttachmentCreateRequest.

        VPC子网id，取值范围：最大长度36字节，带“-”连字符的UUID格式

        :return: The virsubnet_id of this VpcAttachmentCreateRequest.
        :rtype: str
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        r"""Sets the virsubnet_id of this VpcAttachmentCreateRequest.

        VPC子网id，取值范围：最大长度36字节，带“-”连字符的UUID格式

        :param virsubnet_id: The virsubnet_id of this VpcAttachmentCreateRequest.
        :type virsubnet_id: str
        """
        self._virsubnet_id = virsubnet_id

    @property
    def description(self):
        r"""Gets the description of this VpcAttachmentCreateRequest.

        描述信息，取值范围：0-255个字符，不能包含“<”和“>”

        :return: The description of this VpcAttachmentCreateRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this VpcAttachmentCreateRequest.

        描述信息，取值范围：0-255个字符，不能包含“<”和“>”

        :param description: The description of this VpcAttachmentCreateRequest.
        :type description: str
        """
        self._description = description

    @property
    def auto_create_vpc_routes(self):
        r"""Gets the auto_create_vpc_routes of this VpcAttachmentCreateRequest.

        默认为false，为true表示自动为vpc配置指向企业路由器的路由

        :return: The auto_create_vpc_routes of this VpcAttachmentCreateRequest.
        :rtype: bool
        """
        return self._auto_create_vpc_routes

    @auto_create_vpc_routes.setter
    def auto_create_vpc_routes(self, auto_create_vpc_routes):
        r"""Sets the auto_create_vpc_routes of this VpcAttachmentCreateRequest.

        默认为false，为true表示自动为vpc配置指向企业路由器的路由

        :param auto_create_vpc_routes: The auto_create_vpc_routes of this VpcAttachmentCreateRequest.
        :type auto_create_vpc_routes: bool
        """
        self._auto_create_vpc_routes = auto_create_vpc_routes

    @property
    def tags(self):
        r"""Gets the tags of this VpcAttachmentCreateRequest.

        标签信息

        :return: The tags of this VpcAttachmentCreateRequest.
        :rtype: list[:class:`huaweicloudsdker.v3.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this VpcAttachmentCreateRequest.

        标签信息

        :param tags: The tags of this VpcAttachmentCreateRequest.
        :type tags: list[:class:`huaweicloudsdker.v3.Tag`]
        """
        self._tags = tags

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
        if not isinstance(other, VpcAttachmentCreateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
