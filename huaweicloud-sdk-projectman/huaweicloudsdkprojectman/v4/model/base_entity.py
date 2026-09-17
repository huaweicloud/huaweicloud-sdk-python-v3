# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BaseEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tenant_id': 'str',
        'modified_by': 'str',
        'modified_date': 'str',
        'created_by': 'str',
        'created_date': 'str'
    }

    attribute_map = {
        'tenant_id': 'tenant_id',
        'modified_by': 'modified_by',
        'modified_date': 'modified_date',
        'created_by': 'created_by',
        'created_date': 'created_date'
    }

    def __init__(self, tenant_id=None, modified_by=None, modified_date=None, created_by=None, created_date=None):
        r"""BaseEntity

        The model defined in huaweicloud sdk

        :param tenant_id: **参数解释**： 租户ID。 **取值范围**： 不涉及。
        :type tenant_id: str
        :param modified_by: **参数解释**： 修改人。 **取值范围**： 不涉及。
        :type modified_by: str
        :param modified_date: **参数解释**： 修改时间。 **取值范围**： 不涉及。
        :type modified_date: str
        :param created_by: **参数解释**： 创建人。 **取值范围**： 不涉及。
        :type created_by: str
        :param created_date: **参数解释**： 创建时间。 **取值范围**： 不涉及。
        :type created_date: str
        """
        
        

        self._tenant_id = None
        self._modified_by = None
        self._modified_date = None
        self._created_by = None
        self._created_date = None
        self.discriminator = None

        if tenant_id is not None:
            self.tenant_id = tenant_id
        if modified_by is not None:
            self.modified_by = modified_by
        if modified_date is not None:
            self.modified_date = modified_date
        if created_by is not None:
            self.created_by = created_by
        if created_date is not None:
            self.created_date = created_date

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this BaseEntity.

        **参数解释**： 租户ID。 **取值范围**： 不涉及。

        :return: The tenant_id of this BaseEntity.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this BaseEntity.

        **参数解释**： 租户ID。 **取值范围**： 不涉及。

        :param tenant_id: The tenant_id of this BaseEntity.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def modified_by(self):
        r"""Gets the modified_by of this BaseEntity.

        **参数解释**： 修改人。 **取值范围**： 不涉及。

        :return: The modified_by of this BaseEntity.
        :rtype: str
        """
        return self._modified_by

    @modified_by.setter
    def modified_by(self, modified_by):
        r"""Sets the modified_by of this BaseEntity.

        **参数解释**： 修改人。 **取值范围**： 不涉及。

        :param modified_by: The modified_by of this BaseEntity.
        :type modified_by: str
        """
        self._modified_by = modified_by

    @property
    def modified_date(self):
        r"""Gets the modified_date of this BaseEntity.

        **参数解释**： 修改时间。 **取值范围**： 不涉及。

        :return: The modified_date of this BaseEntity.
        :rtype: str
        """
        return self._modified_date

    @modified_date.setter
    def modified_date(self, modified_date):
        r"""Sets the modified_date of this BaseEntity.

        **参数解释**： 修改时间。 **取值范围**： 不涉及。

        :param modified_date: The modified_date of this BaseEntity.
        :type modified_date: str
        """
        self._modified_date = modified_date

    @property
    def created_by(self):
        r"""Gets the created_by of this BaseEntity.

        **参数解释**： 创建人。 **取值范围**： 不涉及。

        :return: The created_by of this BaseEntity.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this BaseEntity.

        **参数解释**： 创建人。 **取值范围**： 不涉及。

        :param created_by: The created_by of this BaseEntity.
        :type created_by: str
        """
        self._created_by = created_by

    @property
    def created_date(self):
        r"""Gets the created_date of this BaseEntity.

        **参数解释**： 创建时间。 **取值范围**： 不涉及。

        :return: The created_date of this BaseEntity.
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        r"""Sets the created_date of this BaseEntity.

        **参数解释**： 创建时间。 **取值范围**： 不涉及。

        :param created_date: The created_date of this BaseEntity.
        :type created_date: str
        """
        self._created_date = created_date

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
        if not isinstance(other, BaseEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
