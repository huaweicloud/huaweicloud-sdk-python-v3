# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTableContentResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_success': 'bool',
        'message': 'str',
        'schema': 'list[object]',
        'rows': 'list[object]'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'schema': 'schema',
        'rows': 'rows'
    }

    def __init__(self, is_success=None, message=None, schema=None, rows=None):
        """ShowTableContentResponse

        The model defined in huaweicloud sdk

        :param is_success: 执行请求是否成功。“true”表示请求执行成功。
        :type is_success: bool
        :param message: 系统提示信息，执行成功时，信息可能为空。
        :type message: str
        :param schema: 表的列名称和类型。
        :type schema: list[object]
        :param rows: 预览的表内容。
        :type rows: list[object]
        """
        
        super(ShowTableContentResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._schema = None
        self._rows = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if schema is not None:
            self.schema = schema
        if rows is not None:
            self.rows = rows

    @property
    def is_success(self):
        """Gets the is_success of this ShowTableContentResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :return: The is_success of this ShowTableContentResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this ShowTableContentResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :param is_success: The is_success of this ShowTableContentResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        """Gets the message of this ShowTableContentResponse.

        系统提示信息，执行成功时，信息可能为空。

        :return: The message of this ShowTableContentResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ShowTableContentResponse.

        系统提示信息，执行成功时，信息可能为空。

        :param message: The message of this ShowTableContentResponse.
        :type message: str
        """
        self._message = message

    @property
    def schema(self):
        """Gets the schema of this ShowTableContentResponse.

        表的列名称和类型。

        :return: The schema of this ShowTableContentResponse.
        :rtype: list[object]
        """
        return self._schema

    @schema.setter
    def schema(self, schema):
        """Sets the schema of this ShowTableContentResponse.

        表的列名称和类型。

        :param schema: The schema of this ShowTableContentResponse.
        :type schema: list[object]
        """
        self._schema = schema

    @property
    def rows(self):
        """Gets the rows of this ShowTableContentResponse.

        预览的表内容。

        :return: The rows of this ShowTableContentResponse.
        :rtype: list[object]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this ShowTableContentResponse.

        预览的表内容。

        :param rows: The rows of this ShowTableContentResponse.
        :type rows: list[object]
        """
        self._rows = rows

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
        if not isinstance(other, ShowTableContentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
