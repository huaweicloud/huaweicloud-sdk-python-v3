# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateOrganizationConformancePackResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'org_conformance_pack_id': 'str',
        'org_conformance_pack_name': 'str',
        'owner_id': 'str',
        'organization_id': 'str',
        'org_conformance_pack_urn': 'str',
        'vars_structure': 'list[VarsStructure]',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'org_conformance_pack_id': 'org_conformance_pack_id',
        'org_conformance_pack_name': 'org_conformance_pack_name',
        'owner_id': 'owner_id',
        'organization_id': 'organization_id',
        'org_conformance_pack_urn': 'org_conformance_pack_urn',
        'vars_structure': 'vars_structure',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, org_conformance_pack_id=None, org_conformance_pack_name=None, owner_id=None, organization_id=None, org_conformance_pack_urn=None, vars_structure=None, created_at=None, updated_at=None):
        r"""CreateOrganizationConformancePackResponse

        The model defined in huaweicloud sdk

        :param org_conformance_pack_id: 组织合规规则包ID。
        :type org_conformance_pack_id: str
        :param org_conformance_pack_name: 组织合规规则包名称。
        :type org_conformance_pack_name: str
        :param owner_id: 组织合规规则包创建者。
        :type owner_id: str
        :param organization_id: 组织ID
        :type organization_id: str
        :param org_conformance_pack_urn: 组织合规规则包资源唯一标识。
        :type org_conformance_pack_urn: str
        :param vars_structure: 合规规则包参数。
        :type vars_structure: list[:class:`huaweicloudsdkconfig.v1.VarsStructure`]
        :param created_at: 组织合规规则包创建时间。
        :type created_at: str
        :param updated_at: 组织合规规则包更新时间。
        :type updated_at: str
        """
        
        super(CreateOrganizationConformancePackResponse, self).__init__()

        self._org_conformance_pack_id = None
        self._org_conformance_pack_name = None
        self._owner_id = None
        self._organization_id = None
        self._org_conformance_pack_urn = None
        self._vars_structure = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if org_conformance_pack_id is not None:
            self.org_conformance_pack_id = org_conformance_pack_id
        if org_conformance_pack_name is not None:
            self.org_conformance_pack_name = org_conformance_pack_name
        if owner_id is not None:
            self.owner_id = owner_id
        if organization_id is not None:
            self.organization_id = organization_id
        if org_conformance_pack_urn is not None:
            self.org_conformance_pack_urn = org_conformance_pack_urn
        if vars_structure is not None:
            self.vars_structure = vars_structure
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def org_conformance_pack_id(self):
        r"""Gets the org_conformance_pack_id of this CreateOrganizationConformancePackResponse.

        组织合规规则包ID。

        :return: The org_conformance_pack_id of this CreateOrganizationConformancePackResponse.
        :rtype: str
        """
        return self._org_conformance_pack_id

    @org_conformance_pack_id.setter
    def org_conformance_pack_id(self, org_conformance_pack_id):
        r"""Sets the org_conformance_pack_id of this CreateOrganizationConformancePackResponse.

        组织合规规则包ID。

        :param org_conformance_pack_id: The org_conformance_pack_id of this CreateOrganizationConformancePackResponse.
        :type org_conformance_pack_id: str
        """
        self._org_conformance_pack_id = org_conformance_pack_id

    @property
    def org_conformance_pack_name(self):
        r"""Gets the org_conformance_pack_name of this CreateOrganizationConformancePackResponse.

        组织合规规则包名称。

        :return: The org_conformance_pack_name of this CreateOrganizationConformancePackResponse.
        :rtype: str
        """
        return self._org_conformance_pack_name

    @org_conformance_pack_name.setter
    def org_conformance_pack_name(self, org_conformance_pack_name):
        r"""Sets the org_conformance_pack_name of this CreateOrganizationConformancePackResponse.

        组织合规规则包名称。

        :param org_conformance_pack_name: The org_conformance_pack_name of this CreateOrganizationConformancePackResponse.
        :type org_conformance_pack_name: str
        """
        self._org_conformance_pack_name = org_conformance_pack_name

    @property
    def owner_id(self):
        r"""Gets the owner_id of this CreateOrganizationConformancePackResponse.

        组织合规规则包创建者。

        :return: The owner_id of this CreateOrganizationConformancePackResponse.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        r"""Sets the owner_id of this CreateOrganizationConformancePackResponse.

        组织合规规则包创建者。

        :param owner_id: The owner_id of this CreateOrganizationConformancePackResponse.
        :type owner_id: str
        """
        self._owner_id = owner_id

    @property
    def organization_id(self):
        r"""Gets the organization_id of this CreateOrganizationConformancePackResponse.

        组织ID

        :return: The organization_id of this CreateOrganizationConformancePackResponse.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        r"""Sets the organization_id of this CreateOrganizationConformancePackResponse.

        组织ID

        :param organization_id: The organization_id of this CreateOrganizationConformancePackResponse.
        :type organization_id: str
        """
        self._organization_id = organization_id

    @property
    def org_conformance_pack_urn(self):
        r"""Gets the org_conformance_pack_urn of this CreateOrganizationConformancePackResponse.

        组织合规规则包资源唯一标识。

        :return: The org_conformance_pack_urn of this CreateOrganizationConformancePackResponse.
        :rtype: str
        """
        return self._org_conformance_pack_urn

    @org_conformance_pack_urn.setter
    def org_conformance_pack_urn(self, org_conformance_pack_urn):
        r"""Sets the org_conformance_pack_urn of this CreateOrganizationConformancePackResponse.

        组织合规规则包资源唯一标识。

        :param org_conformance_pack_urn: The org_conformance_pack_urn of this CreateOrganizationConformancePackResponse.
        :type org_conformance_pack_urn: str
        """
        self._org_conformance_pack_urn = org_conformance_pack_urn

    @property
    def vars_structure(self):
        r"""Gets the vars_structure of this CreateOrganizationConformancePackResponse.

        合规规则包参数。

        :return: The vars_structure of this CreateOrganizationConformancePackResponse.
        :rtype: list[:class:`huaweicloudsdkconfig.v1.VarsStructure`]
        """
        return self._vars_structure

    @vars_structure.setter
    def vars_structure(self, vars_structure):
        r"""Sets the vars_structure of this CreateOrganizationConformancePackResponse.

        合规规则包参数。

        :param vars_structure: The vars_structure of this CreateOrganizationConformancePackResponse.
        :type vars_structure: list[:class:`huaweicloudsdkconfig.v1.VarsStructure`]
        """
        self._vars_structure = vars_structure

    @property
    def created_at(self):
        r"""Gets the created_at of this CreateOrganizationConformancePackResponse.

        组织合规规则包创建时间。

        :return: The created_at of this CreateOrganizationConformancePackResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CreateOrganizationConformancePackResponse.

        组织合规规则包创建时间。

        :param created_at: The created_at of this CreateOrganizationConformancePackResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this CreateOrganizationConformancePackResponse.

        组织合规规则包更新时间。

        :return: The updated_at of this CreateOrganizationConformancePackResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this CreateOrganizationConformancePackResponse.

        组织合规规则包更新时间。

        :param updated_at: The updated_at of this CreateOrganizationConformancePackResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

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
        if not isinstance(other, CreateOrganizationConformancePackResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
