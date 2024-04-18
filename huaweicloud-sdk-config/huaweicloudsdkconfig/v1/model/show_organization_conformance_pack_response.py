# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOrganizationConformancePackResponse(SdkResponse):

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
        'excluded_accounts': 'list[str]',
        'vars_structure': 'list[VarsStructure]',
        'created_at': 'str',
        'updated_at': 'str',
        'template_key': 'str',
        'template_uri': 'str'
    }

    attribute_map = {
        'org_conformance_pack_id': 'org_conformance_pack_id',
        'org_conformance_pack_name': 'org_conformance_pack_name',
        'owner_id': 'owner_id',
        'organization_id': 'organization_id',
        'org_conformance_pack_urn': 'org_conformance_pack_urn',
        'excluded_accounts': 'excluded_accounts',
        'vars_structure': 'vars_structure',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'template_key': 'template_key',
        'template_uri': 'template_uri'
    }

    def __init__(self, org_conformance_pack_id=None, org_conformance_pack_name=None, owner_id=None, organization_id=None, org_conformance_pack_urn=None, excluded_accounts=None, vars_structure=None, created_at=None, updated_at=None, template_key=None, template_uri=None):
        """ShowOrganizationConformancePackResponse

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
        :param excluded_accounts: 排除配置合规包的帐号。
        :type excluded_accounts: list[str]
        :param vars_structure: 合规规则包参数。
        :type vars_structure: list[:class:`huaweicloudsdkconfig.v1.VarsStructure`]
        :param created_at: 组织合规规则包创建时间。
        :type created_at: str
        :param updated_at: 组织合规规则包更新时间。
        :type updated_at: str
        :param template_key: 预定义合规规则包模板名称。
        :type template_key: str
        :param template_uri: 合规规则包模板OBS地址
        :type template_uri: str
        """
        
        super(ShowOrganizationConformancePackResponse, self).__init__()

        self._org_conformance_pack_id = None
        self._org_conformance_pack_name = None
        self._owner_id = None
        self._organization_id = None
        self._org_conformance_pack_urn = None
        self._excluded_accounts = None
        self._vars_structure = None
        self._created_at = None
        self._updated_at = None
        self._template_key = None
        self._template_uri = None
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
        if excluded_accounts is not None:
            self.excluded_accounts = excluded_accounts
        if vars_structure is not None:
            self.vars_structure = vars_structure
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if template_key is not None:
            self.template_key = template_key
        if template_uri is not None:
            self.template_uri = template_uri

    @property
    def org_conformance_pack_id(self):
        """Gets the org_conformance_pack_id of this ShowOrganizationConformancePackResponse.

        组织合规规则包ID。

        :return: The org_conformance_pack_id of this ShowOrganizationConformancePackResponse.
        :rtype: str
        """
        return self._org_conformance_pack_id

    @org_conformance_pack_id.setter
    def org_conformance_pack_id(self, org_conformance_pack_id):
        """Sets the org_conformance_pack_id of this ShowOrganizationConformancePackResponse.

        组织合规规则包ID。

        :param org_conformance_pack_id: The org_conformance_pack_id of this ShowOrganizationConformancePackResponse.
        :type org_conformance_pack_id: str
        """
        self._org_conformance_pack_id = org_conformance_pack_id

    @property
    def org_conformance_pack_name(self):
        """Gets the org_conformance_pack_name of this ShowOrganizationConformancePackResponse.

        组织合规规则包名称。

        :return: The org_conformance_pack_name of this ShowOrganizationConformancePackResponse.
        :rtype: str
        """
        return self._org_conformance_pack_name

    @org_conformance_pack_name.setter
    def org_conformance_pack_name(self, org_conformance_pack_name):
        """Sets the org_conformance_pack_name of this ShowOrganizationConformancePackResponse.

        组织合规规则包名称。

        :param org_conformance_pack_name: The org_conformance_pack_name of this ShowOrganizationConformancePackResponse.
        :type org_conformance_pack_name: str
        """
        self._org_conformance_pack_name = org_conformance_pack_name

    @property
    def owner_id(self):
        """Gets the owner_id of this ShowOrganizationConformancePackResponse.

        组织合规规则包创建者。

        :return: The owner_id of this ShowOrganizationConformancePackResponse.
        :rtype: str
        """
        return self._owner_id

    @owner_id.setter
    def owner_id(self, owner_id):
        """Sets the owner_id of this ShowOrganizationConformancePackResponse.

        组织合规规则包创建者。

        :param owner_id: The owner_id of this ShowOrganizationConformancePackResponse.
        :type owner_id: str
        """
        self._owner_id = owner_id

    @property
    def organization_id(self):
        """Gets the organization_id of this ShowOrganizationConformancePackResponse.

        组织ID

        :return: The organization_id of this ShowOrganizationConformancePackResponse.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        """Sets the organization_id of this ShowOrganizationConformancePackResponse.

        组织ID

        :param organization_id: The organization_id of this ShowOrganizationConformancePackResponse.
        :type organization_id: str
        """
        self._organization_id = organization_id

    @property
    def org_conformance_pack_urn(self):
        """Gets the org_conformance_pack_urn of this ShowOrganizationConformancePackResponse.

        组织合规规则包资源唯一标识。

        :return: The org_conformance_pack_urn of this ShowOrganizationConformancePackResponse.
        :rtype: str
        """
        return self._org_conformance_pack_urn

    @org_conformance_pack_urn.setter
    def org_conformance_pack_urn(self, org_conformance_pack_urn):
        """Sets the org_conformance_pack_urn of this ShowOrganizationConformancePackResponse.

        组织合规规则包资源唯一标识。

        :param org_conformance_pack_urn: The org_conformance_pack_urn of this ShowOrganizationConformancePackResponse.
        :type org_conformance_pack_urn: str
        """
        self._org_conformance_pack_urn = org_conformance_pack_urn

    @property
    def excluded_accounts(self):
        """Gets the excluded_accounts of this ShowOrganizationConformancePackResponse.

        排除配置合规包的帐号。

        :return: The excluded_accounts of this ShowOrganizationConformancePackResponse.
        :rtype: list[str]
        """
        return self._excluded_accounts

    @excluded_accounts.setter
    def excluded_accounts(self, excluded_accounts):
        """Sets the excluded_accounts of this ShowOrganizationConformancePackResponse.

        排除配置合规包的帐号。

        :param excluded_accounts: The excluded_accounts of this ShowOrganizationConformancePackResponse.
        :type excluded_accounts: list[str]
        """
        self._excluded_accounts = excluded_accounts

    @property
    def vars_structure(self):
        """Gets the vars_structure of this ShowOrganizationConformancePackResponse.

        合规规则包参数。

        :return: The vars_structure of this ShowOrganizationConformancePackResponse.
        :rtype: list[:class:`huaweicloudsdkconfig.v1.VarsStructure`]
        """
        return self._vars_structure

    @vars_structure.setter
    def vars_structure(self, vars_structure):
        """Sets the vars_structure of this ShowOrganizationConformancePackResponse.

        合规规则包参数。

        :param vars_structure: The vars_structure of this ShowOrganizationConformancePackResponse.
        :type vars_structure: list[:class:`huaweicloudsdkconfig.v1.VarsStructure`]
        """
        self._vars_structure = vars_structure

    @property
    def created_at(self):
        """Gets the created_at of this ShowOrganizationConformancePackResponse.

        组织合规规则包创建时间。

        :return: The created_at of this ShowOrganizationConformancePackResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ShowOrganizationConformancePackResponse.

        组织合规规则包创建时间。

        :param created_at: The created_at of this ShowOrganizationConformancePackResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ShowOrganizationConformancePackResponse.

        组织合规规则包更新时间。

        :return: The updated_at of this ShowOrganizationConformancePackResponse.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ShowOrganizationConformancePackResponse.

        组织合规规则包更新时间。

        :param updated_at: The updated_at of this ShowOrganizationConformancePackResponse.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def template_key(self):
        """Gets the template_key of this ShowOrganizationConformancePackResponse.

        预定义合规规则包模板名称。

        :return: The template_key of this ShowOrganizationConformancePackResponse.
        :rtype: str
        """
        return self._template_key

    @template_key.setter
    def template_key(self, template_key):
        """Sets the template_key of this ShowOrganizationConformancePackResponse.

        预定义合规规则包模板名称。

        :param template_key: The template_key of this ShowOrganizationConformancePackResponse.
        :type template_key: str
        """
        self._template_key = template_key

    @property
    def template_uri(self):
        """Gets the template_uri of this ShowOrganizationConformancePackResponse.

        合规规则包模板OBS地址

        :return: The template_uri of this ShowOrganizationConformancePackResponse.
        :rtype: str
        """
        return self._template_uri

    @template_uri.setter
    def template_uri(self, template_uri):
        """Sets the template_uri of this ShowOrganizationConformancePackResponse.

        合规规则包模板OBS地址

        :param template_uri: The template_uri of this ShowOrganizationConformancePackResponse.
        :type template_uri: str
        """
        self._template_uri = template_uri

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
        if not isinstance(other, ShowOrganizationConformancePackResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
