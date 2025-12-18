# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProjectProtectedRefsUserGroupsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'search': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'offset': 'offset',
        'limit': 'limit',
        'search': 'search'
    }

    def __init__(self, project_id=None, offset=None, limit=None, search=None):
        r"""ListProjectProtectedRefsUserGroupsRequest

        The model defined in huaweicloud sdk

        :param project_id: **参数解释：** 项目的32位uuid，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/en-us/api-projectman/ListProjectsV4.html)](tag:hws_hk)[[查询项目列表](https://support.huaweicloud.com/eu/api-projectman/ListProjectsV4.html)](tag:hws_eu)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **取值范围：** 字符串长度32。
        :type project_id: str
        :param offset: **参数解释：** 偏移量，从0开始。
        :type offset: int
        :param limit: **参数解释：** 返回数量。
        :type limit: int
        :param search: **参数解释：** 查询关键字，可模糊匹配用户名称、用户昵称、租户名称。
        :type search: str
        """
        
        

        self._project_id = None
        self._offset = None
        self._limit = None
        self._search = None
        self.discriminator = None

        self.project_id = project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if search is not None:
            self.search = search

    @property
    def project_id(self):
        r"""Gets the project_id of this ListProjectProtectedRefsUserGroupsRequest.

        **参数解释：** 项目的32位uuid，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/en-us/api-projectman/ListProjectsV4.html)](tag:hws_hk)[[查询项目列表](https://support.huaweicloud.com/eu/api-projectman/ListProjectsV4.html)](tag:hws_eu)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **取值范围：** 字符串长度32。

        :return: The project_id of this ListProjectProtectedRefsUserGroupsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListProjectProtectedRefsUserGroupsRequest.

        **参数解释：** 项目的32位uuid，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/en-us/api-projectman/ListProjectsV4.html)](tag:hws_hk)[[查询项目列表](https://support.huaweicloud.com/eu/api-projectman/ListProjectsV4.html)](tag:hws_eu)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **取值范围：** 字符串长度32。

        :param project_id: The project_id of this ListProjectProtectedRefsUserGroupsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListProjectProtectedRefsUserGroupsRequest.

        **参数解释：** 偏移量，从0开始。

        :return: The offset of this ListProjectProtectedRefsUserGroupsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListProjectProtectedRefsUserGroupsRequest.

        **参数解释：** 偏移量，从0开始。

        :param offset: The offset of this ListProjectProtectedRefsUserGroupsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListProjectProtectedRefsUserGroupsRequest.

        **参数解释：** 返回数量。

        :return: The limit of this ListProjectProtectedRefsUserGroupsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListProjectProtectedRefsUserGroupsRequest.

        **参数解释：** 返回数量。

        :param limit: The limit of this ListProjectProtectedRefsUserGroupsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def search(self):
        r"""Gets the search of this ListProjectProtectedRefsUserGroupsRequest.

        **参数解释：** 查询关键字，可模糊匹配用户名称、用户昵称、租户名称。

        :return: The search of this ListProjectProtectedRefsUserGroupsRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        r"""Sets the search of this ListProjectProtectedRefsUserGroupsRequest.

        **参数解释：** 查询关键字，可模糊匹配用户名称、用户昵称、租户名称。

        :param search: The search of this ListProjectProtectedRefsUserGroupsRequest.
        :type search: str
        """
        self._search = search

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
        if not isinstance(other, ListProjectProtectedRefsUserGroupsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
