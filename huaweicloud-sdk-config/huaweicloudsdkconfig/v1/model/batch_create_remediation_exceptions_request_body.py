# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateRemediationExceptionsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'exceptions': 'list[RemediationExceptionRequest]'
    }

    attribute_map = {
        'exceptions': 'exceptions'
    }

    def __init__(self, exceptions=None):
        r"""BatchCreateRemediationExceptionsRequestBody

        The model defined in huaweicloud sdk

        :param exceptions: 批量创建合规规则修正例外的详情。
        :type exceptions: list[:class:`huaweicloudsdkconfig.v1.RemediationExceptionRequest`]
        """
        
        

        self._exceptions = None
        self.discriminator = None

        self.exceptions = exceptions

    @property
    def exceptions(self):
        r"""Gets the exceptions of this BatchCreateRemediationExceptionsRequestBody.

        批量创建合规规则修正例外的详情。

        :return: The exceptions of this BatchCreateRemediationExceptionsRequestBody.
        :rtype: list[:class:`huaweicloudsdkconfig.v1.RemediationExceptionRequest`]
        """
        return self._exceptions

    @exceptions.setter
    def exceptions(self, exceptions):
        r"""Sets the exceptions of this BatchCreateRemediationExceptionsRequestBody.

        批量创建合规规则修正例外的详情。

        :param exceptions: The exceptions of this BatchCreateRemediationExceptionsRequestBody.
        :type exceptions: list[:class:`huaweicloudsdkconfig.v1.RemediationExceptionRequest`]
        """
        self._exceptions = exceptions

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
        if not isinstance(other, BatchCreateRemediationExceptionsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
