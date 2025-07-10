# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListControlViolationsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'control_violations': 'list[ControlViolation]'
    }

    attribute_map = {
        'control_violations': 'control_violations'
    }

    def __init__(self, control_violations=None):
        r"""ListControlViolationsResponse

        The model defined in huaweicloud sdk

        :param control_violations: 控制策略合规性。
        :type control_violations: list[:class:`huaweicloudsdkrgc.v1.ControlViolation`]
        """
        
        super(ListControlViolationsResponse, self).__init__()

        self._control_violations = None
        self.discriminator = None

        if control_violations is not None:
            self.control_violations = control_violations

    @property
    def control_violations(self):
        r"""Gets the control_violations of this ListControlViolationsResponse.

        控制策略合规性。

        :return: The control_violations of this ListControlViolationsResponse.
        :rtype: list[:class:`huaweicloudsdkrgc.v1.ControlViolation`]
        """
        return self._control_violations

    @control_violations.setter
    def control_violations(self, control_violations):
        r"""Sets the control_violations of this ListControlViolationsResponse.

        控制策略合规性。

        :param control_violations: The control_violations of this ListControlViolationsResponse.
        :type control_violations: list[:class:`huaweicloudsdkrgc.v1.ControlViolation`]
        """
        self._control_violations = control_violations

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
        if not isinstance(other, ListControlViolationsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
