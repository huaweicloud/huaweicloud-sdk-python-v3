# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ErrorDetailInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'failed': 'list[ErrorCaseInfoBean]'
    }

    attribute_map = {
        'failed': 'failed'
    }

    def __init__(self, failed=None):
        r"""ErrorDetailInfo

        The model defined in huaweicloud sdk

        :param failed: 批量操作失败的资源的详情信息
        :type failed: list[:class:`huaweicloudsdkcloudtest.v1.ErrorCaseInfoBean`]
        """
        
        

        self._failed = None
        self.discriminator = None

        if failed is not None:
            self.failed = failed

    @property
    def failed(self):
        r"""Gets the failed of this ErrorDetailInfo.

        批量操作失败的资源的详情信息

        :return: The failed of this ErrorDetailInfo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.ErrorCaseInfoBean`]
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        r"""Sets the failed of this ErrorDetailInfo.

        批量操作失败的资源的详情信息

        :param failed: The failed of this ErrorDetailInfo.
        :type failed: list[:class:`huaweicloudsdkcloudtest.v1.ErrorCaseInfoBean`]
        """
        self._failed = failed

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
        if not isinstance(other, ErrorDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
