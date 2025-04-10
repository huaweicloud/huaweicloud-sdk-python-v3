# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAclAccountRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'account_name': 'str',
        'account_role': 'str',
        'account_password': 'str',
        'description': 'str'
    }

    attribute_map = {
        'account_name': 'account_name',
        'account_role': 'account_role',
        'account_password': 'account_password',
        'description': 'description'
    }

    def __init__(self, account_name=None, account_role=None, account_password=None, description=None):
        r"""CreateAclAccountRequestBody

        The model defined in huaweicloud sdk

        :param account_name: 账号名称 - 以字母开头。 - 内容由字母、数字、中划线、下划线组成。 - 长度范围[1~64]个字符。 
        :type account_name: str
        :param account_role: 账号权限
        :type account_role: str
        :param account_password: 账号密码 - 输入长度为8到64位的字符串。 - 不能包含正序逆序用户名。 - 必须包含如下四种字符中的三种组合（不允许包含冒号）：   - 小写字母   - 大写字母   - 数字   - 特殊字符包括（&#x60;~!@#$%^&amp;*()-_&#x3D;+\\|{},&lt;.&gt;/?） 
        :type account_password: str
        :param description: 账号描述
        :type description: str
        """
        
        

        self._account_name = None
        self._account_role = None
        self._account_password = None
        self._description = None
        self.discriminator = None

        self.account_name = account_name
        self.account_role = account_role
        self.account_password = account_password
        if description is not None:
            self.description = description

    @property
    def account_name(self):
        r"""Gets the account_name of this CreateAclAccountRequestBody.

        账号名称 - 以字母开头。 - 内容由字母、数字、中划线、下划线组成。 - 长度范围[1~64]个字符。 

        :return: The account_name of this CreateAclAccountRequestBody.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        r"""Sets the account_name of this CreateAclAccountRequestBody.

        账号名称 - 以字母开头。 - 内容由字母、数字、中划线、下划线组成。 - 长度范围[1~64]个字符。 

        :param account_name: The account_name of this CreateAclAccountRequestBody.
        :type account_name: str
        """
        self._account_name = account_name

    @property
    def account_role(self):
        r"""Gets the account_role of this CreateAclAccountRequestBody.

        账号权限

        :return: The account_role of this CreateAclAccountRequestBody.
        :rtype: str
        """
        return self._account_role

    @account_role.setter
    def account_role(self, account_role):
        r"""Sets the account_role of this CreateAclAccountRequestBody.

        账号权限

        :param account_role: The account_role of this CreateAclAccountRequestBody.
        :type account_role: str
        """
        self._account_role = account_role

    @property
    def account_password(self):
        r"""Gets the account_password of this CreateAclAccountRequestBody.

        账号密码 - 输入长度为8到64位的字符串。 - 不能包含正序逆序用户名。 - 必须包含如下四种字符中的三种组合（不允许包含冒号）：   - 小写字母   - 大写字母   - 数字   - 特殊字符包括（`~!@#$%^&*()-_=+\\|{},<.>/?） 

        :return: The account_password of this CreateAclAccountRequestBody.
        :rtype: str
        """
        return self._account_password

    @account_password.setter
    def account_password(self, account_password):
        r"""Sets the account_password of this CreateAclAccountRequestBody.

        账号密码 - 输入长度为8到64位的字符串。 - 不能包含正序逆序用户名。 - 必须包含如下四种字符中的三种组合（不允许包含冒号）：   - 小写字母   - 大写字母   - 数字   - 特殊字符包括（`~!@#$%^&*()-_=+\\|{},<.>/?） 

        :param account_password: The account_password of this CreateAclAccountRequestBody.
        :type account_password: str
        """
        self._account_password = account_password

    @property
    def description(self):
        r"""Gets the description of this CreateAclAccountRequestBody.

        账号描述

        :return: The description of this CreateAclAccountRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateAclAccountRequestBody.

        账号描述

        :param description: The description of this CreateAclAccountRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CreateAclAccountRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
