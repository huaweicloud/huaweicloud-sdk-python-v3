# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImportErrorMessageResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sheet_name': 'str',
        'row_rum': 'str',
        'value': 'str',
        'error_message': 'str'
    }

    attribute_map = {
        'sheet_name': 'sheet_name',
        'row_rum': 'row_rum',
        'value': 'value',
        'error_message': 'error_message'
    }

    def __init__(self, sheet_name=None, row_rum=None, value=None, error_message=None):
        """ImportErrorMessageResp

        The model defined in huaweicloud sdk

        :param sheet_name: sheet名称。
        :type sheet_name: str
        :param row_rum: 行号。
        :type row_rum: str
        :param value: 字段值。
        :type value: str
        :param error_message: 错误信息。
        :type error_message: str
        """
        
        

        self._sheet_name = None
        self._row_rum = None
        self._value = None
        self._error_message = None
        self.discriminator = None

        if sheet_name is not None:
            self.sheet_name = sheet_name
        if row_rum is not None:
            self.row_rum = row_rum
        if value is not None:
            self.value = value
        if error_message is not None:
            self.error_message = error_message

    @property
    def sheet_name(self):
        """Gets the sheet_name of this ImportErrorMessageResp.

        sheet名称。

        :return: The sheet_name of this ImportErrorMessageResp.
        :rtype: str
        """
        return self._sheet_name

    @sheet_name.setter
    def sheet_name(self, sheet_name):
        """Sets the sheet_name of this ImportErrorMessageResp.

        sheet名称。

        :param sheet_name: The sheet_name of this ImportErrorMessageResp.
        :type sheet_name: str
        """
        self._sheet_name = sheet_name

    @property
    def row_rum(self):
        """Gets the row_rum of this ImportErrorMessageResp.

        行号。

        :return: The row_rum of this ImportErrorMessageResp.
        :rtype: str
        """
        return self._row_rum

    @row_rum.setter
    def row_rum(self, row_rum):
        """Sets the row_rum of this ImportErrorMessageResp.

        行号。

        :param row_rum: The row_rum of this ImportErrorMessageResp.
        :type row_rum: str
        """
        self._row_rum = row_rum

    @property
    def value(self):
        """Gets the value of this ImportErrorMessageResp.

        字段值。

        :return: The value of this ImportErrorMessageResp.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this ImportErrorMessageResp.

        字段值。

        :param value: The value of this ImportErrorMessageResp.
        :type value: str
        """
        self._value = value

    @property
    def error_message(self):
        """Gets the error_message of this ImportErrorMessageResp.

        错误信息。

        :return: The error_message of this ImportErrorMessageResp.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this ImportErrorMessageResp.

        错误信息。

        :param error_message: The error_message of this ImportErrorMessageResp.
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
        if not isinstance(other, ImportErrorMessageResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
