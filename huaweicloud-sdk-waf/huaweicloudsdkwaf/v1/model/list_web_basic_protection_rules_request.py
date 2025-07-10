# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWebBasicProtectionRulesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'enterprise_project_id': 'str',
        'offset': 'int',
        'limit': 'int',
        '_from': 'int',
        'to': 'int',
        'level': 'int',
        'id': 'str',
        'description': 'str',
        'cve_number': 'str',
        'risk_level': 'int',
        'protection_type_names': 'str',
        'application_type_names': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        '_from': 'from',
        'to': 'to',
        'level': 'level',
        'id': 'id',
        'description': 'description',
        'cve_number': 'cve_number',
        'risk_level': 'risk_level',
        'protection_type_names': 'protection_type_names',
        'application_type_names': 'application_type_names'
    }

    def __init__(self, x_language=None, enterprise_project_id=None, offset=None, limit=None, _from=None, to=None, level=None, id=None, description=None, cve_number=None, risk_level=None, protection_type_names=None, application_type_names=None):
        r"""ListWebBasicProtectionRulesRequest

        The model defined in huaweicloud sdk

        :param x_language: **参数解释：** 语言，默认值为zh-cn。zh-cn（中文）/en-us（英文）。 **约束限制：** 不涉及 **取值范围：** - zh-cn：中文 - en-us：英文  **默认取值：** - zh-cn
        :type x_language: str
        :param enterprise_project_id: **参数解释：** 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目ID。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。 **约束限制：** 不涉及 **取值范围：**  - 0：代表default企业项目  - all_granted_eps：代表所有企业项目  - 其它企业项目ID：长度为36个字符  **默认取值：** 0
        :type enterprise_project_id: str
        :param offset: **参数解释：** 分页查询的起始位置，表示从第几条记录开始返回（从1开始计数）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 1
        :type offset: int
        :param limit: **参数解释：** 分页查询的单页返回数量，控制每次请求返回的记录条数。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 10
        :type limit: int
        :param _from: **参数解释：** 起始时间（13位毫秒时间戳），需要和to同时使用。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type _from: int
        :param to: **参数解释：** 结束时间（13位毫秒时间戳），需要和from同时使用。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type to: int
        :param level: **参数解释：** 规则集的防护严格程度。规则集（宽松）下对业务的误报率降低，但漏报率可能会增高；而规则集（严格）下对业务的误报率可能会增高，但漏报率降低。 **约束限制：** 不涉及 **取值范围：** - 1：宽松 - 2：中等 - 3：严格  **默认取值：** 不涉及
        :type level: int
        :param id: **参数解释：** 规则ID，规则的唯一标识。 **约束限制：** 不涉及 **取值范围：** 长度为6个字符 **默认取值：** 不涉及
        :type id: str
        :param description: **参数解释：** 规则描述 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type description: str
        :param cve_number: **参数解释：** CVE编号 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type cve_number: str
        :param risk_level: **参数解释：** 危险等级 **约束限制：** 不涉及 **取值范围：** - 1：高危 - 2：中危 - 3：低危  **默认取值：** 不涉及
        :type risk_level: int
        :param protection_type_names: **参数解释：** 防护类型 **约束限制：** 不涉及 **取值范围：** - vuln：其他 - xss：跨站脚本 - cmdi：命令注入 - lfi：本地文件包含 - rfi：远程文件包含 - webshell：网站木马 - robot：恶意爬虫 - sqli：SQL注入  **默认取值：** 不涉及
        :type protection_type_names: str
        :param application_type_names: **参数解释：** 应用类型 **约束限制：** 不涉及 **取值范围：** 请参见WAF控制台，Web基础防护规则详情页面的应用类型。 **默认取值：** 不涉及
        :type application_type_names: str
        """
        
        

        self._x_language = None
        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self.__from = None
        self._to = None
        self._level = None
        self._id = None
        self._description = None
        self._cve_number = None
        self._risk_level = None
        self._protection_type_names = None
        self._application_type_names = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if level is not None:
            self.level = level
        if id is not None:
            self.id = id
        if description is not None:
            self.description = description
        if cve_number is not None:
            self.cve_number = cve_number
        if risk_level is not None:
            self.risk_level = risk_level
        if protection_type_names is not None:
            self.protection_type_names = protection_type_names
        if application_type_names is not None:
            self.application_type_names = application_type_names

    @property
    def x_language(self):
        r"""Gets the x_language of this ListWebBasicProtectionRulesRequest.

        **参数解释：** 语言，默认值为zh-cn。zh-cn（中文）/en-us（英文）。 **约束限制：** 不涉及 **取值范围：** - zh-cn：中文 - en-us：英文  **默认取值：** - zh-cn

        :return: The x_language of this ListWebBasicProtectionRulesRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListWebBasicProtectionRulesRequest.

        **参数解释：** 语言，默认值为zh-cn。zh-cn（中文）/en-us（英文）。 **约束限制：** 不涉及 **取值范围：** - zh-cn：中文 - en-us：英文  **默认取值：** - zh-cn

        :param x_language: The x_language of this ListWebBasicProtectionRulesRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListWebBasicProtectionRulesRequest.

        **参数解释：** 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目ID。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。 **约束限制：** 不涉及 **取值范围：**  - 0：代表default企业项目  - all_granted_eps：代表所有企业项目  - 其它企业项目ID：长度为36个字符  **默认取值：** 0

        :return: The enterprise_project_id of this ListWebBasicProtectionRulesRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListWebBasicProtectionRulesRequest.

        **参数解释：** 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目ID。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。 **约束限制：** 不涉及 **取值范围：**  - 0：代表default企业项目  - all_granted_eps：代表所有企业项目  - 其它企业项目ID：长度为36个字符  **默认取值：** 0

        :param enterprise_project_id: The enterprise_project_id of this ListWebBasicProtectionRulesRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListWebBasicProtectionRulesRequest.

        **参数解释：** 分页查询的起始位置，表示从第几条记录开始返回（从1开始计数）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 1

        :return: The offset of this ListWebBasicProtectionRulesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListWebBasicProtectionRulesRequest.

        **参数解释：** 分页查询的起始位置，表示从第几条记录开始返回（从1开始计数）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 1

        :param offset: The offset of this ListWebBasicProtectionRulesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListWebBasicProtectionRulesRequest.

        **参数解释：** 分页查询的单页返回数量，控制每次请求返回的记录条数。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 10

        :return: The limit of this ListWebBasicProtectionRulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListWebBasicProtectionRulesRequest.

        **参数解释：** 分页查询的单页返回数量，控制每次请求返回的记录条数。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 10

        :param limit: The limit of this ListWebBasicProtectionRulesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def _from(self):
        r"""Gets the _from of this ListWebBasicProtectionRulesRequest.

        **参数解释：** 起始时间（13位毫秒时间戳），需要和to同时使用。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The _from of this ListWebBasicProtectionRulesRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        r"""Sets the _from of this ListWebBasicProtectionRulesRequest.

        **参数解释：** 起始时间（13位毫秒时间戳），需要和to同时使用。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param _from: The _from of this ListWebBasicProtectionRulesRequest.
        :type _from: int
        """
        self.__from = _from

    @property
    def to(self):
        r"""Gets the to of this ListWebBasicProtectionRulesRequest.

        **参数解释：** 结束时间（13位毫秒时间戳），需要和from同时使用。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The to of this ListWebBasicProtectionRulesRequest.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        r"""Sets the to of this ListWebBasicProtectionRulesRequest.

        **参数解释：** 结束时间（13位毫秒时间戳），需要和from同时使用。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param to: The to of this ListWebBasicProtectionRulesRequest.
        :type to: int
        """
        self._to = to

    @property
    def level(self):
        r"""Gets the level of this ListWebBasicProtectionRulesRequest.

        **参数解释：** 规则集的防护严格程度。规则集（宽松）下对业务的误报率降低，但漏报率可能会增高；而规则集（严格）下对业务的误报率可能会增高，但漏报率降低。 **约束限制：** 不涉及 **取值范围：** - 1：宽松 - 2：中等 - 3：严格  **默认取值：** 不涉及

        :return: The level of this ListWebBasicProtectionRulesRequest.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this ListWebBasicProtectionRulesRequest.

        **参数解释：** 规则集的防护严格程度。规则集（宽松）下对业务的误报率降低，但漏报率可能会增高；而规则集（严格）下对业务的误报率可能会增高，但漏报率降低。 **约束限制：** 不涉及 **取值范围：** - 1：宽松 - 2：中等 - 3：严格  **默认取值：** 不涉及

        :param level: The level of this ListWebBasicProtectionRulesRequest.
        :type level: int
        """
        self._level = level

    @property
    def id(self):
        r"""Gets the id of this ListWebBasicProtectionRulesRequest.

        **参数解释：** 规则ID，规则的唯一标识。 **约束限制：** 不涉及 **取值范围：** 长度为6个字符 **默认取值：** 不涉及

        :return: The id of this ListWebBasicProtectionRulesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListWebBasicProtectionRulesRequest.

        **参数解释：** 规则ID，规则的唯一标识。 **约束限制：** 不涉及 **取值范围：** 长度为6个字符 **默认取值：** 不涉及

        :param id: The id of this ListWebBasicProtectionRulesRequest.
        :type id: str
        """
        self._id = id

    @property
    def description(self):
        r"""Gets the description of this ListWebBasicProtectionRulesRequest.

        **参数解释：** 规则描述 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The description of this ListWebBasicProtectionRulesRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListWebBasicProtectionRulesRequest.

        **参数解释：** 规则描述 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param description: The description of this ListWebBasicProtectionRulesRequest.
        :type description: str
        """
        self._description = description

    @property
    def cve_number(self):
        r"""Gets the cve_number of this ListWebBasicProtectionRulesRequest.

        **参数解释：** CVE编号 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The cve_number of this ListWebBasicProtectionRulesRequest.
        :rtype: str
        """
        return self._cve_number

    @cve_number.setter
    def cve_number(self, cve_number):
        r"""Sets the cve_number of this ListWebBasicProtectionRulesRequest.

        **参数解释：** CVE编号 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param cve_number: The cve_number of this ListWebBasicProtectionRulesRequest.
        :type cve_number: str
        """
        self._cve_number = cve_number

    @property
    def risk_level(self):
        r"""Gets the risk_level of this ListWebBasicProtectionRulesRequest.

        **参数解释：** 危险等级 **约束限制：** 不涉及 **取值范围：** - 1：高危 - 2：中危 - 3：低危  **默认取值：** 不涉及

        :return: The risk_level of this ListWebBasicProtectionRulesRequest.
        :rtype: int
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        r"""Sets the risk_level of this ListWebBasicProtectionRulesRequest.

        **参数解释：** 危险等级 **约束限制：** 不涉及 **取值范围：** - 1：高危 - 2：中危 - 3：低危  **默认取值：** 不涉及

        :param risk_level: The risk_level of this ListWebBasicProtectionRulesRequest.
        :type risk_level: int
        """
        self._risk_level = risk_level

    @property
    def protection_type_names(self):
        r"""Gets the protection_type_names of this ListWebBasicProtectionRulesRequest.

        **参数解释：** 防护类型 **约束限制：** 不涉及 **取值范围：** - vuln：其他 - xss：跨站脚本 - cmdi：命令注入 - lfi：本地文件包含 - rfi：远程文件包含 - webshell：网站木马 - robot：恶意爬虫 - sqli：SQL注入  **默认取值：** 不涉及

        :return: The protection_type_names of this ListWebBasicProtectionRulesRequest.
        :rtype: str
        """
        return self._protection_type_names

    @protection_type_names.setter
    def protection_type_names(self, protection_type_names):
        r"""Sets the protection_type_names of this ListWebBasicProtectionRulesRequest.

        **参数解释：** 防护类型 **约束限制：** 不涉及 **取值范围：** - vuln：其他 - xss：跨站脚本 - cmdi：命令注入 - lfi：本地文件包含 - rfi：远程文件包含 - webshell：网站木马 - robot：恶意爬虫 - sqli：SQL注入  **默认取值：** 不涉及

        :param protection_type_names: The protection_type_names of this ListWebBasicProtectionRulesRequest.
        :type protection_type_names: str
        """
        self._protection_type_names = protection_type_names

    @property
    def application_type_names(self):
        r"""Gets the application_type_names of this ListWebBasicProtectionRulesRequest.

        **参数解释：** 应用类型 **约束限制：** 不涉及 **取值范围：** 请参见WAF控制台，Web基础防护规则详情页面的应用类型。 **默认取值：** 不涉及

        :return: The application_type_names of this ListWebBasicProtectionRulesRequest.
        :rtype: str
        """
        return self._application_type_names

    @application_type_names.setter
    def application_type_names(self, application_type_names):
        r"""Sets the application_type_names of this ListWebBasicProtectionRulesRequest.

        **参数解释：** 应用类型 **约束限制：** 不涉及 **取值范围：** 请参见WAF控制台，Web基础防护规则详情页面的应用类型。 **默认取值：** 不涉及

        :param application_type_names: The application_type_names of this ListWebBasicProtectionRulesRequest.
        :type application_type_names: str
        """
        self._application_type_names = application_type_names

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
        if not isinstance(other, ListWebBasicProtectionRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
