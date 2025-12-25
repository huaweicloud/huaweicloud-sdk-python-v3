# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WebCmsVulDetailInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vul_id': 'str',
        'app': 'str',
        'name_zh': 'str',
        'name_en': 'str',
        'public_time': 'int',
        'vul_label_zh': 'str',
        'vul_label_en': 'str',
        'repair_necessity': 'int',
        'severity_level': 'str',
        'description_zh': 'str',
        'description_en': 'str',
        'solution_zh': 'str',
        'solution_en': 'str',
        'cve_id': 'str',
        'cve_score': 'float',
        'cnvd_id': 'str',
        'cnnvd_id': 'str',
        'bugtraq_id': 'str',
        'suffix_path': 'str',
        'md5': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'tags_zh': 'str',
        'tags_en': 'str',
        'patch_url': 'str',
        'hosts_num': 'VulnerabilityHostNumberInfo',
        'cve_level': 'str',
        'cvss': 'float',
        'cvss_version': 'str',
        'description': 'str',
        'cve_name': 'str',
        'cvss_vector': 'str',
        'cve_solution': 'str',
        'cve_affect': 'str',
        'cve_affect_description': 'str',
        'cve_type': 'str',
        'cve_type_description': 'str'
    }

    attribute_map = {
        'vul_id': 'vul_id',
        'app': 'app',
        'name_zh': 'name_zh',
        'name_en': 'name_en',
        'public_time': 'public_time',
        'vul_label_zh': 'vulLabel_zh',
        'vul_label_en': 'vulLabel_en',
        'repair_necessity': 'repair_necessity',
        'severity_level': 'severity_level',
        'description_zh': 'description_zh',
        'description_en': 'description_en',
        'solution_zh': 'solution_zh',
        'solution_en': 'solution_en',
        'cve_id': 'cve_id',
        'cve_score': 'cve_score',
        'cnvd_id': 'cnvd_id',
        'cnnvd_id': 'cnnvd_id',
        'bugtraq_id': 'bugtraq_id',
        'suffix_path': 'suffix_path',
        'md5': 'md5',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'tags_zh': 'tags_zh',
        'tags_en': 'tags_en',
        'patch_url': 'patch_url',
        'hosts_num': 'hosts_num',
        'cve_level': 'cve_level',
        'cvss': 'cvss',
        'cvss_version': 'cvss_version',
        'description': 'description',
        'cve_name': 'cve_name',
        'cvss_vector': 'cvss_vector',
        'cve_solution': 'cve_solution',
        'cve_affect': 'cve_affect',
        'cve_affect_description': 'cve_affect_description',
        'cve_type': 'cve_type',
        'cve_type_description': 'cve_type_description'
    }

    def __init__(self, vul_id=None, app=None, name_zh=None, name_en=None, public_time=None, vul_label_zh=None, vul_label_en=None, repair_necessity=None, severity_level=None, description_zh=None, description_en=None, solution_zh=None, solution_en=None, cve_id=None, cve_score=None, cnvd_id=None, cnnvd_id=None, bugtraq_id=None, suffix_path=None, md5=None, create_time=None, update_time=None, tags_zh=None, tags_en=None, patch_url=None, hosts_num=None, cve_level=None, cvss=None, cvss_version=None, description=None, cve_name=None, cvss_vector=None, cve_solution=None, cve_affect=None, cve_affect_description=None, cve_type=None, cve_type_description=None):
        r"""WebCmsVulDetailInfo

        The model defined in huaweicloud sdk

        :param vul_id: **参数解释**: 漏洞补丁编号 **取值范围**: 字符长度0-256 
        :type vul_id: str
        :param app: **参数解释**: 软件名称 **取值范围**: 字符长度0-32 
        :type app: str
        :param name_zh: **参数解释**: 中文名称 **取值范围**: 字符长度0-128 
        :type name_zh: str
        :param name_en: **参数解释**: 英文名称 **取值范围**: 字符长度0-128 
        :type name_en: str
        :param public_time: **参数解释**: 披露时间 **取值范围**: 最小值0，最大值2^63-1 
        :type public_time: int
        :param vul_label_zh: **参数解释**: 漏洞标签中文名称（已废弃，后续删除） **取值范围**: 字符长度0-64 
        :type vul_label_zh: str
        :param vul_label_en: **参数解释**: 漏洞标签英文名称（已废弃，后续删除） **取值范围**: 字符长度0-64 
        :type vul_label_en: str
        :param repair_necessity: **参数解释**: 修复必要性 **取值范围**: - 1：高 - 2：中 - 3：低 
        :type repair_necessity: int
        :param severity_level: **参数解释**: 修复必要性 **取值范围**: - Low：低危 - Medium：中危 - High：高危 - Critical：紧急 
        :type severity_level: str
        :param description_zh: **参数解释**: cve漏洞中文描述 **取值范围**: 字符长度0-1024 
        :type description_zh: str
        :param description_en: **参数解释**: cve漏洞英文描述 **取值范围**: 字符长度0-1024 
        :type description_en: str
        :param solution_zh: **参数解释**: cve漏洞中文修复建议 **取值范围**: 字符长度0-1024 
        :type solution_zh: str
        :param solution_en: **参数解释**: cve漏洞英文修复建议 **取值范围**: 字符长度0-1024 
        :type solution_en: str
        :param cve_id: **参数解释**: 漏洞编号 **取值范围**: 字符长度0-255 
        :type cve_id: str
        :param cve_score: **参数解释**: cve分数 **取值范围**: 最小值0，最大值10 
        :type cve_score: float
        :param cnvd_id: **参数解释**: cnvd编号 **取值范围**: 字符长度0-32 
        :type cnvd_id: str
        :param cnnvd_id: **参数解释**: cnnvd编号 **取值范围**: 字符长度0-32 
        :type cnnvd_id: str
        :param bugtraq_id: **参数解释**: bugtraq编号 **取值范围**: 字符长度0-32 
        :type bugtraq_id: str
        :param suffix_path: **参数解释**: 后缀路径 **取值范围**: 字符长度0-128 
        :type suffix_path: str
        :param md5: **参数解释**: md5 **取值范围**: 字符长度0-32 
        :type md5: str
        :param create_time: **参数解释**: 创建时间 **取值范围**: 最小值0，最大值9223372036854775807 
        :type create_time: int
        :param update_time: **参数解释**: 更新时间 **取值范围**: 最小值0，最大值9223372036854775807 
        :type update_time: int
        :param tags_zh: **参数解释**: 漏洞标签中文名称 **取值范围**: 字符长度0-64 
        :type tags_zh: str
        :param tags_en: **参数解释**: 漏洞标签英文名称 **取值范围**: 字符长度0-64 
        :type tags_en: str
        :param patch_url: **参数解释**: 补丁地址 **取值范围**: 字符长度0-512 
        :type patch_url: str
        :param hosts_num: 
        :type hosts_num: :class:`huaweicloudsdkhss.v5.VulnerabilityHostNumberInfo`
        :param cve_level: **参数解释**: cve危险程度 **取值范围**: - Low：低危 - Medium：中危 - High：高危 
        :type cve_level: str
        :param cvss: **参数解释**: 漏洞分值 **取值范围**: 最小值0，最大值10 
        :type cvss: float
        :param cvss_version: **参数解释**: cvss评分版本 **取值范围**: 字符长度0-32 
        :type cvss_version: str
        :param description: **参数解释**: 漏洞描述 **取值范围**: 字符长度0-1024 
        :type description: str
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
        """
        
        

        self._vul_id = None
        self._app = None
        self._name_zh = None
        self._name_en = None
        self._public_time = None
        self._vul_label_zh = None
        self._vul_label_en = None
        self._repair_necessity = None
        self._severity_level = None
        self._description_zh = None
        self._description_en = None
        self._solution_zh = None
        self._solution_en = None
        self._cve_id = None
        self._cve_score = None
        self._cnvd_id = None
        self._cnnvd_id = None
        self._bugtraq_id = None
        self._suffix_path = None
        self._md5 = None
        self._create_time = None
        self._update_time = None
        self._tags_zh = None
        self._tags_en = None
        self._patch_url = None
        self._hosts_num = None
        self._cve_level = None
        self._cvss = None
        self._cvss_version = None
        self._description = None
        self._cve_name = None
        self._cvss_vector = None
        self._cve_solution = None
        self._cve_affect = None
        self._cve_affect_description = None
        self._cve_type = None
        self._cve_type_description = None
        self.discriminator = None

        if vul_id is not None:
            self.vul_id = vul_id
        if app is not None:
            self.app = app
        if name_zh is not None:
            self.name_zh = name_zh
        if name_en is not None:
            self.name_en = name_en
        if public_time is not None:
            self.public_time = public_time
        if vul_label_zh is not None:
            self.vul_label_zh = vul_label_zh
        if vul_label_en is not None:
            self.vul_label_en = vul_label_en
        if repair_necessity is not None:
            self.repair_necessity = repair_necessity
        if severity_level is not None:
            self.severity_level = severity_level
        if description_zh is not None:
            self.description_zh = description_zh
        if description_en is not None:
            self.description_en = description_en
        if solution_zh is not None:
            self.solution_zh = solution_zh
        if solution_en is not None:
            self.solution_en = solution_en
        if cve_id is not None:
            self.cve_id = cve_id
        if cve_score is not None:
            self.cve_score = cve_score
        if cnvd_id is not None:
            self.cnvd_id = cnvd_id
        if cnnvd_id is not None:
            self.cnnvd_id = cnnvd_id
        if bugtraq_id is not None:
            self.bugtraq_id = bugtraq_id
        if suffix_path is not None:
            self.suffix_path = suffix_path
        if md5 is not None:
            self.md5 = md5
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if tags_zh is not None:
            self.tags_zh = tags_zh
        if tags_en is not None:
            self.tags_en = tags_en
        if patch_url is not None:
            self.patch_url = patch_url
        if hosts_num is not None:
            self.hosts_num = hosts_num
        if cve_level is not None:
            self.cve_level = cve_level
        if cvss is not None:
            self.cvss = cvss
        if cvss_version is not None:
            self.cvss_version = cvss_version
        if description is not None:
            self.description = description
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

    @property
    def vul_id(self):
        r"""Gets the vul_id of this WebCmsVulDetailInfo.

        **参数解释**: 漏洞补丁编号 **取值范围**: 字符长度0-256 

        :return: The vul_id of this WebCmsVulDetailInfo.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        r"""Sets the vul_id of this WebCmsVulDetailInfo.

        **参数解释**: 漏洞补丁编号 **取值范围**: 字符长度0-256 

        :param vul_id: The vul_id of this WebCmsVulDetailInfo.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def app(self):
        r"""Gets the app of this WebCmsVulDetailInfo.

        **参数解释**: 软件名称 **取值范围**: 字符长度0-32 

        :return: The app of this WebCmsVulDetailInfo.
        :rtype: str
        """
        return self._app

    @app.setter
    def app(self, app):
        r"""Sets the app of this WebCmsVulDetailInfo.

        **参数解释**: 软件名称 **取值范围**: 字符长度0-32 

        :param app: The app of this WebCmsVulDetailInfo.
        :type app: str
        """
        self._app = app

    @property
    def name_zh(self):
        r"""Gets the name_zh of this WebCmsVulDetailInfo.

        **参数解释**: 中文名称 **取值范围**: 字符长度0-128 

        :return: The name_zh of this WebCmsVulDetailInfo.
        :rtype: str
        """
        return self._name_zh

    @name_zh.setter
    def name_zh(self, name_zh):
        r"""Sets the name_zh of this WebCmsVulDetailInfo.

        **参数解释**: 中文名称 **取值范围**: 字符长度0-128 

        :param name_zh: The name_zh of this WebCmsVulDetailInfo.
        :type name_zh: str
        """
        self._name_zh = name_zh

    @property
    def name_en(self):
        r"""Gets the name_en of this WebCmsVulDetailInfo.

        **参数解释**: 英文名称 **取值范围**: 字符长度0-128 

        :return: The name_en of this WebCmsVulDetailInfo.
        :rtype: str
        """
        return self._name_en

    @name_en.setter
    def name_en(self, name_en):
        r"""Sets the name_en of this WebCmsVulDetailInfo.

        **参数解释**: 英文名称 **取值范围**: 字符长度0-128 

        :param name_en: The name_en of this WebCmsVulDetailInfo.
        :type name_en: str
        """
        self._name_en = name_en

    @property
    def public_time(self):
        r"""Gets the public_time of this WebCmsVulDetailInfo.

        **参数解释**: 披露时间 **取值范围**: 最小值0，最大值2^63-1 

        :return: The public_time of this WebCmsVulDetailInfo.
        :rtype: int
        """
        return self._public_time

    @public_time.setter
    def public_time(self, public_time):
        r"""Sets the public_time of this WebCmsVulDetailInfo.

        **参数解释**: 披露时间 **取值范围**: 最小值0，最大值2^63-1 

        :param public_time: The public_time of this WebCmsVulDetailInfo.
        :type public_time: int
        """
        self._public_time = public_time

    @property
    def vul_label_zh(self):
        r"""Gets the vul_label_zh of this WebCmsVulDetailInfo.

        **参数解释**: 漏洞标签中文名称（已废弃，后续删除） **取值范围**: 字符长度0-64 

        :return: The vul_label_zh of this WebCmsVulDetailInfo.
        :rtype: str
        """
        return self._vul_label_zh

    @vul_label_zh.setter
    def vul_label_zh(self, vul_label_zh):
        r"""Sets the vul_label_zh of this WebCmsVulDetailInfo.

        **参数解释**: 漏洞标签中文名称（已废弃，后续删除） **取值范围**: 字符长度0-64 

        :param vul_label_zh: The vul_label_zh of this WebCmsVulDetailInfo.
        :type vul_label_zh: str
        """
        self._vul_label_zh = vul_label_zh

    @property
    def vul_label_en(self):
        r"""Gets the vul_label_en of this WebCmsVulDetailInfo.

        **参数解释**: 漏洞标签英文名称（已废弃，后续删除） **取值范围**: 字符长度0-64 

        :return: The vul_label_en of this WebCmsVulDetailInfo.
        :rtype: str
        """
        return self._vul_label_en

    @vul_label_en.setter
    def vul_label_en(self, vul_label_en):
        r"""Sets the vul_label_en of this WebCmsVulDetailInfo.

        **参数解释**: 漏洞标签英文名称（已废弃，后续删除） **取值范围**: 字符长度0-64 

        :param vul_label_en: The vul_label_en of this WebCmsVulDetailInfo.
        :type vul_label_en: str
        """
        self._vul_label_en = vul_label_en

    @property
    def repair_necessity(self):
        r"""Gets the repair_necessity of this WebCmsVulDetailInfo.

        **参数解释**: 修复必要性 **取值范围**: - 1：高 - 2：中 - 3：低 

        :return: The repair_necessity of this WebCmsVulDetailInfo.
        :rtype: int
        """
        return self._repair_necessity

    @repair_necessity.setter
    def repair_necessity(self, repair_necessity):
        r"""Sets the repair_necessity of this WebCmsVulDetailInfo.

        **参数解释**: 修复必要性 **取值范围**: - 1：高 - 2：中 - 3：低 

        :param repair_necessity: The repair_necessity of this WebCmsVulDetailInfo.
        :type repair_necessity: int
        """
        self._repair_necessity = repair_necessity

    @property
    def severity_level(self):
        r"""Gets the severity_level of this WebCmsVulDetailInfo.

        **参数解释**: 修复必要性 **取值范围**: - Low：低危 - Medium：中危 - High：高危 - Critical：紧急 

        :return: The severity_level of this WebCmsVulDetailInfo.
        :rtype: str
        """
        return self._severity_level

    @severity_level.setter
    def severity_level(self, severity_level):
        r"""Sets the severity_level of this WebCmsVulDetailInfo.

        **参数解释**: 修复必要性 **取值范围**: - Low：低危 - Medium：中危 - High：高危 - Critical：紧急 

        :param severity_level: The severity_level of this WebCmsVulDetailInfo.
        :type severity_level: str
        """
        self._severity_level = severity_level

    @property
    def description_zh(self):
        r"""Gets the description_zh of this WebCmsVulDetailInfo.

        **参数解释**: cve漏洞中文描述 **取值范围**: 字符长度0-1024 

        :return: The description_zh of this WebCmsVulDetailInfo.
        :rtype: str
        """
        return self._description_zh

    @description_zh.setter
    def description_zh(self, description_zh):
        r"""Sets the description_zh of this WebCmsVulDetailInfo.

        **参数解释**: cve漏洞中文描述 **取值范围**: 字符长度0-1024 

        :param description_zh: The description_zh of this WebCmsVulDetailInfo.
        :type description_zh: str
        """
        self._description_zh = description_zh

    @property
    def description_en(self):
        r"""Gets the description_en of this WebCmsVulDetailInfo.

        **参数解释**: cve漏洞英文描述 **取值范围**: 字符长度0-1024 

        :return: The description_en of this WebCmsVulDetailInfo.
        :rtype: str
        """
        return self._description_en

    @description_en.setter
    def description_en(self, description_en):
        r"""Sets the description_en of this WebCmsVulDetailInfo.

        **参数解释**: cve漏洞英文描述 **取值范围**: 字符长度0-1024 

        :param description_en: The description_en of this WebCmsVulDetailInfo.
        :type description_en: str
        """
        self._description_en = description_en

    @property
    def solution_zh(self):
        r"""Gets the solution_zh of this WebCmsVulDetailInfo.

        **参数解释**: cve漏洞中文修复建议 **取值范围**: 字符长度0-1024 

        :return: The solution_zh of this WebCmsVulDetailInfo.
        :rtype: str
        """
        return self._solution_zh

    @solution_zh.setter
    def solution_zh(self, solution_zh):
        r"""Sets the solution_zh of this WebCmsVulDetailInfo.

        **参数解释**: cve漏洞中文修复建议 **取值范围**: 字符长度0-1024 

        :param solution_zh: The solution_zh of this WebCmsVulDetailInfo.
        :type solution_zh: str
        """
        self._solution_zh = solution_zh

    @property
    def solution_en(self):
        r"""Gets the solution_en of this WebCmsVulDetailInfo.

        **参数解释**: cve漏洞英文修复建议 **取值范围**: 字符长度0-1024 

        :return: The solution_en of this WebCmsVulDetailInfo.
        :rtype: str
        """
        return self._solution_en

    @solution_en.setter
    def solution_en(self, solution_en):
        r"""Sets the solution_en of this WebCmsVulDetailInfo.

        **参数解释**: cve漏洞英文修复建议 **取值范围**: 字符长度0-1024 

        :param solution_en: The solution_en of this WebCmsVulDetailInfo.
        :type solution_en: str
        """
        self._solution_en = solution_en

    @property
    def cve_id(self):
        r"""Gets the cve_id of this WebCmsVulDetailInfo.

        **参数解释**: 漏洞编号 **取值范围**: 字符长度0-255 

        :return: The cve_id of this WebCmsVulDetailInfo.
        :rtype: str
        """
        return self._cve_id

    @cve_id.setter
    def cve_id(self, cve_id):
        r"""Sets the cve_id of this WebCmsVulDetailInfo.

        **参数解释**: 漏洞编号 **取值范围**: 字符长度0-255 

        :param cve_id: The cve_id of this WebCmsVulDetailInfo.
        :type cve_id: str
        """
        self._cve_id = cve_id

    @property
    def cve_score(self):
        r"""Gets the cve_score of this WebCmsVulDetailInfo.

        **参数解释**: cve分数 **取值范围**: 最小值0，最大值10 

        :return: The cve_score of this WebCmsVulDetailInfo.
        :rtype: float
        """
        return self._cve_score

    @cve_score.setter
    def cve_score(self, cve_score):
        r"""Sets the cve_score of this WebCmsVulDetailInfo.

        **参数解释**: cve分数 **取值范围**: 最小值0，最大值10 

        :param cve_score: The cve_score of this WebCmsVulDetailInfo.
        :type cve_score: float
        """
        self._cve_score = cve_score

    @property
    def cnvd_id(self):
        r"""Gets the cnvd_id of this WebCmsVulDetailInfo.

        **参数解释**: cnvd编号 **取值范围**: 字符长度0-32 

        :return: The cnvd_id of this WebCmsVulDetailInfo.
        :rtype: str
        """
        return self._cnvd_id

    @cnvd_id.setter
    def cnvd_id(self, cnvd_id):
        r"""Sets the cnvd_id of this WebCmsVulDetailInfo.

        **参数解释**: cnvd编号 **取值范围**: 字符长度0-32 

        :param cnvd_id: The cnvd_id of this WebCmsVulDetailInfo.
        :type cnvd_id: str
        """
        self._cnvd_id = cnvd_id

    @property
    def cnnvd_id(self):
        r"""Gets the cnnvd_id of this WebCmsVulDetailInfo.

        **参数解释**: cnnvd编号 **取值范围**: 字符长度0-32 

        :return: The cnnvd_id of this WebCmsVulDetailInfo.
        :rtype: str
        """
        return self._cnnvd_id

    @cnnvd_id.setter
    def cnnvd_id(self, cnnvd_id):
        r"""Sets the cnnvd_id of this WebCmsVulDetailInfo.

        **参数解释**: cnnvd编号 **取值范围**: 字符长度0-32 

        :param cnnvd_id: The cnnvd_id of this WebCmsVulDetailInfo.
        :type cnnvd_id: str
        """
        self._cnnvd_id = cnnvd_id

    @property
    def bugtraq_id(self):
        r"""Gets the bugtraq_id of this WebCmsVulDetailInfo.

        **参数解释**: bugtraq编号 **取值范围**: 字符长度0-32 

        :return: The bugtraq_id of this WebCmsVulDetailInfo.
        :rtype: str
        """
        return self._bugtraq_id

    @bugtraq_id.setter
    def bugtraq_id(self, bugtraq_id):
        r"""Sets the bugtraq_id of this WebCmsVulDetailInfo.

        **参数解释**: bugtraq编号 **取值范围**: 字符长度0-32 

        :param bugtraq_id: The bugtraq_id of this WebCmsVulDetailInfo.
        :type bugtraq_id: str
        """
        self._bugtraq_id = bugtraq_id

    @property
    def suffix_path(self):
        r"""Gets the suffix_path of this WebCmsVulDetailInfo.

        **参数解释**: 后缀路径 **取值范围**: 字符长度0-128 

        :return: The suffix_path of this WebCmsVulDetailInfo.
        :rtype: str
        """
        return self._suffix_path

    @suffix_path.setter
    def suffix_path(self, suffix_path):
        r"""Sets the suffix_path of this WebCmsVulDetailInfo.

        **参数解释**: 后缀路径 **取值范围**: 字符长度0-128 

        :param suffix_path: The suffix_path of this WebCmsVulDetailInfo.
        :type suffix_path: str
        """
        self._suffix_path = suffix_path

    @property
    def md5(self):
        r"""Gets the md5 of this WebCmsVulDetailInfo.

        **参数解释**: md5 **取值范围**: 字符长度0-32 

        :return: The md5 of this WebCmsVulDetailInfo.
        :rtype: str
        """
        return self._md5

    @md5.setter
    def md5(self, md5):
        r"""Sets the md5 of this WebCmsVulDetailInfo.

        **参数解释**: md5 **取值范围**: 字符长度0-32 

        :param md5: The md5 of this WebCmsVulDetailInfo.
        :type md5: str
        """
        self._md5 = md5

    @property
    def create_time(self):
        r"""Gets the create_time of this WebCmsVulDetailInfo.

        **参数解释**: 创建时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The create_time of this WebCmsVulDetailInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this WebCmsVulDetailInfo.

        **参数解释**: 创建时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :param create_time: The create_time of this WebCmsVulDetailInfo.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this WebCmsVulDetailInfo.

        **参数解释**: 更新时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :return: The update_time of this WebCmsVulDetailInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this WebCmsVulDetailInfo.

        **参数解释**: 更新时间 **取值范围**: 最小值0，最大值9223372036854775807 

        :param update_time: The update_time of this WebCmsVulDetailInfo.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def tags_zh(self):
        r"""Gets the tags_zh of this WebCmsVulDetailInfo.

        **参数解释**: 漏洞标签中文名称 **取值范围**: 字符长度0-64 

        :return: The tags_zh of this WebCmsVulDetailInfo.
        :rtype: str
        """
        return self._tags_zh

    @tags_zh.setter
    def tags_zh(self, tags_zh):
        r"""Sets the tags_zh of this WebCmsVulDetailInfo.

        **参数解释**: 漏洞标签中文名称 **取值范围**: 字符长度0-64 

        :param tags_zh: The tags_zh of this WebCmsVulDetailInfo.
        :type tags_zh: str
        """
        self._tags_zh = tags_zh

    @property
    def tags_en(self):
        r"""Gets the tags_en of this WebCmsVulDetailInfo.

        **参数解释**: 漏洞标签英文名称 **取值范围**: 字符长度0-64 

        :return: The tags_en of this WebCmsVulDetailInfo.
        :rtype: str
        """
        return self._tags_en

    @tags_en.setter
    def tags_en(self, tags_en):
        r"""Sets the tags_en of this WebCmsVulDetailInfo.

        **参数解释**: 漏洞标签英文名称 **取值范围**: 字符长度0-64 

        :param tags_en: The tags_en of this WebCmsVulDetailInfo.
        :type tags_en: str
        """
        self._tags_en = tags_en

    @property
    def patch_url(self):
        r"""Gets the patch_url of this WebCmsVulDetailInfo.

        **参数解释**: 补丁地址 **取值范围**: 字符长度0-512 

        :return: The patch_url of this WebCmsVulDetailInfo.
        :rtype: str
        """
        return self._patch_url

    @patch_url.setter
    def patch_url(self, patch_url):
        r"""Sets the patch_url of this WebCmsVulDetailInfo.

        **参数解释**: 补丁地址 **取值范围**: 字符长度0-512 

        :param patch_url: The patch_url of this WebCmsVulDetailInfo.
        :type patch_url: str
        """
        self._patch_url = patch_url

    @property
    def hosts_num(self):
        r"""Gets the hosts_num of this WebCmsVulDetailInfo.

        :return: The hosts_num of this WebCmsVulDetailInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.VulnerabilityHostNumberInfo`
        """
        return self._hosts_num

    @hosts_num.setter
    def hosts_num(self, hosts_num):
        r"""Sets the hosts_num of this WebCmsVulDetailInfo.

        :param hosts_num: The hosts_num of this WebCmsVulDetailInfo.
        :type hosts_num: :class:`huaweicloudsdkhss.v5.VulnerabilityHostNumberInfo`
        """
        self._hosts_num = hosts_num

    @property
    def cve_level(self):
        r"""Gets the cve_level of this WebCmsVulDetailInfo.

        **参数解释**: cve危险程度 **取值范围**: - Low：低危 - Medium：中危 - High：高危 

        :return: The cve_level of this WebCmsVulDetailInfo.
        :rtype: str
        """
        return self._cve_level

    @cve_level.setter
    def cve_level(self, cve_level):
        r"""Sets the cve_level of this WebCmsVulDetailInfo.

        **参数解释**: cve危险程度 **取值范围**: - Low：低危 - Medium：中危 - High：高危 

        :param cve_level: The cve_level of this WebCmsVulDetailInfo.
        :type cve_level: str
        """
        self._cve_level = cve_level

    @property
    def cvss(self):
        r"""Gets the cvss of this WebCmsVulDetailInfo.

        **参数解释**: 漏洞分值 **取值范围**: 最小值0，最大值10 

        :return: The cvss of this WebCmsVulDetailInfo.
        :rtype: float
        """
        return self._cvss

    @cvss.setter
    def cvss(self, cvss):
        r"""Sets the cvss of this WebCmsVulDetailInfo.

        **参数解释**: 漏洞分值 **取值范围**: 最小值0，最大值10 

        :param cvss: The cvss of this WebCmsVulDetailInfo.
        :type cvss: float
        """
        self._cvss = cvss

    @property
    def cvss_version(self):
        r"""Gets the cvss_version of this WebCmsVulDetailInfo.

        **参数解释**: cvss评分版本 **取值范围**: 字符长度0-32 

        :return: The cvss_version of this WebCmsVulDetailInfo.
        :rtype: str
        """
        return self._cvss_version

    @cvss_version.setter
    def cvss_version(self, cvss_version):
        r"""Sets the cvss_version of this WebCmsVulDetailInfo.

        **参数解释**: cvss评分版本 **取值范围**: 字符长度0-32 

        :param cvss_version: The cvss_version of this WebCmsVulDetailInfo.
        :type cvss_version: str
        """
        self._cvss_version = cvss_version

    @property
    def description(self):
        r"""Gets the description of this WebCmsVulDetailInfo.

        **参数解释**: 漏洞描述 **取值范围**: 字符长度0-1024 

        :return: The description of this WebCmsVulDetailInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this WebCmsVulDetailInfo.

        **参数解释**: 漏洞描述 **取值范围**: 字符长度0-1024 

        :param description: The description of this WebCmsVulDetailInfo.
        :type description: str
        """
        self._description = description

    @property
    def cve_name(self):
        r"""Gets the cve_name of this WebCmsVulDetailInfo.

        **参数解释**: cve漏洞名称 **取值范围**: 字符长度0-512 

        :return: The cve_name of this WebCmsVulDetailInfo.
        :rtype: str
        """
        return self._cve_name

    @cve_name.setter
    def cve_name(self, cve_name):
        r"""Sets the cve_name of this WebCmsVulDetailInfo.

        **参数解释**: cve漏洞名称 **取值范围**: 字符长度0-512 

        :param cve_name: The cve_name of this WebCmsVulDetailInfo.
        :type cve_name: str
        """
        self._cve_name = cve_name

    @property
    def cvss_vector(self):
        r"""Gets the cvss_vector of this WebCmsVulDetailInfo.

        **参数解释**: 攻击矢量 **取值范围**: 字符长度0-255 

        :return: The cvss_vector of this WebCmsVulDetailInfo.
        :rtype: str
        """
        return self._cvss_vector

    @cvss_vector.setter
    def cvss_vector(self, cvss_vector):
        r"""Sets the cvss_vector of this WebCmsVulDetailInfo.

        **参数解释**: 攻击矢量 **取值范围**: 字符长度0-255 

        :param cvss_vector: The cvss_vector of this WebCmsVulDetailInfo.
        :type cvss_vector: str
        """
        self._cvss_vector = cvss_vector

    @property
    def cve_solution(self):
        r"""Gets the cve_solution of this WebCmsVulDetailInfo.

        **参数解释**: cve修复建议 **取值范围**: 字符长度0-4096 

        :return: The cve_solution of this WebCmsVulDetailInfo.
        :rtype: str
        """
        return self._cve_solution

    @cve_solution.setter
    def cve_solution(self, cve_solution):
        r"""Sets the cve_solution of this WebCmsVulDetailInfo.

        **参数解释**: cve修复建议 **取值范围**: 字符长度0-4096 

        :param cve_solution: The cve_solution of this WebCmsVulDetailInfo.
        :type cve_solution: str
        """
        self._cve_solution = cve_solution

    @property
    def cve_affect(self):
        r"""Gets the cve_affect of this WebCmsVulDetailInfo.

        **参数解释**: cve漏洞危害 **取值范围**: 字符长度0-128 

        :return: The cve_affect of this WebCmsVulDetailInfo.
        :rtype: str
        """
        return self._cve_affect

    @cve_affect.setter
    def cve_affect(self, cve_affect):
        r"""Sets the cve_affect of this WebCmsVulDetailInfo.

        **参数解释**: cve漏洞危害 **取值范围**: 字符长度0-128 

        :param cve_affect: The cve_affect of this WebCmsVulDetailInfo.
        :type cve_affect: str
        """
        self._cve_affect = cve_affect

    @property
    def cve_affect_description(self):
        r"""Gets the cve_affect_description of this WebCmsVulDetailInfo.

        **参数解释**: cve漏洞危害的描述信息 **取值范围**: 字符长度0-4096 

        :return: The cve_affect_description of this WebCmsVulDetailInfo.
        :rtype: str
        """
        return self._cve_affect_description

    @cve_affect_description.setter
    def cve_affect_description(self, cve_affect_description):
        r"""Sets the cve_affect_description of this WebCmsVulDetailInfo.

        **参数解释**: cve漏洞危害的描述信息 **取值范围**: 字符长度0-4096 

        :param cve_affect_description: The cve_affect_description of this WebCmsVulDetailInfo.
        :type cve_affect_description: str
        """
        self._cve_affect_description = cve_affect_description

    @property
    def cve_type(self):
        r"""Gets the cve_type of this WebCmsVulDetailInfo.

        **参数解释**: cve漏洞类型 **取值范围**: 字符长度0-128 

        :return: The cve_type of this WebCmsVulDetailInfo.
        :rtype: str
        """
        return self._cve_type

    @cve_type.setter
    def cve_type(self, cve_type):
        r"""Sets the cve_type of this WebCmsVulDetailInfo.

        **参数解释**: cve漏洞类型 **取值范围**: 字符长度0-128 

        :param cve_type: The cve_type of this WebCmsVulDetailInfo.
        :type cve_type: str
        """
        self._cve_type = cve_type

    @property
    def cve_type_description(self):
        r"""Gets the cve_type_description of this WebCmsVulDetailInfo.

        **参数解释**: cve漏洞类型的描述信息 **取值范围**: 字符长度0-4096 

        :return: The cve_type_description of this WebCmsVulDetailInfo.
        :rtype: str
        """
        return self._cve_type_description

    @cve_type_description.setter
    def cve_type_description(self, cve_type_description):
        r"""Sets the cve_type_description of this WebCmsVulDetailInfo.

        **参数解释**: cve漏洞类型的描述信息 **取值范围**: 字符长度0-4096 

        :param cve_type_description: The cve_type_description of this WebCmsVulDetailInfo.
        :type cve_type_description: str
        """
        self._cve_type_description = cve_type_description

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
        if not isinstance(other, WebCmsVulDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
