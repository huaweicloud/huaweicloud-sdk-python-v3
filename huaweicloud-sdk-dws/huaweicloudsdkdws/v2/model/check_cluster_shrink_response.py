# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckClusterShrinkResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_passed': 'bool'
    }

    attribute_map = {
        'is_passed': 'is_passed'
    }

    def __init__(self, is_passed=None):
        r"""CheckClusterShrinkResponse

        The model defined in huaweicloud sdk

        :param is_passed: **参数解释**： 检查是否通过。如不通过，需要调整缩容节点数重试，或者是当前集群就不满足缩容前置条件。 **取值范围**： 不涉及。
        :type is_passed: bool
        """
        
        super(CheckClusterShrinkResponse, self).__init__()

        self._is_passed = None
        self.discriminator = None

        if is_passed is not None:
            self.is_passed = is_passed

    @property
    def is_passed(self):
        r"""Gets the is_passed of this CheckClusterShrinkResponse.

        **参数解释**： 检查是否通过。如不通过，需要调整缩容节点数重试，或者是当前集群就不满足缩容前置条件。 **取值范围**： 不涉及。

        :return: The is_passed of this CheckClusterShrinkResponse.
        :rtype: bool
        """
        return self._is_passed

    @is_passed.setter
    def is_passed(self, is_passed):
        r"""Sets the is_passed of this CheckClusterShrinkResponse.

        **参数解释**： 检查是否通过。如不通过，需要调整缩容节点数重试，或者是当前集群就不满足缩容前置条件。 **取值范围**： 不涉及。

        :param is_passed: The is_passed of this CheckClusterShrinkResponse.
        :type is_passed: bool
        """
        self._is_passed = is_passed

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
        if not isinstance(other, CheckClusterShrinkResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
