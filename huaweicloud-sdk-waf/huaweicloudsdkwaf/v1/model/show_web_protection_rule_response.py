# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWebProtectionRuleResponse(SdkResponse):

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
        'cve_number': 'str',
        'risk_level': 'int',
        'application_type': 'str',
        'protection_type': 'str',
        'description': 'str',
        'create_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'cve_number': 'cve_number',
        'risk_level': 'risk_level',
        'application_type': 'application_type',
        'protection_type': 'protection_type',
        'description': 'description',
        'create_time': 'create_time'
    }

    def __init__(self, id=None, cve_number=None, risk_level=None, application_type=None, protection_type=None, description=None, create_time=None):
        r"""ShowWebProtectionRuleResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 规则id，唯一标识一条Web防护规则 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type id: str
        :param cve_number: **参数解释：** 关联的CVE编号，对应规则防护的漏洞的CVE标准编号（如CVE-2021-41773） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type cve_number: str
        :param risk_level: **参数解释：** 危险等级 - 1：高危 - 2：中危 - 3：低危  **取值范围：** - 1 - 2 - 3
        :type risk_level: int
        :param application_type: **参数解释：** 应用类型，指定规则适用的应用场景（如Web应用、API接口） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type application_type: str
        :param protection_type: **参数解释：** 防护类型，区分规则的防护类别（如SQL注入防护、XSS防护、命令注入防护） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type protection_type: str
        :param description: **参数解释：** 描述，对Web防护规则的功能、适用场景等补充说明 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type description: str
        :param create_time: **参数解释：** 规则上线时间，Web防护规则正式启用的时间（时间戳格式） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type create_time: int
        """
        
        super(ShowWebProtectionRuleResponse, self).__init__()

        self._id = None
        self._cve_number = None
        self._risk_level = None
        self._application_type = None
        self._protection_type = None
        self._description = None
        self._create_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if cve_number is not None:
            self.cve_number = cve_number
        if risk_level is not None:
            self.risk_level = risk_level
        if application_type is not None:
            self.application_type = application_type
        if protection_type is not None:
            self.protection_type = protection_type
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time

    @property
    def id(self):
        r"""Gets the id of this ShowWebProtectionRuleResponse.

        **参数解释：** 规则id，唯一标识一条Web防护规则 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The id of this ShowWebProtectionRuleResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowWebProtectionRuleResponse.

        **参数解释：** 规则id，唯一标识一条Web防护规则 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param id: The id of this ShowWebProtectionRuleResponse.
        :type id: str
        """
        self._id = id

    @property
    def cve_number(self):
        r"""Gets the cve_number of this ShowWebProtectionRuleResponse.

        **参数解释：** 关联的CVE编号，对应规则防护的漏洞的CVE标准编号（如CVE-2021-41773） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The cve_number of this ShowWebProtectionRuleResponse.
        :rtype: str
        """
        return self._cve_number

    @cve_number.setter
    def cve_number(self, cve_number):
        r"""Sets the cve_number of this ShowWebProtectionRuleResponse.

        **参数解释：** 关联的CVE编号，对应规则防护的漏洞的CVE标准编号（如CVE-2021-41773） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param cve_number: The cve_number of this ShowWebProtectionRuleResponse.
        :type cve_number: str
        """
        self._cve_number = cve_number

    @property
    def risk_level(self):
        r"""Gets the risk_level of this ShowWebProtectionRuleResponse.

        **参数解释：** 危险等级 - 1：高危 - 2：中危 - 3：低危  **取值范围：** - 1 - 2 - 3

        :return: The risk_level of this ShowWebProtectionRuleResponse.
        :rtype: int
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        r"""Sets the risk_level of this ShowWebProtectionRuleResponse.

        **参数解释：** 危险等级 - 1：高危 - 2：中危 - 3：低危  **取值范围：** - 1 - 2 - 3

        :param risk_level: The risk_level of this ShowWebProtectionRuleResponse.
        :type risk_level: int
        """
        self._risk_level = risk_level

    @property
    def application_type(self):
        r"""Gets the application_type of this ShowWebProtectionRuleResponse.

        **参数解释：** 应用类型，指定规则适用的应用场景（如Web应用、API接口） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The application_type of this ShowWebProtectionRuleResponse.
        :rtype: str
        """
        return self._application_type

    @application_type.setter
    def application_type(self, application_type):
        r"""Sets the application_type of this ShowWebProtectionRuleResponse.

        **参数解释：** 应用类型，指定规则适用的应用场景（如Web应用、API接口） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param application_type: The application_type of this ShowWebProtectionRuleResponse.
        :type application_type: str
        """
        self._application_type = application_type

    @property
    def protection_type(self):
        r"""Gets the protection_type of this ShowWebProtectionRuleResponse.

        **参数解释：** 防护类型，区分规则的防护类别（如SQL注入防护、XSS防护、命令注入防护） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The protection_type of this ShowWebProtectionRuleResponse.
        :rtype: str
        """
        return self._protection_type

    @protection_type.setter
    def protection_type(self, protection_type):
        r"""Sets the protection_type of this ShowWebProtectionRuleResponse.

        **参数解释：** 防护类型，区分规则的防护类别（如SQL注入防护、XSS防护、命令注入防护） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param protection_type: The protection_type of this ShowWebProtectionRuleResponse.
        :type protection_type: str
        """
        self._protection_type = protection_type

    @property
    def description(self):
        r"""Gets the description of this ShowWebProtectionRuleResponse.

        **参数解释：** 描述，对Web防护规则的功能、适用场景等补充说明 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The description of this ShowWebProtectionRuleResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowWebProtectionRuleResponse.

        **参数解释：** 描述，对Web防护规则的功能、适用场景等补充说明 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param description: The description of this ShowWebProtectionRuleResponse.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowWebProtectionRuleResponse.

        **参数解释：** 规则上线时间，Web防护规则正式启用的时间（时间戳格式） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The create_time of this ShowWebProtectionRuleResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowWebProtectionRuleResponse.

        **参数解释：** 规则上线时间，Web防护规则正式启用的时间（时间戳格式） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param create_time: The create_time of this ShowWebProtectionRuleResponse.
        :type create_time: int
        """
        self._create_time = create_time

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
        if not isinstance(other, ShowWebProtectionRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
