# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RepoMemberInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_id': 'str',
        'domain_name': 'str',
        'id': 'str',
        'name': 'str',
        'role': 'int'
    }

    attribute_map = {
        'domain_id': 'domain_id',
        'domain_name': 'domain_name',
        'id': 'id',
        'name': 'name',
        'role': 'role'
    }

    def __init__(self, domain_id=None, domain_name=None, id=None, name=None, role=None):
        """RepoMemberInfo

        The model defined in huaweicloud sdk

        :param domain_id: 用户的租户ID
        :type domain_id: str
        :param domain_name: 用户的租户名称
        :type domain_name: str
        :param id: 添加的用户ID
        :type id: str
        :param name: 添加的用户名
        :type name: str
        :param role: 添加的用户权限，取值范围：20-&gt;浏览者，30-&gt;普通成员，40-&gt;管理员
        :type role: int
        """
        
        

        self._domain_id = None
        self._domain_name = None
        self._id = None
        self._name = None
        self._role = None
        self.discriminator = None

        if domain_id is not None:
            self.domain_id = domain_id
        if domain_name is not None:
            self.domain_name = domain_name
        self.id = id
        self.name = name
        self.role = role

    @property
    def domain_id(self):
        """Gets the domain_id of this RepoMemberInfo.

        用户的租户ID

        :return: The domain_id of this RepoMemberInfo.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this RepoMemberInfo.

        用户的租户ID

        :param domain_id: The domain_id of this RepoMemberInfo.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def domain_name(self):
        """Gets the domain_name of this RepoMemberInfo.

        用户的租户名称

        :return: The domain_name of this RepoMemberInfo.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this RepoMemberInfo.

        用户的租户名称

        :param domain_name: The domain_name of this RepoMemberInfo.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def id(self):
        """Gets the id of this RepoMemberInfo.

        添加的用户ID

        :return: The id of this RepoMemberInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RepoMemberInfo.

        添加的用户ID

        :param id: The id of this RepoMemberInfo.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this RepoMemberInfo.

        添加的用户名

        :return: The name of this RepoMemberInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RepoMemberInfo.

        添加的用户名

        :param name: The name of this RepoMemberInfo.
        :type name: str
        """
        self._name = name

    @property
    def role(self):
        """Gets the role of this RepoMemberInfo.

        添加的用户权限，取值范围：20->浏览者，30->普通成员，40->管理员

        :return: The role of this RepoMemberInfo.
        :rtype: int
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this RepoMemberInfo.

        添加的用户权限，取值范围：20->浏览者，30->普通成员，40->管理员

        :param role: The role of this RepoMemberInfo.
        :type role: int
        """
        self._role = role

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
        if not isinstance(other, RepoMemberInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
