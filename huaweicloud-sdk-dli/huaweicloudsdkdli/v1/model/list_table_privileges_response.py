# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTablePrivilegesResponse(SdkResponse):

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
        'user_name': 'str',
        'privileges': 'list[TableUserPermissionsRespPrivilege]'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'user_name': 'user_name',
        'privileges': 'privileges'
    }

    def __init__(self, is_success=None, message=None, user_name=None, privileges=None):
        """ListTablePrivilegesResponse

        The model defined in huaweicloud sdk

        :param is_success: 执行请求是否成功。“true”表示请求执行成功。
        :type is_success: bool
        :param message: 系统提示信息，执行成功时，信息可能为空。
        :type message: str
        :param user_name: 被查询的用户名称。
        :type user_name: str
        :param privileges: 权限信息。
        :type privileges: list[:class:`huaweicloudsdkdli.v1.TableUserPermissionsRespPrivilege`]
        """
        
        super(ListTablePrivilegesResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._user_name = None
        self._privileges = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if user_name is not None:
            self.user_name = user_name
        if privileges is not None:
            self.privileges = privileges

    @property
    def is_success(self):
        """Gets the is_success of this ListTablePrivilegesResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :return: The is_success of this ListTablePrivilegesResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this ListTablePrivilegesResponse.

        执行请求是否成功。“true”表示请求执行成功。

        :param is_success: The is_success of this ListTablePrivilegesResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        """Gets the message of this ListTablePrivilegesResponse.

        系统提示信息，执行成功时，信息可能为空。

        :return: The message of this ListTablePrivilegesResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ListTablePrivilegesResponse.

        系统提示信息，执行成功时，信息可能为空。

        :param message: The message of this ListTablePrivilegesResponse.
        :type message: str
        """
        self._message = message

    @property
    def user_name(self):
        """Gets the user_name of this ListTablePrivilegesResponse.

        被查询的用户名称。

        :return: The user_name of this ListTablePrivilegesResponse.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ListTablePrivilegesResponse.

        被查询的用户名称。

        :param user_name: The user_name of this ListTablePrivilegesResponse.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def privileges(self):
        """Gets the privileges of this ListTablePrivilegesResponse.

        权限信息。

        :return: The privileges of this ListTablePrivilegesResponse.
        :rtype: list[:class:`huaweicloudsdkdli.v1.TableUserPermissionsRespPrivilege`]
        """
        return self._privileges

    @privileges.setter
    def privileges(self, privileges):
        """Sets the privileges of this ListTablePrivilegesResponse.

        权限信息。

        :param privileges: The privileges of this ListTablePrivilegesResponse.
        :type privileges: list[:class:`huaweicloudsdkdli.v1.TableUserPermissionsRespPrivilege`]
        """
        self._privileges = privileges

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
        if not isinstance(other, ListTablePrivilegesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
