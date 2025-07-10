# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WebBasicProtectionRulesItem:

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
        'description': 'str',
        'cve_number': 'str',
        'risk_level': 'int',
        'application_type': 'str',
        'protection_type': 'str',
        'effective_time': 'int',
        'create_time': 'int',
        'update_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'description': 'description',
        'cve_number': 'cve_number',
        'risk_level': 'risk_level',
        'application_type': 'application_type',
        'protection_type': 'protection_type',
        'effective_time': 'effective_time',
        'create_time': 'create_time',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, description=None, cve_number=None, risk_level=None, application_type=None, protection_type=None, effective_time=None, create_time=None, update_time=None):
        r"""WebBasicProtectionRulesItem

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 规则的ID，规则的唯一标识 **取值范围：** 不涉及
        :type id: str
        :param description: **参数解释：** 规则描述 **取值范围：** 不涉及
        :type description: str
        :param cve_number: **参数解释：** CVE编号 **取值范围：** 不涉及
        :type cve_number: str
        :param risk_level: **参数解释：** 危险等级 - 1：高危 - 2：中危 - 3：低危  **取值范围：** - 1 - 2 - 3
        :type risk_level: int
        :param application_type: **参数解释：** 应用类型 **取值范围：** 不涉及
        :type application_type: str
        :param protection_type: **参数解释：** 防护类型 **取值范围：** 不涉及
        :type protection_type: str
        :param effective_time: **参数解释：** 生效时间 **取值范围：** 不涉及
        :type effective_time: int
        :param create_time: **参数解释：** 创建时间 **取值范围：** 不涉及
        :type create_time: int
        :param update_time: **参数解释：** 更新时间 **取值范围：** 不涉及
        :type update_time: int
        """
        
        

        self._id = None
        self._description = None
        self._cve_number = None
        self._risk_level = None
        self._application_type = None
        self._protection_type = None
        self._effective_time = None
        self._create_time = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if description is not None:
            self.description = description
        if cve_number is not None:
            self.cve_number = cve_number
        if risk_level is not None:
            self.risk_level = risk_level
        if application_type is not None:
            self.application_type = application_type
        if protection_type is not None:
            self.protection_type = protection_type
        if effective_time is not None:
            self.effective_time = effective_time
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this WebBasicProtectionRulesItem.

        **参数解释：** 规则的ID，规则的唯一标识 **取值范围：** 不涉及

        :return: The id of this WebBasicProtectionRulesItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this WebBasicProtectionRulesItem.

        **参数解释：** 规则的ID，规则的唯一标识 **取值范围：** 不涉及

        :param id: The id of this WebBasicProtectionRulesItem.
        :type id: str
        """
        self._id = id

    @property
    def description(self):
        r"""Gets the description of this WebBasicProtectionRulesItem.

        **参数解释：** 规则描述 **取值范围：** 不涉及

        :return: The description of this WebBasicProtectionRulesItem.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this WebBasicProtectionRulesItem.

        **参数解释：** 规则描述 **取值范围：** 不涉及

        :param description: The description of this WebBasicProtectionRulesItem.
        :type description: str
        """
        self._description = description

    @property
    def cve_number(self):
        r"""Gets the cve_number of this WebBasicProtectionRulesItem.

        **参数解释：** CVE编号 **取值范围：** 不涉及

        :return: The cve_number of this WebBasicProtectionRulesItem.
        :rtype: str
        """
        return self._cve_number

    @cve_number.setter
    def cve_number(self, cve_number):
        r"""Sets the cve_number of this WebBasicProtectionRulesItem.

        **参数解释：** CVE编号 **取值范围：** 不涉及

        :param cve_number: The cve_number of this WebBasicProtectionRulesItem.
        :type cve_number: str
        """
        self._cve_number = cve_number

    @property
    def risk_level(self):
        r"""Gets the risk_level of this WebBasicProtectionRulesItem.

        **参数解释：** 危险等级 - 1：高危 - 2：中危 - 3：低危  **取值范围：** - 1 - 2 - 3

        :return: The risk_level of this WebBasicProtectionRulesItem.
        :rtype: int
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        r"""Sets the risk_level of this WebBasicProtectionRulesItem.

        **参数解释：** 危险等级 - 1：高危 - 2：中危 - 3：低危  **取值范围：** - 1 - 2 - 3

        :param risk_level: The risk_level of this WebBasicProtectionRulesItem.
        :type risk_level: int
        """
        self._risk_level = risk_level

    @property
    def application_type(self):
        r"""Gets the application_type of this WebBasicProtectionRulesItem.

        **参数解释：** 应用类型 **取值范围：** 不涉及

        :return: The application_type of this WebBasicProtectionRulesItem.
        :rtype: str
        """
        return self._application_type

    @application_type.setter
    def application_type(self, application_type):
        r"""Sets the application_type of this WebBasicProtectionRulesItem.

        **参数解释：** 应用类型 **取值范围：** 不涉及

        :param application_type: The application_type of this WebBasicProtectionRulesItem.
        :type application_type: str
        """
        self._application_type = application_type

    @property
    def protection_type(self):
        r"""Gets the protection_type of this WebBasicProtectionRulesItem.

        **参数解释：** 防护类型 **取值范围：** 不涉及

        :return: The protection_type of this WebBasicProtectionRulesItem.
        :rtype: str
        """
        return self._protection_type

    @protection_type.setter
    def protection_type(self, protection_type):
        r"""Sets the protection_type of this WebBasicProtectionRulesItem.

        **参数解释：** 防护类型 **取值范围：** 不涉及

        :param protection_type: The protection_type of this WebBasicProtectionRulesItem.
        :type protection_type: str
        """
        self._protection_type = protection_type

    @property
    def effective_time(self):
        r"""Gets the effective_time of this WebBasicProtectionRulesItem.

        **参数解释：** 生效时间 **取值范围：** 不涉及

        :return: The effective_time of this WebBasicProtectionRulesItem.
        :rtype: int
        """
        return self._effective_time

    @effective_time.setter
    def effective_time(self, effective_time):
        r"""Sets the effective_time of this WebBasicProtectionRulesItem.

        **参数解释：** 生效时间 **取值范围：** 不涉及

        :param effective_time: The effective_time of this WebBasicProtectionRulesItem.
        :type effective_time: int
        """
        self._effective_time = effective_time

    @property
    def create_time(self):
        r"""Gets the create_time of this WebBasicProtectionRulesItem.

        **参数解释：** 创建时间 **取值范围：** 不涉及

        :return: The create_time of this WebBasicProtectionRulesItem.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this WebBasicProtectionRulesItem.

        **参数解释：** 创建时间 **取值范围：** 不涉及

        :param create_time: The create_time of this WebBasicProtectionRulesItem.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this WebBasicProtectionRulesItem.

        **参数解释：** 更新时间 **取值范围：** 不涉及

        :return: The update_time of this WebBasicProtectionRulesItem.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this WebBasicProtectionRulesItem.

        **参数解释：** 更新时间 **取值范围：** 不涉及

        :param update_time: The update_time of this WebBasicProtectionRulesItem.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, WebBasicProtectionRulesItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
