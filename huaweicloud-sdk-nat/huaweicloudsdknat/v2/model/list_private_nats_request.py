# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPrivateNatsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'marker': 'str',
        'page_reverse': 'bool',
        'id': 'list[str]',
        'name': 'list[str]',
        'description': 'list[str]',
        'spec': 'list[str]',
        'status': 'list[str]',
        'vpc_id': 'list[str]',
        'virsubnet_id': 'list[str]',
        'enterprise_project_id': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'marker': 'marker',
        'page_reverse': 'page_reverse',
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'spec': 'spec',
        'status': 'status',
        'vpc_id': 'vpc_id',
        'virsubnet_id': 'virsubnet_id',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, limit=None, marker=None, page_reverse=None, id=None, name=None, description=None, spec=None, status=None, vpc_id=None, virsubnet_id=None, enterprise_project_id=None):
        r"""ListPrivateNatsRequest

        The model defined in huaweicloud sdk

        :param limit: 功能说明：每页返回的个数。 取值范围：0~2000。 默认值：2000。
        :type limit: int
        :param marker: 功能说明：分页查询起始的资源ID，为空时查询第一页。 值从上一次查询的PageInfo中的next_marker或者previous_marker中获取。
        :type marker: str
        :param page_reverse: 是否查询前一页。
        :type page_reverse: bool
        :param id: 私网NAT网关实例的ID。
        :type id: list[str]
        :param name: 私网NAT网关实例的名字。
        :type name: list[str]
        :param description: 私网NAT网关实例的描述。长度范围小于等于255个字符，不能包含“&lt;”和“&gt;”。
        :type description: list[str]
        :param spec: 私网NAT网关实例的规格。 取值为： \&quot;Small\&quot;：小型 \&quot;Medium\&quot;：中型 \&quot;Large\&quot;：大型 \&quot;Extra-large\&quot;：超大型
        :type spec: list[str]
        :param status: 私网NAT网关实例的状态。 取值为： \&quot;ACTIVE\&quot;：正常运行 \&quot;FROZEN\&quot;：冻结
        :type status: list[str]
        :param vpc_id: 私网NAT网关实例所属VPC的ID。
        :type vpc_id: list[str]
        :param virsubnet_id: 私网NAT网关实例所属子网的ID。
        :type virsubnet_id: list[str]
        :param enterprise_project_id: 企业项目ID。创建私网NAT网关实例时，关联的企业项目ID。
        :type enterprise_project_id: list[str]
        """
        
        

        self._limit = None
        self._marker = None
        self._page_reverse = None
        self._id = None
        self._name = None
        self._description = None
        self._spec = None
        self._status = None
        self._vpc_id = None
        self._virsubnet_id = None
        self._enterprise_project_id = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if page_reverse is not None:
            self.page_reverse = page_reverse
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if spec is not None:
            self.spec = spec
        if status is not None:
            self.status = status
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if virsubnet_id is not None:
            self.virsubnet_id = virsubnet_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def limit(self):
        r"""Gets the limit of this ListPrivateNatsRequest.

        功能说明：每页返回的个数。 取值范围：0~2000。 默认值：2000。

        :return: The limit of this ListPrivateNatsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPrivateNatsRequest.

        功能说明：每页返回的个数。 取值范围：0~2000。 默认值：2000。

        :param limit: The limit of this ListPrivateNatsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListPrivateNatsRequest.

        功能说明：分页查询起始的资源ID，为空时查询第一页。 值从上一次查询的PageInfo中的next_marker或者previous_marker中获取。

        :return: The marker of this ListPrivateNatsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListPrivateNatsRequest.

        功能说明：分页查询起始的资源ID，为空时查询第一页。 值从上一次查询的PageInfo中的next_marker或者previous_marker中获取。

        :param marker: The marker of this ListPrivateNatsRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        r"""Gets the page_reverse of this ListPrivateNatsRequest.

        是否查询前一页。

        :return: The page_reverse of this ListPrivateNatsRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        r"""Sets the page_reverse of this ListPrivateNatsRequest.

        是否查询前一页。

        :param page_reverse: The page_reverse of this ListPrivateNatsRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

    @property
    def id(self):
        r"""Gets the id of this ListPrivateNatsRequest.

        私网NAT网关实例的ID。

        :return: The id of this ListPrivateNatsRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListPrivateNatsRequest.

        私网NAT网关实例的ID。

        :param id: The id of this ListPrivateNatsRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListPrivateNatsRequest.

        私网NAT网关实例的名字。

        :return: The name of this ListPrivateNatsRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListPrivateNatsRequest.

        私网NAT网关实例的名字。

        :param name: The name of this ListPrivateNatsRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ListPrivateNatsRequest.

        私网NAT网关实例的描述。长度范围小于等于255个字符，不能包含“<”和“>”。

        :return: The description of this ListPrivateNatsRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListPrivateNatsRequest.

        私网NAT网关实例的描述。长度范围小于等于255个字符，不能包含“<”和“>”。

        :param description: The description of this ListPrivateNatsRequest.
        :type description: list[str]
        """
        self._description = description

    @property
    def spec(self):
        r"""Gets the spec of this ListPrivateNatsRequest.

        私网NAT网关实例的规格。 取值为： \"Small\"：小型 \"Medium\"：中型 \"Large\"：大型 \"Extra-large\"：超大型

        :return: The spec of this ListPrivateNatsRequest.
        :rtype: list[str]
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this ListPrivateNatsRequest.

        私网NAT网关实例的规格。 取值为： \"Small\"：小型 \"Medium\"：中型 \"Large\"：大型 \"Extra-large\"：超大型

        :param spec: The spec of this ListPrivateNatsRequest.
        :type spec: list[str]
        """
        self._spec = spec

    @property
    def status(self):
        r"""Gets the status of this ListPrivateNatsRequest.

        私网NAT网关实例的状态。 取值为： \"ACTIVE\"：正常运行 \"FROZEN\"：冻结

        :return: The status of this ListPrivateNatsRequest.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListPrivateNatsRequest.

        私网NAT网关实例的状态。 取值为： \"ACTIVE\"：正常运行 \"FROZEN\"：冻结

        :param status: The status of this ListPrivateNatsRequest.
        :type status: list[str]
        """
        self._status = status

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ListPrivateNatsRequest.

        私网NAT网关实例所属VPC的ID。

        :return: The vpc_id of this ListPrivateNatsRequest.
        :rtype: list[str]
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ListPrivateNatsRequest.

        私网NAT网关实例所属VPC的ID。

        :param vpc_id: The vpc_id of this ListPrivateNatsRequest.
        :type vpc_id: list[str]
        """
        self._vpc_id = vpc_id

    @property
    def virsubnet_id(self):
        r"""Gets the virsubnet_id of this ListPrivateNatsRequest.

        私网NAT网关实例所属子网的ID。

        :return: The virsubnet_id of this ListPrivateNatsRequest.
        :rtype: list[str]
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        r"""Sets the virsubnet_id of this ListPrivateNatsRequest.

        私网NAT网关实例所属子网的ID。

        :param virsubnet_id: The virsubnet_id of this ListPrivateNatsRequest.
        :type virsubnet_id: list[str]
        """
        self._virsubnet_id = virsubnet_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListPrivateNatsRequest.

        企业项目ID。创建私网NAT网关实例时，关联的企业项目ID。

        :return: The enterprise_project_id of this ListPrivateNatsRequest.
        :rtype: list[str]
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListPrivateNatsRequest.

        企业项目ID。创建私网NAT网关实例时，关联的企业项目ID。

        :param enterprise_project_id: The enterprise_project_id of this ListPrivateNatsRequest.
        :type enterprise_project_id: list[str]
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListPrivateNatsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
