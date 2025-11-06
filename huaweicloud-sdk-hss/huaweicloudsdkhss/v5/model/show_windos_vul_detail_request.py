# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWindosVulDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'vul_id': 'str',
        'cve_id': 'str',
        'handle_status': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'limit': 'limit',
        'offset': 'offset',
        'vul_id': 'vul_id',
        'cve_id': 'cve_id',
        'handle_status': 'handle_status'
    }

    def __init__(self, enterprise_project_id=None, limit=None, offset=None, vul_id=None, cve_id=None, handle_status=None):
        r"""ShowWindosVulDetailRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param vul_id: **参数解释**: 漏洞ID **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type vul_id: str
        :param cve_id: **参数解释**: 漏洞cve编号 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type cve_id: str
        :param handle_status: **参数解释**: 漏洞处置状态 **约束限制**: 不涉及 **取值范围**: - handled : 已处理 - unhandled : 未处理  **默认取值**: 不涉及 
        :type handle_status: str
        """
        
        

        self._enterprise_project_id = None
        self._limit = None
        self._offset = None
        self._vul_id = None
        self._cve_id = None
        self._handle_status = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        self.vul_id = vul_id
        if cve_id is not None:
            self.cve_id = cve_id
        if handle_status is not None:
            self.handle_status = handle_status

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ShowWindosVulDetailRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ShowWindosVulDetailRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ShowWindosVulDetailRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ShowWindosVulDetailRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def limit(self):
        r"""Gets the limit of this ShowWindosVulDetailRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ShowWindosVulDetailRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowWindosVulDetailRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ShowWindosVulDetailRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowWindosVulDetailRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ShowWindosVulDetailRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowWindosVulDetailRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ShowWindosVulDetailRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def vul_id(self):
        r"""Gets the vul_id of this ShowWindosVulDetailRequest.

        **参数解释**: 漏洞ID **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The vul_id of this ShowWindosVulDetailRequest.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        r"""Sets the vul_id of this ShowWindosVulDetailRequest.

        **参数解释**: 漏洞ID **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param vul_id: The vul_id of this ShowWindosVulDetailRequest.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def cve_id(self):
        r"""Gets the cve_id of this ShowWindosVulDetailRequest.

        **参数解释**: 漏洞cve编号 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The cve_id of this ShowWindosVulDetailRequest.
        :rtype: str
        """
        return self._cve_id

    @cve_id.setter
    def cve_id(self, cve_id):
        r"""Sets the cve_id of this ShowWindosVulDetailRequest.

        **参数解释**: 漏洞cve编号 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param cve_id: The cve_id of this ShowWindosVulDetailRequest.
        :type cve_id: str
        """
        self._cve_id = cve_id

    @property
    def handle_status(self):
        r"""Gets the handle_status of this ShowWindosVulDetailRequest.

        **参数解释**: 漏洞处置状态 **约束限制**: 不涉及 **取值范围**: - handled : 已处理 - unhandled : 未处理  **默认取值**: 不涉及 

        :return: The handle_status of this ShowWindosVulDetailRequest.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        r"""Sets the handle_status of this ShowWindosVulDetailRequest.

        **参数解释**: 漏洞处置状态 **约束限制**: 不涉及 **取值范围**: - handled : 已处理 - unhandled : 未处理  **默认取值**: 不涉及 

        :param handle_status: The handle_status of this ShowWindosVulDetailRequest.
        :type handle_status: str
        """
        self._handle_status = handle_status

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
        if not isinstance(other, ShowWindosVulDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
