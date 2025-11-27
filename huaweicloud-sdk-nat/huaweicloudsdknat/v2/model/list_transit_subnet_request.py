# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTransitSubnetRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'list[str]',
        'name': 'list[str]',
        'description': 'list[str]',
        'virsubnet_project_id': 'list[str]',
        'vpc_id': 'list[str]',
        'virsubnet_id': 'list[str]',
        'status': 'list[str]',
        'limit': 'int',
        'marker': 'str',
        'page_reverse': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'virsubnet_project_id': 'virsubnet_project_id',
        'vpc_id': 'vpc_id',
        'virsubnet_id': 'virsubnet_id',
        'status': 'status',
        'limit': 'limit',
        'marker': 'marker',
        'page_reverse': 'page_reverse'
    }

    def __init__(self, id=None, name=None, description=None, virsubnet_project_id=None, vpc_id=None, virsubnet_id=None, status=None, limit=None, marker=None, page_reverse=None):
        r"""ListTransitSubnetRequest

        The model defined in huaweicloud sdk

        :param id: 中转子网的ID
        :type id: list[str]
        :param name: 中转子网的名字
        :type name: list[str]
        :param description: 中转子网的描述
        :type description: list[str]
        :param virsubnet_project_id: 中转子网的子网所属项目的ID
        :type virsubnet_project_id: list[str]
        :param vpc_id: 中转子网的子网所属的VPC的ID
        :type vpc_id: list[str]
        :param virsubnet_id: 中转子网的子网ID
        :type virsubnet_id: list[str]
        :param status: 中转子网状态。 取值范围： ACTIVE： 当前资源状态正常。 INACTIVE： 不可用。
        :type status: list[str]
        :param limit: 功能说明：每页返回的个数。 取值范围：1~2000。 默认值：2000
        :type limit: int
        :param marker: 功能说明：分页查询起始的资源ID，为空时查询第一页。 值从上一次查询的PageInfo中的next_marker或者previous_marker中获取
        :type marker: str
        :param page_reverse: 是否查询前一页
        :type page_reverse: bool
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._virsubnet_project_id = None
        self._vpc_id = None
        self._virsubnet_id = None
        self._status = None
        self._limit = None
        self._marker = None
        self._page_reverse = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if virsubnet_project_id is not None:
            self.virsubnet_project_id = virsubnet_project_id
        if vpc_id is not None:
            self.vpc_id = vpc_id
        if virsubnet_id is not None:
            self.virsubnet_id = virsubnet_id
        if status is not None:
            self.status = status
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if page_reverse is not None:
            self.page_reverse = page_reverse

    @property
    def id(self):
        r"""Gets the id of this ListTransitSubnetRequest.

        中转子网的ID

        :return: The id of this ListTransitSubnetRequest.
        :rtype: list[str]
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListTransitSubnetRequest.

        中转子网的ID

        :param id: The id of this ListTransitSubnetRequest.
        :type id: list[str]
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListTransitSubnetRequest.

        中转子网的名字

        :return: The name of this ListTransitSubnetRequest.
        :rtype: list[str]
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListTransitSubnetRequest.

        中转子网的名字

        :param name: The name of this ListTransitSubnetRequest.
        :type name: list[str]
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ListTransitSubnetRequest.

        中转子网的描述

        :return: The description of this ListTransitSubnetRequest.
        :rtype: list[str]
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListTransitSubnetRequest.

        中转子网的描述

        :param description: The description of this ListTransitSubnetRequest.
        :type description: list[str]
        """
        self._description = description

    @property
    def virsubnet_project_id(self):
        r"""Gets the virsubnet_project_id of this ListTransitSubnetRequest.

        中转子网的子网所属项目的ID

        :return: The virsubnet_project_id of this ListTransitSubnetRequest.
        :rtype: list[str]
        """
        return self._virsubnet_project_id

    @virsubnet_project_id.setter
    def virsubnet_project_id(self, virsubnet_project_id):
        r"""Sets the virsubnet_project_id of this ListTransitSubnetRequest.

        中转子网的子网所属项目的ID

        :param virsubnet_project_id: The virsubnet_project_id of this ListTransitSubnetRequest.
        :type virsubnet_project_id: list[str]
        """
        self._virsubnet_project_id = virsubnet_project_id

    @property
    def vpc_id(self):
        r"""Gets the vpc_id of this ListTransitSubnetRequest.

        中转子网的子网所属的VPC的ID

        :return: The vpc_id of this ListTransitSubnetRequest.
        :rtype: list[str]
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        r"""Sets the vpc_id of this ListTransitSubnetRequest.

        中转子网的子网所属的VPC的ID

        :param vpc_id: The vpc_id of this ListTransitSubnetRequest.
        :type vpc_id: list[str]
        """
        self._vpc_id = vpc_id

    @property
    def virsubnet_id(self):
        r"""Gets the virsubnet_id of this ListTransitSubnetRequest.

        中转子网的子网ID

        :return: The virsubnet_id of this ListTransitSubnetRequest.
        :rtype: list[str]
        """
        return self._virsubnet_id

    @virsubnet_id.setter
    def virsubnet_id(self, virsubnet_id):
        r"""Sets the virsubnet_id of this ListTransitSubnetRequest.

        中转子网的子网ID

        :param virsubnet_id: The virsubnet_id of this ListTransitSubnetRequest.
        :type virsubnet_id: list[str]
        """
        self._virsubnet_id = virsubnet_id

    @property
    def status(self):
        r"""Gets the status of this ListTransitSubnetRequest.

        中转子网状态。 取值范围： ACTIVE： 当前资源状态正常。 INACTIVE： 不可用。

        :return: The status of this ListTransitSubnetRequest.
        :rtype: list[str]
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListTransitSubnetRequest.

        中转子网状态。 取值范围： ACTIVE： 当前资源状态正常。 INACTIVE： 不可用。

        :param status: The status of this ListTransitSubnetRequest.
        :type status: list[str]
        """
        self._status = status

    @property
    def limit(self):
        r"""Gets the limit of this ListTransitSubnetRequest.

        功能说明：每页返回的个数。 取值范围：1~2000。 默认值：2000

        :return: The limit of this ListTransitSubnetRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTransitSubnetRequest.

        功能说明：每页返回的个数。 取值范围：1~2000。 默认值：2000

        :param limit: The limit of this ListTransitSubnetRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListTransitSubnetRequest.

        功能说明：分页查询起始的资源ID，为空时查询第一页。 值从上一次查询的PageInfo中的next_marker或者previous_marker中获取

        :return: The marker of this ListTransitSubnetRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListTransitSubnetRequest.

        功能说明：分页查询起始的资源ID，为空时查询第一页。 值从上一次查询的PageInfo中的next_marker或者previous_marker中获取

        :param marker: The marker of this ListTransitSubnetRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def page_reverse(self):
        r"""Gets the page_reverse of this ListTransitSubnetRequest.

        是否查询前一页

        :return: The page_reverse of this ListTransitSubnetRequest.
        :rtype: bool
        """
        return self._page_reverse

    @page_reverse.setter
    def page_reverse(self, page_reverse):
        r"""Sets the page_reverse of this ListTransitSubnetRequest.

        是否查询前一页

        :param page_reverse: The page_reverse of this ListTransitSubnetRequest.
        :type page_reverse: bool
        """
        self._page_reverse = page_reverse

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
        if not isinstance(other, ListTransitSubnetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
