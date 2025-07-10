# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesSeamlessOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'seamless_apply_path': 'str'
    }

    attribute_map = {
        'seamless_apply_path': 'seamless_apply_path'
    }

    def __init__(self, seamless_apply_path=None):
        r"""PoliciesSeamlessOptions

        The model defined in huaweicloud sdk

        :param seamless_apply_path: 软件路径。长度不能超过1000个字符。
        :type seamless_apply_path: str
        """
        
        

        self._seamless_apply_path = None
        self.discriminator = None

        if seamless_apply_path is not None:
            self.seamless_apply_path = seamless_apply_path

    @property
    def seamless_apply_path(self):
        r"""Gets the seamless_apply_path of this PoliciesSeamlessOptions.

        软件路径。长度不能超过1000个字符。

        :return: The seamless_apply_path of this PoliciesSeamlessOptions.
        :rtype: str
        """
        return self._seamless_apply_path

    @seamless_apply_path.setter
    def seamless_apply_path(self, seamless_apply_path):
        r"""Sets the seamless_apply_path of this PoliciesSeamlessOptions.

        软件路径。长度不能超过1000个字符。

        :param seamless_apply_path: The seamless_apply_path of this PoliciesSeamlessOptions.
        :type seamless_apply_path: str
        """
        self._seamless_apply_path = seamless_apply_path

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
        if not isinstance(other, PoliciesSeamlessOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
