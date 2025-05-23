# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAutoUpgradePolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'switch_option': 'bool'
    }

    attribute_map = {
        'switch_option': 'switch_option'
    }

    def __init__(self, switch_option=None):
        r"""ShowAutoUpgradePolicyResponse

        The model defined in huaweicloud sdk

        :param switch_option: 自动小版本升级开关选项 true：打开自动小版本升级 false：关闭自动小版本升级
        :type switch_option: bool
        """
        
        super(ShowAutoUpgradePolicyResponse, self).__init__()

        self._switch_option = None
        self.discriminator = None

        if switch_option is not None:
            self.switch_option = switch_option

    @property
    def switch_option(self):
        r"""Gets the switch_option of this ShowAutoUpgradePolicyResponse.

        自动小版本升级开关选项 true：打开自动小版本升级 false：关闭自动小版本升级

        :return: The switch_option of this ShowAutoUpgradePolicyResponse.
        :rtype: bool
        """
        return self._switch_option

    @switch_option.setter
    def switch_option(self, switch_option):
        r"""Sets the switch_option of this ShowAutoUpgradePolicyResponse.

        自动小版本升级开关选项 true：打开自动小版本升级 false：关闭自动小版本升级

        :param switch_option: The switch_option of this ShowAutoUpgradePolicyResponse.
        :type switch_option: bool
        """
        self._switch_option = switch_option

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
        if not isinstance(other, ShowAutoUpgradePolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
