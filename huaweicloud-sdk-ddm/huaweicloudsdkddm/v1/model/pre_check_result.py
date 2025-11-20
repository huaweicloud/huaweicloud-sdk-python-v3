# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PreCheckResult:

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
        'status': 'str',
        'note': 'str',
        'handling_suggestion': 'str',
        'error_message': 'str',
        'error_detail_message': 'str'
    }

    attribute_map = {
        'name': 'name',
        'status': 'status',
        'note': 'note',
        'handling_suggestion': 'handling_suggestion',
        'error_message': 'error_message',
        'error_detail_message': 'error_detail_message'
    }

    def __init__(self, name=None, status=None, note=None, handling_suggestion=None, error_message=None, error_detail_message=None):
        r"""PreCheckResult

        The model defined in huaweicloud sdk

        :param name: 检查项名称。
        :type name: str
        :param status: 检查项结果。
        :type status: str
        :param note: 检查项提示信息。
        :type note: str
        :param handling_suggestion: 处理建议。
        :type handling_suggestion: str
        :param error_message: 错误信息。
        :type error_message: str
        :param error_detail_message: 详细错误信息。
        :type error_detail_message: str
        """
        
        

        self._name = None
        self._status = None
        self._note = None
        self._handling_suggestion = None
        self._error_message = None
        self._error_detail_message = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if note is not None:
            self.note = note
        if handling_suggestion is not None:
            self.handling_suggestion = handling_suggestion
        if error_message is not None:
            self.error_message = error_message
        if error_detail_message is not None:
            self.error_detail_message = error_detail_message

    @property
    def name(self):
        r"""Gets the name of this PreCheckResult.

        检查项名称。

        :return: The name of this PreCheckResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PreCheckResult.

        检查项名称。

        :param name: The name of this PreCheckResult.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this PreCheckResult.

        检查项结果。

        :return: The status of this PreCheckResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this PreCheckResult.

        检查项结果。

        :param status: The status of this PreCheckResult.
        :type status: str
        """
        self._status = status

    @property
    def note(self):
        r"""Gets the note of this PreCheckResult.

        检查项提示信息。

        :return: The note of this PreCheckResult.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        r"""Sets the note of this PreCheckResult.

        检查项提示信息。

        :param note: The note of this PreCheckResult.
        :type note: str
        """
        self._note = note

    @property
    def handling_suggestion(self):
        r"""Gets the handling_suggestion of this PreCheckResult.

        处理建议。

        :return: The handling_suggestion of this PreCheckResult.
        :rtype: str
        """
        return self._handling_suggestion

    @handling_suggestion.setter
    def handling_suggestion(self, handling_suggestion):
        r"""Sets the handling_suggestion of this PreCheckResult.

        处理建议。

        :param handling_suggestion: The handling_suggestion of this PreCheckResult.
        :type handling_suggestion: str
        """
        self._handling_suggestion = handling_suggestion

    @property
    def error_message(self):
        r"""Gets the error_message of this PreCheckResult.

        错误信息。

        :return: The error_message of this PreCheckResult.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this PreCheckResult.

        错误信息。

        :param error_message: The error_message of this PreCheckResult.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def error_detail_message(self):
        r"""Gets the error_detail_message of this PreCheckResult.

        详细错误信息。

        :return: The error_detail_message of this PreCheckResult.
        :rtype: str
        """
        return self._error_detail_message

    @error_detail_message.setter
    def error_detail_message(self, error_detail_message):
        r"""Sets the error_detail_message of this PreCheckResult.

        详细错误信息。

        :param error_detail_message: The error_detail_message of this PreCheckResult.
        :type error_detail_message: str
        """
        self._error_detail_message = error_detail_message

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PreCheckResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
