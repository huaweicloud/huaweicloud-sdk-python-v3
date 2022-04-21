# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMetadatasResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'error_message': 'str',
        'error_code': 'str',
        'schema_count': 'int',
        'schema_list': 'list[Metadata]'
    }

    attribute_map = {
        'error_message': 'errorMessage',
        'error_code': 'errorCode',
        'schema_count': 'schemaCount',
        'schema_list': 'schemaList'
    }

    def __init__(self, error_message=None, error_code=None, schema_count=None, schema_list=None):
        """ListMetadatasResponse

        The model defined in huaweicloud sdk

        :param error_message: 系统提示信息，执行成功时，字段可能为空。执行失败时，用于显示错误信息。
        :type error_message: str
        :param error_code: 系统提示信息，执行成功时，字段可能为空。执行失败时，用于显示错误码。
        :type error_code: str
        :param schema_count: 元数据返回个数。请求失败时，字段为空。
        :type schema_count: int
        :param schema_list: 当前projectId下的所有元数据列表。请求失败时，字段为空。
        :type schema_list: list[:class:`huaweicloudsdkges.v1.Metadata`]
        """
        
        super(ListMetadatasResponse, self).__init__()

        self._error_message = None
        self._error_code = None
        self._schema_count = None
        self._schema_list = None
        self.discriminator = None

        if error_message is not None:
            self.error_message = error_message
        if error_code is not None:
            self.error_code = error_code
        if schema_count is not None:
            self.schema_count = schema_count
        if schema_list is not None:
            self.schema_list = schema_list

    @property
    def error_message(self):
        """Gets the error_message of this ListMetadatasResponse.

        系统提示信息，执行成功时，字段可能为空。执行失败时，用于显示错误信息。

        :return: The error_message of this ListMetadatasResponse.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        """Sets the error_message of this ListMetadatasResponse.

        系统提示信息，执行成功时，字段可能为空。执行失败时，用于显示错误信息。

        :param error_message: The error_message of this ListMetadatasResponse.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def error_code(self):
        """Gets the error_code of this ListMetadatasResponse.

        系统提示信息，执行成功时，字段可能为空。执行失败时，用于显示错误码。

        :return: The error_code of this ListMetadatasResponse.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ListMetadatasResponse.

        系统提示信息，执行成功时，字段可能为空。执行失败时，用于显示错误码。

        :param error_code: The error_code of this ListMetadatasResponse.
        :type error_code: str
        """
        self._error_code = error_code

    @property
    def schema_count(self):
        """Gets the schema_count of this ListMetadatasResponse.

        元数据返回个数。请求失败时，字段为空。

        :return: The schema_count of this ListMetadatasResponse.
        :rtype: int
        """
        return self._schema_count

    @schema_count.setter
    def schema_count(self, schema_count):
        """Sets the schema_count of this ListMetadatasResponse.

        元数据返回个数。请求失败时，字段为空。

        :param schema_count: The schema_count of this ListMetadatasResponse.
        :type schema_count: int
        """
        self._schema_count = schema_count

    @property
    def schema_list(self):
        """Gets the schema_list of this ListMetadatasResponse.

        当前projectId下的所有元数据列表。请求失败时，字段为空。

        :return: The schema_list of this ListMetadatasResponse.
        :rtype: list[:class:`huaweicloudsdkges.v1.Metadata`]
        """
        return self._schema_list

    @schema_list.setter
    def schema_list(self, schema_list):
        """Sets the schema_list of this ListMetadatasResponse.

        当前projectId下的所有元数据列表。请求失败时，字段为空。

        :param schema_list: The schema_list of this ListMetadatasResponse.
        :type schema_list: list[:class:`huaweicloudsdkges.v1.Metadata`]
        """
        self._schema_list = schema_list

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
        if not isinstance(other, ListMetadatasResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
