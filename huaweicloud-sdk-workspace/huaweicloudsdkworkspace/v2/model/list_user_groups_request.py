# coding: utf-8

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
        'keyword': 'str',
        'domain': 'str',
        'platform_type': 'list[str]'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'keyword': 'keyword',
        'domain': 'domain',
        'platform_type': 'platform_type'
    }

    def __init__(self, limit=None, offset=None, keyword=None, domain=None, platform_type=None):
        r"""ListUserGroupsRequest

        The model defined in huaweicloud sdk

        :param limit: 用于分页查询，返回用户组数量限制。如果不指定或为0，则使用默认值100，从1开始，最大100。
        :type limit: str
        :param offset: 用于分页查询，查询的起始记录序号，从0开始，默认值0，必须与limit同时使用。
        :type offset: str
        :param keyword: 用来匹配用户组的搜索关键字。例如根据组名模糊查询。
        :type keyword: str
        :param domain: 根据用户组的域名进行过滤。
        :type domain: str
        :param platform_type: 用户类型。 * AD： AD域用户 * LOCAL： 本地liteAs用户 * UOS： UOS域用户
        :type platform_type: list[str]
        """
        
        

        self._limit = None
        self._offset = None
        self._keyword = None
        self._domain = None
        self._platform_type = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if keyword is not None:
            self.keyword = keyword
        if domain is not None:
            self.domain = domain
        if platform_type is not None:
            self.platform_type = platform_type

    @property
    def limit(self):
        r"""Gets the limit of this ListUserGroupsRequest.

        用于分页查询，返回用户组数量限制。如果不指定或为0，则使用默认值100，从1开始，最大100。

        :return: The limit of this ListUserGroupsRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListUserGroupsRequest.

        用于分页查询，返回用户组数量限制。如果不指定或为0，则使用默认值100，从1开始，最大100。

        :param limit: The limit of this ListUserGroupsRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListUserGroupsRequest.

        用于分页查询，查询的起始记录序号，从0开始，默认值0，必须与limit同时使用。

        :return: The offset of this ListUserGroupsRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListUserGroupsRequest.

        用于分页查询，查询的起始记录序号，从0开始，默认值0，必须与limit同时使用。

        :param offset: The offset of this ListUserGroupsRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def keyword(self):
        r"""Gets the keyword of this ListUserGroupsRequest.

        用来匹配用户组的搜索关键字。例如根据组名模糊查询。

        :return: The keyword of this ListUserGroupsRequest.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        r"""Sets the keyword of this ListUserGroupsRequest.

        用来匹配用户组的搜索关键字。例如根据组名模糊查询。

        :param keyword: The keyword of this ListUserGroupsRequest.
        :type keyword: str
        """
        self._keyword = keyword

    @property
    def domain(self):
        r"""Gets the domain of this ListUserGroupsRequest.

        根据用户组的域名进行过滤。

        :return: The domain of this ListUserGroupsRequest.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this ListUserGroupsRequest.

        根据用户组的域名进行过滤。

        :param domain: The domain of this ListUserGroupsRequest.
        :type domain: str
        """
        self._domain = domain

    @property
    def platform_type(self):
        r"""Gets the platform_type of this ListUserGroupsRequest.

        用户类型。 * AD： AD域用户 * LOCAL： 本地liteAs用户 * UOS： UOS域用户

        :return: The platform_type of this ListUserGroupsRequest.
        :rtype: list[str]
        """
        return self._platform_type

    @platform_type.setter
    def platform_type(self, platform_type):
        r"""Sets the platform_type of this ListUserGroupsRequest.

        用户类型。 * AD： AD域用户 * LOCAL： 本地liteAs用户 * UOS： UOS域用户

        :param platform_type: The platform_type of this ListUserGroupsRequest.
        :type platform_type: list[str]
        """
        self._platform_type = platform_type

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
        if not isinstance(other, ListUserGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
