# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEpConfigsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'support_item': 'EnterpriseProjectConfig'
    }

    attribute_map = {
        'support_item': 'support_item'
    }

    def __init__(self, support_item=None):
        r"""ShowEpConfigsResponse

        The model defined in huaweicloud sdk

        :param support_item: 
        :type support_item: :class:`huaweicloudsdkeps.v1.EnterpriseProjectConfig`
        """
        
        super(ShowEpConfigsResponse, self).__init__()

        self._support_item = None
        self.discriminator = None

        if support_item is not None:
            self.support_item = support_item

    @property
    def support_item(self):
        r"""Gets the support_item of this ShowEpConfigsResponse.

        :return: The support_item of this ShowEpConfigsResponse.
        :rtype: :class:`huaweicloudsdkeps.v1.EnterpriseProjectConfig`
        """
        return self._support_item

    @support_item.setter
    def support_item(self, support_item):
        r"""Sets the support_item of this ShowEpConfigsResponse.

        :param support_item: The support_item of this ShowEpConfigsResponse.
        :type support_item: :class:`huaweicloudsdkeps.v1.EnterpriseProjectConfig`
        """
        self._support_item = support_item

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
        if not isinstance(other, ShowEpConfigsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
