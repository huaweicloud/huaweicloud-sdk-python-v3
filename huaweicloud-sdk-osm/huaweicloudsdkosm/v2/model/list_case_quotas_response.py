# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCaseQuotasResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'un_used': 'int'
    }

    attribute_map = {
        'total': 'total',
        'un_used': 'un_used'
    }

    def __init__(self, total=None, un_used=None):
        """ListCaseQuotasResponse

        The model defined in huaweicloud sdk

        :param total: 总配额
        :type total: int
        :param un_used: 未使用
        :type un_used: int
        """
        
        super(ListCaseQuotasResponse, self).__init__()

        self._total = None
        self._un_used = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if un_used is not None:
            self.un_used = un_used

    @property
    def total(self):
        """Gets the total of this ListCaseQuotasResponse.

        总配额

        :return: The total of this ListCaseQuotasResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListCaseQuotasResponse.

        总配额

        :param total: The total of this ListCaseQuotasResponse.
        :type total: int
        """
        self._total = total

    @property
    def un_used(self):
        """Gets the un_used of this ListCaseQuotasResponse.

        未使用

        :return: The un_used of this ListCaseQuotasResponse.
        :rtype: int
        """
        return self._un_used

    @un_used.setter
    def un_used(self, un_used):
        """Sets the un_used of this ListCaseQuotasResponse.

        未使用

        :param un_used: The un_used of this ListCaseQuotasResponse.
        :type un_used: int
        """
        self._un_used = un_used

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
        if not isinstance(other, ListCaseQuotasResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
