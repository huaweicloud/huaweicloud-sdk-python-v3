# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CommitStatsDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'additions': 'int',
        'deletions': 'int',
        'total': 'int'
    }

    attribute_map = {
        'additions': 'additions',
        'deletions': 'deletions',
        'total': 'total'
    }

    def __init__(self, additions=None, deletions=None, total=None):
        r"""CommitStatsDto

        The model defined in huaweicloud sdk

        :param additions: **参数解释：** 增加行数。 **取值范围：** 不涉及。
        :type additions: int
        :param deletions: **参数解释：** 删除行数。 **取值范围：** 不涉及。
        :type deletions: int
        :param total: **参数解释：** 变更行数。 **取值范围：** 不涉及。
        :type total: int
        """
        
        

        self._additions = None
        self._deletions = None
        self._total = None
        self.discriminator = None

        if additions is not None:
            self.additions = additions
        if deletions is not None:
            self.deletions = deletions
        if total is not None:
            self.total = total

    @property
    def additions(self):
        r"""Gets the additions of this CommitStatsDto.

        **参数解释：** 增加行数。 **取值范围：** 不涉及。

        :return: The additions of this CommitStatsDto.
        :rtype: int
        """
        return self._additions

    @additions.setter
    def additions(self, additions):
        r"""Sets the additions of this CommitStatsDto.

        **参数解释：** 增加行数。 **取值范围：** 不涉及。

        :param additions: The additions of this CommitStatsDto.
        :type additions: int
        """
        self._additions = additions

    @property
    def deletions(self):
        r"""Gets the deletions of this CommitStatsDto.

        **参数解释：** 删除行数。 **取值范围：** 不涉及。

        :return: The deletions of this CommitStatsDto.
        :rtype: int
        """
        return self._deletions

    @deletions.setter
    def deletions(self, deletions):
        r"""Sets the deletions of this CommitStatsDto.

        **参数解释：** 删除行数。 **取值范围：** 不涉及。

        :param deletions: The deletions of this CommitStatsDto.
        :type deletions: int
        """
        self._deletions = deletions

    @property
    def total(self):
        r"""Gets the total of this CommitStatsDto.

        **参数解释：** 变更行数。 **取值范围：** 不涉及。

        :return: The total of this CommitStatsDto.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this CommitStatsDto.

        **参数解释：** 变更行数。 **取值范围：** 不涉及。

        :param total: The total of this CommitStatsDto.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, CommitStatsDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
