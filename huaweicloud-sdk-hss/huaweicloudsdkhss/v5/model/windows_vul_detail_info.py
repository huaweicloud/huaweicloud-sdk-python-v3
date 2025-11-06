# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WindowsVulDetailInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cve_id': 'str',
        'cve_name': 'str',
        'cvss_version': 'str',
        'cvss_vector': 'str',
        'cve_solution': 'str',
        'cve_affect': 'str',
        'cve_affect_description': 'str',
        'cve_type': 'str',
        'cve_type_description': 'str',
        'cve_level': 'str',
        'cvss': 'float',
        'public_time': 'int',
        'description': 'str',
        'hosts_num': 'VulnerabilityHostNumberInfo'
    }

    attribute_map = {
        'cve_id': 'cve_id',
        'cve_name': 'cve_name',
        'cvss_version': 'cvss_version',
        'cvss_vector': 'cvss_vector',
        'cve_solution': 'cve_solution',
        'cve_affect': 'cve_affect',
        'cve_affect_description': 'cve_affect_description',
        'cve_type': 'cve_type',
        'cve_type_description': 'cve_type_description',
        'cve_level': 'cve_level',
        'cvss': 'cvss',
        'public_time': 'public_time',
        'description': 'description',
        'hosts_num': 'hosts_num'
    }

    def __init__(self, cve_id=None, cve_name=None, cvss_version=None, cvss_vector=None, cve_solution=None, cve_affect=None, cve_affect_description=None, cve_type=None, cve_type_description=None, cve_level=None, cvss=None, public_time=None, description=None, hosts_num=None):
        r"""WindowsVulDetailInfo

        The model defined in huaweicloud sdk

        :param cve_id: **参数解释**: CVE ID **取值范围**: 字符范围1-32位 
        :type cve_id: str
        :param cve_name: **参数解释**: cve漏洞名称 **取值范围**: 字符范围0-512位 
        :type cve_name: str
        :param cvss_version: **参数解释**: cvss评分版本 **取值范围**: 字符范围0-32位 
        :type cvss_version: str
        :param cvss_vector: **参数解释**: 攻击矢量 **取值范围**: 字符范围0-128位 
        :type cvss_vector: str
        :param cve_solution: **参数解释**: cve修复建议 **取值范围**: 字符范围0-128位 
        :type cve_solution: str
        :param cve_affect: **参数解释**: cve漏洞危害 **取值范围**: 字符范围0-128位 
        :type cve_affect: str
        :param cve_affect_description: **参数解释**: cve漏洞危害的描述信息 **取值范围**: 字符范围0-4096位 
        :type cve_affect_description: str
        :param cve_type: **参数解释**: cve漏洞类型 **取值范围**: 字符范围0-128位 
        :type cve_type: str
        :param cve_type_description: **参数解释**: cve漏洞类型的描述信息 **取值范围**: 字符范围0-4096位 
        :type cve_type_description: str
        :param cve_level: **参数解释**: 危险程度 **取值范围**: - Low：低危险程度 - Medium：中危险程度 - High：高危险程度 
        :type cve_level: str
        :param cvss: **参数解释**: cvss评分 **取值范围**: 最小值0，最大值10 
        :type cvss: float
        :param public_time: **参数解释**: 漏洞披露时间 **取值范围**: 最小值0，最大值9223372036854775807 
        :type public_time: int
        :param description: **参数解释**: cve漏洞描述 **取值范围**: 字符范围0-65535位 
        :type description: str
        :param hosts_num: 
        :type hosts_num: :class:`huaweicloudsdkhss.v5.VulnerabilityHostNumberInfo`
        """
        
        

        self._cve_id = None
        self._cve_name = None
        self._cvss_version = None
        self._cvss_vector = None
        self._cve_solution = None
        self._cve_affect = None
        self._cve_affect_description = None
        self._cve_type = None
        self._cve_type_description = None
        self._cve_level = None
        self._cvss = None
        self._public_time = None
        self._description = None
        self._hosts_num = None
        self.discriminator = None

        if cve_id is not None:
            self.cve_id = cve_id
        if cve_name is not None:
            self.cve_name = cve_name
        if cvss_version is not None:
            self.cvss_version = cvss_version
        if cvss_vector is not None:
            self.cvss_vector = cvss_vector
        if cve_solution is not None:
            self.cve_solution = cve_solution
        if cve_affect is not None:
            self.cve_affect = cve_affect
        if cve_affect_description is not None:
            self.cve_affect_description = cve_affect_description
        if cve_type is not None:
            self.cve_type = cve_type
        if cve_type_description is not None:
            self.cve_type_description = cve_type_description
        if cve_level is not None:
            self.cve_level = cve_level
        if cvss is not None:
            self.cvss = cvss
        if public_time is not None:
            self.public_time = public_time
        if description is not None:
            self.description = description
        if hosts_num is not None:
            self.hosts_num = hosts_num

    @property
    def cve_id(self):
        r"""Gets the cve_id of this WindowsVulDetailInfo.

        **参数解释**: CVE ID **取值范围**: 字符范围1-32位 

        :return: The cve_id of this WindowsVulDetailInfo.
        :rtype: str
        """
        return self._cve_id

    @cve_id.setter
    def cve_id(self, cve_id):
        r"""Sets the cve_id of this WindowsVulDetailInfo.

        **参数解释**: CVE ID **取值范围**: 字符范围1-32位 

        :param cve_id: The cve_id of this WindowsVulDetailInfo.
        :type cve_id: str
        """
        self._cve_id = cve_id

    @property
    def cve_name(self):
        r"""Gets the cve_name of this WindowsVulDetailInfo.

        **参数解释**: cve漏洞名称 **取值范围**: 字符范围0-512位 

        :return: The cve_name of this WindowsVulDetailInfo.
        :rtype: str
        """
        return self._cve_name

    @cve_name.setter
    def cve_name(self, cve_name):
        r"""Sets the cve_name of this WindowsVulDetailInfo.

        **参数解释**: cve漏洞名称 **取值范围**: 字符范围0-512位 

        :param cve_name: The cve_name of this WindowsVulDetailInfo.
        :type cve_name: str
        """
        self._cve_name = cve_name

    @property
    def cvss_version(self):
        r"""Gets the cvss_version of this WindowsVulDetailInfo.

        **参数解释**: cvss评分版本 **取值范围**: 字符范围0-32位 

        :return: The cvss_version of this WindowsVulDetailInfo.
        :rtype: str
        """
        return self._cvss_version

    @cvss_version.setter
    def cvss_version(self, cvss_version):
        r"""Sets the cvss_version of this WindowsVulDetailInfo.

        **参数解释**: cvss评分版本 **取值范围**: 字符范围0-32位 

        :param cvss_version: The cvss_version of this WindowsVulDetailInfo.
        :type cvss_version: str
        """
        self._cvss_version = cvss_version

    @property
    def cvss_vector(self):
        r"""Gets the cvss_vector of this WindowsVulDetailInfo.

        **参数解释**: 攻击矢量 **取值范围**: 字符范围0-128位 

        :return: The cvss_vector of this WindowsVulDetailInfo.
        :rtype: str
        """
        return self._cvss_vector

    @cvss_vector.setter
    def cvss_vector(self, cvss_vector):
        r"""Sets the cvss_vector of this WindowsVulDetailInfo.

        **参数解释**: 攻击矢量 **取值范围**: 字符范围0-128位 

        :param cvss_vector: The cvss_vector of this WindowsVulDetailInfo.
        :type cvss_vector: str
        """
        self._cvss_vector = cvss_vector

    @property
    def cve_solution(self):
        r"""Gets the cve_solution of this WindowsVulDetailInfo.

        **参数解释**: cve修复建议 **取值范围**: 字符范围0-128位 

        :return: The cve_solution of this WindowsVulDetailInfo.
        :rtype: str
        """
        return self._cve_solution

    @cve_solution.setter
    def cve_solution(self, cve_solution):
        r"""Sets the cve_solution of this WindowsVulDetailInfo.

        **参数解释**: cve修复建议 **取值范围**: 字符范围0-128位 

        :param cve_solution: The cve_solution of this WindowsVulDetailInfo.
        :type cve_solution: str
        """
        self._cve_solution = cve_solution

    @property
    def cve_affect(self):
        r"""Gets the cve_affect of this WindowsVulDetailInfo.

        **参数解释**: cve漏洞危害 **取值范围**: 字符范围0-128位 

        :return: The cve_affect of this WindowsVulDetailInfo.
        :rtype: str
        """
        return self._cve_affect

    @cve_affect.setter
    def cve_affect(self, cve_affect):
        r"""Sets the cve_affect of this WindowsVulDetailInfo.

        **参数解释**: cve漏洞危害 **取值范围**: 字符范围0-128位 

        :param cve_affect: The cve_affect of this WindowsVulDetailInfo.
        :type cve_affect: str
        """
        self._cve_affect = cve_affect

    @property
    def cve_affect_description(self):
        r"""Gets the cve_affect_description of this WindowsVulDetailInfo.

        **参数解释**: cve漏洞危害的描述信息 **取值范围**: 字符范围0-4096位 

        :return: The cve_affect_description of this WindowsVulDetailInfo.
        :rtype: str
        """
        return self._cve_affect_description

    @cve_affect_description.setter
    def cve_affect_description(self, cve_affect_description):
        r"""Sets the cve_affect_description of this WindowsVulDetailInfo.

        **参数解释**: cve漏洞危害的描述信息 **取值范围**: 字符范围0-4096位 

        :param cve_affect_description: The cve_affect_description of this WindowsVulDetailInfo.
        :type cve_affect_description: str
        """
        self._cve_affect_description = cve_affect_description

    @property
    def cve_type(self):
        r"""Gets the cve_type of this WindowsVulDetailInfo.

        **参数解释**: cve漏洞类型 **取值范围**: 字符范围0-128位 

        :return: The cve_type of this WindowsVulDetailInfo.
        :rtype: str
        """
        return self._cve_type

    @cve_type.setter
    def cve_type(self, cve_type):
        r"""Sets the cve_type of this WindowsVulDetailInfo.

        **参数解释**: cve漏洞类型 **取值范围**: 字符范围0-128位 

        :param cve_type: The cve_type of this WindowsVulDetailInfo.
        :type cve_type: str
        """
        self._cve_type = cve_type

    @property
    def cve_type_description(self):
        r"""Gets the cve_type_description of this WindowsVulDetailInfo.

        **参数解释**: cve漏洞类型的描述信息 **取值范围**: 字符范围0-4096位 

        :return: The cve_type_description of this WindowsVulDetailInfo.
        :rtype: str
        """
        return self._cve_type_description

    @cve_type_description.setter
    def cve_type_description(self, cve_type_description):
        r"""Sets the cve_type_description of this WindowsVulDetailInfo.

        **参数解释**: cve漏洞类型的描述信息 **取值范围**: 字符范围0-4096位 

        :param cve_type_description: The cve_type_description of this WindowsVulDetailInfo.
        :type cve_type_description: str
        """
        self._cve_type_description = cve_type_description

    @property
    def cve_level(self):
        r"""Gets the cve_level of this WindowsVulDetailInfo.

        **参数解释**: 危险程度 **取值范围**: - Low：低危险程度 - Medium：中危险程度 - High：高危险程度 

        :return: The cve_level of this WindowsVulDetailInfo.
        :rtype: str
        """
        return self._cve_level

    @cve_level.setter
    def cve_level(self, cve_level):
        r"""Sets the cve_level of this WindowsVulDetailInfo.

        **参数解释**: 危险程度 **取值范围**: - Low：低危险程度 - Medium：中危险程度 - High：高危险程度 

        :param cve_level: The cve_level of this WindowsVulDetailInfo.
        :type cve_level: str
        """
        self._cve_level = cve_level

    @property
    def cvss(self):
        r"""Gets the cvss of this WindowsVulDetailInfo.

        **参数解释**: cvss评分 **取值范围**: 最小值0，最大值10 

        :return: The cvss of this WindowsVulDetailInfo.
        :rtype: float
        """
        return self._cvss

    @cvss.setter
    def cvss(self, cvss):
        r"""Sets the cvss of this WindowsVulDetailInfo.

        **参数解释**: cvss评分 **取值范围**: 最小值0，最大值10 

        :param cvss: The cvss of this WindowsVulDetailInfo.
        :type cvss: float
        """
        self._cvss = cvss

    @property
    def public_time(self):
        r"""Gets the public_time of this WindowsVulDetailInfo.

        **参数解释**: 漏洞披露时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The public_time of this WindowsVulDetailInfo.
        :rtype: int
        """
        return self._public_time

    @public_time.setter
    def public_time(self, public_time):
        r"""Sets the public_time of this WindowsVulDetailInfo.

        **参数解释**: 漏洞披露时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :param public_time: The public_time of this WindowsVulDetailInfo.
        :type public_time: int
        """
        self._public_time = public_time

    @property
    def description(self):
        r"""Gets the description of this WindowsVulDetailInfo.

        **参数解释**: cve漏洞描述 **取值范围**: 字符范围0-65535位 

        :return: The description of this WindowsVulDetailInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this WindowsVulDetailInfo.

        **参数解释**: cve漏洞描述 **取值范围**: 字符范围0-65535位 

        :param description: The description of this WindowsVulDetailInfo.
        :type description: str
        """
        self._description = description

    @property
    def hosts_num(self):
        r"""Gets the hosts_num of this WindowsVulDetailInfo.

        :return: The hosts_num of this WindowsVulDetailInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.VulnerabilityHostNumberInfo`
        """
        return self._hosts_num

    @hosts_num.setter
    def hosts_num(self, hosts_num):
        r"""Sets the hosts_num of this WindowsVulDetailInfo.

        :param hosts_num: The hosts_num of this WindowsVulDetailInfo.
        :type hosts_num: :class:`huaweicloudsdkhss.v5.VulnerabilityHostNumberInfo`
        """
        self._hosts_num = hosts_num

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
        if not isinstance(other, WindowsVulDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
