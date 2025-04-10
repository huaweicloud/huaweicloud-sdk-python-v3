# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InputAudioSelector:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'selector_settings': 'AudioSelectorSettings'
    }

    attribute_map = {
        'name': 'name',
        'selector_settings': 'selector_settings'
    }

    def __init__(self, name=None, selector_settings=None):
        r"""InputAudioSelector

        The model defined in huaweicloud sdk

        :param name: 音频选择器的名称。仅支持大小写字母、数字、中划线和下划线。  同一个频道中每个选择器的名称需要唯一。
        :type name: str
        :param selector_settings: 
        :type selector_settings: :class:`huaweicloudsdklive.v1.AudioSelectorSettings`
        """
        
        

        self._name = None
        self._selector_settings = None
        self.discriminator = None

        self.name = name
        if selector_settings is not None:
            self.selector_settings = selector_settings

    @property
    def name(self):
        r"""Gets the name of this InputAudioSelector.

        音频选择器的名称。仅支持大小写字母、数字、中划线和下划线。  同一个频道中每个选择器的名称需要唯一。

        :return: The name of this InputAudioSelector.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this InputAudioSelector.

        音频选择器的名称。仅支持大小写字母、数字、中划线和下划线。  同一个频道中每个选择器的名称需要唯一。

        :param name: The name of this InputAudioSelector.
        :type name: str
        """
        self._name = name

    @property
    def selector_settings(self):
        r"""Gets the selector_settings of this InputAudioSelector.

        :return: The selector_settings of this InputAudioSelector.
        :rtype: :class:`huaweicloudsdklive.v1.AudioSelectorSettings`
        """
        return self._selector_settings

    @selector_settings.setter
    def selector_settings(self, selector_settings):
        r"""Sets the selector_settings of this InputAudioSelector.

        :param selector_settings: The selector_settings of this InputAudioSelector.
        :type selector_settings: :class:`huaweicloudsdklive.v1.AudioSelectorSettings`
        """
        self._selector_settings = selector_settings

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
        if not isinstance(other, InputAudioSelector):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
