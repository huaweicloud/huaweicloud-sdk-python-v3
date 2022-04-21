# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunModerationAudioRequestBodyConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'format': 'str',
        '_property': 'str'
    }

    attribute_map = {
        'format': 'format',
        '_property': 'property'
    }

    def __init__(self, format=None, _property=None):
        """RunModerationAudioRequestBodyConfig

        The model defined in huaweicloud sdk

        :param format: 支持的语音格式
        :type format: str
        :param _property: 所使用的模型特征串。通常是 “语种_采样率_领域”的形式。 采样率需要与音频采样率保持一致。 当前支持如下模型特征串：   chinese_8k_common   chinese_16k_common 
        :type _property: str
        """
        
        

        self._format = None
        self.__property = None
        self.discriminator = None

        self.format = format
        self._property = _property

    @property
    def format(self):
        """Gets the format of this RunModerationAudioRequestBodyConfig.

        支持的语音格式

        :return: The format of this RunModerationAudioRequestBodyConfig.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this RunModerationAudioRequestBodyConfig.

        支持的语音格式

        :param format: The format of this RunModerationAudioRequestBodyConfig.
        :type format: str
        """
        self._format = format

    @property
    def _property(self):
        """Gets the _property of this RunModerationAudioRequestBodyConfig.

        所使用的模型特征串。通常是 “语种_采样率_领域”的形式。 采样率需要与音频采样率保持一致。 当前支持如下模型特征串：   chinese_8k_common   chinese_16k_common 

        :return: The _property of this RunModerationAudioRequestBodyConfig.
        :rtype: str
        """
        return self.__property

    @_property.setter
    def _property(self, _property):
        """Sets the _property of this RunModerationAudioRequestBodyConfig.

        所使用的模型特征串。通常是 “语种_采样率_领域”的形式。 采样率需要与音频采样率保持一致。 当前支持如下模型特征串：   chinese_8k_common   chinese_16k_common 

        :param _property: The _property of this RunModerationAudioRequestBodyConfig.
        :type _property: str
        """
        self.__property = _property

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
        if not isinstance(other, RunModerationAudioRequestBodyConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
