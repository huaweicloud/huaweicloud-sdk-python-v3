# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LinuxVulDetailInfo:

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
        'cvss_vector': 'str',
        'cve_solution': 'str',
        'cve_affect': 'str',
        'cve_affect_description': 'str',
        'cve_type': 'str',
        'cve_type_description': 'str',
        'cve_level': 'str',
        'cvss': 'float',
        'cvss_version': 'str',
        'description': 'str',
        'public_time': 'int',
        'cnvd_id': 'str',
        'cnnvd_id': 'str',
        'hosts_num': 'VulnerabilityHostNumberInfo'
    }

    attribute_map = {
        'cve_id': 'cve_id',
        'cve_name': 'cve_name',
        'cvss_vector': 'cvss_vector',
        'cve_solution': 'cve_solution',
        'cve_affect': 'cve_affect',
        'cve_affect_description': 'cve_affect_description',
        'cve_type': 'cve_type',
        'cve_type_description': 'cve_type_description',
        'cve_level': 'cve_level',
        'cvss': 'cvss',
        'cvss_version': 'cvss_version',
        'description': 'description',
        'public_time': 'public_time',
        'cnvd_id': 'cnvd_id',
        'cnnvd_id': 'cnnvd_id',
        'hosts_num': 'hosts_num'
    }

    def __init__(self, cve_id=None, cve_name=None, cvss_vector=None, cve_solution=None, cve_affect=None, cve_affect_description=None, cve_type=None, cve_type_description=None, cve_level=None, cvss=None, cvss_version=None, description=None, public_time=None, cnvd_id=None, cnnvd_id=None, hosts_num=None):
        r"""LinuxVulDetailInfo

        The model defined in huaweicloud sdk

        :param cve_id: **参数解释**: 漏洞编号 **取值范围**: 字符长度0-255 
        :type cve_id: str
        :param cve_name: **参数解释**: cve漏洞名称 **取值范围**: 字符长度0-512 
        :type cve_name: str
        :param cvss_vector: **参数解释**: 攻击矢量 **取值范围**: 字符长度0-255 
        :type cvss_vector: str
        :param cve_solution: **参数解释**: cve修复建议 **取值范围**: 字符长度0-4096 
        :type cve_solution: str
        :param cve_affect: **参数解释**: cve漏洞危害 **取值范围**: 字符长度0-128 
        :type cve_affect: str
        :param cve_affect_description: **参数解释**: cve漏洞危害的描述信息 **取值范围**: 字符长度0-4096 
        :type cve_affect_description: str
        :param cve_type: **参数解释**: cve漏洞类型 **取值范围**: 字符长度0-128 
        :type cve_type: str
        :param cve_type_description: **参数解释**: cve漏洞类型的描述信息 **取值范围**: 字符长度0-4096 
        :type cve_type_description: str
        :param cve_level: **参数解释**: cve危险程度 **取值范围**: - Low：低危 - Medium：中危 - High：高危 
        :type cve_level: str
        :param cvss: **参数解释**: 漏洞分值 **取值范围**: 最小值0，最大值10 
        :type cvss: float
        :param cvss_version: **参数解释**: cvss评分版本 **取值范围**: 字符长度0-32 
        :type cvss_version: str
        :param description: **参数解释**: 漏洞描述 **取值范围**: 字符长度0-1024 
        :type description: str
        :param public_time: **参数解释**: 披露时间 **取值范围**: 最小值0，最大值2^63-1 
        :type public_time: int
        :param cnvd_id: **参数解释**: cnvd编号 **取值范围**: 字符长度0-32 
        :type cnvd_id: str
        :param cnnvd_id: **参数解释**: cnnvd编号 **取值范围**: 字符长度0-32 
        :type cnnvd_id: str
        :param hosts_num: 
        :type hosts_num: :class:`huaweicloudsdkhss.v5.VulnerabilityHostNumberInfo`
        """
        
        

        self._cve_id = None
        self._cve_name = None
        self._cvss_vector = None
        self._cve_solution = None
        self._cve_affect = None
        self._cve_affect_description = None
        self._cve_type = None
        self._cve_type_description = None
        self._cve_level = None
        self._cvss = None
        self._cvss_version = None
        self._description = None
        self._public_time = None
        self._cnvd_id = None
        self._cnnvd_id = None
        self._hosts_num = None
        self.discriminator = None

        if cve_id is not None:
            self.cve_id = cve_id
        if cve_name is not None:
            self.cve_name = cve_name
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
        if cvss_version is not None:
            self.cvss_version = cvss_version
        if description is not None:
            self.description = description
        if public_time is not None:
            self.public_time = public_time
        if cnvd_id is not None:
            self.cnvd_id = cnvd_id
        if cnnvd_id is not None:
            self.cnnvd_id = cnnvd_id
        if hosts_num is not None:
            self.hosts_num = hosts_num

    @property
    def cve_id(self):
        r"""Gets the cve_id of this LinuxVulDetailInfo.

        **参数解释**: 漏洞编号 **取值范围**: 字符长度0-255 

        :return: The cve_id of this LinuxVulDetailInfo.
        :rtype: str
        """
        return self._cve_id

    @cve_id.setter
    def cve_id(self, cve_id):
        r"""Sets the cve_id of this LinuxVulDetailInfo.

        **参数解释**: 漏洞编号 **取值范围**: 字符长度0-255 

        :param cve_id: The cve_id of this LinuxVulDetailInfo.
        :type cve_id: str
        """
        self._cve_id = cve_id

    @property
    def cve_name(self):
        r"""Gets the cve_name of this LinuxVulDetailInfo.

        **参数解释**: cve漏洞名称 **取值范围**: 字符长度0-512 

        :return: The cve_name of this LinuxVulDetailInfo.
        :rtype: str
        """
        return self._cve_name

    @cve_name.setter
    def cve_name(self, cve_name):
        r"""Sets the cve_name of this LinuxVulDetailInfo.

        **参数解释**: cve漏洞名称 **取值范围**: 字符长度0-512 

        :param cve_name: The cve_name of this LinuxVulDetailInfo.
        :type cve_name: str
        """
        self._cve_name = cve_name

    @property
    def cvss_vector(self):
        r"""Gets the cvss_vector of this LinuxVulDetailInfo.

        **参数解释**: 攻击矢量 **取值范围**: 字符长度0-255 

        :return: The cvss_vector of this LinuxVulDetailInfo.
        :rtype: str
        """
        return self._cvss_vector

    @cvss_vector.setter
    def cvss_vector(self, cvss_vector):
        r"""Sets the cvss_vector of this LinuxVulDetailInfo.

        **参数解释**: 攻击矢量 **取值范围**: 字符长度0-255 

        :param cvss_vector: The cvss_vector of this LinuxVulDetailInfo.
        :type cvss_vector: str
        """
        self._cvss_vector = cvss_vector

    @property
    def cve_solution(self):
        r"""Gets the cve_solution of this LinuxVulDetailInfo.

        **参数解释**: cve修复建议 **取值范围**: 字符长度0-4096 

        :return: The cve_solution of this LinuxVulDetailInfo.
        :rtype: str
        """
        return self._cve_solution

    @cve_solution.setter
    def cve_solution(self, cve_solution):
        r"""Sets the cve_solution of this LinuxVulDetailInfo.

        **参数解释**: cve修复建议 **取值范围**: 字符长度0-4096 

        :param cve_solution: The cve_solution of this LinuxVulDetailInfo.
        :type cve_solution: str
        """
        self._cve_solution = cve_solution

    @property
    def cve_affect(self):
        r"""Gets the cve_affect of this LinuxVulDetailInfo.

        **参数解释**: cve漏洞危害 **取值范围**: 字符长度0-128 

        :return: The cve_affect of this LinuxVulDetailInfo.
        :rtype: str
        """
        return self._cve_affect

    @cve_affect.setter
    def cve_affect(self, cve_affect):
        r"""Sets the cve_affect of this LinuxVulDetailInfo.

        **参数解释**: cve漏洞危害 **取值范围**: 字符长度0-128 

        :param cve_affect: The cve_affect of this LinuxVulDetailInfo.
        :type cve_affect: str
        """
        self._cve_affect = cve_affect

    @property
    def cve_affect_description(self):
        r"""Gets the cve_affect_description of this LinuxVulDetailInfo.

        **参数解释**: cve漏洞危害的描述信息 **取值范围**: 字符长度0-4096 

        :return: The cve_affect_description of this LinuxVulDetailInfo.
        :rtype: str
        """
        return self._cve_affect_description

    @cve_affect_description.setter
    def cve_affect_description(self, cve_affect_description):
        r"""Sets the cve_affect_description of this LinuxVulDetailInfo.

        **参数解释**: cve漏洞危害的描述信息 **取值范围**: 字符长度0-4096 

        :param cve_affect_description: The cve_affect_description of this LinuxVulDetailInfo.
        :type cve_affect_description: str
        """
        self._cve_affect_description = cve_affect_description

    @property
    def cve_type(self):
        r"""Gets the cve_type of this LinuxVulDetailInfo.

        **参数解释**: cve漏洞类型 **取值范围**: 字符长度0-128 

        :return: The cve_type of this LinuxVulDetailInfo.
        :rtype: str
        """
        return self._cve_type

    @cve_type.setter
    def cve_type(self, cve_type):
        r"""Sets the cve_type of this LinuxVulDetailInfo.

        **参数解释**: cve漏洞类型 **取值范围**: 字符长度0-128 

        :param cve_type: The cve_type of this LinuxVulDetailInfo.
        :type cve_type: str
        """
        self._cve_type = cve_type

    @property
    def cve_type_description(self):
        r"""Gets the cve_type_description of this LinuxVulDetailInfo.

        **参数解释**: cve漏洞类型的描述信息 **取值范围**: 字符长度0-4096 

        :return: The cve_type_description of this LinuxVulDetailInfo.
        :rtype: str
        """
        return self._cve_type_description

    @cve_type_description.setter
    def cve_type_description(self, cve_type_description):
        r"""Sets the cve_type_description of this LinuxVulDetailInfo.

        **参数解释**: cve漏洞类型的描述信息 **取值范围**: 字符长度0-4096 

        :param cve_type_description: The cve_type_description of this LinuxVulDetailInfo.
        :type cve_type_description: str
        """
        self._cve_type_description = cve_type_description

    @property
    def cve_level(self):
        r"""Gets the cve_level of this LinuxVulDetailInfo.

        **参数解释**: cve危险程度 **取值范围**: - Low：低危 - Medium：中危 - High：高危 

        :return: The cve_level of this LinuxVulDetailInfo.
        :rtype: str
        """
        return self._cve_level

    @cve_level.setter
    def cve_level(self, cve_level):
        r"""Sets the cve_level of this LinuxVulDetailInfo.

        **参数解释**: cve危险程度 **取值范围**: - Low：低危 - Medium：中危 - High：高危 

        :param cve_level: The cve_level of this LinuxVulDetailInfo.
        :type cve_level: str
        """
        self._cve_level = cve_level

    @property
    def cvss(self):
        r"""Gets the cvss of this LinuxVulDetailInfo.

        **参数解释**: 漏洞分值 **取值范围**: 最小值0，最大值10 

        :return: The cvss of this LinuxVulDetailInfo.
        :rtype: float
        """
        return self._cvss

    @cvss.setter
    def cvss(self, cvss):
        r"""Sets the cvss of this LinuxVulDetailInfo.

        **参数解释**: 漏洞分值 **取值范围**: 最小值0，最大值10 

        :param cvss: The cvss of this LinuxVulDetailInfo.
        :type cvss: float
        """
        self._cvss = cvss

    @property
    def cvss_version(self):
        r"""Gets the cvss_version of this LinuxVulDetailInfo.

        **参数解释**: cvss评分版本 **取值范围**: 字符长度0-32 

        :return: The cvss_version of this LinuxVulDetailInfo.
        :rtype: str
        """
        return self._cvss_version

    @cvss_version.setter
    def cvss_version(self, cvss_version):
        r"""Sets the cvss_version of this LinuxVulDetailInfo.

        **参数解释**: cvss评分版本 **取值范围**: 字符长度0-32 

        :param cvss_version: The cvss_version of this LinuxVulDetailInfo.
        :type cvss_version: str
        """
        self._cvss_version = cvss_version

    @property
    def description(self):
        r"""Gets the description of this LinuxVulDetailInfo.

        **参数解释**: 漏洞描述 **取值范围**: 字符长度0-1024 

        :return: The description of this LinuxVulDetailInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this LinuxVulDetailInfo.

        **参数解释**: 漏洞描述 **取值范围**: 字符长度0-1024 

        :param description: The description of this LinuxVulDetailInfo.
        :type description: str
        """
        self._description = description

    @property
    def public_time(self):
        r"""Gets the public_time of this LinuxVulDetailInfo.

        **参数解释**: 披露时间 **取值范围**: 最小值0，最大值2^63-1 

        :return: The public_time of this LinuxVulDetailInfo.
        :rtype: int
        """
        return self._public_time

    @public_time.setter
    def public_time(self, public_time):
        r"""Sets the public_time of this LinuxVulDetailInfo.

        **参数解释**: 披露时间 **取值范围**: 最小值0，最大值2^63-1 

        :param public_time: The public_time of this LinuxVulDetailInfo.
        :type public_time: int
        """
        self._public_time = public_time

    @property
    def cnvd_id(self):
        r"""Gets the cnvd_id of this LinuxVulDetailInfo.

        **参数解释**: cnvd编号 **取值范围**: 字符长度0-32 

        :return: The cnvd_id of this LinuxVulDetailInfo.
        :rtype: str
        """
        return self._cnvd_id

    @cnvd_id.setter
    def cnvd_id(self, cnvd_id):
        r"""Sets the cnvd_id of this LinuxVulDetailInfo.

        **参数解释**: cnvd编号 **取值范围**: 字符长度0-32 

        :param cnvd_id: The cnvd_id of this LinuxVulDetailInfo.
        :type cnvd_id: str
        """
        self._cnvd_id = cnvd_id

    @property
    def cnnvd_id(self):
        r"""Gets the cnnvd_id of this LinuxVulDetailInfo.

        **参数解释**: cnnvd编号 **取值范围**: 字符长度0-32 

        :return: The cnnvd_id of this LinuxVulDetailInfo.
        :rtype: str
        """
        return self._cnnvd_id

    @cnnvd_id.setter
    def cnnvd_id(self, cnnvd_id):
        r"""Sets the cnnvd_id of this LinuxVulDetailInfo.

        **参数解释**: cnnvd编号 **取值范围**: 字符长度0-32 

        :param cnnvd_id: The cnnvd_id of this LinuxVulDetailInfo.
        :type cnnvd_id: str
        """
        self._cnnvd_id = cnnvd_id

    @property
    def hosts_num(self):
        r"""Gets the hosts_num of this LinuxVulDetailInfo.

        :return: The hosts_num of this LinuxVulDetailInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.VulnerabilityHostNumberInfo`
        """
        return self._hosts_num

    @hosts_num.setter
    def hosts_num(self, hosts_num):
        r"""Sets the hosts_num of this LinuxVulDetailInfo.

        :param hosts_num: The hosts_num of this LinuxVulDetailInfo.
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
        if not isinstance(other, LinuxVulDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
