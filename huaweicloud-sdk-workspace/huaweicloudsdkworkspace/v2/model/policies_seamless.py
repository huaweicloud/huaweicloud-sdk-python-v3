# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesSeamless:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'seamless_enable': 'bool',
        'options': 'PoliciesSeamlessOptions'
    }

    attribute_map = {
        'seamless_enable': 'seamless_enable',
        'options': 'options'
    }

    def __init__(self, seamless_enable=None, options=None):
        r"""PoliciesSeamless

        The model defined in huaweicloud sdk

        :param seamless_enable: 是否开启通用音视频开关。取值为： false：表示关闭。 true：表示开启。
        :type seamless_enable: bool
        :param options: 
        :type options: :class:`huaweicloudsdkworkspace.v2.PoliciesSeamlessOptions`
        """
        
        

        self._seamless_enable = None
        self._options = None
        self.discriminator = None

        if seamless_enable is not None:
            self.seamless_enable = seamless_enable
        if options is not None:
            self.options = options

    @property
    def seamless_enable(self):
        r"""Gets the seamless_enable of this PoliciesSeamless.

        是否开启通用音视频开关。取值为： false：表示关闭。 true：表示开启。

        :return: The seamless_enable of this PoliciesSeamless.
        :rtype: bool
        """
        return self._seamless_enable

    @seamless_enable.setter
    def seamless_enable(self, seamless_enable):
        r"""Sets the seamless_enable of this PoliciesSeamless.

        是否开启通用音视频开关。取值为： false：表示关闭。 true：表示开启。

        :param seamless_enable: The seamless_enable of this PoliciesSeamless.
        :type seamless_enable: bool
        """
        self._seamless_enable = seamless_enable

    @property
    def options(self):
        r"""Gets the options of this PoliciesSeamless.

        :return: The options of this PoliciesSeamless.
        :rtype: :class:`huaweicloudsdkworkspace.v2.PoliciesSeamlessOptions`
        """
        return self._options

    @options.setter
    def options(self, options):
        r"""Sets the options of this PoliciesSeamless.

        :param options: The options of this PoliciesSeamless.
        :type options: :class:`huaweicloudsdkworkspace.v2.PoliciesSeamlessOptions`
        """
        self._options = options

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
        if not isinstance(other, PoliciesSeamless):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
