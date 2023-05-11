# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListL7policiesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'l7policies': 'list[L7policyResp]'
    }

    attribute_map = {
        'l7policies': 'l7policies'
    }

    def __init__(self, l7policies=None):
        """ListL7policiesResponse

        The model defined in huaweicloud sdk

        :param l7policies: 转发策略对象的列表
        :type l7policies: list[:class:`huaweicloudsdkelb.v2.L7policyResp`]
        """
        
        super(ListL7policiesResponse, self).__init__()

        self._l7policies = None
        self.discriminator = None

        if l7policies is not None:
            self.l7policies = l7policies

    @property
    def l7policies(self):
        """Gets the l7policies of this ListL7policiesResponse.

        转发策略对象的列表

        :return: The l7policies of this ListL7policiesResponse.
        :rtype: list[:class:`huaweicloudsdkelb.v2.L7policyResp`]
        """
        return self._l7policies

    @l7policies.setter
    def l7policies(self, l7policies):
        """Sets the l7policies of this ListL7policiesResponse.

        转发策略对象的列表

        :param l7policies: The l7policies of this ListL7policiesResponse.
        :type l7policies: list[:class:`huaweicloudsdkelb.v2.L7policyResp`]
        """
        self._l7policies = l7policies

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
        if not isinstance(other, ListL7policiesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
