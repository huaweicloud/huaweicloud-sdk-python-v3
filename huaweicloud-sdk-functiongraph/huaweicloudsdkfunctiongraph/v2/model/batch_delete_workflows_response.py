# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteWorkflowsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success': 'list[str]',
        'fail': 'list[OperateErrorInfo]'
    }

    attribute_map = {
        'success': 'success',
        'fail': 'fail'
    }

    def __init__(self, success=None, fail=None):
        """BatchDeleteWorkflowsResponse

        The model defined in huaweicloud sdk

        :param success: 成功流程URN列表
        :type success: list[str]
        :param fail: 错误流程详情
        :type fail: list[:class:`huaweicloudsdkfunctiongraph.v2.OperateErrorInfo`]
        """
        
        super(BatchDeleteWorkflowsResponse, self).__init__()

        self._success = None
        self._fail = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if fail is not None:
            self.fail = fail

    @property
    def success(self):
        """Gets the success of this BatchDeleteWorkflowsResponse.

        成功流程URN列表

        :return: The success of this BatchDeleteWorkflowsResponse.
        :rtype: list[str]
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this BatchDeleteWorkflowsResponse.

        成功流程URN列表

        :param success: The success of this BatchDeleteWorkflowsResponse.
        :type success: list[str]
        """
        self._success = success

    @property
    def fail(self):
        """Gets the fail of this BatchDeleteWorkflowsResponse.

        错误流程详情

        :return: The fail of this BatchDeleteWorkflowsResponse.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.OperateErrorInfo`]
        """
        return self._fail

    @fail.setter
    def fail(self, fail):
        """Sets the fail of this BatchDeleteWorkflowsResponse.

        错误流程详情

        :param fail: The fail of this BatchDeleteWorkflowsResponse.
        :type fail: list[:class:`huaweicloudsdkfunctiongraph.v2.OperateErrorInfo`]
        """
        self._fail = fail

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
        if not isinstance(other, BatchDeleteWorkflowsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
