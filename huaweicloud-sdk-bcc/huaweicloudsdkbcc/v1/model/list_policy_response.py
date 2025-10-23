# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'bcc_policies': 'list[BccPolicy]'
    }

    attribute_map = {
        'count': 'count',
        'bcc_policies': 'bcc_policies'
    }

    def __init__(self, count=None, bcc_policies=None):
        r"""ListPolicyResponse

        The model defined in huaweicloud sdk

        :param count: count
        :type count: int
        :param bcc_policies: bccPolicies
        :type bcc_policies: list[:class:`huaweicloudsdkbcc.v1.BccPolicy`]
        """
        
        super(ListPolicyResponse, self).__init__()

        self._count = None
        self._bcc_policies = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if bcc_policies is not None:
            self.bcc_policies = bcc_policies

    @property
    def count(self):
        r"""Gets the count of this ListPolicyResponse.

        count

        :return: The count of this ListPolicyResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListPolicyResponse.

        count

        :param count: The count of this ListPolicyResponse.
        :type count: int
        """
        self._count = count

    @property
    def bcc_policies(self):
        r"""Gets the bcc_policies of this ListPolicyResponse.

        bccPolicies

        :return: The bcc_policies of this ListPolicyResponse.
        :rtype: list[:class:`huaweicloudsdkbcc.v1.BccPolicy`]
        """
        return self._bcc_policies

    @bcc_policies.setter
    def bcc_policies(self, bcc_policies):
        r"""Sets the bcc_policies of this ListPolicyResponse.

        bccPolicies

        :param bcc_policies: The bcc_policies of this ListPolicyResponse.
        :type bcc_policies: list[:class:`huaweicloudsdkbcc.v1.BccPolicy`]
        """
        self._bcc_policies = bcc_policies

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
        if not isinstance(other, ListPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
