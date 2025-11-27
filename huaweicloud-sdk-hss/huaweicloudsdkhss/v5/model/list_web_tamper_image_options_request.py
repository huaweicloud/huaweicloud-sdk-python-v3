# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWebTamperImageOptionsRequest:

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
        'registry_type': 'str',
        'image_namespace': 'str',
        'registry_name': 'str',
        'image_type': 'str',
        'image_name': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'registry_type': 'registry_type',
        'image_namespace': 'image_namespace',
        'registry_name': 'registry_name',
        'image_type': 'image_type',
        'image_name': 'image_name'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, registry_type=None, image_namespace=None, registry_name=None, image_type=None, image_name=None):
        r"""ListWebTamperImageOptionsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param registry_type: **参数解释**: 仓库镜像镜像仓类型 **约束限制**: 不涉及。 **取值范围**: 字符长度1-512位 **默认取值**: 不涉及 
        :type registry_type: str
        :param image_namespace: **参数解释**: 仓库镜像的组织名称 **约束限制**: 不涉及。 **取值范围**: 字符长度1-512位 **默认取值**: 不涉及 
        :type image_namespace: str
        :param registry_name: **参数解释**: 仓库镜像镜像仓名称 **约束限制**: 不涉及。 **取值范围**: 字符长度1-512位 **默认取值**: 不涉及 
        :type registry_name: str
        :param image_type: **参数解释**: 查询镜像类型 **约束限制**: 不涉及。 **取值范围**: - registry：仓库镜像。 - local：本地镜像。 **默认取值**: 不涉及 
        :type image_type: str
        :param image_name: **参数解释**: 镜像名称 **约束限制**: 不涉及。 **取值范围**: 字符长度1-512位 **默认取值**: 不涉及 
        :type image_name: str
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._registry_type = None
        self._image_namespace = None
        self._registry_name = None
        self._image_type = None
        self._image_name = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if registry_type is not None:
            self.registry_type = registry_type
        if image_namespace is not None:
            self.image_namespace = image_namespace
        if registry_name is not None:
            self.registry_name = registry_name
        self.image_type = image_type
        if image_name is not None:
            self.image_name = image_name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListWebTamperImageOptionsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListWebTamperImageOptionsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListWebTamperImageOptionsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListWebTamperImageOptionsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListWebTamperImageOptionsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListWebTamperImageOptionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListWebTamperImageOptionsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListWebTamperImageOptionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListWebTamperImageOptionsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListWebTamperImageOptionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListWebTamperImageOptionsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListWebTamperImageOptionsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def registry_type(self):
        r"""Gets the registry_type of this ListWebTamperImageOptionsRequest.

        **参数解释**: 仓库镜像镜像仓类型 **约束限制**: 不涉及。 **取值范围**: 字符长度1-512位 **默认取值**: 不涉及 

        :return: The registry_type of this ListWebTamperImageOptionsRequest.
        :rtype: str
        """
        return self._registry_type

    @registry_type.setter
    def registry_type(self, registry_type):
        r"""Sets the registry_type of this ListWebTamperImageOptionsRequest.

        **参数解释**: 仓库镜像镜像仓类型 **约束限制**: 不涉及。 **取值范围**: 字符长度1-512位 **默认取值**: 不涉及 

        :param registry_type: The registry_type of this ListWebTamperImageOptionsRequest.
        :type registry_type: str
        """
        self._registry_type = registry_type

    @property
    def image_namespace(self):
        r"""Gets the image_namespace of this ListWebTamperImageOptionsRequest.

        **参数解释**: 仓库镜像的组织名称 **约束限制**: 不涉及。 **取值范围**: 字符长度1-512位 **默认取值**: 不涉及 

        :return: The image_namespace of this ListWebTamperImageOptionsRequest.
        :rtype: str
        """
        return self._image_namespace

    @image_namespace.setter
    def image_namespace(self, image_namespace):
        r"""Sets the image_namespace of this ListWebTamperImageOptionsRequest.

        **参数解释**: 仓库镜像的组织名称 **约束限制**: 不涉及。 **取值范围**: 字符长度1-512位 **默认取值**: 不涉及 

        :param image_namespace: The image_namespace of this ListWebTamperImageOptionsRequest.
        :type image_namespace: str
        """
        self._image_namespace = image_namespace

    @property
    def registry_name(self):
        r"""Gets the registry_name of this ListWebTamperImageOptionsRequest.

        **参数解释**: 仓库镜像镜像仓名称 **约束限制**: 不涉及。 **取值范围**: 字符长度1-512位 **默认取值**: 不涉及 

        :return: The registry_name of this ListWebTamperImageOptionsRequest.
        :rtype: str
        """
        return self._registry_name

    @registry_name.setter
    def registry_name(self, registry_name):
        r"""Sets the registry_name of this ListWebTamperImageOptionsRequest.

        **参数解释**: 仓库镜像镜像仓名称 **约束限制**: 不涉及。 **取值范围**: 字符长度1-512位 **默认取值**: 不涉及 

        :param registry_name: The registry_name of this ListWebTamperImageOptionsRequest.
        :type registry_name: str
        """
        self._registry_name = registry_name

    @property
    def image_type(self):
        r"""Gets the image_type of this ListWebTamperImageOptionsRequest.

        **参数解释**: 查询镜像类型 **约束限制**: 不涉及。 **取值范围**: - registry：仓库镜像。 - local：本地镜像。 **默认取值**: 不涉及 

        :return: The image_type of this ListWebTamperImageOptionsRequest.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this ListWebTamperImageOptionsRequest.

        **参数解释**: 查询镜像类型 **约束限制**: 不涉及。 **取值范围**: - registry：仓库镜像。 - local：本地镜像。 **默认取值**: 不涉及 

        :param image_type: The image_type of this ListWebTamperImageOptionsRequest.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def image_name(self):
        r"""Gets the image_name of this ListWebTamperImageOptionsRequest.

        **参数解释**: 镜像名称 **约束限制**: 不涉及。 **取值范围**: 字符长度1-512位 **默认取值**: 不涉及 

        :return: The image_name of this ListWebTamperImageOptionsRequest.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ListWebTamperImageOptionsRequest.

        **参数解释**: 镜像名称 **约束限制**: 不涉及。 **取值范围**: 字符长度1-512位 **默认取值**: 不涉及 

        :param image_name: The image_name of this ListWebTamperImageOptionsRequest.
        :type image_name: str
        """
        self._image_name = image_name

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
        if not isinstance(other, ListWebTamperImageOptionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
