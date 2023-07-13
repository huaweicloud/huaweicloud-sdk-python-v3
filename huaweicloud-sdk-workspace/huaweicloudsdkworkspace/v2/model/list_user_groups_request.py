# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListUserGroupsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'str',
        'offset': 'str',
        'keyword': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'keyword': 'keyword'
    }

    def __init__(self, limit=None, offset=None, keyword=None):
        """ListUserGroupsRequest

        The model defined in huaweicloud sdk

        :param limit: 用于分页查询，返回用户组数量限制。如果不指定或为0，则使用默认值100，从1开始，最大100。
        :type limit: str
        :param offset: 用于分页查询，查询的起始记录序号，从0开始，默认值0，必须与limit同时使用。
        :type offset: str
        :param keyword: 用来匹配用户组的搜索关键字。例如根据组名模糊查询。
        :type keyword: str
        """
        
        

        self._limit = None
        self._offset = None
        self._keyword = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if keyword is not None:
            self.keyword = keyword

    @property
    def limit(self):
        """Gets the limit of this ListUserGroupsRequest.

        用于分页查询，返回用户组数量限制。如果不指定或为0，则使用默认值100，从1开始，最大100。

        :return: The limit of this ListUserGroupsRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListUserGroupsRequest.

        用于分页查询，返回用户组数量限制。如果不指定或为0，则使用默认值100，从1开始，最大100。

        :param limit: The limit of this ListUserGroupsRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListUserGroupsRequest.

        用于分页查询，查询的起始记录序号，从0开始，默认值0，必须与limit同时使用。

        :return: The offset of this ListUserGroupsRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListUserGroupsRequest.

        用于分页查询，查询的起始记录序号，从0开始，默认值0，必须与limit同时使用。

        :param offset: The offset of this ListUserGroupsRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def keyword(self):
        """Gets the keyword of this ListUserGroupsRequest.

        用来匹配用户组的搜索关键字。例如根据组名模糊查询。

        :return: The keyword of this ListUserGroupsRequest.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        """Sets the keyword of this ListUserGroupsRequest.

        用来匹配用户组的搜索关键字。例如根据组名模糊查询。

        :param keyword: The keyword of this ListUserGroupsRequest.
        :type keyword: str
        """
        self._keyword = keyword

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
        if not isinstance(other, ListUserGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
