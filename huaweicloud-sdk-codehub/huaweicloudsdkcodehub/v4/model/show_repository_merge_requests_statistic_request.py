# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRepositoryMergeRequestsStatisticRequest:

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
        'iids': 'str',
        'fields': 'str'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'iids': 'iids',
        'fields': 'fields'
    }

    def __init__(self, repository_id=None, iids=None, fields=None):
        r"""ShowRepositoryMergeRequestsStatisticRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。
        :type repository_id: int
        :param iids: **参数解释：** 合并请求iid。
        :type iids: str
        :param fields: **参数解释：** 统计字段。 **约束限制 ** - commits_count，统计提交数 - changed_files_count，文件变更数 - notes_count， 检视意见数 - changed_lines_count，代码变更行数
        :type fields: str
        """
        
        

        self._repository_id = None
        self._iids = None
        self._fields = None
        self.discriminator = None

        self.repository_id = repository_id
        self.iids = iids
        if fields is not None:
            self.fields = fields

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ShowRepositoryMergeRequestsStatisticRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :return: The repository_id of this ShowRepositoryMergeRequestsStatisticRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ShowRepositoryMergeRequestsStatisticRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :param repository_id: The repository_id of this ShowRepositoryMergeRequestsStatisticRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def iids(self):
        r"""Gets the iids of this ShowRepositoryMergeRequestsStatisticRequest.

        **参数解释：** 合并请求iid。

        :return: The iids of this ShowRepositoryMergeRequestsStatisticRequest.
        :rtype: str
        """
        return self._iids

    @iids.setter
    def iids(self, iids):
        r"""Sets the iids of this ShowRepositoryMergeRequestsStatisticRequest.

        **参数解释：** 合并请求iid。

        :param iids: The iids of this ShowRepositoryMergeRequestsStatisticRequest.
        :type iids: str
        """
        self._iids = iids

    @property
    def fields(self):
        r"""Gets the fields of this ShowRepositoryMergeRequestsStatisticRequest.

        **参数解释：** 统计字段。 **约束限制 ** - commits_count，统计提交数 - changed_files_count，文件变更数 - notes_count， 检视意见数 - changed_lines_count，代码变更行数

        :return: The fields of this ShowRepositoryMergeRequestsStatisticRequest.
        :rtype: str
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        r"""Sets the fields of this ShowRepositoryMergeRequestsStatisticRequest.

        **参数解释：** 统计字段。 **约束限制 ** - commits_count，统计提交数 - changed_files_count，文件变更数 - notes_count， 检视意见数 - changed_lines_count，代码变更行数

        :param fields: The fields of this ShowRepositoryMergeRequestsStatisticRequest.
        :type fields: str
        """
        self._fields = fields

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
        if not isinstance(other, ShowRepositoryMergeRequestsStatisticRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
