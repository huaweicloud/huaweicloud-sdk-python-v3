# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddMemberRequestV4:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_name': 'str',
        'domain_id': 'str',
        'role_id': 'int',
        'user_id': 'str'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'domain_id': 'domain_id',
        'role_id': 'role_id',
        'user_id': 'user_id'
    }

    def __init__(self, domain_name=None, domain_id=None, role_id=None, user_id=None):
        """AddMemberRequestV4

        The model defined in huaweicloud sdk

        :param domain_name: 租户名称（跨租户添加用户时，填写正确的租户名称，可将未授权的租户主动授权，将用户添加为项目成员）
        :type domain_name: str
        :param domain_id: 租户id
        :type domain_id: str
        :param role_id: &#39;用户在项目中的角色ID&#39; 成员角色, -1 项目创建者, 3 项目经理, 4 开发人员, 5 测试经理, 6 测试人员, 7 参与者, 8 浏览者, 9 运维经理
        :type role_id: int
        :param user_id: 用户32位uuid
        :type user_id: str
        """
        
        

        self._domain_name = None
        self._domain_id = None
        self._role_id = None
        self._user_id = None
        self.discriminator = None

        if domain_name is not None:
            self.domain_name = domain_name
        self.domain_id = domain_id
        if role_id is not None:
            self.role_id = role_id
        self.user_id = user_id

    @property
    def domain_name(self):
        """Gets the domain_name of this AddMemberRequestV4.

        租户名称（跨租户添加用户时，填写正确的租户名称，可将未授权的租户主动授权，将用户添加为项目成员）

        :return: The domain_name of this AddMemberRequestV4.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this AddMemberRequestV4.

        租户名称（跨租户添加用户时，填写正确的租户名称，可将未授权的租户主动授权，将用户添加为项目成员）

        :param domain_name: The domain_name of this AddMemberRequestV4.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def domain_id(self):
        """Gets the domain_id of this AddMemberRequestV4.

        租户id

        :return: The domain_id of this AddMemberRequestV4.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this AddMemberRequestV4.

        租户id

        :param domain_id: The domain_id of this AddMemberRequestV4.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def role_id(self):
        """Gets the role_id of this AddMemberRequestV4.

        '用户在项目中的角色ID' 成员角色, -1 项目创建者, 3 项目经理, 4 开发人员, 5 测试经理, 6 测试人员, 7 参与者, 8 浏览者, 9 运维经理

        :return: The role_id of this AddMemberRequestV4.
        :rtype: int
        """
        return self._role_id

    @role_id.setter
    def role_id(self, role_id):
        """Sets the role_id of this AddMemberRequestV4.

        '用户在项目中的角色ID' 成员角色, -1 项目创建者, 3 项目经理, 4 开发人员, 5 测试经理, 6 测试人员, 7 参与者, 8 浏览者, 9 运维经理

        :param role_id: The role_id of this AddMemberRequestV4.
        :type role_id: int
        """
        self._role_id = role_id

    @property
    def user_id(self):
        """Gets the user_id of this AddMemberRequestV4.

        用户32位uuid

        :return: The user_id of this AddMemberRequestV4.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this AddMemberRequestV4.

        用户32位uuid

        :param user_id: The user_id of this AddMemberRequestV4.
        :type user_id: str
        """
        self._user_id = user_id

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
        if not isinstance(other, AddMemberRequestV4):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
