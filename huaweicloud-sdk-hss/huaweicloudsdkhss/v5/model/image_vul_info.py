# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ImageVulInfo:

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
        'vul_name': 'str',
        'repair_necessity': 'str',
        'description': 'str',
        'position': 'str',
        'app_name': 'str',
        'app_path': 'str',
        'version': 'str',
        'solution': 'str',
        'url': 'str',
        'data_list': 'list[CveInfo]',
        'status': 'str',
        'severity_level': 'str'
    }

    attribute_map = {
        'vul_id': 'vul_id',
        'vul_name': 'vul_name',
        'repair_necessity': 'repair_necessity',
        'description': 'description',
        'position': 'position',
        'app_name': 'app_name',
        'app_path': 'app_path',
        'version': 'version',
        'solution': 'solution',
        'url': 'url',
        'data_list': 'data_list',
        'status': 'status',
        'severity_level': 'severity_level'
    }

    def __init__(self, vul_id=None, vul_name=None, repair_necessity=None, description=None, position=None, app_name=None, app_path=None, version=None, solution=None, url=None, data_list=None, status=None, severity_level=None):
        r"""ImageVulInfo

        The model defined in huaweicloud sdk

        :param vul_id: **参数解释**: 漏洞ID **取值范围**: 字符长度1-64位 
        :type vul_id: str
        :param vul_name: **参数解释**: 漏洞名称 **取值范围**: 字符长度0-256位 
        :type vul_name: str
        :param repair_necessity: **参数解释**: 修复紧急度 **取值范围**: - immediate_repair：紧急修复 - delay_repair：延迟修复 - not_needed_repair：无需修复 
        :type repair_necessity: str
        :param description: **参数解释**: 漏洞描述 **取值范围**: 字符长度0-4096位 
        :type description: str
        :param position: **参数解释**: 漏洞位置 **取值范围**: 字符长度0-512位 
        :type position: str
        :param app_name: **参数解释**: 软件名称 **取值范围**: 字符长度0-128位 
        :type app_name: str
        :param app_path: **参数解释**: 软件路径 **取值范围**: 字符长度0-512位 
        :type app_path: str
        :param version: **参数解释**: 软件版本 **取值范围**: 字符长度0-128位 
        :type version: str
        :param solution: **参数解释**: 修复建议 **取值范围**: 字符长度0-4096位 
        :type solution: str
        :param url: **参数解释**: URL **取值范围**: 字符长度0-2048位 
        :type url: str
        :param data_list: **参数解释**: CVE列表 **取值范围**: 取值0-100个CveInfo对象 
        :type data_list: list[:class:`huaweicloudsdkhss.v5.CveInfo`]
        :param status: **参数解释**: 漏洞状态 **取值范围**: 字符长度0-64位 
        :type status: str
        :param severity_level: **参数解释**: 危险程度 **取值范围**: - Low：低危 - Medium：中危 - High：高危 - Critical：危急 
        :type severity_level: str
        """
        
        

        self._vul_id = None
        self._vul_name = None
        self._repair_necessity = None
        self._description = None
        self._position = None
        self._app_name = None
        self._app_path = None
        self._version = None
        self._solution = None
        self._url = None
        self._data_list = None
        self._status = None
        self._severity_level = None
        self.discriminator = None

        if vul_id is not None:
            self.vul_id = vul_id
        if vul_name is not None:
            self.vul_name = vul_name
        if repair_necessity is not None:
            self.repair_necessity = repair_necessity
        if description is not None:
            self.description = description
        if position is not None:
            self.position = position
        if app_name is not None:
            self.app_name = app_name
        if app_path is not None:
            self.app_path = app_path
        if version is not None:
            self.version = version
        if solution is not None:
            self.solution = solution
        if url is not None:
            self.url = url
        if data_list is not None:
            self.data_list = data_list
        if status is not None:
            self.status = status
        if severity_level is not None:
            self.severity_level = severity_level

    @property
    def vul_id(self):
        r"""Gets the vul_id of this ImageVulInfo.

        **参数解释**: 漏洞ID **取值范围**: 字符长度1-64位 

        :return: The vul_id of this ImageVulInfo.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        r"""Sets the vul_id of this ImageVulInfo.

        **参数解释**: 漏洞ID **取值范围**: 字符长度1-64位 

        :param vul_id: The vul_id of this ImageVulInfo.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def vul_name(self):
        r"""Gets the vul_name of this ImageVulInfo.

        **参数解释**: 漏洞名称 **取值范围**: 字符长度0-256位 

        :return: The vul_name of this ImageVulInfo.
        :rtype: str
        """
        return self._vul_name

    @vul_name.setter
    def vul_name(self, vul_name):
        r"""Sets the vul_name of this ImageVulInfo.

        **参数解释**: 漏洞名称 **取值范围**: 字符长度0-256位 

        :param vul_name: The vul_name of this ImageVulInfo.
        :type vul_name: str
        """
        self._vul_name = vul_name

    @property
    def repair_necessity(self):
        r"""Gets the repair_necessity of this ImageVulInfo.

        **参数解释**: 修复紧急度 **取值范围**: - immediate_repair：紧急修复 - delay_repair：延迟修复 - not_needed_repair：无需修复 

        :return: The repair_necessity of this ImageVulInfo.
        :rtype: str
        """
        return self._repair_necessity

    @repair_necessity.setter
    def repair_necessity(self, repair_necessity):
        r"""Sets the repair_necessity of this ImageVulInfo.

        **参数解释**: 修复紧急度 **取值范围**: - immediate_repair：紧急修复 - delay_repair：延迟修复 - not_needed_repair：无需修复 

        :param repair_necessity: The repair_necessity of this ImageVulInfo.
        :type repair_necessity: str
        """
        self._repair_necessity = repair_necessity

    @property
    def description(self):
        r"""Gets the description of this ImageVulInfo.

        **参数解释**: 漏洞描述 **取值范围**: 字符长度0-4096位 

        :return: The description of this ImageVulInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ImageVulInfo.

        **参数解释**: 漏洞描述 **取值范围**: 字符长度0-4096位 

        :param description: The description of this ImageVulInfo.
        :type description: str
        """
        self._description = description

    @property
    def position(self):
        r"""Gets the position of this ImageVulInfo.

        **参数解释**: 漏洞位置 **取值范围**: 字符长度0-512位 

        :return: The position of this ImageVulInfo.
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        r"""Sets the position of this ImageVulInfo.

        **参数解释**: 漏洞位置 **取值范围**: 字符长度0-512位 

        :param position: The position of this ImageVulInfo.
        :type position: str
        """
        self._position = position

    @property
    def app_name(self):
        r"""Gets the app_name of this ImageVulInfo.

        **参数解释**: 软件名称 **取值范围**: 字符长度0-128位 

        :return: The app_name of this ImageVulInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ImageVulInfo.

        **参数解释**: 软件名称 **取值范围**: 字符长度0-128位 

        :param app_name: The app_name of this ImageVulInfo.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def app_path(self):
        r"""Gets the app_path of this ImageVulInfo.

        **参数解释**: 软件路径 **取值范围**: 字符长度0-512位 

        :return: The app_path of this ImageVulInfo.
        :rtype: str
        """
        return self._app_path

    @app_path.setter
    def app_path(self, app_path):
        r"""Sets the app_path of this ImageVulInfo.

        **参数解释**: 软件路径 **取值范围**: 字符长度0-512位 

        :param app_path: The app_path of this ImageVulInfo.
        :type app_path: str
        """
        self._app_path = app_path

    @property
    def version(self):
        r"""Gets the version of this ImageVulInfo.

        **参数解释**: 软件版本 **取值范围**: 字符长度0-128位 

        :return: The version of this ImageVulInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ImageVulInfo.

        **参数解释**: 软件版本 **取值范围**: 字符长度0-128位 

        :param version: The version of this ImageVulInfo.
        :type version: str
        """
        self._version = version

    @property
    def solution(self):
        r"""Gets the solution of this ImageVulInfo.

        **参数解释**: 修复建议 **取值范围**: 字符长度0-4096位 

        :return: The solution of this ImageVulInfo.
        :rtype: str
        """
        return self._solution

    @solution.setter
    def solution(self, solution):
        r"""Sets the solution of this ImageVulInfo.

        **参数解释**: 修复建议 **取值范围**: 字符长度0-4096位 

        :param solution: The solution of this ImageVulInfo.
        :type solution: str
        """
        self._solution = solution

    @property
    def url(self):
        r"""Gets the url of this ImageVulInfo.

        **参数解释**: URL **取值范围**: 字符长度0-2048位 

        :return: The url of this ImageVulInfo.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ImageVulInfo.

        **参数解释**: URL **取值范围**: 字符长度0-2048位 

        :param url: The url of this ImageVulInfo.
        :type url: str
        """
        self._url = url

    @property
    def data_list(self):
        r"""Gets the data_list of this ImageVulInfo.

        **参数解释**: CVE列表 **取值范围**: 取值0-100个CveInfo对象 

        :return: The data_list of this ImageVulInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.CveInfo`]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        r"""Sets the data_list of this ImageVulInfo.

        **参数解释**: CVE列表 **取值范围**: 取值0-100个CveInfo对象 

        :param data_list: The data_list of this ImageVulInfo.
        :type data_list: list[:class:`huaweicloudsdkhss.v5.CveInfo`]
        """
        self._data_list = data_list

    @property
    def status(self):
        r"""Gets the status of this ImageVulInfo.

        **参数解释**: 漏洞状态 **取值范围**: 字符长度0-64位 

        :return: The status of this ImageVulInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ImageVulInfo.

        **参数解释**: 漏洞状态 **取值范围**: 字符长度0-64位 

        :param status: The status of this ImageVulInfo.
        :type status: str
        """
        self._status = status

    @property
    def severity_level(self):
        r"""Gets the severity_level of this ImageVulInfo.

        **参数解释**: 危险程度 **取值范围**: - Low：低危 - Medium：中危 - High：高危 - Critical：危急 

        :return: The severity_level of this ImageVulInfo.
        :rtype: str
        """
        return self._severity_level

    @severity_level.setter
    def severity_level(self, severity_level):
        r"""Sets the severity_level of this ImageVulInfo.

        **参数解释**: 危险程度 **取值范围**: - Low：低危 - Medium：中危 - High：高危 - Critical：危急 

        :param severity_level: The severity_level of this ImageVulInfo.
        :type severity_level: str
        """
        self._severity_level = severity_level

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
        if not isinstance(other, ImageVulInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
