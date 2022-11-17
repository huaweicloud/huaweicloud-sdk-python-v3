# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDliAgencyResponse(SdkResponse):

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
        'version': 'str',
        'current_roles': 'list[str]'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'version': 'version',
        'current_roles': 'current_roles'
    }

    def __init__(self, is_success=None, message=None, version=None, current_roles=None):
        """ShowDliAgencyResponse

        The model defined in huaweicloud sdk

        :param is_success: 执行请求是否成功。“true”表示请求执行成功。
        :type is_success: bool
        :param message: 系统提示信息，执行成功时，信息可能为空。
        :type message: str
        :param version: 版本号
        :type version: str
        :param current_roles: 当前已有委托
        :type current_roles: list[str]
        """
        
        super(ShowDliAgencyResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._version = None
        self._current_roles = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if version is not None:
            self.version = version
        if current_roles is not None:
            self.current_roles = current_roles

    @property
    def is_success(self):
        """Gets the is_success of this ShowDliAgencyResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :return: The is_success of this ShowDliAgencyResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this ShowDliAgencyResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :param is_success: The is_success of this ShowDliAgencyResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        """Gets the message of this ShowDliAgencyResponse.

        系统提示信息，执行成功时，信息可能为空。

        :return: The message of this ShowDliAgencyResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ShowDliAgencyResponse.

        系统提示信息，执行成功时，信息可能为空。

        :param message: The message of this ShowDliAgencyResponse.
        :type message: str
        """
        self._message = message

    @property
    def version(self):
        """Gets the version of this ShowDliAgencyResponse.

        版本号

        :return: The version of this ShowDliAgencyResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShowDliAgencyResponse.

        版本号

        :param version: The version of this ShowDliAgencyResponse.
        :type version: str
        """
        self._version = version

    @property
    def current_roles(self):
        """Gets the current_roles of this ShowDliAgencyResponse.

        当前已有委托

        :return: The current_roles of this ShowDliAgencyResponse.
        :rtype: list[str]
        """
        return self._current_roles

    @current_roles.setter
    def current_roles(self, current_roles):
        """Sets the current_roles of this ShowDliAgencyResponse.

        当前已有委托

        :param current_roles: The current_roles of this ShowDliAgencyResponse.
        :type current_roles: list[str]
        """
        self._current_roles = current_roles

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
        if not isinstance(other, ShowDliAgencyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
