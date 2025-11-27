# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListReplicationErrorsResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'occur_time': 'str',
        'source_type_id': 'str',
        'source_name': 'str',
        'error_code': 'str',
        'error_text': 'str'
    }

    attribute_map = {
        'occur_time': 'occur_time',
        'source_type_id': 'source_type_id',
        'source_name': 'source_name',
        'error_code': 'error_code',
        'error_text': 'error_text'
    }

    def __init__(self, occur_time=None, source_type_id=None, source_name=None, error_code=None, error_text=None):
        r"""ListReplicationErrorsResult

        The model defined in huaweicloud sdk

        :param occur_time: 报错发生时间。
        :type occur_time: str
        :param source_type_id: 错误源类型id。
        :type source_type_id: str
        :param source_name: 错误源名称。
        :type source_name: str
        :param error_code: 错误代码。
        :type error_code: str
        :param error_text: 错误消息。
        :type error_text: str
        """
        
        

        self._occur_time = None
        self._source_type_id = None
        self._source_name = None
        self._error_code = None
        self._error_text = None
        self.discriminator = None

        if occur_time is not None:
            self.occur_time = occur_time
        if source_type_id is not None:
            self.source_type_id = source_type_id
        if source_name is not None:
            self.source_name = source_name
        if error_code is not None:
            self.error_code = error_code
        if error_text is not None:
            self.error_text = error_text

    @property
    def occur_time(self):
        r"""Gets the occur_time of this ListReplicationErrorsResult.

        报错发生时间。

        :return: The occur_time of this ListReplicationErrorsResult.
        :rtype: str
        """
        return self._occur_time

    @occur_time.setter
    def occur_time(self, occur_time):
        r"""Sets the occur_time of this ListReplicationErrorsResult.

        报错发生时间。

        :param occur_time: The occur_time of this ListReplicationErrorsResult.
        :type occur_time: str
        """
        self._occur_time = occur_time

    @property
    def source_type_id(self):
        r"""Gets the source_type_id of this ListReplicationErrorsResult.

        错误源类型id。

        :return: The source_type_id of this ListReplicationErrorsResult.
        :rtype: str
        """
        return self._source_type_id

    @source_type_id.setter
    def source_type_id(self, source_type_id):
        r"""Sets the source_type_id of this ListReplicationErrorsResult.

        错误源类型id。

        :param source_type_id: The source_type_id of this ListReplicationErrorsResult.
        :type source_type_id: str
        """
        self._source_type_id = source_type_id

    @property
    def source_name(self):
        r"""Gets the source_name of this ListReplicationErrorsResult.

        错误源名称。

        :return: The source_name of this ListReplicationErrorsResult.
        :rtype: str
        """
        return self._source_name

    @source_name.setter
    def source_name(self, source_name):
        r"""Sets the source_name of this ListReplicationErrorsResult.

        错误源名称。

        :param source_name: The source_name of this ListReplicationErrorsResult.
        :type source_name: str
        """
        self._source_name = source_name

    @property
    def error_code(self):
        r"""Gets the error_code of this ListReplicationErrorsResult.

        错误代码。

        :return: The error_code of this ListReplicationErrorsResult.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this ListReplicationErrorsResult.

        错误代码。

        :param error_code: The error_code of this ListReplicationErrorsResult.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def error_text(self):
        r"""Gets the error_text of this ListReplicationErrorsResult.

        错误消息。

        :return: The error_text of this ListReplicationErrorsResult.
        :rtype: str
        """
        return self._error_text

    @error_text.setter
    def error_text(self, error_text):
        r"""Sets the error_text of this ListReplicationErrorsResult.

        错误消息。

        :param error_text: The error_text of this ListReplicationErrorsResult.
        :type error_text: str
        """
        self._error_text = error_text

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
        if not isinstance(other, ListReplicationErrorsResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
