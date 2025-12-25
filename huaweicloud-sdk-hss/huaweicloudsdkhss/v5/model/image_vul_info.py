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
        'repair_necessity': 'str',
        'description': 'str',
        'position': 'str',
        'app_name': 'str',
        'app_path': 'str',
        'version': 'str',
        'solution': 'str',
        'url': 'str'
    }

    attribute_map = {
        'vul_id': 'vul_id',
        'repair_necessity': 'repair_necessity',
        'description': 'description',
        'position': 'position',
        'app_name': 'app_name',
        'app_path': 'app_path',
        'version': 'version',
        'solution': 'solution',
        'url': 'url'
    }

    def __init__(self, vul_id=None, repair_necessity=None, description=None, position=None, app_name=None, app_path=None, version=None, solution=None, url=None):
        r"""ImageVulInfo

        The model defined in huaweicloud sdk

        :param vul_id: **参数解释**: 漏洞ID **取值范围**: 字符长度0-128 
        :type vul_id: str
        :param repair_necessity: **参数解释**: 危险程度 **取值范围**: - immediate_repair：高危 - delay_repair：中危 - not_needed_repair：低危 
        :type repair_necessity: str
        :param description: **参数解释**: 漏洞描述 **取值范围** : 字符长度0-128 
        :type description: str
        :param position: **参数解释**: 漏洞所在镜像层 **取值范围** : 字符长度0-128 
        :type position: str
        :param app_name: **参数解释**: 漏洞的软件名称 **取值范围** : 字符长度0-128 
        :type app_name: str
        :param app_path: **参数解释**: 应用软件的路径（只有应用漏洞有该字段） **取值范围** : 字符长度1-512 
        :type app_path: str
        :param version: **参数解释**: 软件版本 **取值范围** : 字符长度0-128 
        :type version: str
        :param solution: **参数解释**: 解决方案 **取值范围** : 字符长度0-256 
        :type solution: str
        :param url: **参数解释**: 补丁地址 **取值范围** : 字符长度0-128 
        :type url: str
        """
        
        

        self._vul_id = None
        self._repair_necessity = None
        self._description = None
        self._position = None
        self._app_name = None
        self._app_path = None
        self._version = None
        self._solution = None
        self._url = None
        self.discriminator = None

        if vul_id is not None:
            self.vul_id = vul_id
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

    @property
    def vul_id(self):
        r"""Gets the vul_id of this ImageVulInfo.

        **参数解释**: 漏洞ID **取值范围**: 字符长度0-128 

        :return: The vul_id of this ImageVulInfo.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        r"""Sets the vul_id of this ImageVulInfo.

        **参数解释**: 漏洞ID **取值范围**: 字符长度0-128 

        :param vul_id: The vul_id of this ImageVulInfo.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def repair_necessity(self):
        r"""Gets the repair_necessity of this ImageVulInfo.

        **参数解释**: 危险程度 **取值范围**: - immediate_repair：高危 - delay_repair：中危 - not_needed_repair：低危 

        :return: The repair_necessity of this ImageVulInfo.
        :rtype: str
        """
        return self._repair_necessity

    @repair_necessity.setter
    def repair_necessity(self, repair_necessity):
        r"""Sets the repair_necessity of this ImageVulInfo.

        **参数解释**: 危险程度 **取值范围**: - immediate_repair：高危 - delay_repair：中危 - not_needed_repair：低危 

        :param repair_necessity: The repair_necessity of this ImageVulInfo.
        :type repair_necessity: str
        """
        self._repair_necessity = repair_necessity

    @property
    def description(self):
        r"""Gets the description of this ImageVulInfo.

        **参数解释**: 漏洞描述 **取值范围** : 字符长度0-128 

        :return: The description of this ImageVulInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ImageVulInfo.

        **参数解释**: 漏洞描述 **取值范围** : 字符长度0-128 

        :param description: The description of this ImageVulInfo.
        :type description: str
        """
        self._description = description

    @property
    def position(self):
        r"""Gets the position of this ImageVulInfo.

        **参数解释**: 漏洞所在镜像层 **取值范围** : 字符长度0-128 

        :return: The position of this ImageVulInfo.
        :rtype: str
        """
        return self._position

    @position.setter
    def position(self, position):
        r"""Sets the position of this ImageVulInfo.

        **参数解释**: 漏洞所在镜像层 **取值范围** : 字符长度0-128 

        :param position: The position of this ImageVulInfo.
        :type position: str
        """
        self._position = position

    @property
    def app_name(self):
        r"""Gets the app_name of this ImageVulInfo.

        **参数解释**: 漏洞的软件名称 **取值范围** : 字符长度0-128 

        :return: The app_name of this ImageVulInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ImageVulInfo.

        **参数解释**: 漏洞的软件名称 **取值范围** : 字符长度0-128 

        :param app_name: The app_name of this ImageVulInfo.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def app_path(self):
        r"""Gets the app_path of this ImageVulInfo.

        **参数解释**: 应用软件的路径（只有应用漏洞有该字段） **取值范围** : 字符长度1-512 

        :return: The app_path of this ImageVulInfo.
        :rtype: str
        """
        return self._app_path

    @app_path.setter
    def app_path(self, app_path):
        r"""Sets the app_path of this ImageVulInfo.

        **参数解释**: 应用软件的路径（只有应用漏洞有该字段） **取值范围** : 字符长度1-512 

        :param app_path: The app_path of this ImageVulInfo.
        :type app_path: str
        """
        self._app_path = app_path

    @property
    def version(self):
        r"""Gets the version of this ImageVulInfo.

        **参数解释**: 软件版本 **取值范围** : 字符长度0-128 

        :return: The version of this ImageVulInfo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this ImageVulInfo.

        **参数解释**: 软件版本 **取值范围** : 字符长度0-128 

        :param version: The version of this ImageVulInfo.
        :type version: str
        """
        self._version = version

    @property
    def solution(self):
        r"""Gets the solution of this ImageVulInfo.

        **参数解释**: 解决方案 **取值范围** : 字符长度0-256 

        :return: The solution of this ImageVulInfo.
        :rtype: str
        """
        return self._solution

    @solution.setter
    def solution(self, solution):
        r"""Sets the solution of this ImageVulInfo.

        **参数解释**: 解决方案 **取值范围** : 字符长度0-256 

        :param solution: The solution of this ImageVulInfo.
        :type solution: str
        """
        self._solution = solution

    @property
    def url(self):
        r"""Gets the url of this ImageVulInfo.

        **参数解释**: 补丁地址 **取值范围** : 字符长度0-128 

        :return: The url of this ImageVulInfo.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ImageVulInfo.

        **参数解释**: 补丁地址 **取值范围** : 字符长度0-128 

        :param url: The url of this ImageVulInfo.
        :type url: str
        """
        self._url = url

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
