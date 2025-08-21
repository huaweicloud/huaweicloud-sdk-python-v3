# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListProtectedTagsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repository_id': 'int',
        'offset': 'int',
        'limit': 'int',
        'search': 'str'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'offset': 'offset',
        'limit': 'limit',
        'search': 'search'
    }

    def __init__(self, repository_id=None, offset=None, limit=None, search=None):
        r"""ListProtectedTagsRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。
        :type repository_id: int
        :param offset: **参数解释：** 偏移量，从0开始。
        :type offset: int
        :param limit: **参数解释：** 返回数量。
        :type limit: int
        :param search: **参数解释：** 查询关键字，可模糊匹配保护Tag名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type search: str
        """
        
        

        self._repository_id = None
        self._offset = None
        self._limit = None
        self._search = None
        self.discriminator = None

        self.repository_id = repository_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if search is not None:
            self.search = search

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ListProtectedTagsRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :return: The repository_id of this ListProtectedTagsRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ListProtectedTagsRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :param repository_id: The repository_id of this ListProtectedTagsRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def offset(self):
        r"""Gets the offset of this ListProtectedTagsRequest.

        **参数解释：** 偏移量，从0开始。

        :return: The offset of this ListProtectedTagsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListProtectedTagsRequest.

        **参数解释：** 偏移量，从0开始。

        :param offset: The offset of this ListProtectedTagsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListProtectedTagsRequest.

        **参数解释：** 返回数量。

        :return: The limit of this ListProtectedTagsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListProtectedTagsRequest.

        **参数解释：** 返回数量。

        :param limit: The limit of this ListProtectedTagsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def search(self):
        r"""Gets the search of this ListProtectedTagsRequest.

        **参数解释：** 查询关键字，可模糊匹配保护Tag名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The search of this ListProtectedTagsRequest.
        :rtype: str
        """
        return self._search

    @search.setter
    def search(self, search):
        r"""Sets the search of this ListProtectedTagsRequest.

        **参数解释：** 查询关键字，可模糊匹配保护Tag名。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param search: The search of this ListProtectedTagsRequest.
        :type search: str
        """
        self._search = search

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
        if not isinstance(other, ListProtectedTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
