# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AffectedResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'affected_attached_domain_id': 'str',
        'affected_attached_project_id': 'str',
        'affected_head': 'DataResourceHead',
        'affected_properties': 'object',
        'affected_protected_id': 'str',
        'affected_subtype': 'str',
        'affected_type': 'str',
        'affected_urn': 'str',
        'affected_urnext': 'str',
        'affected_value': 'str'
    }

    attribute_map = {
        'affected_attached_domain_id': 'affected_attached_domain_id',
        'affected_attached_project_id': 'affected_attached_project_id',
        'affected_head': 'affected_head',
        'affected_properties': 'affected_properties',
        'affected_protected_id': 'affected_protected_id',
        'affected_subtype': 'affected_subtype',
        'affected_type': 'affected_type',
        'affected_urn': 'affected_urn',
        'affected_urnext': 'affected_urnext',
        'affected_value': 'affected_value'
    }

    def __init__(self, affected_attached_domain_id=None, affected_attached_project_id=None, affected_head=None, affected_properties=None, affected_protected_id=None, affected_subtype=None, affected_type=None, affected_urn=None, affected_urnext=None, affected_value=None):
        r"""AffectedResource

        The model defined in huaweicloud sdk

        :param affected_attached_domain_id: 被防护对象账户ID
        :type affected_attached_domain_id: str
        :param affected_attached_project_id: 被防护对象项目ID
        :type affected_attached_project_id: str
        :param affected_head: 
        :type affected_head: :class:`huaweicloudsdkdbss.v1.DataResourceHead`
        :param affected_properties: 资源扩展信息
        :type affected_properties: object
        :param affected_protected_id: 被防护(受影响）对象在防线系统内唯一ID
        :type affected_protected_id: str
        :param affected_subtype: 被防护(受影响）对象子类型: 固定为：DB
        :type affected_subtype: str
        :param affected_type: 被防护(受影响）对象类型，数据库资产，固定为：Data
        :type affected_type: str
        :param affected_urn: 被防护对象urn
        :type affected_urn: str
        :param affected_urnext: 被防护对象URN扩展
        :type affected_urnext: str
        :param affected_value: 被防护(受影响）对象值，云下数据库同affectedProtectedId，云上不传
        :type affected_value: str
        """
        
        

        self._affected_attached_domain_id = None
        self._affected_attached_project_id = None
        self._affected_head = None
        self._affected_properties = None
        self._affected_protected_id = None
        self._affected_subtype = None
        self._affected_type = None
        self._affected_urn = None
        self._affected_urnext = None
        self._affected_value = None
        self.discriminator = None

        if affected_attached_domain_id is not None:
            self.affected_attached_domain_id = affected_attached_domain_id
        if affected_attached_project_id is not None:
            self.affected_attached_project_id = affected_attached_project_id
        if affected_head is not None:
            self.affected_head = affected_head
        if affected_properties is not None:
            self.affected_properties = affected_properties
        if affected_protected_id is not None:
            self.affected_protected_id = affected_protected_id
        if affected_subtype is not None:
            self.affected_subtype = affected_subtype
        if affected_type is not None:
            self.affected_type = affected_type
        if affected_urn is not None:
            self.affected_urn = affected_urn
        if affected_urnext is not None:
            self.affected_urnext = affected_urnext
        if affected_value is not None:
            self.affected_value = affected_value

    @property
    def affected_attached_domain_id(self):
        r"""Gets the affected_attached_domain_id of this AffectedResource.

        被防护对象账户ID

        :return: The affected_attached_domain_id of this AffectedResource.
        :rtype: str
        """
        return self._affected_attached_domain_id

    @affected_attached_domain_id.setter
    def affected_attached_domain_id(self, affected_attached_domain_id):
        r"""Sets the affected_attached_domain_id of this AffectedResource.

        被防护对象账户ID

        :param affected_attached_domain_id: The affected_attached_domain_id of this AffectedResource.
        :type affected_attached_domain_id: str
        """
        self._affected_attached_domain_id = affected_attached_domain_id

    @property
    def affected_attached_project_id(self):
        r"""Gets the affected_attached_project_id of this AffectedResource.

        被防护对象项目ID

        :return: The affected_attached_project_id of this AffectedResource.
        :rtype: str
        """
        return self._affected_attached_project_id

    @affected_attached_project_id.setter
    def affected_attached_project_id(self, affected_attached_project_id):
        r"""Sets the affected_attached_project_id of this AffectedResource.

        被防护对象项目ID

        :param affected_attached_project_id: The affected_attached_project_id of this AffectedResource.
        :type affected_attached_project_id: str
        """
        self._affected_attached_project_id = affected_attached_project_id

    @property
    def affected_head(self):
        r"""Gets the affected_head of this AffectedResource.

        :return: The affected_head of this AffectedResource.
        :rtype: :class:`huaweicloudsdkdbss.v1.DataResourceHead`
        """
        return self._affected_head

    @affected_head.setter
    def affected_head(self, affected_head):
        r"""Sets the affected_head of this AffectedResource.

        :param affected_head: The affected_head of this AffectedResource.
        :type affected_head: :class:`huaweicloudsdkdbss.v1.DataResourceHead`
        """
        self._affected_head = affected_head

    @property
    def affected_properties(self):
        r"""Gets the affected_properties of this AffectedResource.

        资源扩展信息

        :return: The affected_properties of this AffectedResource.
        :rtype: object
        """
        return self._affected_properties

    @affected_properties.setter
    def affected_properties(self, affected_properties):
        r"""Sets the affected_properties of this AffectedResource.

        资源扩展信息

        :param affected_properties: The affected_properties of this AffectedResource.
        :type affected_properties: object
        """
        self._affected_properties = affected_properties

    @property
    def affected_protected_id(self):
        r"""Gets the affected_protected_id of this AffectedResource.

        被防护(受影响）对象在防线系统内唯一ID

        :return: The affected_protected_id of this AffectedResource.
        :rtype: str
        """
        return self._affected_protected_id

    @affected_protected_id.setter
    def affected_protected_id(self, affected_protected_id):
        r"""Sets the affected_protected_id of this AffectedResource.

        被防护(受影响）对象在防线系统内唯一ID

        :param affected_protected_id: The affected_protected_id of this AffectedResource.
        :type affected_protected_id: str
        """
        self._affected_protected_id = affected_protected_id

    @property
    def affected_subtype(self):
        r"""Gets the affected_subtype of this AffectedResource.

        被防护(受影响）对象子类型: 固定为：DB

        :return: The affected_subtype of this AffectedResource.
        :rtype: str
        """
        return self._affected_subtype

    @affected_subtype.setter
    def affected_subtype(self, affected_subtype):
        r"""Sets the affected_subtype of this AffectedResource.

        被防护(受影响）对象子类型: 固定为：DB

        :param affected_subtype: The affected_subtype of this AffectedResource.
        :type affected_subtype: str
        """
        self._affected_subtype = affected_subtype

    @property
    def affected_type(self):
        r"""Gets the affected_type of this AffectedResource.

        被防护(受影响）对象类型，数据库资产，固定为：Data

        :return: The affected_type of this AffectedResource.
        :rtype: str
        """
        return self._affected_type

    @affected_type.setter
    def affected_type(self, affected_type):
        r"""Sets the affected_type of this AffectedResource.

        被防护(受影响）对象类型，数据库资产，固定为：Data

        :param affected_type: The affected_type of this AffectedResource.
        :type affected_type: str
        """
        self._affected_type = affected_type

    @property
    def affected_urn(self):
        r"""Gets the affected_urn of this AffectedResource.

        被防护对象urn

        :return: The affected_urn of this AffectedResource.
        :rtype: str
        """
        return self._affected_urn

    @affected_urn.setter
    def affected_urn(self, affected_urn):
        r"""Sets the affected_urn of this AffectedResource.

        被防护对象urn

        :param affected_urn: The affected_urn of this AffectedResource.
        :type affected_urn: str
        """
        self._affected_urn = affected_urn

    @property
    def affected_urnext(self):
        r"""Gets the affected_urnext of this AffectedResource.

        被防护对象URN扩展

        :return: The affected_urnext of this AffectedResource.
        :rtype: str
        """
        return self._affected_urnext

    @affected_urnext.setter
    def affected_urnext(self, affected_urnext):
        r"""Sets the affected_urnext of this AffectedResource.

        被防护对象URN扩展

        :param affected_urnext: The affected_urnext of this AffectedResource.
        :type affected_urnext: str
        """
        self._affected_urnext = affected_urnext

    @property
    def affected_value(self):
        r"""Gets the affected_value of this AffectedResource.

        被防护(受影响）对象值，云下数据库同affectedProtectedId，云上不传

        :return: The affected_value of this AffectedResource.
        :rtype: str
        """
        return self._affected_value

    @affected_value.setter
    def affected_value(self, affected_value):
        r"""Sets the affected_value of this AffectedResource.

        被防护(受影响）对象值，云下数据库同affectedProtectedId，云上不传

        :param affected_value: The affected_value of this AffectedResource.
        :type affected_value: str
        """
        self._affected_value = affected_value

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AffectedResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
