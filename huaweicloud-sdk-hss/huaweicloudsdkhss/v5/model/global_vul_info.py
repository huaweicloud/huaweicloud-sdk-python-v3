# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GlobalVulInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vul_name': 'str',
        'vul_id': 'str',
        'repair_necessity': 'str',
        'decription': 'str',
        'solution': 'str',
        'url': 'str',
        'history_number': 'int',
        'undeal_number': 'int',
        'data_list': 'list[CveInfo]'
    }

    attribute_map = {
        'vul_name': 'vul_name',
        'vul_id': 'vul_id',
        'repair_necessity': 'repair_necessity',
        'decription': 'decription',
        'solution': 'solution',
        'url': 'url',
        'history_number': 'history_number',
        'undeal_number': 'undeal_number',
        'data_list': 'data_list'
    }

    def __init__(self, vul_name=None, vul_id=None, repair_necessity=None, decription=None, solution=None, url=None, history_number=None, undeal_number=None, data_list=None):
        r"""GlobalVulInfo

        The model defined in huaweicloud sdk

        :param vul_name: 漏洞名称
        :type vul_name: str
        :param vul_id: **参数解释** 漏洞ID **取值范围** 字符长度0-65535位 
        :type vul_id: str
        :param repair_necessity: **参数解释**: 修复紧急度 **取值范围**: - immediate_repair：需尽快修复。 - delay_repair：可延后修复。 - not_needed_repair：暂可不修复。 
        :type repair_necessity: str
        :param decription: **参数解释** 漏洞描述 **取值范围** 字符长度0-65535位 
        :type decription: str
        :param solution: **参数解释** 解决方案 **取值范围** 字符长度0-65535位 
        :type solution: str
        :param url: **参数解释** URL链接 **取值范围** 字符长度0-65535位 
        :type url: str
        :param history_number: **参数解释** 历史受影响镜像的个数 **取值范围** 取值0-65535 
        :type history_number: int
        :param undeal_number: **参数解释** 未处理镜像的格式 **取值范围** 取值0-65535 
        :type undeal_number: int
        :param data_list: cve列表
        :type data_list: list[:class:`huaweicloudsdkhss.v5.CveInfo`]
        """
        
        

        self._vul_name = None
        self._vul_id = None
        self._repair_necessity = None
        self._decription = None
        self._solution = None
        self._url = None
        self._history_number = None
        self._undeal_number = None
        self._data_list = None
        self.discriminator = None

        if vul_name is not None:
            self.vul_name = vul_name
        if vul_id is not None:
            self.vul_id = vul_id
        if repair_necessity is not None:
            self.repair_necessity = repair_necessity
        if decription is not None:
            self.decription = decription
        if solution is not None:
            self.solution = solution
        if url is not None:
            self.url = url
        if history_number is not None:
            self.history_number = history_number
        if undeal_number is not None:
            self.undeal_number = undeal_number
        if data_list is not None:
            self.data_list = data_list

    @property
    def vul_name(self):
        r"""Gets the vul_name of this GlobalVulInfo.

        漏洞名称

        :return: The vul_name of this GlobalVulInfo.
        :rtype: str
        """
        return self._vul_name

    @vul_name.setter
    def vul_name(self, vul_name):
        r"""Sets the vul_name of this GlobalVulInfo.

        漏洞名称

        :param vul_name: The vul_name of this GlobalVulInfo.
        :type vul_name: str
        """
        self._vul_name = vul_name

    @property
    def vul_id(self):
        r"""Gets the vul_id of this GlobalVulInfo.

        **参数解释** 漏洞ID **取值范围** 字符长度0-65535位 

        :return: The vul_id of this GlobalVulInfo.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        r"""Sets the vul_id of this GlobalVulInfo.

        **参数解释** 漏洞ID **取值范围** 字符长度0-65535位 

        :param vul_id: The vul_id of this GlobalVulInfo.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def repair_necessity(self):
        r"""Gets the repair_necessity of this GlobalVulInfo.

        **参数解释**: 修复紧急度 **取值范围**: - immediate_repair：需尽快修复。 - delay_repair：可延后修复。 - not_needed_repair：暂可不修复。 

        :return: The repair_necessity of this GlobalVulInfo.
        :rtype: str
        """
        return self._repair_necessity

    @repair_necessity.setter
    def repair_necessity(self, repair_necessity):
        r"""Sets the repair_necessity of this GlobalVulInfo.

        **参数解释**: 修复紧急度 **取值范围**: - immediate_repair：需尽快修复。 - delay_repair：可延后修复。 - not_needed_repair：暂可不修复。 

        :param repair_necessity: The repair_necessity of this GlobalVulInfo.
        :type repair_necessity: str
        """
        self._repair_necessity = repair_necessity

    @property
    def decription(self):
        r"""Gets the decription of this GlobalVulInfo.

        **参数解释** 漏洞描述 **取值范围** 字符长度0-65535位 

        :return: The decription of this GlobalVulInfo.
        :rtype: str
        """
        return self._decription

    @decription.setter
    def decription(self, decription):
        r"""Sets the decription of this GlobalVulInfo.

        **参数解释** 漏洞描述 **取值范围** 字符长度0-65535位 

        :param decription: The decription of this GlobalVulInfo.
        :type decription: str
        """
        self._decription = decription

    @property
    def solution(self):
        r"""Gets the solution of this GlobalVulInfo.

        **参数解释** 解决方案 **取值范围** 字符长度0-65535位 

        :return: The solution of this GlobalVulInfo.
        :rtype: str
        """
        return self._solution

    @solution.setter
    def solution(self, solution):
        r"""Sets the solution of this GlobalVulInfo.

        **参数解释** 解决方案 **取值范围** 字符长度0-65535位 

        :param solution: The solution of this GlobalVulInfo.
        :type solution: str
        """
        self._solution = solution

    @property
    def url(self):
        r"""Gets the url of this GlobalVulInfo.

        **参数解释** URL链接 **取值范围** 字符长度0-65535位 

        :return: The url of this GlobalVulInfo.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this GlobalVulInfo.

        **参数解释** URL链接 **取值范围** 字符长度0-65535位 

        :param url: The url of this GlobalVulInfo.
        :type url: str
        """
        self._url = url

    @property
    def history_number(self):
        r"""Gets the history_number of this GlobalVulInfo.

        **参数解释** 历史受影响镜像的个数 **取值范围** 取值0-65535 

        :return: The history_number of this GlobalVulInfo.
        :rtype: int
        """
        return self._history_number

    @history_number.setter
    def history_number(self, history_number):
        r"""Sets the history_number of this GlobalVulInfo.

        **参数解释** 历史受影响镜像的个数 **取值范围** 取值0-65535 

        :param history_number: The history_number of this GlobalVulInfo.
        :type history_number: int
        """
        self._history_number = history_number

    @property
    def undeal_number(self):
        r"""Gets the undeal_number of this GlobalVulInfo.

        **参数解释** 未处理镜像的格式 **取值范围** 取值0-65535 

        :return: The undeal_number of this GlobalVulInfo.
        :rtype: int
        """
        return self._undeal_number

    @undeal_number.setter
    def undeal_number(self, undeal_number):
        r"""Sets the undeal_number of this GlobalVulInfo.

        **参数解释** 未处理镜像的格式 **取值范围** 取值0-65535 

        :param undeal_number: The undeal_number of this GlobalVulInfo.
        :type undeal_number: int
        """
        self._undeal_number = undeal_number

    @property
    def data_list(self):
        r"""Gets the data_list of this GlobalVulInfo.

        cve列表

        :return: The data_list of this GlobalVulInfo.
        :rtype: list[:class:`huaweicloudsdkhss.v5.CveInfo`]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        r"""Sets the data_list of this GlobalVulInfo.

        cve列表

        :param data_list: The data_list of this GlobalVulInfo.
        :type data_list: list[:class:`huaweicloudsdkhss.v5.CveInfo`]
        """
        self._data_list = data_list

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
        if not isinstance(other, GlobalVulInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
