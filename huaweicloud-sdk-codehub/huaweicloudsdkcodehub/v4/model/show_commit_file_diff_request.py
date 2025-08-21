# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCommitFileDiffRequest:

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
        'sha': 'str',
        'path': 'str',
        'old_path': 'str',
        'ignore_whitespace_change': 'bool'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'sha': 'sha',
        'path': 'path',
        'old_path': 'old_path',
        'ignore_whitespace_change': 'ignore_whitespace_change'
    }

    def __init__(self, repository_id=None, sha=None, path=None, old_path=None, ignore_whitespace_change=None):
        r"""ShowCommitFileDiffRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。
        :type repository_id: int
        :param sha: **参数解释：** 分支名、tag名、提交ID。
        :type sha: str
        :param path: **参数解释：** 文件路径。 **取值范围：** 字符串长度不少于1，不超过100000。
        :type path: str
        :param old_path: **参数解释：** 改名之前的文件路径。 **取值范围：** 字符串长度不少于1，不超过100000。
        :type old_path: str
        :param ignore_whitespace_change: **参数解释：** 是否忽略空白数量更改。 **取值范围：** - true，忽略空白数量的更改。 - false，不会忽略空白数量的更改。
        :type ignore_whitespace_change: bool
        """
        
        

        self._repository_id = None
        self._sha = None
        self._path = None
        self._old_path = None
        self._ignore_whitespace_change = None
        self.discriminator = None

        self.repository_id = repository_id
        self.sha = sha
        if path is not None:
            self.path = path
        if old_path is not None:
            self.old_path = old_path
        if ignore_whitespace_change is not None:
            self.ignore_whitespace_change = ignore_whitespace_change

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ShowCommitFileDiffRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :return: The repository_id of this ShowCommitFileDiffRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ShowCommitFileDiffRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :param repository_id: The repository_id of this ShowCommitFileDiffRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def sha(self):
        r"""Gets the sha of this ShowCommitFileDiffRequest.

        **参数解释：** 分支名、tag名、提交ID。

        :return: The sha of this ShowCommitFileDiffRequest.
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        r"""Sets the sha of this ShowCommitFileDiffRequest.

        **参数解释：** 分支名、tag名、提交ID。

        :param sha: The sha of this ShowCommitFileDiffRequest.
        :type sha: str
        """
        self._sha = sha

    @property
    def path(self):
        r"""Gets the path of this ShowCommitFileDiffRequest.

        **参数解释：** 文件路径。 **取值范围：** 字符串长度不少于1，不超过100000。

        :return: The path of this ShowCommitFileDiffRequest.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        r"""Sets the path of this ShowCommitFileDiffRequest.

        **参数解释：** 文件路径。 **取值范围：** 字符串长度不少于1，不超过100000。

        :param path: The path of this ShowCommitFileDiffRequest.
        :type path: str
        """
        self._path = path

    @property
    def old_path(self):
        r"""Gets the old_path of this ShowCommitFileDiffRequest.

        **参数解释：** 改名之前的文件路径。 **取值范围：** 字符串长度不少于1，不超过100000。

        :return: The old_path of this ShowCommitFileDiffRequest.
        :rtype: str
        """
        return self._old_path

    @old_path.setter
    def old_path(self, old_path):
        r"""Sets the old_path of this ShowCommitFileDiffRequest.

        **参数解释：** 改名之前的文件路径。 **取值范围：** 字符串长度不少于1，不超过100000。

        :param old_path: The old_path of this ShowCommitFileDiffRequest.
        :type old_path: str
        """
        self._old_path = old_path

    @property
    def ignore_whitespace_change(self):
        r"""Gets the ignore_whitespace_change of this ShowCommitFileDiffRequest.

        **参数解释：** 是否忽略空白数量更改。 **取值范围：** - true，忽略空白数量的更改。 - false，不会忽略空白数量的更改。

        :return: The ignore_whitespace_change of this ShowCommitFileDiffRequest.
        :rtype: bool
        """
        return self._ignore_whitespace_change

    @ignore_whitespace_change.setter
    def ignore_whitespace_change(self, ignore_whitespace_change):
        r"""Sets the ignore_whitespace_change of this ShowCommitFileDiffRequest.

        **参数解释：** 是否忽略空白数量更改。 **取值范围：** - true，忽略空白数量的更改。 - false，不会忽略空白数量的更改。

        :param ignore_whitespace_change: The ignore_whitespace_change of this ShowCommitFileDiffRequest.
        :type ignore_whitespace_change: bool
        """
        self._ignore_whitespace_change = ignore_whitespace_change

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
        if not isinstance(other, ShowCommitFileDiffRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
