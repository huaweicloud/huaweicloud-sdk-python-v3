# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RemediationExecutionStatusesSummaryRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_keys': 'list[RemediationResourceKey]'
    }

    attribute_map = {
        'resource_keys': 'resource_keys'
    }

    def __init__(self, resource_keys=None):
        r"""RemediationExecutionStatusesSummaryRequestBody

        The model defined in huaweicloud sdk

        :param resource_keys: 合规规则最新修正记录查询条件列表。
        :type resource_keys: list[:class:`huaweicloudsdkconfig.v1.RemediationResourceKey`]
        """
        
        

        self._resource_keys = None
        self.discriminator = None

        self.resource_keys = resource_keys

    @property
    def resource_keys(self):
        r"""Gets the resource_keys of this RemediationExecutionStatusesSummaryRequestBody.

        合规规则最新修正记录查询条件列表。

        :return: The resource_keys of this RemediationExecutionStatusesSummaryRequestBody.
        :rtype: list[:class:`huaweicloudsdkconfig.v1.RemediationResourceKey`]
        """
        return self._resource_keys

    @resource_keys.setter
    def resource_keys(self, resource_keys):
        r"""Sets the resource_keys of this RemediationExecutionStatusesSummaryRequestBody.

        合规规则最新修正记录查询条件列表。

        :param resource_keys: The resource_keys of this RemediationExecutionStatusesSummaryRequestBody.
        :type resource_keys: list[:class:`huaweicloudsdkconfig.v1.RemediationResourceKey`]
        """
        self._resource_keys = resource_keys

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
        if not isinstance(other, RemediationExecutionStatusesSummaryRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
