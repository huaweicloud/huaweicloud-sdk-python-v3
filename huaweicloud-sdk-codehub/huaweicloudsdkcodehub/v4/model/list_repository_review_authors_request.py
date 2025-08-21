# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRepositoryReviewAuthorsRequest:

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
        'noteable_type': 'str',
        'resolved_status': 'str',
        'reviewers_filter': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'noteable_type': 'noteable_type',
        'resolved_status': 'resolved_status',
        'reviewers_filter': 'reviewers_filter',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, repository_id=None, noteable_type=None, resolved_status=None, reviewers_filter=None, offset=None, limit=None):
        r"""ListRepositoryReviewAuthorsRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。
        :type repository_id: int
        :param noteable_type: **参数解释：** 意见类型。 **取值范围：** - Commit，提交。 - MergeRequest，合并请求。  
        :type noteable_type: str
        :param resolved_status: **参数解释：** 解决状态。 **取值范围：** - resolved，已解决。 - unresolved，未解决。   - all，全部。
        :type resolved_status: str
        :param reviewers_filter: **参数解释：** 根据检视人名字或用户名筛选意见。
        :type reviewers_filter: str
        :param offset: **参数解释：** 偏移量，从0开始。
        :type offset: int
        :param limit: **参数解释：** 返回数量。
        :type limit: int
        """
        
        

        self._repository_id = None
        self._noteable_type = None
        self._resolved_status = None
        self._reviewers_filter = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.repository_id = repository_id
        self.noteable_type = noteable_type
        self.resolved_status = resolved_status
        if reviewers_filter is not None:
            self.reviewers_filter = reviewers_filter
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ListRepositoryReviewAuthorsRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :return: The repository_id of this ListRepositoryReviewAuthorsRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ListRepositoryReviewAuthorsRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :param repository_id: The repository_id of this ListRepositoryReviewAuthorsRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def noteable_type(self):
        r"""Gets the noteable_type of this ListRepositoryReviewAuthorsRequest.

        **参数解释：** 意见类型。 **取值范围：** - Commit，提交。 - MergeRequest，合并请求。  

        :return: The noteable_type of this ListRepositoryReviewAuthorsRequest.
        :rtype: str
        """
        return self._noteable_type

    @noteable_type.setter
    def noteable_type(self, noteable_type):
        r"""Sets the noteable_type of this ListRepositoryReviewAuthorsRequest.

        **参数解释：** 意见类型。 **取值范围：** - Commit，提交。 - MergeRequest，合并请求。  

        :param noteable_type: The noteable_type of this ListRepositoryReviewAuthorsRequest.
        :type noteable_type: str
        """
        self._noteable_type = noteable_type

    @property
    def resolved_status(self):
        r"""Gets the resolved_status of this ListRepositoryReviewAuthorsRequest.

        **参数解释：** 解决状态。 **取值范围：** - resolved，已解决。 - unresolved，未解决。   - all，全部。

        :return: The resolved_status of this ListRepositoryReviewAuthorsRequest.
        :rtype: str
        """
        return self._resolved_status

    @resolved_status.setter
    def resolved_status(self, resolved_status):
        r"""Sets the resolved_status of this ListRepositoryReviewAuthorsRequest.

        **参数解释：** 解决状态。 **取值范围：** - resolved，已解决。 - unresolved，未解决。   - all，全部。

        :param resolved_status: The resolved_status of this ListRepositoryReviewAuthorsRequest.
        :type resolved_status: str
        """
        self._resolved_status = resolved_status

    @property
    def reviewers_filter(self):
        r"""Gets the reviewers_filter of this ListRepositoryReviewAuthorsRequest.

        **参数解释：** 根据检视人名字或用户名筛选意见。

        :return: The reviewers_filter of this ListRepositoryReviewAuthorsRequest.
        :rtype: str
        """
        return self._reviewers_filter

    @reviewers_filter.setter
    def reviewers_filter(self, reviewers_filter):
        r"""Sets the reviewers_filter of this ListRepositoryReviewAuthorsRequest.

        **参数解释：** 根据检视人名字或用户名筛选意见。

        :param reviewers_filter: The reviewers_filter of this ListRepositoryReviewAuthorsRequest.
        :type reviewers_filter: str
        """
        self._reviewers_filter = reviewers_filter

    @property
    def offset(self):
        r"""Gets the offset of this ListRepositoryReviewAuthorsRequest.

        **参数解释：** 偏移量，从0开始。

        :return: The offset of this ListRepositoryReviewAuthorsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListRepositoryReviewAuthorsRequest.

        **参数解释：** 偏移量，从0开始。

        :param offset: The offset of this ListRepositoryReviewAuthorsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListRepositoryReviewAuthorsRequest.

        **参数解释：** 返回数量。

        :return: The limit of this ListRepositoryReviewAuthorsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRepositoryReviewAuthorsRequest.

        **参数解释：** 返回数量。

        :param limit: The limit of this ListRepositoryReviewAuthorsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListRepositoryReviewAuthorsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
