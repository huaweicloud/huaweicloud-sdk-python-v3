# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWebTamperProtectionDirectoryRequest:

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
        'type': 'str',
        'protection_config_id': 'str',
        'container_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'status': 'str',
        'protect_directory': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'type': 'type',
        'protection_config_id': 'protection_config_id',
        'container_id': 'container_id',
        'offset': 'offset',
        'limit': 'limit',
        'status': 'status',
        'protect_directory': 'protect_directory'
    }

    def __init__(self, enterprise_project_id=None, type=None, protection_config_id=None, container_id=None, offset=None, limit=None, status=None, protect_directory=None):
        r"""ListWebTamperProtectionDirectoryRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param type: **参数解释**: 网页防篡改类型 **约束限制**: 不涉及。 **取值范围**: - container_wtp：容器网页防篡改 **默认取值**: 不涉及 
        :type type: str
        :param protection_config_id: **参数解释**: 防护配置id **约束限制**: 不涉及。 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 
        :type protection_config_id: str
        :param container_id: **参数解释**: 受影响容器id **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 
        :type container_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param status: **参数解释**: 防护状态 **约束限制**: type为container_wtp时必传 **取值范围**: - protected：防护中 - protect_failed：防护失败 **默认取值**: 不涉及 
        :type status: str
        :param protect_directory: **参数解释**: 防护目录 **约束限制**: 不涉及。 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 
        :type protect_directory: str
        """
        
        

        self._enterprise_project_id = None
        self._type = None
        self._protection_config_id = None
        self._container_id = None
        self._offset = None
        self._limit = None
        self._status = None
        self._protect_directory = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.type = type
        self.protection_config_id = protection_config_id
        if container_id is not None:
            self.container_id = container_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if status is not None:
            self.status = status
        if protect_directory is not None:
            self.protect_directory = protect_directory

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListWebTamperProtectionDirectoryRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListWebTamperProtectionDirectoryRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListWebTamperProtectionDirectoryRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListWebTamperProtectionDirectoryRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def type(self):
        r"""Gets the type of this ListWebTamperProtectionDirectoryRequest.

        **参数解释**: 网页防篡改类型 **约束限制**: 不涉及。 **取值范围**: - container_wtp：容器网页防篡改 **默认取值**: 不涉及 

        :return: The type of this ListWebTamperProtectionDirectoryRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListWebTamperProtectionDirectoryRequest.

        **参数解释**: 网页防篡改类型 **约束限制**: 不涉及。 **取值范围**: - container_wtp：容器网页防篡改 **默认取值**: 不涉及 

        :param type: The type of this ListWebTamperProtectionDirectoryRequest.
        :type type: str
        """
        self._type = type

    @property
    def protection_config_id(self):
        r"""Gets the protection_config_id of this ListWebTamperProtectionDirectoryRequest.

        **参数解释**: 防护配置id **约束限制**: 不涉及。 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :return: The protection_config_id of this ListWebTamperProtectionDirectoryRequest.
        :rtype: str
        """
        return self._protection_config_id

    @protection_config_id.setter
    def protection_config_id(self, protection_config_id):
        r"""Sets the protection_config_id of this ListWebTamperProtectionDirectoryRequest.

        **参数解释**: 防护配置id **约束限制**: 不涉及。 **取值范围**: 字符长度1-64位 **默认取值**: 不涉及 

        :param protection_config_id: The protection_config_id of this ListWebTamperProtectionDirectoryRequest.
        :type protection_config_id: str
        """
        self._protection_config_id = protection_config_id

    @property
    def container_id(self):
        r"""Gets the container_id of this ListWebTamperProtectionDirectoryRequest.

        **参数解释**: 受影响容器id **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :return: The container_id of this ListWebTamperProtectionDirectoryRequest.
        :rtype: str
        """
        return self._container_id

    @container_id.setter
    def container_id(self, container_id):
        r"""Sets the container_id of this ListWebTamperProtectionDirectoryRequest.

        **参数解释**: 受影响容器id **约束限制**: 不涉及 **取值范围**: 字符长度0-256位 **默认取值**: 不涉及 

        :param container_id: The container_id of this ListWebTamperProtectionDirectoryRequest.
        :type container_id: str
        """
        self._container_id = container_id

    @property
    def offset(self):
        r"""Gets the offset of this ListWebTamperProtectionDirectoryRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListWebTamperProtectionDirectoryRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListWebTamperProtectionDirectoryRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListWebTamperProtectionDirectoryRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListWebTamperProtectionDirectoryRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListWebTamperProtectionDirectoryRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListWebTamperProtectionDirectoryRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListWebTamperProtectionDirectoryRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def status(self):
        r"""Gets the status of this ListWebTamperProtectionDirectoryRequest.

        **参数解释**: 防护状态 **约束限制**: type为container_wtp时必传 **取值范围**: - protected：防护中 - protect_failed：防护失败 **默认取值**: 不涉及 

        :return: The status of this ListWebTamperProtectionDirectoryRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListWebTamperProtectionDirectoryRequest.

        **参数解释**: 防护状态 **约束限制**: type为container_wtp时必传 **取值范围**: - protected：防护中 - protect_failed：防护失败 **默认取值**: 不涉及 

        :param status: The status of this ListWebTamperProtectionDirectoryRequest.
        :type status: str
        """
        self._status = status

    @property
    def protect_directory(self):
        r"""Gets the protect_directory of this ListWebTamperProtectionDirectoryRequest.

        **参数解释**: 防护目录 **约束限制**: 不涉及。 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :return: The protect_directory of this ListWebTamperProtectionDirectoryRequest.
        :rtype: str
        """
        return self._protect_directory

    @protect_directory.setter
    def protect_directory(self, protect_directory):
        r"""Sets the protect_directory of this ListWebTamperProtectionDirectoryRequest.

        **参数解释**: 防护目录 **约束限制**: 不涉及。 **取值范围**: 字符长度1-256位 **默认取值**: 不涉及 

        :param protect_directory: The protect_directory of this ListWebTamperProtectionDirectoryRequest.
        :type protect_directory: str
        """
        self._protect_directory = protect_directory

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
        if not isinstance(other, ListWebTamperProtectionDirectoryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
