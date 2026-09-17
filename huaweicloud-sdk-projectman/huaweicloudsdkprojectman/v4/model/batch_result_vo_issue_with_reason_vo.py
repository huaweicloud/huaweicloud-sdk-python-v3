# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchResultVOIssueWithReasonVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success_num': 'int',
        'fail_num': 'int',
        'failed': 'list[IssueWithReasonVO]'
    }

    attribute_map = {
        'success_num': 'success_num',
        'fail_num': 'fail_num',
        'failed': 'failed'
    }

    def __init__(self, success_num=None, fail_num=None, failed=None):
        r"""BatchResultVOIssueWithReasonVO

        The model defined in huaweicloud sdk

        :param success_num: **参数解释**： 批量操作成功条数。 **取值范围**： 不涉及。
        :type success_num: int
        :param fail_num: **参数解释**： 批量操作失败条数。 **取值范围**： 不涉及。
        :type fail_num: int
        :param failed: **参数解释**： 批量操作失败数据及失败原因。 **取值范围**： 不涉及。
        :type failed: list[:class:`huaweicloudsdkprojectman.v4.IssueWithReasonVO`]
        """
        
        

        self._success_num = None
        self._fail_num = None
        self._failed = None
        self.discriminator = None

        if success_num is not None:
            self.success_num = success_num
        if fail_num is not None:
            self.fail_num = fail_num
        if failed is not None:
            self.failed = failed

    @property
    def success_num(self):
        r"""Gets the success_num of this BatchResultVOIssueWithReasonVO.

        **参数解释**： 批量操作成功条数。 **取值范围**： 不涉及。

        :return: The success_num of this BatchResultVOIssueWithReasonVO.
        :rtype: int
        """
        return self._success_num

    @success_num.setter
    def success_num(self, success_num):
        r"""Sets the success_num of this BatchResultVOIssueWithReasonVO.

        **参数解释**： 批量操作成功条数。 **取值范围**： 不涉及。

        :param success_num: The success_num of this BatchResultVOIssueWithReasonVO.
        :type success_num: int
        """
        self._success_num = success_num

    @property
    def fail_num(self):
        r"""Gets the fail_num of this BatchResultVOIssueWithReasonVO.

        **参数解释**： 批量操作失败条数。 **取值范围**： 不涉及。

        :return: The fail_num of this BatchResultVOIssueWithReasonVO.
        :rtype: int
        """
        return self._fail_num

    @fail_num.setter
    def fail_num(self, fail_num):
        r"""Sets the fail_num of this BatchResultVOIssueWithReasonVO.

        **参数解释**： 批量操作失败条数。 **取值范围**： 不涉及。

        :param fail_num: The fail_num of this BatchResultVOIssueWithReasonVO.
        :type fail_num: int
        """
        self._fail_num = fail_num

    @property
    def failed(self):
        r"""Gets the failed of this BatchResultVOIssueWithReasonVO.

        **参数解释**： 批量操作失败数据及失败原因。 **取值范围**： 不涉及。

        :return: The failed of this BatchResultVOIssueWithReasonVO.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.IssueWithReasonVO`]
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        r"""Sets the failed of this BatchResultVOIssueWithReasonVO.

        **参数解释**： 批量操作失败数据及失败原因。 **取值范围**： 不涉及。

        :param failed: The failed of this BatchResultVOIssueWithReasonVO.
        :type failed: list[:class:`huaweicloudsdkprojectman.v4.IssueWithReasonVO`]
        """
        self._failed = failed

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
        if not isinstance(other, BatchResultVOIssueWithReasonVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
