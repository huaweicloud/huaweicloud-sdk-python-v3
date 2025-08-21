# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRepositoryStatisticsSummaryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'branches_count': 'int',
        'commits_count': 'int',
        'members_count': 'int',
        'tags_count': 'int',
        'merge_request_count': 'int',
        'note_count': 'int'
    }

    attribute_map = {
        'branches_count': 'branches_count',
        'commits_count': 'commits_count',
        'members_count': 'members_count',
        'tags_count': 'tags_count',
        'merge_request_count': 'merge_request_count',
        'note_count': 'note_count'
    }

    def __init__(self, branches_count=None, commits_count=None, members_count=None, tags_count=None, merge_request_count=None, note_count=None):
        r"""ShowRepositoryStatisticsSummaryResponse

        The model defined in huaweicloud sdk

        :param branches_count: **参数解释：** 分支数量。 **取值范围：** 不涉及。
        :type branches_count: int
        :param commits_count: **参数解释：** 提交数量。 **取值范围：** 不涉及。
        :type commits_count: int
        :param members_count: **参数解释：** 成员数量。
        :type members_count: int
        :param tags_count: **参数解释：** Tag数量。 **取值范围：** 不涉及。
        :type tags_count: int
        :param merge_request_count: **参数解释：** 合并请求数量。 **取值范围：** 不涉及。
        :type merge_request_count: int
        :param note_count: **参数解释：** 备注数量。 **取值范围：** 不涉及。
        :type note_count: int
        """
        
        super(ShowRepositoryStatisticsSummaryResponse, self).__init__()

        self._branches_count = None
        self._commits_count = None
        self._members_count = None
        self._tags_count = None
        self._merge_request_count = None
        self._note_count = None
        self.discriminator = None

        if branches_count is not None:
            self.branches_count = branches_count
        if commits_count is not None:
            self.commits_count = commits_count
        if members_count is not None:
            self.members_count = members_count
        if tags_count is not None:
            self.tags_count = tags_count
        if merge_request_count is not None:
            self.merge_request_count = merge_request_count
        if note_count is not None:
            self.note_count = note_count

    @property
    def branches_count(self):
        r"""Gets the branches_count of this ShowRepositoryStatisticsSummaryResponse.

        **参数解释：** 分支数量。 **取值范围：** 不涉及。

        :return: The branches_count of this ShowRepositoryStatisticsSummaryResponse.
        :rtype: int
        """
        return self._branches_count

    @branches_count.setter
    def branches_count(self, branches_count):
        r"""Sets the branches_count of this ShowRepositoryStatisticsSummaryResponse.

        **参数解释：** 分支数量。 **取值范围：** 不涉及。

        :param branches_count: The branches_count of this ShowRepositoryStatisticsSummaryResponse.
        :type branches_count: int
        """
        self._branches_count = branches_count

    @property
    def commits_count(self):
        r"""Gets the commits_count of this ShowRepositoryStatisticsSummaryResponse.

        **参数解释：** 提交数量。 **取值范围：** 不涉及。

        :return: The commits_count of this ShowRepositoryStatisticsSummaryResponse.
        :rtype: int
        """
        return self._commits_count

    @commits_count.setter
    def commits_count(self, commits_count):
        r"""Sets the commits_count of this ShowRepositoryStatisticsSummaryResponse.

        **参数解释：** 提交数量。 **取值范围：** 不涉及。

        :param commits_count: The commits_count of this ShowRepositoryStatisticsSummaryResponse.
        :type commits_count: int
        """
        self._commits_count = commits_count

    @property
    def members_count(self):
        r"""Gets the members_count of this ShowRepositoryStatisticsSummaryResponse.

        **参数解释：** 成员数量。

        :return: The members_count of this ShowRepositoryStatisticsSummaryResponse.
        :rtype: int
        """
        return self._members_count

    @members_count.setter
    def members_count(self, members_count):
        r"""Sets the members_count of this ShowRepositoryStatisticsSummaryResponse.

        **参数解释：** 成员数量。

        :param members_count: The members_count of this ShowRepositoryStatisticsSummaryResponse.
        :type members_count: int
        """
        self._members_count = members_count

    @property
    def tags_count(self):
        r"""Gets the tags_count of this ShowRepositoryStatisticsSummaryResponse.

        **参数解释：** Tag数量。 **取值范围：** 不涉及。

        :return: The tags_count of this ShowRepositoryStatisticsSummaryResponse.
        :rtype: int
        """
        return self._tags_count

    @tags_count.setter
    def tags_count(self, tags_count):
        r"""Sets the tags_count of this ShowRepositoryStatisticsSummaryResponse.

        **参数解释：** Tag数量。 **取值范围：** 不涉及。

        :param tags_count: The tags_count of this ShowRepositoryStatisticsSummaryResponse.
        :type tags_count: int
        """
        self._tags_count = tags_count

    @property
    def merge_request_count(self):
        r"""Gets the merge_request_count of this ShowRepositoryStatisticsSummaryResponse.

        **参数解释：** 合并请求数量。 **取值范围：** 不涉及。

        :return: The merge_request_count of this ShowRepositoryStatisticsSummaryResponse.
        :rtype: int
        """
        return self._merge_request_count

    @merge_request_count.setter
    def merge_request_count(self, merge_request_count):
        r"""Sets the merge_request_count of this ShowRepositoryStatisticsSummaryResponse.

        **参数解释：** 合并请求数量。 **取值范围：** 不涉及。

        :param merge_request_count: The merge_request_count of this ShowRepositoryStatisticsSummaryResponse.
        :type merge_request_count: int
        """
        self._merge_request_count = merge_request_count

    @property
    def note_count(self):
        r"""Gets the note_count of this ShowRepositoryStatisticsSummaryResponse.

        **参数解释：** 备注数量。 **取值范围：** 不涉及。

        :return: The note_count of this ShowRepositoryStatisticsSummaryResponse.
        :rtype: int
        """
        return self._note_count

    @note_count.setter
    def note_count(self, note_count):
        r"""Sets the note_count of this ShowRepositoryStatisticsSummaryResponse.

        **参数解释：** 备注数量。 **取值范围：** 不涉及。

        :param note_count: The note_count of this ShowRepositoryStatisticsSummaryResponse.
        :type note_count: int
        """
        self._note_count = note_count

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
        if not isinstance(other, ShowRepositoryStatisticsSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
