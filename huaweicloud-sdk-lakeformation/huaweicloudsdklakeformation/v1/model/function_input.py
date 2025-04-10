# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FunctionInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'function_name': 'str',
        'function_type': 'str',
        'owner': 'str',
        'owner_type': 'str',
        'owner_auth_source_type': 'str',
        'class_name': 'str',
        'create_time': 'datetime',
        'resource_uris': 'list[FunctionResourceUri]'
    }

    attribute_map = {
        'function_name': 'function_name',
        'function_type': 'function_type',
        'owner': 'owner',
        'owner_type': 'owner_type',
        'owner_auth_source_type': 'owner_auth_source_type',
        'class_name': 'class_name',
        'create_time': 'create_time',
        'resource_uris': 'resource_uris'
    }

    def __init__(self, function_name=None, function_type=None, owner=None, owner_type=None, owner_auth_source_type=None, class_name=None, create_time=None, resource_uris=None):
        r"""FunctionInput

        The model defined in huaweicloud sdk

        :param function_name: 函数名称。只能包含字母、数字和下划线，且长度为1~256个字符。
        :type function_name: str
        :param function_type: 函数类型，JAVA
        :type function_type: str
        :param owner: 函数所有者。只能包含字母、数字和下划线，且长度为1~256个字符。
        :type owner: str
        :param owner_type: 所有者类型，USER-用户,GROUP-组,ROLE-角色
        :type owner_type: str
        :param owner_auth_source_type: 所有者授权来源类型,IAM-云,SAML-联邦,LDAP-ld用户,LOCAL-本地,AGENTTENANT-委托,OTHER-其它
        :type owner_auth_source_type: str
        :param class_name: 函数类名。长度为1~4000个字符。
        :type class_name: str
        :param create_time: 创建时间格式为yyyy-mm-ddThh:mm:sss
        :type create_time: datetime
        :param resource_uris: 函数地址信息
        :type resource_uris: list[:class:`huaweicloudsdklakeformation.v1.FunctionResourceUri`]
        """
        
        

        self._function_name = None
        self._function_type = None
        self._owner = None
        self._owner_type = None
        self._owner_auth_source_type = None
        self._class_name = None
        self._create_time = None
        self._resource_uris = None
        self.discriminator = None

        self.function_name = function_name
        self.function_type = function_type
        self.owner = owner
        self.owner_type = owner_type
        if owner_auth_source_type is not None:
            self.owner_auth_source_type = owner_auth_source_type
        self.class_name = class_name
        if create_time is not None:
            self.create_time = create_time
        if resource_uris is not None:
            self.resource_uris = resource_uris

    @property
    def function_name(self):
        r"""Gets the function_name of this FunctionInput.

        函数名称。只能包含字母、数字和下划线，且长度为1~256个字符。

        :return: The function_name of this FunctionInput.
        :rtype: str
        """
        return self._function_name

    @function_name.setter
    def function_name(self, function_name):
        r"""Sets the function_name of this FunctionInput.

        函数名称。只能包含字母、数字和下划线，且长度为1~256个字符。

        :param function_name: The function_name of this FunctionInput.
        :type function_name: str
        """
        self._function_name = function_name

    @property
    def function_type(self):
        r"""Gets the function_type of this FunctionInput.

        函数类型，JAVA

        :return: The function_type of this FunctionInput.
        :rtype: str
        """
        return self._function_type

    @function_type.setter
    def function_type(self, function_type):
        r"""Sets the function_type of this FunctionInput.

        函数类型，JAVA

        :param function_type: The function_type of this FunctionInput.
        :type function_type: str
        """
        self._function_type = function_type

    @property
    def owner(self):
        r"""Gets the owner of this FunctionInput.

        函数所有者。只能包含字母、数字和下划线，且长度为1~256个字符。

        :return: The owner of this FunctionInput.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this FunctionInput.

        函数所有者。只能包含字母、数字和下划线，且长度为1~256个字符。

        :param owner: The owner of this FunctionInput.
        :type owner: str
        """
        self._owner = owner

    @property
    def owner_type(self):
        r"""Gets the owner_type of this FunctionInput.

        所有者类型，USER-用户,GROUP-组,ROLE-角色

        :return: The owner_type of this FunctionInput.
        :rtype: str
        """
        return self._owner_type

    @owner_type.setter
    def owner_type(self, owner_type):
        r"""Sets the owner_type of this FunctionInput.

        所有者类型，USER-用户,GROUP-组,ROLE-角色

        :param owner_type: The owner_type of this FunctionInput.
        :type owner_type: str
        """
        self._owner_type = owner_type

    @property
    def owner_auth_source_type(self):
        r"""Gets the owner_auth_source_type of this FunctionInput.

        所有者授权来源类型,IAM-云,SAML-联邦,LDAP-ld用户,LOCAL-本地,AGENTTENANT-委托,OTHER-其它

        :return: The owner_auth_source_type of this FunctionInput.
        :rtype: str
        """
        return self._owner_auth_source_type

    @owner_auth_source_type.setter
    def owner_auth_source_type(self, owner_auth_source_type):
        r"""Sets the owner_auth_source_type of this FunctionInput.

        所有者授权来源类型,IAM-云,SAML-联邦,LDAP-ld用户,LOCAL-本地,AGENTTENANT-委托,OTHER-其它

        :param owner_auth_source_type: The owner_auth_source_type of this FunctionInput.
        :type owner_auth_source_type: str
        """
        self._owner_auth_source_type = owner_auth_source_type

    @property
    def class_name(self):
        r"""Gets the class_name of this FunctionInput.

        函数类名。长度为1~4000个字符。

        :return: The class_name of this FunctionInput.
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        r"""Sets the class_name of this FunctionInput.

        函数类名。长度为1~4000个字符。

        :param class_name: The class_name of this FunctionInput.
        :type class_name: str
        """
        self._class_name = class_name

    @property
    def create_time(self):
        r"""Gets the create_time of this FunctionInput.

        创建时间格式为yyyy-mm-ddThh:mm:sss

        :return: The create_time of this FunctionInput.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this FunctionInput.

        创建时间格式为yyyy-mm-ddThh:mm:sss

        :param create_time: The create_time of this FunctionInput.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def resource_uris(self):
        r"""Gets the resource_uris of this FunctionInput.

        函数地址信息

        :return: The resource_uris of this FunctionInput.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.FunctionResourceUri`]
        """
        return self._resource_uris

    @resource_uris.setter
    def resource_uris(self, resource_uris):
        r"""Sets the resource_uris of this FunctionInput.

        函数地址信息

        :param resource_uris: The resource_uris of this FunctionInput.
        :type resource_uris: list[:class:`huaweicloudsdklakeformation.v1.FunctionResourceUri`]
        """
        self._resource_uris = resource_uris

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
        if not isinstance(other, FunctionInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
