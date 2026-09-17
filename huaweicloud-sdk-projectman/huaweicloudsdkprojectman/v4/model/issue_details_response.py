# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IssueDetailsResponse:

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
        'number': 'str',
        'type': 'str',
        'stay_days': 'int',
        'tenant_id': 'str',
        'created_date': 'str',
        'title': 'str',
        'security_level': 'SecurityLevelResult'
    }

    attribute_map = {
        'id': 'id',
        'number': 'number',
        'type': 'type',
        'stay_days': 'stay_days',
        'tenant_id': 'tenant_id',
        'created_date': 'created_date',
        'title': 'title',
        'security_level': 'security_level'
    }

    def __init__(self, id=None, number=None, type=None, stay_days=None, tenant_id=None, created_date=None, title=None, security_level=None):
        r"""IssueDetailsResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 工作项ID。 **取值范围**： 不涉及。
        :type id: str
        :param number: **参数解释**： 工作项编号。 **取值范围**： 不涉及。
        :type number: str
        :param type: **参数解释**： 工作项类型。 **取值范围**： 不涉及。
        :type type: str
        :param stay_days: **参数解释**： 停留天数。 **取值范围**： 不涉及。
        :type stay_days: int
        :param tenant_id: **参数解释**： 租户ID。 **取值范围**： 不涉及。
        :type tenant_id: str
        :param created_date: **参数解释**： 工作项创建时间。 **取值范围**： 不涉及。
        :type created_date: str
        :param title: **参数解释**： 工作项标题。 **取值范围**： 不涉及。
        :type title: str
        :param security_level: 
        :type security_level: :class:`huaweicloudsdkprojectman.v4.SecurityLevelResult`
        """
        
        

        self._id = None
        self._number = None
        self._type = None
        self._stay_days = None
        self._tenant_id = None
        self._created_date = None
        self._title = None
        self._security_level = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if number is not None:
            self.number = number
        if type is not None:
            self.type = type
        if stay_days is not None:
            self.stay_days = stay_days
        if tenant_id is not None:
            self.tenant_id = tenant_id
        if created_date is not None:
            self.created_date = created_date
        if title is not None:
            self.title = title
        if security_level is not None:
            self.security_level = security_level

    @property
    def id(self):
        r"""Gets the id of this IssueDetailsResponse.

        **参数解释**： 工作项ID。 **取值范围**： 不涉及。

        :return: The id of this IssueDetailsResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this IssueDetailsResponse.

        **参数解释**： 工作项ID。 **取值范围**： 不涉及。

        :param id: The id of this IssueDetailsResponse.
        :type id: str
        """
        self._id = id

    @property
    def number(self):
        r"""Gets the number of this IssueDetailsResponse.

        **参数解释**： 工作项编号。 **取值范围**： 不涉及。

        :return: The number of this IssueDetailsResponse.
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this IssueDetailsResponse.

        **参数解释**： 工作项编号。 **取值范围**： 不涉及。

        :param number: The number of this IssueDetailsResponse.
        :type number: str
        """
        self._number = number

    @property
    def type(self):
        r"""Gets the type of this IssueDetailsResponse.

        **参数解释**： 工作项类型。 **取值范围**： 不涉及。

        :return: The type of this IssueDetailsResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this IssueDetailsResponse.

        **参数解释**： 工作项类型。 **取值范围**： 不涉及。

        :param type: The type of this IssueDetailsResponse.
        :type type: str
        """
        self._type = type

    @property
    def stay_days(self):
        r"""Gets the stay_days of this IssueDetailsResponse.

        **参数解释**： 停留天数。 **取值范围**： 不涉及。

        :return: The stay_days of this IssueDetailsResponse.
        :rtype: int
        """
        return self._stay_days

    @stay_days.setter
    def stay_days(self, stay_days):
        r"""Sets the stay_days of this IssueDetailsResponse.

        **参数解释**： 停留天数。 **取值范围**： 不涉及。

        :param stay_days: The stay_days of this IssueDetailsResponse.
        :type stay_days: int
        """
        self._stay_days = stay_days

    @property
    def tenant_id(self):
        r"""Gets the tenant_id of this IssueDetailsResponse.

        **参数解释**： 租户ID。 **取值范围**： 不涉及。

        :return: The tenant_id of this IssueDetailsResponse.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        r"""Sets the tenant_id of this IssueDetailsResponse.

        **参数解释**： 租户ID。 **取值范围**： 不涉及。

        :param tenant_id: The tenant_id of this IssueDetailsResponse.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def created_date(self):
        r"""Gets the created_date of this IssueDetailsResponse.

        **参数解释**： 工作项创建时间。 **取值范围**： 不涉及。

        :return: The created_date of this IssueDetailsResponse.
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        r"""Sets the created_date of this IssueDetailsResponse.

        **参数解释**： 工作项创建时间。 **取值范围**： 不涉及。

        :param created_date: The created_date of this IssueDetailsResponse.
        :type created_date: str
        """
        self._created_date = created_date

    @property
    def title(self):
        r"""Gets the title of this IssueDetailsResponse.

        **参数解释**： 工作项标题。 **取值范围**： 不涉及。

        :return: The title of this IssueDetailsResponse.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this IssueDetailsResponse.

        **参数解释**： 工作项标题。 **取值范围**： 不涉及。

        :param title: The title of this IssueDetailsResponse.
        :type title: str
        """
        self._title = title

    @property
    def security_level(self):
        r"""Gets the security_level of this IssueDetailsResponse.

        :return: The security_level of this IssueDetailsResponse.
        :rtype: :class:`huaweicloudsdkprojectman.v4.SecurityLevelResult`
        """
        return self._security_level

    @security_level.setter
    def security_level(self, security_level):
        r"""Sets the security_level of this IssueDetailsResponse.

        :param security_level: The security_level of this IssueDetailsResponse.
        :type security_level: :class:`huaweicloudsdkprojectman.v4.SecurityLevelResult`
        """
        self._security_level = security_level

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
        if not isinstance(other, IssueDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
