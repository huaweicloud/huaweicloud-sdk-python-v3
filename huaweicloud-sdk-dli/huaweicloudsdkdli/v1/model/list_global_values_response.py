# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGlobalValuesResponse(SdkResponse):

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
        'global_vars': 'list[ListGlobalValue]',
        'count': 'int'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'global_vars': 'global_vars',
        'count': 'count'
    }

    def __init__(self, is_success=None, message=None, global_vars=None, count=None):
        """ListGlobalValuesResponse

        The model defined in huaweicloud sdk

        :param is_success: 请求执行是否成功。“true”表示请求执行成功。
        :type is_success: bool
        :param message: 系统提示信息，执行成功时，信息可能为空。
        :type message: str
        :param global_vars: 全局变量
        :type global_vars: list[:class:`huaweicloudsdkdli.v1.ListGlobalValue`]
        :param count: 全局变量总数
        :type count: int
        """
        
        super(ListGlobalValuesResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._global_vars = None
        self._count = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if global_vars is not None:
            self.global_vars = global_vars
        if count is not None:
            self.count = count

    @property
    def is_success(self):
        """Gets the is_success of this ListGlobalValuesResponse.

        请求执行是否成功。“true”表示请求执行成功。

        :return: The is_success of this ListGlobalValuesResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this ListGlobalValuesResponse.

        请求执行是否成功。“true”表示请求执行成功。

        :param is_success: The is_success of this ListGlobalValuesResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        """Gets the message of this ListGlobalValuesResponse.

        系统提示信息，执行成功时，信息可能为空。

        :return: The message of this ListGlobalValuesResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ListGlobalValuesResponse.

        系统提示信息，执行成功时，信息可能为空。

        :param message: The message of this ListGlobalValuesResponse.
        :type message: str
        """
        self._message = message

    @property
    def global_vars(self):
        """Gets the global_vars of this ListGlobalValuesResponse.

        全局变量

        :return: The global_vars of this ListGlobalValuesResponse.
        :rtype: list[:class:`huaweicloudsdkdli.v1.ListGlobalValue`]
        """
        return self._global_vars

    @global_vars.setter
    def global_vars(self, global_vars):
        """Sets the global_vars of this ListGlobalValuesResponse.

        全局变量

        :param global_vars: The global_vars of this ListGlobalValuesResponse.
        :type global_vars: list[:class:`huaweicloudsdkdli.v1.ListGlobalValue`]
        """
        self._global_vars = global_vars

    @property
    def count(self):
        """Gets the count of this ListGlobalValuesResponse.

        全局变量总数

        :return: The count of this ListGlobalValuesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListGlobalValuesResponse.

        全局变量总数

        :param count: The count of this ListGlobalValuesResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListGlobalValuesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
