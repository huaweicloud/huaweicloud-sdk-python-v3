# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PostCustomTTSReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'text': 'str',
        'config': 'TtsConfig'
    }

    attribute_map = {
        'text': 'text',
        'config': 'config'
    }

    def __init__(self, text=None, config=None):
        r"""PostCustomTTSReq

        The model defined in huaweicloud sdk

        :param text: 待合成的文本，文本长度限制小于500字符。
        :type text: str
        :param config: 
        :type config: :class:`huaweicloudsdksis.v1.TtsConfig`
        """
        
        

        self._text = None
        self._config = None
        self.discriminator = None

        self.text = text
        if config is not None:
            self.config = config

    @property
    def text(self):
        r"""Gets the text of this PostCustomTTSReq.

        待合成的文本，文本长度限制小于500字符。

        :return: The text of this PostCustomTTSReq.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        r"""Sets the text of this PostCustomTTSReq.

        待合成的文本，文本长度限制小于500字符。

        :param text: The text of this PostCustomTTSReq.
        :type text: str
        """
        self._text = text

    @property
    def config(self):
        r"""Gets the config of this PostCustomTTSReq.

        :return: The config of this PostCustomTTSReq.
        :rtype: :class:`huaweicloudsdksis.v1.TtsConfig`
        """
        return self._config

    @config.setter
    def config(self, config):
        r"""Sets the config of this PostCustomTTSReq.

        :param config: The config of this PostCustomTTSReq.
        :type config: :class:`huaweicloudsdksis.v1.TtsConfig`
        """
        self._config = config

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
        if not isinstance(other, PostCustomTTSReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
