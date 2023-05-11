# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OrganizationalUnitDto:

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
        'urn': 'str',
        'name': 'str',
        'created_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'urn': 'urn',
        'name': 'name',
        'created_at': 'created_at'
    }

    def __init__(self, id=None, urn=None, name=None, created_at=None):
        """OrganizationalUnitDto

        The model defined in huaweicloud sdk

        :param id: 与组织单元关联的唯一标识符（ID）。
        :type id: str
        :param urn: 组织单元的统一资源名称。
        :type urn: str
        :param name: 组织单元的名称。
        :type name: str
        :param created_at: 组织单元的创建时间。
        :type created_at: datetime
        """
        
        

        self._id = None
        self._urn = None
        self._name = None
        self._created_at = None
        self.discriminator = None

        self.id = id
        self.urn = urn
        self.name = name
        self.created_at = created_at

    @property
    def id(self):
        """Gets the id of this OrganizationalUnitDto.

        与组织单元关联的唯一标识符（ID）。

        :return: The id of this OrganizationalUnitDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this OrganizationalUnitDto.

        与组织单元关联的唯一标识符（ID）。

        :param id: The id of this OrganizationalUnitDto.
        :type id: str
        """
        self._id = id

    @property
    def urn(self):
        """Gets the urn of this OrganizationalUnitDto.

        组织单元的统一资源名称。

        :return: The urn of this OrganizationalUnitDto.
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        """Sets the urn of this OrganizationalUnitDto.

        组织单元的统一资源名称。

        :param urn: The urn of this OrganizationalUnitDto.
        :type urn: str
        """
        self._urn = urn

    @property
    def name(self):
        """Gets the name of this OrganizationalUnitDto.

        组织单元的名称。

        :return: The name of this OrganizationalUnitDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrganizationalUnitDto.

        组织单元的名称。

        :param name: The name of this OrganizationalUnitDto.
        :type name: str
        """
        self._name = name

    @property
    def created_at(self):
        """Gets the created_at of this OrganizationalUnitDto.

        组织单元的创建时间。

        :return: The created_at of this OrganizationalUnitDto.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this OrganizationalUnitDto.

        组织单元的创建时间。

        :param created_at: The created_at of this OrganizationalUnitDto.
        :type created_at: datetime
        """
        self._created_at = created_at

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
        if not isinstance(other, OrganizationalUnitDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
