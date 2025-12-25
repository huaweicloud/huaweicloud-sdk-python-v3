# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DomainIPWhiteListModel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'domain_id': 'str',
        'region': 'str',
        'type': 'str',
        'value': 'str',
        'created': 'int',
        'updated': 'int'
    }

    attribute_map = {
        'id': 'id',
        'domain_id': 'domain_id',
        'region': 'region',
        'type': 'type',
        'value': 'value',
        'created': 'created',
        'updated': 'updated'
    }

    def __init__(self, id=None, domain_id=None, region=None, type=None, value=None, created=None, updated=None):
        r"""DomainIPWhiteListModel

        The model defined in huaweicloud sdk

        :param id: **参数解释**: id。 **取值范围**: 不涉及。 
        :type id: int
        :param domain_id: **参数解释**: 租户id。 **取值范围**: 不涉及。 
        :type domain_id: str
        :param region: **参数解释**: 区域。 **取值范围**: 不涉及。 
        :type region: str
        :param type: **参数解释**: 类型。 **取值范围**: 不涉及。 
        :type type: str
        :param value: **参数解释**: ip地址。 **取值范围**: 不涉及。 
        :type value: str
        :param created: **参数解释**: 创建时间。 **取值范围**: 不涉及。 
        :type created: int
        :param updated: **参数解释**: 更新时间。 **取值范围**: 不涉及。 
        :type updated: int
        """
        
        

        self._id = None
        self._domain_id = None
        self._region = None
        self._type = None
        self._value = None
        self._created = None
        self._updated = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if domain_id is not None:
            self.domain_id = domain_id
        if region is not None:
            self.region = region
        if type is not None:
            self.type = type
        if value is not None:
            self.value = value
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated

    @property
    def id(self):
        r"""Gets the id of this DomainIPWhiteListModel.

        **参数解释**: id。 **取值范围**: 不涉及。 

        :return: The id of this DomainIPWhiteListModel.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DomainIPWhiteListModel.

        **参数解释**: id。 **取值范围**: 不涉及。 

        :param id: The id of this DomainIPWhiteListModel.
        :type id: int
        """
        self._id = id

    @property
    def domain_id(self):
        r"""Gets the domain_id of this DomainIPWhiteListModel.

        **参数解释**: 租户id。 **取值范围**: 不涉及。 

        :return: The domain_id of this DomainIPWhiteListModel.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        r"""Sets the domain_id of this DomainIPWhiteListModel.

        **参数解释**: 租户id。 **取值范围**: 不涉及。 

        :param domain_id: The domain_id of this DomainIPWhiteListModel.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def region(self):
        r"""Gets the region of this DomainIPWhiteListModel.

        **参数解释**: 区域。 **取值范围**: 不涉及。 

        :return: The region of this DomainIPWhiteListModel.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this DomainIPWhiteListModel.

        **参数解释**: 区域。 **取值范围**: 不涉及。 

        :param region: The region of this DomainIPWhiteListModel.
        :type region: str
        """
        self._region = region

    @property
    def type(self):
        r"""Gets the type of this DomainIPWhiteListModel.

        **参数解释**: 类型。 **取值范围**: 不涉及。 

        :return: The type of this DomainIPWhiteListModel.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DomainIPWhiteListModel.

        **参数解释**: 类型。 **取值范围**: 不涉及。 

        :param type: The type of this DomainIPWhiteListModel.
        :type type: str
        """
        self._type = type

    @property
    def value(self):
        r"""Gets the value of this DomainIPWhiteListModel.

        **参数解释**: ip地址。 **取值范围**: 不涉及。 

        :return: The value of this DomainIPWhiteListModel.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this DomainIPWhiteListModel.

        **参数解释**: ip地址。 **取值范围**: 不涉及。 

        :param value: The value of this DomainIPWhiteListModel.
        :type value: str
        """
        self._value = value

    @property
    def created(self):
        r"""Gets the created of this DomainIPWhiteListModel.

        **参数解释**: 创建时间。 **取值范围**: 不涉及。 

        :return: The created of this DomainIPWhiteListModel.
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this DomainIPWhiteListModel.

        **参数解释**: 创建时间。 **取值范围**: 不涉及。 

        :param created: The created of this DomainIPWhiteListModel.
        :type created: int
        """
        self._created = created

    @property
    def updated(self):
        r"""Gets the updated of this DomainIPWhiteListModel.

        **参数解释**: 更新时间。 **取值范围**: 不涉及。 

        :return: The updated of this DomainIPWhiteListModel.
        :rtype: int
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this DomainIPWhiteListModel.

        **参数解释**: 更新时间。 **取值范围**: 不涉及。 

        :param updated: The updated of this DomainIPWhiteListModel.
        :type updated: int
        """
        self._updated = updated

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
        if not isinstance(other, DomainIPWhiteListModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
