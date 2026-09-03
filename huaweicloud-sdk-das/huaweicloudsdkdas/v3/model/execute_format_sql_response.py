# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExecuteFormatSqlResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'format_sql': 'str'
    }

    attribute_map = {
        'format_sql': 'format_sql'
    }

    def __init__(self, format_sql=None):
        r"""ExecuteFormatSqlResponse

        The model defined in huaweicloud sdk

        :param format_sql: 格式化后的SQL语句
        :type format_sql: str
        """
        
        super().__init__()

        self._format_sql = None
        self.discriminator = None

        if format_sql is not None:
            self.format_sql = format_sql

    @property
    def format_sql(self):
        r"""Gets the format_sql of this ExecuteFormatSqlResponse.

        格式化后的SQL语句

        :return: The format_sql of this ExecuteFormatSqlResponse.
        :rtype: str
        """
        return self._format_sql

    @format_sql.setter
    def format_sql(self, format_sql):
        r"""Sets the format_sql of this ExecuteFormatSqlResponse.

        格式化后的SQL语句

        :param format_sql: The format_sql of this ExecuteFormatSqlResponse.
        :type format_sql: str
        """
        self._format_sql = format_sql

    def to_dict(self):
        import warnings
        warnings.warn("ExecuteFormatSqlResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ExecuteFormatSqlResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
