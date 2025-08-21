# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCommitRequest:

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
        'stats': 'bool',
        'show_code_changes': 'bool'
    }

    attribute_map = {
        'repository_id': 'repository_id',
        'sha': 'sha',
        'stats': 'stats',
        'show_code_changes': 'show_code_changes'
    }

    def __init__(self, repository_id=None, sha=None, stats=None, show_code_changes=None):
        r"""ShowCommitRequest

        The model defined in huaweicloud sdk

        :param repository_id: **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。
        :type repository_id: int
        :param sha: **参数解释：** 分支名、tag名、提交ID。
        :type sha: str
        :param stats: **参数解释：** 是否包含状态信息。 **取值范围：** - true，包含。 - false，不包含。
        :type stats: bool
        :param show_code_changes: **参数解释：** 是否包含代码变化信息。 **取值范围：** - true，包含。 - false，不包含。
        :type show_code_changes: bool
        """
        
        

        self._repository_id = None
        self._sha = None
        self._stats = None
        self._show_code_changes = None
        self.discriminator = None

        self.repository_id = repository_id
        self.sha = sha
        if stats is not None:
            self.stats = stats
        if show_code_changes is not None:
            self.show_code_changes = show_code_changes

    @property
    def repository_id(self):
        r"""Gets the repository_id of this ShowCommitRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :return: The repository_id of this ShowCommitRequest.
        :rtype: int
        """
        return self._repository_id

    @repository_id.setter
    def repository_id(self, repository_id):
        r"""Sets the repository_id of this ShowCommitRequest.

        **参数解释：** 仓库的ID，通过[[查询用户所有仓库](https://support.huaweicloud.com/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws)[[查询用户所有仓库](https://support.huaweicloud.com/intl/en-us/api-codeartsrepo/ListUserAllRepositories.html)](tag:hws_hk)[查询项目列表](tag:hcs,hcs_sm)接口查询项目列表获取。 **约束限制：** 不涉及。

        :param repository_id: The repository_id of this ShowCommitRequest.
        :type repository_id: int
        """
        self._repository_id = repository_id

    @property
    def sha(self):
        r"""Gets the sha of this ShowCommitRequest.

        **参数解释：** 分支名、tag名、提交ID。

        :return: The sha of this ShowCommitRequest.
        :rtype: str
        """
        return self._sha

    @sha.setter
    def sha(self, sha):
        r"""Sets the sha of this ShowCommitRequest.

        **参数解释：** 分支名、tag名、提交ID。

        :param sha: The sha of this ShowCommitRequest.
        :type sha: str
        """
        self._sha = sha

    @property
    def stats(self):
        r"""Gets the stats of this ShowCommitRequest.

        **参数解释：** 是否包含状态信息。 **取值范围：** - true，包含。 - false，不包含。

        :return: The stats of this ShowCommitRequest.
        :rtype: bool
        """
        return self._stats

    @stats.setter
    def stats(self, stats):
        r"""Sets the stats of this ShowCommitRequest.

        **参数解释：** 是否包含状态信息。 **取值范围：** - true，包含。 - false，不包含。

        :param stats: The stats of this ShowCommitRequest.
        :type stats: bool
        """
        self._stats = stats

    @property
    def show_code_changes(self):
        r"""Gets the show_code_changes of this ShowCommitRequest.

        **参数解释：** 是否包含代码变化信息。 **取值范围：** - true，包含。 - false，不包含。

        :return: The show_code_changes of this ShowCommitRequest.
        :rtype: bool
        """
        return self._show_code_changes

    @show_code_changes.setter
    def show_code_changes(self, show_code_changes):
        r"""Sets the show_code_changes of this ShowCommitRequest.

        **参数解释：** 是否包含代码变化信息。 **取值范围：** - true，包含。 - false，不包含。

        :param show_code_changes: The show_code_changes of this ShowCommitRequest.
        :type show_code_changes: bool
        """
        self._show_code_changes = show_code_changes

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
        if not isinstance(other, ShowCommitRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
