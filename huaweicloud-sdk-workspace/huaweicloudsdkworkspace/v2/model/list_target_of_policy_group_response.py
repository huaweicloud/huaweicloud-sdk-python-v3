# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTargetOfPolicyGroupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'targets': 'list[Target]',
        'total_count': 'int'
    }

    attribute_map = {
        'targets': 'targets',
        'total_count': 'total_count'
    }

    def __init__(self, targets=None, total_count=None):
        r"""ListTargetOfPolicyGroupResponse

        The model defined in huaweicloud sdk

        :param targets: 应用对象列表。
        :type targets: list[:class:`huaweicloudsdkworkspace.v2.Target`]
        :param total_count: 用户列表数量。
        :type total_count: int
        """
        
        super(ListTargetOfPolicyGroupResponse, self).__init__()

        self._targets = None
        self._total_count = None
        self.discriminator = None

        if targets is not None:
            self.targets = targets
        if total_count is not None:
            self.total_count = total_count

    @property
    def targets(self):
        r"""Gets the targets of this ListTargetOfPolicyGroupResponse.

        应用对象列表。

        :return: The targets of this ListTargetOfPolicyGroupResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Target`]
        """
        return self._targets

    @targets.setter
    def targets(self, targets):
        r"""Sets the targets of this ListTargetOfPolicyGroupResponse.

        应用对象列表。

        :param targets: The targets of this ListTargetOfPolicyGroupResponse.
        :type targets: list[:class:`huaweicloudsdkworkspace.v2.Target`]
        """
        self._targets = targets

    @property
    def total_count(self):
        r"""Gets the total_count of this ListTargetOfPolicyGroupResponse.

        用户列表数量。

        :return: The total_count of this ListTargetOfPolicyGroupResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListTargetOfPolicyGroupResponse.

        用户列表数量。

        :param total_count: The total_count of this ListTargetOfPolicyGroupResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListTargetOfPolicyGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
