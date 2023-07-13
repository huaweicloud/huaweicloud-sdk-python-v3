# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunSqlConversionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_support_conversion': 'bool',
        'converted_sql_statement': 'str',
        'unsupported_items': 'list[UnSupportedItem]'
    }

    attribute_map = {
        'is_support_conversion': 'is_support_conversion',
        'converted_sql_statement': 'converted_sql_statement',
        'unsupported_items': 'unsupported_items'
    }

    def __init__(self, is_support_conversion=None, converted_sql_statement=None, unsupported_items=None):
        """RunSqlConversionResponse

        The model defined in huaweicloud sdk

        :param is_support_conversion: 是否支持SQL语句转换。
        :type is_support_conversion: bool
        :param converted_sql_statement: 转换后的SQL语句。
        :type converted_sql_statement: str
        :param unsupported_items: 不支持SQL语句转换的详情。
        :type unsupported_items: list[:class:`huaweicloudsdkugo.v1.UnSupportedItem`]
        """
        
        super(RunSqlConversionResponse, self).__init__()

        self._is_support_conversion = None
        self._converted_sql_statement = None
        self._unsupported_items = None
        self.discriminator = None

        if is_support_conversion is not None:
            self.is_support_conversion = is_support_conversion
        if converted_sql_statement is not None:
            self.converted_sql_statement = converted_sql_statement
        if unsupported_items is not None:
            self.unsupported_items = unsupported_items

    @property
    def is_support_conversion(self):
        """Gets the is_support_conversion of this RunSqlConversionResponse.

        是否支持SQL语句转换。

        :return: The is_support_conversion of this RunSqlConversionResponse.
        :rtype: bool
        """
        return self._is_support_conversion

    @is_support_conversion.setter
    def is_support_conversion(self, is_support_conversion):
        """Sets the is_support_conversion of this RunSqlConversionResponse.

        是否支持SQL语句转换。

        :param is_support_conversion: The is_support_conversion of this RunSqlConversionResponse.
        :type is_support_conversion: bool
        """
        self._is_support_conversion = is_support_conversion

    @property
    def converted_sql_statement(self):
        """Gets the converted_sql_statement of this RunSqlConversionResponse.

        转换后的SQL语句。

        :return: The converted_sql_statement of this RunSqlConversionResponse.
        :rtype: str
        """
        return self._converted_sql_statement

    @converted_sql_statement.setter
    def converted_sql_statement(self, converted_sql_statement):
        """Sets the converted_sql_statement of this RunSqlConversionResponse.

        转换后的SQL语句。

        :param converted_sql_statement: The converted_sql_statement of this RunSqlConversionResponse.
        :type converted_sql_statement: str
        """
        self._converted_sql_statement = converted_sql_statement

    @property
    def unsupported_items(self):
        """Gets the unsupported_items of this RunSqlConversionResponse.

        不支持SQL语句转换的详情。

        :return: The unsupported_items of this RunSqlConversionResponse.
        :rtype: list[:class:`huaweicloudsdkugo.v1.UnSupportedItem`]
        """
        return self._unsupported_items

    @unsupported_items.setter
    def unsupported_items(self, unsupported_items):
        """Sets the unsupported_items of this RunSqlConversionResponse.

        不支持SQL语句转换的详情。

        :param unsupported_items: The unsupported_items of this RunSqlConversionResponse.
        :type unsupported_items: list[:class:`huaweicloudsdkugo.v1.UnSupportedItem`]
        """
        self._unsupported_items = unsupported_items

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
        if not isinstance(other, RunSqlConversionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
