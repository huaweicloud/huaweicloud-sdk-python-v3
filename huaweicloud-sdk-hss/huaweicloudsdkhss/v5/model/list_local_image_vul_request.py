# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLocalImageVulRequest:

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
        'offset': 'int',
        'limit': 'int',
        'repair_necessity': 'str',
        'image_id': 'str',
        'vul_id': 'str',
        'app_name': 'str',
        'type': 'str',
        'handle_status': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'repair_necessity': 'repair_necessity',
        'image_id': 'image_id',
        'vul_id': 'vul_id',
        'app_name': 'app_name',
        'type': 'type',
        'handle_status': 'handle_status'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, repair_necessity=None, image_id=None, vul_id=None, app_name=None, type=None, handle_status=None):
        r"""ListLocalImageVulRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param repair_necessity: **参数解释**: 修复紧急度 **约束限制**: 不涉及 **取值范围**: - immediate_repair：紧急修复 - delay_repair：延迟修复 - not_needed_repair：无需修复  **默认取值**: 不涉及 
        :type repair_necessity: str
        :param image_id: **参数解释**: 镜像ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type image_id: str
        :param vul_id: **参数解释**: 漏洞ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type vul_id: str
        :param app_name: **参数解释**: 软件名 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type app_name: str
        :param type: **参数解释**: 漏洞类型 **约束限制**: 不涉及 **取值范围**: - linux_vul：linux漏洞 - app_vul：应用漏洞  **默认取值**: 不涉及 
        :type type: str
        :param handle_status: **参数解释**: 处置状态 **约束限制**: 不涉及 **取值范围**: 包含如下:   - unhandled：未处理   - handled：已处理  **默认取值**: 不涉及 
        :type handle_status: str
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._repair_necessity = None
        self._image_id = None
        self._vul_id = None
        self._app_name = None
        self._type = None
        self._handle_status = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if repair_necessity is not None:
            self.repair_necessity = repair_necessity
        if image_id is not None:
            self.image_id = image_id
        if vul_id is not None:
            self.vul_id = vul_id
        if app_name is not None:
            self.app_name = app_name
        if type is not None:
            self.type = type
        if handle_status is not None:
            self.handle_status = handle_status

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListLocalImageVulRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListLocalImageVulRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListLocalImageVulRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListLocalImageVulRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListLocalImageVulRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListLocalImageVulRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListLocalImageVulRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListLocalImageVulRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListLocalImageVulRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListLocalImageVulRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListLocalImageVulRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListLocalImageVulRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def repair_necessity(self):
        r"""Gets the repair_necessity of this ListLocalImageVulRequest.

        **参数解释**: 修复紧急度 **约束限制**: 不涉及 **取值范围**: - immediate_repair：紧急修复 - delay_repair：延迟修复 - not_needed_repair：无需修复  **默认取值**: 不涉及 

        :return: The repair_necessity of this ListLocalImageVulRequest.
        :rtype: str
        """
        return self._repair_necessity

    @repair_necessity.setter
    def repair_necessity(self, repair_necessity):
        r"""Sets the repair_necessity of this ListLocalImageVulRequest.

        **参数解释**: 修复紧急度 **约束限制**: 不涉及 **取值范围**: - immediate_repair：紧急修复 - delay_repair：延迟修复 - not_needed_repair：无需修复  **默认取值**: 不涉及 

        :param repair_necessity: The repair_necessity of this ListLocalImageVulRequest.
        :type repair_necessity: str
        """
        self._repair_necessity = repair_necessity

    @property
    def image_id(self):
        r"""Gets the image_id of this ListLocalImageVulRequest.

        **参数解释**: 镜像ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The image_id of this ListLocalImageVulRequest.
        :rtype: str
        """
        return self._image_id

    @image_id.setter
    def image_id(self, image_id):
        r"""Sets the image_id of this ListLocalImageVulRequest.

        **参数解释**: 镜像ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param image_id: The image_id of this ListLocalImageVulRequest.
        :type image_id: str
        """
        self._image_id = image_id

    @property
    def vul_id(self):
        r"""Gets the vul_id of this ListLocalImageVulRequest.

        **参数解释**: 漏洞ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The vul_id of this ListLocalImageVulRequest.
        :rtype: str
        """
        return self._vul_id

    @vul_id.setter
    def vul_id(self, vul_id):
        r"""Sets the vul_id of this ListLocalImageVulRequest.

        **参数解释**: 漏洞ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param vul_id: The vul_id of this ListLocalImageVulRequest.
        :type vul_id: str
        """
        self._vul_id = vul_id

    @property
    def app_name(self):
        r"""Gets the app_name of this ListLocalImageVulRequest.

        **参数解释**: 软件名 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The app_name of this ListLocalImageVulRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ListLocalImageVulRequest.

        **参数解释**: 软件名 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param app_name: The app_name of this ListLocalImageVulRequest.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def type(self):
        r"""Gets the type of this ListLocalImageVulRequest.

        **参数解释**: 漏洞类型 **约束限制**: 不涉及 **取值范围**: - linux_vul：linux漏洞 - app_vul：应用漏洞  **默认取值**: 不涉及 

        :return: The type of this ListLocalImageVulRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListLocalImageVulRequest.

        **参数解释**: 漏洞类型 **约束限制**: 不涉及 **取值范围**: - linux_vul：linux漏洞 - app_vul：应用漏洞  **默认取值**: 不涉及 

        :param type: The type of this ListLocalImageVulRequest.
        :type type: str
        """
        self._type = type

    @property
    def handle_status(self):
        r"""Gets the handle_status of this ListLocalImageVulRequest.

        **参数解释**: 处置状态 **约束限制**: 不涉及 **取值范围**: 包含如下:   - unhandled：未处理   - handled：已处理  **默认取值**: 不涉及 

        :return: The handle_status of this ListLocalImageVulRequest.
        :rtype: str
        """
        return self._handle_status

    @handle_status.setter
    def handle_status(self, handle_status):
        r"""Sets the handle_status of this ListLocalImageVulRequest.

        **参数解释**: 处置状态 **约束限制**: 不涉及 **取值范围**: 包含如下:   - unhandled：未处理   - handled：已处理  **默认取值**: 不涉及 

        :param handle_status: The handle_status of this ListLocalImageVulRequest.
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
        if not isinstance(other, ListLocalImageVulRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
