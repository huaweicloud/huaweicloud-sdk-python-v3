# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRepositoryWorkItemsRequest:

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
        'project_id': 'str',
        'is_ipd': 'bool',
        'subject': 'str',
        'target_branch': 'str'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'offset': 'offset',
        'limit': 'limit',
        'project_id': 'project_id',
        'is_ipd': 'is_ipd',
        'subject': 'subject',
        'target_branch': 'target_branch'
    }

    def __init__(self, repository_id=None, offset=None, limit=None, project_id=None, is_ipd=None, subject=None, target_branch=None):
        r"""ListRepositoryWorkItemsRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。
        :type repository_id: int
        :param offset: **参数解释：** 偏移量，从0开始。
        :type offset: int
        :param limit: **参数解释：** 返回数量。
        :type limit: int
        :param project_id: **参数解释：** 项目的32位uuid，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/en-us/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **取值范围：** 字符串长度32。
        :type project_id: str
        :param is_ipd: **参数解释：** 是否为IPD类型项目的工作项。 **取值范围：** true/false
        :type is_ipd: bool
        :param subject: **参数解释：** 工作项标题搜索关键字。 **取值范围：** 字符串长度不少于1，不超过200。
        :type subject: str
        :param target_branch: **参数解释：** 合并请求的目标分支，如果要获取合并请求可关联的工作项列表，则需要传递该字段。  **约束限制：** 不支持以 - . refs/heads/ refs/remotes/ 开头，不支持空格 [ \\ &lt; ~ ^ : ? * ! ( ) &#39; \&quot; | 等特殊字符，不支持以. / .lock结尾。  **取值范围：** 字符串长度不少于1，不超过200。 **默认取值：** 不涉及。
        :type target_branch: str
        """
        
        

        self._repository_id = None
        self._offset = None
        self._limit = None
        self._project_id = None
        self._is_ipd = None
        self._subject = None
        self._target_branch = None
        self.discriminator = None

        self.repository_id = repository_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.project_id = project_id
        self.is_ipd = is_ipd
        if subject is not None:
            self.subject = subject
        if target_branch is not None:
            self.target_branch = target_branch

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ListRepositoryWorkItemsRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :return: The repository_id of this ListRepositoryWorkItemsRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ListRepositoryWorkItemsRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :param repository_id: The repository_id of this ListRepositoryWorkItemsRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def offset(self):
        r"""Gets the offset of this ListRepositoryWorkItemsRequest.

        **参数解释：** 偏移量，从0开始。

        :return: The offset of this ListRepositoryWorkItemsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListRepositoryWorkItemsRequest.

        **参数解释：** 偏移量，从0开始。

        :param offset: The offset of this ListRepositoryWorkItemsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListRepositoryWorkItemsRequest.

        **参数解释：** 返回数量。

        :return: The limit of this ListRepositoryWorkItemsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRepositoryWorkItemsRequest.

        **参数解释：** 返回数量。

        :param limit: The limit of this ListRepositoryWorkItemsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def project_id(self):
        r"""Gets the project_id of this ListRepositoryWorkItemsRequest.

        **参数解释：** 项目的32位uuid，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/en-us/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **取值范围：** 字符串长度32。

        :return: The project_id of this ListRepositoryWorkItemsRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ListRepositoryWorkItemsRequest.

        **参数解释：** 项目的32位uuid，项目唯一标识，通过[[查询项目列表](https://support.huaweicloud.com/api-projectman/ListProjectsV4.html)](tag:hws)[[查询项目列表](https://support.huaweicloud.com/intl/en-us/api-projectman/ListProjectsV4.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **取值范围：** 字符串长度32。

        :param project_id: The project_id of this ListRepositoryWorkItemsRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def is_ipd(self):
        r"""Gets the is_ipd of this ListRepositoryWorkItemsRequest.

        **参数解释：** 是否为IPD类型项目的工作项。 **取值范围：** true/false

        :return: The is_ipd of this ListRepositoryWorkItemsRequest.
        :rtype: bool
        """
        return self._is_ipd

    @is_ipd.setter
    def is_ipd(self, is_ipd):
        r"""Sets the is_ipd of this ListRepositoryWorkItemsRequest.

        **参数解释：** 是否为IPD类型项目的工作项。 **取值范围：** true/false

        :param is_ipd: The is_ipd of this ListRepositoryWorkItemsRequest.
        :type is_ipd: bool
        """
        self._is_ipd = is_ipd

    @property
    def subject(self):
        r"""Gets the subject of this ListRepositoryWorkItemsRequest.

        **参数解释：** 工作项标题搜索关键字。 **取值范围：** 字符串长度不少于1，不超过200。

        :return: The subject of this ListRepositoryWorkItemsRequest.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        r"""Sets the subject of this ListRepositoryWorkItemsRequest.

        **参数解释：** 工作项标题搜索关键字。 **取值范围：** 字符串长度不少于1，不超过200。

        :param subject: The subject of this ListRepositoryWorkItemsRequest.
        :type subject: str
        """
        self._subject = subject

    @property
    def target_branch(self):
        r"""Gets the target_branch of this ListRepositoryWorkItemsRequest.

        **参数解释：** 合并请求的目标分支，如果要获取合并请求可关联的工作项列表，则需要传递该字段。  **约束限制：** 不支持以 - . refs/heads/ refs/remotes/ 开头，不支持空格 [ \\ < ~ ^ : ? * ! ( ) ' \" | 等特殊字符，不支持以. / .lock结尾。  **取值范围：** 字符串长度不少于1，不超过200。 **默认取值：** 不涉及。

        :return: The target_branch of this ListRepositoryWorkItemsRequest.
        :rtype: str
        """
        return self._target_branch

    @target_branch.setter
    def target_branch(self, target_branch):
        r"""Sets the target_branch of this ListRepositoryWorkItemsRequest.

        **参数解释：** 合并请求的目标分支，如果要获取合并请求可关联的工作项列表，则需要传递该字段。  **约束限制：** 不支持以 - . refs/heads/ refs/remotes/ 开头，不支持空格 [ \\ < ~ ^ : ? * ! ( ) ' \" | 等特殊字符，不支持以. / .lock结尾。  **取值范围：** 字符串长度不少于1，不超过200。 **默认取值：** 不涉及。

        :param target_branch: The target_branch of this ListRepositoryWorkItemsRequest.
        :type target_branch: str
        """
        self._target_branch = target_branch

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
        if not isinstance(other, ListRepositoryWorkItemsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
