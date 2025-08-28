# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListImageWhiteListsRequest:

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
        'global_image_type': 'str',
        'type': 'str',
        'vul_name': 'str',
        'vul_type': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'global_image_type': 'global_image_type',
        'type': 'type',
        'vul_name': 'vul_name',
        'vul_type': 'vul_type'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, global_image_type=None, type=None, vul_name=None, vul_type=None):
        r"""ListImageWhiteListsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param global_image_type: **参数解释**： 镜像类型 **约束限制**: 不涉及 **取值范围**: - local：本地镜像。 - registry：仓库镜像。  **默认取值**: 不涉及 
        :type global_image_type: str
        :param type: **参数解释**： 白名单类型 **约束限制**: 不涉及 **取值范围**: - vulnerability：漏洞白名单。  **默认取值**: 不涉及 
        :type type: str
        :param vul_name: **参数解释**： 漏洞名称（只在查询漏洞白名单时使用） **约束限制**： 不涉及 **取值范围**： 字符长度0-256位 **默认取值**： 不涉及 
        :type vul_name: str
        :param vul_type: **参数解释**： 漏洞类型（只在查询漏洞白名单时使用） **约束限制**: 不涉及 **取值范围**: - linux_vul：linux漏洞。 - app_vul：应用漏洞。  **默认取值**: 不涉及 
        :type vul_type: str
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._global_image_type = None
        self._type = None
        self._vul_name = None
        self._vul_type = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        self.global_image_type = global_image_type
        self.type = type
        if vul_name is not None:
            self.vul_name = vul_name
        if vul_type is not None:
            self.vul_type = vul_type

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListImageWhiteListsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListImageWhiteListsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListImageWhiteListsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListImageWhiteListsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListImageWhiteListsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListImageWhiteListsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListImageWhiteListsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListImageWhiteListsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListImageWhiteListsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListImageWhiteListsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListImageWhiteListsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListImageWhiteListsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def global_image_type(self):
        r"""Gets the global_image_type of this ListImageWhiteListsRequest.

        **参数解释**： 镜像类型 **约束限制**: 不涉及 **取值范围**: - local：本地镜像。 - registry：仓库镜像。  **默认取值**: 不涉及 

        :return: The global_image_type of this ListImageWhiteListsRequest.
        :rtype: str
        """
        return self._global_image_type

    @global_image_type.setter
    def global_image_type(self, global_image_type):
        r"""Sets the global_image_type of this ListImageWhiteListsRequest.

        **参数解释**： 镜像类型 **约束限制**: 不涉及 **取值范围**: - local：本地镜像。 - registry：仓库镜像。  **默认取值**: 不涉及 

        :param global_image_type: The global_image_type of this ListImageWhiteListsRequest.
        :type global_image_type: str
        """
        self._global_image_type = global_image_type

    @property
    def type(self):
        r"""Gets the type of this ListImageWhiteListsRequest.

        **参数解释**： 白名单类型 **约束限制**: 不涉及 **取值范围**: - vulnerability：漏洞白名单。  **默认取值**: 不涉及 

        :return: The type of this ListImageWhiteListsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListImageWhiteListsRequest.

        **参数解释**： 白名单类型 **约束限制**: 不涉及 **取值范围**: - vulnerability：漏洞白名单。  **默认取值**: 不涉及 

        :param type: The type of this ListImageWhiteListsRequest.
        :type type: str
        """
        self._type = type

    @property
    def vul_name(self):
        r"""Gets the vul_name of this ListImageWhiteListsRequest.

        **参数解释**： 漏洞名称（只在查询漏洞白名单时使用） **约束限制**： 不涉及 **取值范围**： 字符长度0-256位 **默认取值**： 不涉及 

        :return: The vul_name of this ListImageWhiteListsRequest.
        :rtype: str
        """
        return self._vul_name

    @vul_name.setter
    def vul_name(self, vul_name):
        r"""Sets the vul_name of this ListImageWhiteListsRequest.

        **参数解释**： 漏洞名称（只在查询漏洞白名单时使用） **约束限制**： 不涉及 **取值范围**： 字符长度0-256位 **默认取值**： 不涉及 

        :param vul_name: The vul_name of this ListImageWhiteListsRequest.
        :type vul_name: str
        """
        self._vul_name = vul_name

    @property
    def vul_type(self):
        r"""Gets the vul_type of this ListImageWhiteListsRequest.

        **参数解释**： 漏洞类型（只在查询漏洞白名单时使用） **约束限制**: 不涉及 **取值范围**: - linux_vul：linux漏洞。 - app_vul：应用漏洞。  **默认取值**: 不涉及 

        :return: The vul_type of this ListImageWhiteListsRequest.
        :rtype: str
        """
        return self._vul_type

    @vul_type.setter
    def vul_type(self, vul_type):
        r"""Sets the vul_type of this ListImageWhiteListsRequest.

        **参数解释**： 漏洞类型（只在查询漏洞白名单时使用） **约束限制**: 不涉及 **取值范围**: - linux_vul：linux漏洞。 - app_vul：应用漏洞。  **默认取值**: 不涉及 

        :param vul_type: The vul_type of this ListImageWhiteListsRequest.
        :type vul_type: str
        """
        self._vul_type = vul_type

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
        if not isinstance(other, ListImageWhiteListsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
