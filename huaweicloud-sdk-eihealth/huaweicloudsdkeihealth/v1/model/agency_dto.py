# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgencyDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'trust_domain_name': 'str',
        'description': 'str',
        'roles': 'list[IamRoleDto]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'trust_domain_name': 'trust_domain_name',
        'description': 'description',
        'roles': 'roles'
    }

    def __init__(self, id=None, name=None, trust_domain_name=None, description=None, roles=None):
        r"""AgencyDto

        The model defined in huaweicloud sdk

        :param id: 委托ID。
        :type id: str
        :param name: 委托名。
        :type name: str
        :param trust_domain_name: 被委托方账号名。
        :type trust_domain_name: str
        :param description: 委托描述。
        :type description: str
        :param roles: 委托权限列表。
        :type roles: list[:class:`huaweicloudsdkeihealth.v1.IamRoleDto`]
        """
        
        

        self._id = None
        self._name = None
        self._trust_domain_name = None
        self._description = None
        self._roles = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if trust_domain_name is not None:
            self.trust_domain_name = trust_domain_name
        if description is not None:
            self.description = description
        if roles is not None:
            self.roles = roles

    @property
    def id(self):
        r"""Gets the id of this AgencyDto.

        委托ID。

        :return: The id of this AgencyDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AgencyDto.

        委托ID。

        :param id: The id of this AgencyDto.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this AgencyDto.

        委托名。

        :return: The name of this AgencyDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AgencyDto.

        委托名。

        :param name: The name of this AgencyDto.
        :type name: str
        """
        self._name = name

    @property
    def trust_domain_name(self):
        r"""Gets the trust_domain_name of this AgencyDto.

        被委托方账号名。

        :return: The trust_domain_name of this AgencyDto.
        :rtype: str
        """
        return self._trust_domain_name

    @trust_domain_name.setter
    def trust_domain_name(self, trust_domain_name):
        r"""Sets the trust_domain_name of this AgencyDto.

        被委托方账号名。

        :param trust_domain_name: The trust_domain_name of this AgencyDto.
        :type trust_domain_name: str
        """
        self._trust_domain_name = trust_domain_name

    @property
    def description(self):
        r"""Gets the description of this AgencyDto.

        委托描述。

        :return: The description of this AgencyDto.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AgencyDto.

        委托描述。

        :param description: The description of this AgencyDto.
        :type description: str
        """
        self._description = description

    @property
    def roles(self):
        r"""Gets the roles of this AgencyDto.

        委托权限列表。

        :return: The roles of this AgencyDto.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.IamRoleDto`]
        """
        return self._roles

    @roles.setter
    def roles(self, roles):
        r"""Sets the roles of this AgencyDto.

        委托权限列表。

        :param roles: The roles of this AgencyDto.
        :type roles: list[:class:`huaweicloudsdkeihealth.v1.IamRoleDto`]
        """
        self._roles = roles

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
        if not isinstance(other, AgencyDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
