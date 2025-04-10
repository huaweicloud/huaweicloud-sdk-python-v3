# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAuthorizationPrivilegesResponse(SdkResponse):

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
        'object_name': 'str',
        'object_type': 'str',
        'count': 'int',
        'privileges': 'list[AuthorizationPrivilege]'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'object_name': 'object_name',
        'object_type': 'object_type',
        'count': 'count',
        'privileges': 'privileges'
    }

    def __init__(self, is_success=None, message=None, object_name=None, object_type=None, count=None, privileges=None):
        r"""ListAuthorizationPrivilegesResponse

        The model defined in huaweicloud sdk

        :param is_success: 成功标识
        :type is_success: bool
        :param message: 响应信息
        :type message: str
        :param object_name: 对象名称
        :type object_name: str
        :param object_type: 对象类型
        :type object_type: str
        :param count: 对象类型
        :type count: int
        :param privileges: 权限信息
        :type privileges: list[:class:`huaweicloudsdkdli.v1.AuthorizationPrivilege`]
        """
        
        super(ListAuthorizationPrivilegesResponse, self).__init__()

        self._is_success = None
        self._message = None
        self._object_name = None
        self._object_type = None
        self._count = None
        self._privileges = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if object_name is not None:
            self.object_name = object_name
        if object_type is not None:
            self.object_type = object_type
        if count is not None:
            self.count = count
        if privileges is not None:
            self.privileges = privileges

    @property
    def is_success(self):
        r"""Gets the is_success of this ListAuthorizationPrivilegesResponse.

        成功标识

        :return: The is_success of this ListAuthorizationPrivilegesResponse.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        r"""Sets the is_success of this ListAuthorizationPrivilegesResponse.

        成功标识

        :param is_success: The is_success of this ListAuthorizationPrivilegesResponse.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        r"""Gets the message of this ListAuthorizationPrivilegesResponse.

        响应信息

        :return: The message of this ListAuthorizationPrivilegesResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        r"""Sets the message of this ListAuthorizationPrivilegesResponse.

        响应信息

        :param message: The message of this ListAuthorizationPrivilegesResponse.
        :type message: str
        """
        self._message = message

    @property
    def object_name(self):
        r"""Gets the object_name of this ListAuthorizationPrivilegesResponse.

        对象名称

        :return: The object_name of this ListAuthorizationPrivilegesResponse.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        r"""Sets the object_name of this ListAuthorizationPrivilegesResponse.

        对象名称

        :param object_name: The object_name of this ListAuthorizationPrivilegesResponse.
        :type object_name: str
        """
        self._object_name = object_name

    @property
    def object_type(self):
        r"""Gets the object_type of this ListAuthorizationPrivilegesResponse.

        对象类型

        :return: The object_type of this ListAuthorizationPrivilegesResponse.
        :rtype: str
        """
        return self._object_type

    @object_type.setter
    def object_type(self, object_type):
        r"""Sets the object_type of this ListAuthorizationPrivilegesResponse.

        对象类型

        :param object_type: The object_type of this ListAuthorizationPrivilegesResponse.
        :type object_type: str
        """
        self._object_type = object_type

    @property
    def count(self):
        r"""Gets the count of this ListAuthorizationPrivilegesResponse.

        对象类型

        :return: The count of this ListAuthorizationPrivilegesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListAuthorizationPrivilegesResponse.

        对象类型

        :param count: The count of this ListAuthorizationPrivilegesResponse.
        :type count: int
        """
        self._count = count

    @property
    def privileges(self):
        r"""Gets the privileges of this ListAuthorizationPrivilegesResponse.

        权限信息

        :return: The privileges of this ListAuthorizationPrivilegesResponse.
        :rtype: list[:class:`huaweicloudsdkdli.v1.AuthorizationPrivilege`]
        """
        return self._privileges

    @privileges.setter
    def privileges(self, privileges):
        r"""Sets the privileges of this ListAuthorizationPrivilegesResponse.

        权限信息

        :param privileges: The privileges of this ListAuthorizationPrivilegesResponse.
        :type privileges: list[:class:`huaweicloudsdkdli.v1.AuthorizationPrivilege`]
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
        if not isinstance(other, ListAuthorizationPrivilegesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
