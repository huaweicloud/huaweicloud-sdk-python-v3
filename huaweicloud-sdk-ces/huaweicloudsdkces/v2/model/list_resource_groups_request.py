# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResourceGroupsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'group_name': 'str',
        'group_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'type': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'group_name': 'group_name',
        'group_id': 'group_id',
        'offset': 'offset',
        'limit': 'limit',
        'type': 'type'
    }

    def __init__(self, enterprise_project_id=None, group_name=None, group_id=None, offset=None, limit=None, type=None):
        """ListResourceGroupsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 归属企业项目ID
        :type enterprise_project_id: str
        :param group_name: 资源分组名称，支持模糊查询
        :type group_name: str
        :param group_id: 资源分组ID，以rg开头，后跟22位由字母或数字组成的字符串
        :type group_id: str
        :param offset: 分页查询时查询的起始位置，表示从第几条数据开始，默认为0
        :type offset: int
        :param limit: 分页查询时每页的条目数，取值[1,100]，默认值为100
        :type limit: int
        :param type: 资源分组添加资源方式，取值只能为EPS（同步企业项目）,TAG（标签动态匹配）,Manual（手动添加），不传代表查询所有资源分组类型
        :type type: str
        """
        
        

        self._enterprise_project_id = None
        self._group_name = None
        self._group_id = None
        self._offset = None
        self._limit = None
        self._type = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if group_name is not None:
            self.group_name = group_name
        if group_id is not None:
            self.group_id = group_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if type is not None:
            self.type = type

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListResourceGroupsRequest.

        归属企业项目ID

        :return: The enterprise_project_id of this ListResourceGroupsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListResourceGroupsRequest.

        归属企业项目ID

        :param enterprise_project_id: The enterprise_project_id of this ListResourceGroupsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def group_name(self):
        """Gets the group_name of this ListResourceGroupsRequest.

        资源分组名称，支持模糊查询

        :return: The group_name of this ListResourceGroupsRequest.
        :rtype: str
        """
        return self._group_name

    @group_name.setter
    def group_name(self, group_name):
        """Sets the group_name of this ListResourceGroupsRequest.

        资源分组名称，支持模糊查询

        :param group_name: The group_name of this ListResourceGroupsRequest.
        :type group_name: str
        """
        self._group_name = group_name

    @property
    def group_id(self):
        """Gets the group_id of this ListResourceGroupsRequest.

        资源分组ID，以rg开头，后跟22位由字母或数字组成的字符串

        :return: The group_id of this ListResourceGroupsRequest.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ListResourceGroupsRequest.

        资源分组ID，以rg开头，后跟22位由字母或数字组成的字符串

        :param group_id: The group_id of this ListResourceGroupsRequest.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def offset(self):
        """Gets the offset of this ListResourceGroupsRequest.

        分页查询时查询的起始位置，表示从第几条数据开始，默认为0

        :return: The offset of this ListResourceGroupsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListResourceGroupsRequest.

        分页查询时查询的起始位置，表示从第几条数据开始，默认为0

        :param offset: The offset of this ListResourceGroupsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListResourceGroupsRequest.

        分页查询时每页的条目数，取值[1,100]，默认值为100

        :return: The limit of this ListResourceGroupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListResourceGroupsRequest.

        分页查询时每页的条目数，取值[1,100]，默认值为100

        :param limit: The limit of this ListResourceGroupsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def type(self):
        """Gets the type of this ListResourceGroupsRequest.

        资源分组添加资源方式，取值只能为EPS（同步企业项目）,TAG（标签动态匹配）,Manual（手动添加），不传代表查询所有资源分组类型

        :return: The type of this ListResourceGroupsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ListResourceGroupsRequest.

        资源分组添加资源方式，取值只能为EPS（同步企业项目）,TAG（标签动态匹配）,Manual（手动添加），不传代表查询所有资源分组类型

        :param type: The type of this ListResourceGroupsRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ListResourceGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
