# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssueBatchOperateEntitiesResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success': 'list[IssueOperateResult]',
        'failed': 'list[IssueOperateResult]',
        'undeleted_trees': 'list[IssueOperateResult]'
    }

    attribute_map = {
        'success': 'success',
        'failed': 'failed',
        'undeleted_trees': 'undeleted_trees'
    }

    def __init__(self, success=None, failed=None, undeleted_trees=None):
        r"""IssueBatchOperateEntitiesResult

        The model defined in huaweicloud sdk

        :param success: **参数解释**： 成功的结果。
        :type success: list[:class:`huaweicloudsdkprojectman.v4.IssueOperateResult`]
        :param failed: **参数解释**： 失败的结果。
        :type failed: list[:class:`huaweicloudsdkprojectman.v4.IssueOperateResult`]
        :param undeleted_trees: **参数解释**： 删除失败的工作项。 **取值范围**： 不涉及
        :type undeleted_trees: list[:class:`huaweicloudsdkprojectman.v4.IssueOperateResult`]
        """
        
        

        self._success = None
        self._failed = None
        self._undeleted_trees = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if failed is not None:
            self.failed = failed
        if undeleted_trees is not None:
            self.undeleted_trees = undeleted_trees

    @property
    def success(self):
        r"""Gets the success of this IssueBatchOperateEntitiesResult.

        **参数解释**： 成功的结果。

        :return: The success of this IssueBatchOperateEntitiesResult.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.IssueOperateResult`]
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this IssueBatchOperateEntitiesResult.

        **参数解释**： 成功的结果。

        :param success: The success of this IssueBatchOperateEntitiesResult.
        :type success: list[:class:`huaweicloudsdkprojectman.v4.IssueOperateResult`]
        """
        self._success = success

    @property
    def failed(self):
        r"""Gets the failed of this IssueBatchOperateEntitiesResult.

        **参数解释**： 失败的结果。

        :return: The failed of this IssueBatchOperateEntitiesResult.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.IssueOperateResult`]
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        r"""Sets the failed of this IssueBatchOperateEntitiesResult.

        **参数解释**： 失败的结果。

        :param failed: The failed of this IssueBatchOperateEntitiesResult.
        :type failed: list[:class:`huaweicloudsdkprojectman.v4.IssueOperateResult`]
        """
        self._failed = failed

    @property
    def undeleted_trees(self):
        r"""Gets the undeleted_trees of this IssueBatchOperateEntitiesResult.

        **参数解释**： 删除失败的工作项。 **取值范围**： 不涉及

        :return: The undeleted_trees of this IssueBatchOperateEntitiesResult.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.IssueOperateResult`]
        """
        return self._undeleted_trees

    @undeleted_trees.setter
    def undeleted_trees(self, undeleted_trees):
        r"""Sets the undeleted_trees of this IssueBatchOperateEntitiesResult.

        **参数解释**： 删除失败的工作项。 **取值范围**： 不涉及

        :param undeleted_trees: The undeleted_trees of this IssueBatchOperateEntitiesResult.
        :type undeleted_trees: list[:class:`huaweicloudsdkprojectman.v4.IssueOperateResult`]
        """
        self._undeleted_trees = undeleted_trees

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
        if not isinstance(other, IssueBatchOperateEntitiesResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
