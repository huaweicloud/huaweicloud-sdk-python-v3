# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DisableTheJobRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'reason': 'str',
        'disabled': 'bool'
    }

    attribute_map = {
        'reason': 'reason',
        'disabled': 'disabled'
    }

    def __init__(self, reason=None, disabled=None):
        r"""DisableTheJobRequestBody

        The model defined in huaweicloud sdk

        :param reason: 禁用原因
        :type reason: str
        :param disabled: 是否禁用
        :type disabled: bool
        """
        
        

        self._reason = None
        self._disabled = None
        self.discriminator = None

        if reason is not None:
            self.reason = reason
        self.disabled = disabled

    @property
    def reason(self):
        r"""Gets the reason of this DisableTheJobRequestBody.

        禁用原因

        :return: The reason of this DisableTheJobRequestBody.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this DisableTheJobRequestBody.

        禁用原因

        :param reason: The reason of this DisableTheJobRequestBody.
        :type reason: str
        """
        self._reason = reason

    @property
    def disabled(self):
        r"""Gets the disabled of this DisableTheJobRequestBody.

        是否禁用

        :return: The disabled of this DisableTheJobRequestBody.
        :rtype: bool
        """
        return self._disabled

    @disabled.setter
    def disabled(self, disabled):
        r"""Sets the disabled of this DisableTheJobRequestBody.

        是否禁用

        :param disabled: The disabled of this DisableTheJobRequestBody.
        :type disabled: bool
        """
        self._disabled = disabled

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
        if not isinstance(other, DisableTheJobRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
