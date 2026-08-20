# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchBaselineIssueResponseResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success': 'list[IssueBaselineResult]',
        'failed': 'list[IssueBaselineResult]',
        'success_num': 'int',
        'fail_num': 'int'
    }

    attribute_map = {
        'success': 'success',
        'failed': 'failed',
        'success_num': 'success_num',
        'fail_num': 'fail_num'
    }

    def __init__(self, success=None, failed=None, success_num=None, fail_num=None):
        r"""BatchBaselineIssueResponseResult

        The model defined in huaweicloud sdk

        :param success: 基线成功的工作项列表。
        :type success: list[:class:`huaweicloudsdkprojectman.v4.IssueBaselineResult`]
        :param failed: 基线失败的工作项列表。
        :type failed: list[:class:`huaweicloudsdkprojectman.v4.IssueBaselineResult`]
        :param success_num: 成功数量。
        :type success_num: int
        :param fail_num: 失败数量。
        :type fail_num: int
        """
        
        

        self._success = None
        self._failed = None
        self._success_num = None
        self._fail_num = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if failed is not None:
            self.failed = failed
        if success_num is not None:
            self.success_num = success_num
        if fail_num is not None:
            self.fail_num = fail_num

    @property
    def success(self):
        r"""Gets the success of this BatchBaselineIssueResponseResult.

        基线成功的工作项列表。

        :return: The success of this BatchBaselineIssueResponseResult.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.IssueBaselineResult`]
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this BatchBaselineIssueResponseResult.

        基线成功的工作项列表。

        :param success: The success of this BatchBaselineIssueResponseResult.
        :type success: list[:class:`huaweicloudsdkprojectman.v4.IssueBaselineResult`]
        """
        self._success = success

    @property
    def failed(self):
        r"""Gets the failed of this BatchBaselineIssueResponseResult.

        基线失败的工作项列表。

        :return: The failed of this BatchBaselineIssueResponseResult.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.IssueBaselineResult`]
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        r"""Sets the failed of this BatchBaselineIssueResponseResult.

        基线失败的工作项列表。

        :param failed: The failed of this BatchBaselineIssueResponseResult.
        :type failed: list[:class:`huaweicloudsdkprojectman.v4.IssueBaselineResult`]
        """
        self._failed = failed

    @property
    def success_num(self):
        r"""Gets the success_num of this BatchBaselineIssueResponseResult.

        成功数量。

        :return: The success_num of this BatchBaselineIssueResponseResult.
        :rtype: int
        """
        return self._success_num

    @success_num.setter
    def success_num(self, success_num):
        r"""Sets the success_num of this BatchBaselineIssueResponseResult.

        成功数量。

        :param success_num: The success_num of this BatchBaselineIssueResponseResult.
        :type success_num: int
        """
        self._success_num = success_num

    @property
    def fail_num(self):
        r"""Gets the fail_num of this BatchBaselineIssueResponseResult.

        失败数量。

        :return: The fail_num of this BatchBaselineIssueResponseResult.
        :rtype: int
        """
        return self._fail_num

    @fail_num.setter
    def fail_num(self, fail_num):
        r"""Sets the fail_num of this BatchBaselineIssueResponseResult.

        失败数量。

        :param fail_num: The fail_num of this BatchBaselineIssueResponseResult.
        :type fail_num: int
        """
        self._fail_num = fail_num

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
        if not isinstance(other, BatchBaselineIssueResponseResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
