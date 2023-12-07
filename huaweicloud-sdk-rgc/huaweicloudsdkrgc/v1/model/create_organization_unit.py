# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOrganizationUnit:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'manage_account_id': 'str',
        'organization_unit_id': 'str',
        'organization_unit_name': 'str',
        'organization_unit_status': 'str',
        'organization_unit_type': 'OrganizationalUnitType',
        'parent_organization_unit_id': 'str',
        'parent_organization_unit_name': 'str',
        'created_at': 'datetime'
    }

    attribute_map = {
        'manage_account_id': 'manage_account_id',
        'organization_unit_id': 'organization_unit_id',
        'organization_unit_name': 'organization_unit_name',
        'organization_unit_status': 'organization_unit_status',
        'organization_unit_type': 'organization_unit_type',
        'parent_organization_unit_id': 'parent_organization_unit_id',
        'parent_organization_unit_name': 'parent_organization_unit_name',
        'created_at': 'created_at'
    }

    def __init__(self, manage_account_id=None, organization_unit_id=None, organization_unit_name=None, organization_unit_status=None, organization_unit_type=None, parent_organization_unit_id=None, parent_organization_unit_name=None, created_at=None):
        """CreateOrganizationUnit

        The model defined in huaweicloud sdk

        :param manage_account_id: 管理账号ID。
        :type manage_account_id: str
        :param organization_unit_id: OU ID。
        :type organization_unit_id: str
        :param organization_unit_name: OU名称。
        :type organization_unit_name: str
        :param organization_unit_status: OU状态。
        :type organization_unit_status: str
        :param organization_unit_type: 
        :type organization_unit_type: :class:`huaweicloudsdkrgc.v1.OrganizationalUnitType`
        :param parent_organization_unit_id: 父OU ID。
        :type parent_organization_unit_id: str
        :param parent_organization_unit_name: 父OU名称。
        :type parent_organization_unit_name: str
        :param created_at: 被创建的时间。
        :type created_at: datetime
        """
        
        

        self._manage_account_id = None
        self._organization_unit_id = None
        self._organization_unit_name = None
        self._organization_unit_status = None
        self._organization_unit_type = None
        self._parent_organization_unit_id = None
        self._parent_organization_unit_name = None
        self._created_at = None
        self.discriminator = None

        if manage_account_id is not None:
            self.manage_account_id = manage_account_id
        if organization_unit_id is not None:
            self.organization_unit_id = organization_unit_id
        if organization_unit_name is not None:
            self.organization_unit_name = organization_unit_name
        if organization_unit_status is not None:
            self.organization_unit_status = organization_unit_status
        if organization_unit_type is not None:
            self.organization_unit_type = organization_unit_type
        if parent_organization_unit_id is not None:
            self.parent_organization_unit_id = parent_organization_unit_id
        if parent_organization_unit_name is not None:
            self.parent_organization_unit_name = parent_organization_unit_name
        if created_at is not None:
            self.created_at = created_at

    @property
    def manage_account_id(self):
        """Gets the manage_account_id of this CreateOrganizationUnit.

        管理账号ID。

        :return: The manage_account_id of this CreateOrganizationUnit.
        :rtype: str
        """
        return self._manage_account_id

    @manage_account_id.setter
    def manage_account_id(self, manage_account_id):
        """Sets the manage_account_id of this CreateOrganizationUnit.

        管理账号ID。

        :param manage_account_id: The manage_account_id of this CreateOrganizationUnit.
        :type manage_account_id: str
        """
        self._manage_account_id = manage_account_id

    @property
    def organization_unit_id(self):
        """Gets the organization_unit_id of this CreateOrganizationUnit.

        OU ID。

        :return: The organization_unit_id of this CreateOrganizationUnit.
        :rtype: str
        """
        return self._organization_unit_id

    @organization_unit_id.setter
    def organization_unit_id(self, organization_unit_id):
        """Sets the organization_unit_id of this CreateOrganizationUnit.

        OU ID。

        :param organization_unit_id: The organization_unit_id of this CreateOrganizationUnit.
        :type organization_unit_id: str
        """
        self._organization_unit_id = organization_unit_id

    @property
    def organization_unit_name(self):
        """Gets the organization_unit_name of this CreateOrganizationUnit.

        OU名称。

        :return: The organization_unit_name of this CreateOrganizationUnit.
        :rtype: str
        """
        return self._organization_unit_name

    @organization_unit_name.setter
    def organization_unit_name(self, organization_unit_name):
        """Sets the organization_unit_name of this CreateOrganizationUnit.

        OU名称。

        :param organization_unit_name: The organization_unit_name of this CreateOrganizationUnit.
        :type organization_unit_name: str
        """
        self._organization_unit_name = organization_unit_name

    @property
    def organization_unit_status(self):
        """Gets the organization_unit_status of this CreateOrganizationUnit.

        OU状态。

        :return: The organization_unit_status of this CreateOrganizationUnit.
        :rtype: str
        """
        return self._organization_unit_status

    @organization_unit_status.setter
    def organization_unit_status(self, organization_unit_status):
        """Sets the organization_unit_status of this CreateOrganizationUnit.

        OU状态。

        :param organization_unit_status: The organization_unit_status of this CreateOrganizationUnit.
        :type organization_unit_status: str
        """
        self._organization_unit_status = organization_unit_status

    @property
    def organization_unit_type(self):
        """Gets the organization_unit_type of this CreateOrganizationUnit.

        :return: The organization_unit_type of this CreateOrganizationUnit.
        :rtype: :class:`huaweicloudsdkrgc.v1.OrganizationalUnitType`
        """
        return self._organization_unit_type

    @organization_unit_type.setter
    def organization_unit_type(self, organization_unit_type):
        """Sets the organization_unit_type of this CreateOrganizationUnit.

        :param organization_unit_type: The organization_unit_type of this CreateOrganizationUnit.
        :type organization_unit_type: :class:`huaweicloudsdkrgc.v1.OrganizationalUnitType`
        """
        self._organization_unit_type = organization_unit_type

    @property
    def parent_organization_unit_id(self):
        """Gets the parent_organization_unit_id of this CreateOrganizationUnit.

        父OU ID。

        :return: The parent_organization_unit_id of this CreateOrganizationUnit.
        :rtype: str
        """
        return self._parent_organization_unit_id

    @parent_organization_unit_id.setter
    def parent_organization_unit_id(self, parent_organization_unit_id):
        """Sets the parent_organization_unit_id of this CreateOrganizationUnit.

        父OU ID。

        :param parent_organization_unit_id: The parent_organization_unit_id of this CreateOrganizationUnit.
        :type parent_organization_unit_id: str
        """
        self._parent_organization_unit_id = parent_organization_unit_id

    @property
    def parent_organization_unit_name(self):
        """Gets the parent_organization_unit_name of this CreateOrganizationUnit.

        父OU名称。

        :return: The parent_organization_unit_name of this CreateOrganizationUnit.
        :rtype: str
        """
        return self._parent_organization_unit_name

    @parent_organization_unit_name.setter
    def parent_organization_unit_name(self, parent_organization_unit_name):
        """Sets the parent_organization_unit_name of this CreateOrganizationUnit.

        父OU名称。

        :param parent_organization_unit_name: The parent_organization_unit_name of this CreateOrganizationUnit.
        :type parent_organization_unit_name: str
        """
        self._parent_organization_unit_name = parent_organization_unit_name

    @property
    def created_at(self):
        """Gets the created_at of this CreateOrganizationUnit.

        被创建的时间。

        :return: The created_at of this CreateOrganizationUnit.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CreateOrganizationUnit.

        被创建的时间。

        :param created_at: The created_at of this CreateOrganizationUnit.
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
        if not isinstance(other, CreateOrganizationUnit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
