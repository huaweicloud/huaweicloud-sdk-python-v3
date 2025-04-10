# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubtitleFiles:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'text_subtitle_file': 'SubtitleFileInfo',
        'audio_subtitle_file': 'SubtitleFileInfo'
    }

    attribute_map = {
        'text_subtitle_file': 'text_subtitle_file',
        'audio_subtitle_file': 'audio_subtitle_file'
    }

    def __init__(self, text_subtitle_file=None, audio_subtitle_file=None):
        r"""SubtitleFiles

        The model defined in huaweicloud sdk

        :param text_subtitle_file: 
        :type text_subtitle_file: :class:`huaweicloudsdkmetastudio.v1.SubtitleFileInfo`
        :param audio_subtitle_file: 
        :type audio_subtitle_file: :class:`huaweicloudsdkmetastudio.v1.SubtitleFileInfo`
        """
        
        

        self._text_subtitle_file = None
        self._audio_subtitle_file = None
        self.discriminator = None

        if text_subtitle_file is not None:
            self.text_subtitle_file = text_subtitle_file
        if audio_subtitle_file is not None:
            self.audio_subtitle_file = audio_subtitle_file

    @property
    def text_subtitle_file(self):
        r"""Gets the text_subtitle_file of this SubtitleFiles.

        :return: The text_subtitle_file of this SubtitleFiles.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.SubtitleFileInfo`
        """
        return self._text_subtitle_file

    @text_subtitle_file.setter
    def text_subtitle_file(self, text_subtitle_file):
        r"""Sets the text_subtitle_file of this SubtitleFiles.

        :param text_subtitle_file: The text_subtitle_file of this SubtitleFiles.
        :type text_subtitle_file: :class:`huaweicloudsdkmetastudio.v1.SubtitleFileInfo`
        """
        self._text_subtitle_file = text_subtitle_file

    @property
    def audio_subtitle_file(self):
        r"""Gets the audio_subtitle_file of this SubtitleFiles.

        :return: The audio_subtitle_file of this SubtitleFiles.
        :rtype: :class:`huaweicloudsdkmetastudio.v1.SubtitleFileInfo`
        """
        return self._audio_subtitle_file

    @audio_subtitle_file.setter
    def audio_subtitle_file(self, audio_subtitle_file):
        r"""Sets the audio_subtitle_file of this SubtitleFiles.

        :param audio_subtitle_file: The audio_subtitle_file of this SubtitleFiles.
        :type audio_subtitle_file: :class:`huaweicloudsdkmetastudio.v1.SubtitleFileInfo`
        """
        self._audio_subtitle_file = audio_subtitle_file

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
        if not isinstance(other, SubtitleFiles):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
