# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuditResultSystemAuditResultErrors:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'audio_name': 'str',
        'text_name': 'str',
        'error_code': 'str',
        'error_message': 'str'
    }

    attribute_map = {
        'audio_name': 'audio_name',
        'text_name': 'text_name',
        'error_code': 'error_code',
        'error_message': 'error_message'
    }

    def __init__(self, audio_name=None, text_name=None, error_code=None, error_message=None):
        r"""AuditResultSystemAuditResultErrors

        The model defined in huaweicloud sdk

        :param audio_name: 音频文件名。
        :type audio_name: str
        :param text_name: 文本文件名。
        :type text_name: str
        :param error_code: 异常错误码。
        :type error_code: str
        :param error_message: 异常错误信息。
        :type error_message: str
        """
        
        

        self._audio_name = None
        self._text_name = None
        self._error_code = None
        self._error_message = None
        self.discriminator = None

        if audio_name is not None:
            self.audio_name = audio_name
        if text_name is not None:
            self.text_name = text_name
        if error_code is not None:
            self.error_code = error_code
        if error_message is not None:
            self.error_message = error_message

    @property
    def audio_name(self):
        r"""Gets the audio_name of this AuditResultSystemAuditResultErrors.

        音频文件名。

        :return: The audio_name of this AuditResultSystemAuditResultErrors.
        :rtype: str
        """
        return self._audio_name

    @audio_name.setter
    def audio_name(self, audio_name):
        r"""Sets the audio_name of this AuditResultSystemAuditResultErrors.

        音频文件名。

        :param audio_name: The audio_name of this AuditResultSystemAuditResultErrors.
        :type audio_name: str
        """
        self._audio_name = audio_name

    @property
    def text_name(self):
        r"""Gets the text_name of this AuditResultSystemAuditResultErrors.

        文本文件名。

        :return: The text_name of this AuditResultSystemAuditResultErrors.
        :rtype: str
        """
        return self._text_name

    @text_name.setter
    def text_name(self, text_name):
        r"""Sets the text_name of this AuditResultSystemAuditResultErrors.

        文本文件名。

        :param text_name: The text_name of this AuditResultSystemAuditResultErrors.
        :type text_name: str
        """
        self._text_name = text_name

    @property
    def error_code(self):
        r"""Gets the error_code of this AuditResultSystemAuditResultErrors.

        异常错误码。

        :return: The error_code of this AuditResultSystemAuditResultErrors.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this AuditResultSystemAuditResultErrors.

        异常错误码。

        :param error_code: The error_code of this AuditResultSystemAuditResultErrors.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_message(self):
        r"""Gets the error_message of this AuditResultSystemAuditResultErrors.

        异常错误信息。

        :return: The error_message of this AuditResultSystemAuditResultErrors.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this AuditResultSystemAuditResultErrors.

        异常错误信息。

        :param error_message: The error_message of this AuditResultSystemAuditResultErrors.
        :type error_message: str
        """
        self._error_message = error_message

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
        if not isinstance(other, AuditResultSystemAuditResultErrors):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
