# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBranchConflictRequest:

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
        'source_repository_id': 'int',
        'source_branch': 'str',
        'target_branch': 'str',
        'target_repository_id': 'int'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'source_repository_id': 'source_repository_id',
        'source_branch': 'source_branch',
        'target_branch': 'target_branch',
        'target_repository_id': 'target_repository_id'
    }

    def __init__(self, repository_id=None, source_repository_id=None, source_branch=None, target_branch=None, target_repository_id=None):
        r"""ShowBranchConflictRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。
        :type repository_id: int
        :param source_repository_id: **参数解释：** 查询指定源仓库的数据。
        :type source_repository_id: int
        :param source_branch: **参数解释：** 源分支。
        :type source_branch: str
        :param target_branch: **参数解释：** 目标分支。
        :type target_branch: str
        :param target_repository_id: **参数解释：** 目标仓库id。创建MR时，代码将要合入的仓库。
        :type target_repository_id: int
        """
        
        

        self._repository_id = None
        self._source_repository_id = None
        self._source_branch = None
        self._target_branch = None
        self._target_repository_id = None
        self.discriminator = None

        self.repository_id = repository_id
        self.source_repository_id = source_repository_id
        self.source_branch = source_branch
        self.target_branch = target_branch
        self.target_repository_id = target_repository_id

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ShowBranchConflictRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :return: The repository_id of this ShowBranchConflictRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ShowBranchConflictRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :param repository_id: The repository_id of this ShowBranchConflictRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def source_repository_id(self):
        r"""Gets the source_repository_id of this ShowBranchConflictRequest.

        **参数解释：** 查询指定源仓库的数据。

        :return: The source_repository_id of this ShowBranchConflictRequest.
        :rtype: int
        """
        return self._source_repository_id

    @source_repository_id.setter
    def source_repository_id(self, source_repository_id):
        r"""Sets the source_repository_id of this ShowBranchConflictRequest.

        **参数解释：** 查询指定源仓库的数据。

        :param source_repository_id: The source_repository_id of this ShowBranchConflictRequest.
        :type source_repository_id: int
        """
        self._source_repository_id = source_repository_id

    @property
    def source_branch(self):
        r"""Gets the source_branch of this ShowBranchConflictRequest.

        **参数解释：** 源分支。

        :return: The source_branch of this ShowBranchConflictRequest.
        :rtype: str
        """
        return self._source_branch

    @source_branch.setter
    def source_branch(self, source_branch):
        r"""Sets the source_branch of this ShowBranchConflictRequest.

        **参数解释：** 源分支。

        :param source_branch: The source_branch of this ShowBranchConflictRequest.
        :type source_branch: str
        """
        self._source_branch = source_branch

    @property
    def target_branch(self):
        r"""Gets the target_branch of this ShowBranchConflictRequest.

        **参数解释：** 目标分支。

        :return: The target_branch of this ShowBranchConflictRequest.
        :rtype: str
        """
        return self._target_branch

    @target_branch.setter
    def target_branch(self, target_branch):
        r"""Sets the target_branch of this ShowBranchConflictRequest.

        **参数解释：** 目标分支。

        :param target_branch: The target_branch of this ShowBranchConflictRequest.
        :type target_branch: str
        """
        self._target_branch = target_branch

    @property
    def target_repository_id(self):
        r"""Gets the target_repository_id of this ShowBranchConflictRequest.

        **参数解释：** 目标仓库id。创建MR时，代码将要合入的仓库。

        :return: The target_repository_id of this ShowBranchConflictRequest.
        :rtype: int
        """
        return self._target_repository_id

    @target_repository_id.setter
    def target_repository_id(self, target_repository_id):
        r"""Sets the target_repository_id of this ShowBranchConflictRequest.

        **参数解释：** 目标仓库id。创建MR时，代码将要合入的仓库。

        :param target_repository_id: The target_repository_id of this ShowBranchConflictRequest.
        :type target_repository_id: int
        """
        self._target_repository_id = target_repository_id

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
        if not isinstance(other, ShowBranchConflictRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
