# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDisassociateThrottlingPolicyV2Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'success_count': 'int',
        'failure': 'list[ThrottleBindingBatchFailure]'
    }

    attribute_map = {
        'success_count': 'success_count',
        'failure': 'failure'
    }

    def __init__(self, success_count=None, failure=None):
        """BatchDisassociateThrottlingPolicyV2Response

        The model defined in huaweicloud sdk

        :param success_count: 成功解除绑定的API和流控策略绑定关系的数量
        :type success_count: int
        :param failure: 解除绑定失败的API和流控绑定关系及错误信息
        :type failure: list[:class:`huaweicloudsdkapig.v2.ThrottleBindingBatchFailure`]
        """
        
        super(BatchDisassociateThrottlingPolicyV2Response, self).__init__()

        self._success_count = None
        self._failure = None
        self.discriminator = None

        if success_count is not None:
            self.success_count = success_count
        if failure is not None:
            self.failure = failure

    @property
    def success_count(self):
        """Gets the success_count of this BatchDisassociateThrottlingPolicyV2Response.

        成功解除绑定的API和流控策略绑定关系的数量

        :return: The success_count of this BatchDisassociateThrottlingPolicyV2Response.
        :rtype: int
        """
        return self._success_count

    @success_count.setter
    def success_count(self, success_count):
        """Sets the success_count of this BatchDisassociateThrottlingPolicyV2Response.

        成功解除绑定的API和流控策略绑定关系的数量

        :param success_count: The success_count of this BatchDisassociateThrottlingPolicyV2Response.
        :type success_count: int
        """
        self._success_count = success_count

    @property
    def failure(self):
        """Gets the failure of this BatchDisassociateThrottlingPolicyV2Response.

        解除绑定失败的API和流控绑定关系及错误信息

        :return: The failure of this BatchDisassociateThrottlingPolicyV2Response.
        :rtype: list[:class:`huaweicloudsdkapig.v2.ThrottleBindingBatchFailure`]
        """
        return self._failure

    @failure.setter
    def failure(self, failure):
        """Sets the failure of this BatchDisassociateThrottlingPolicyV2Response.

        解除绑定失败的API和流控绑定关系及错误信息

        :param failure: The failure of this BatchDisassociateThrottlingPolicyV2Response.
        :type failure: list[:class:`huaweicloudsdkapig.v2.ThrottleBindingBatchFailure`]
        """
        self._failure = failure

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
        if not isinstance(other, BatchDisassociateThrottlingPolicyV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
