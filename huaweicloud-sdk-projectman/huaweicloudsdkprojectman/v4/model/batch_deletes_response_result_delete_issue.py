# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeletesResponseResultDeleteIssue:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'del_issue_id': 'list[int]',
        'del_issue': 'list[BatchDeletesResponseResultDeleteIssueDelIssue]'
    }

    attribute_map = {
        'del_issue_id': 'del_issue_id',
        'del_issue': 'del_issue'
    }

    def __init__(self, del_issue_id=None, del_issue=None):
        r"""BatchDeletesResponseResultDeleteIssue

        The model defined in huaweicloud sdk

        :param del_issue_id: **参数解释：** 删除的工作项id。 **取值范围：** 不涉及。
        :type del_issue_id: list[int]
        :param del_issue: **参数解释：** 删除的工作项详情。 **取值范围：** 不涉及。
        :type del_issue: list[:class:`huaweicloudsdkprojectman.v4.BatchDeletesResponseResultDeleteIssueDelIssue`]
        """
        
        

        self._del_issue_id = None
        self._del_issue = None
        self.discriminator = None

        if del_issue_id is not None:
            self.del_issue_id = del_issue_id
        if del_issue is not None:
            self.del_issue = del_issue

    @property
    def del_issue_id(self):
        r"""Gets the del_issue_id of this BatchDeletesResponseResultDeleteIssue.

        **参数解释：** 删除的工作项id。 **取值范围：** 不涉及。

        :return: The del_issue_id of this BatchDeletesResponseResultDeleteIssue.
        :rtype: list[int]
        """
        return self._del_issue_id

    @del_issue_id.setter
    def del_issue_id(self, del_issue_id):
        r"""Sets the del_issue_id of this BatchDeletesResponseResultDeleteIssue.

        **参数解释：** 删除的工作项id。 **取值范围：** 不涉及。

        :param del_issue_id: The del_issue_id of this BatchDeletesResponseResultDeleteIssue.
        :type del_issue_id: list[int]
        """
        self._del_issue_id = del_issue_id

    @property
    def del_issue(self):
        r"""Gets the del_issue of this BatchDeletesResponseResultDeleteIssue.

        **参数解释：** 删除的工作项详情。 **取值范围：** 不涉及。

        :return: The del_issue of this BatchDeletesResponseResultDeleteIssue.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.BatchDeletesResponseResultDeleteIssueDelIssue`]
        """
        return self._del_issue

    @del_issue.setter
    def del_issue(self, del_issue):
        r"""Sets the del_issue of this BatchDeletesResponseResultDeleteIssue.

        **参数解释：** 删除的工作项详情。 **取值范围：** 不涉及。

        :param del_issue: The del_issue of this BatchDeletesResponseResultDeleteIssue.
        :type del_issue: list[:class:`huaweicloudsdkprojectman.v4.BatchDeletesResponseResultDeleteIssueDelIssue`]
        """
        self._del_issue = del_issue

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
        if not isinstance(other, BatchDeletesResponseResultDeleteIssue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
