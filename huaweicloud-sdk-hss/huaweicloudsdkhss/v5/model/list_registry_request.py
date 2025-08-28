# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRegistryRequest:

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
        'registry_name': 'str',
        'registry_id': 'str',
        'registry_type': 'str',
        'registry_addr': 'str',
        'status': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'registry_name': 'registry_name',
        'registry_id': 'registry_id',
        'registry_type': 'registry_type',
        'registry_addr': 'registry_addr',
        'status': 'status'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, registry_name=None, registry_id=None, registry_type=None, registry_addr=None, status=None):
        r"""ListRegistryRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param registry_name: **参数解释**: 仓库名称 **取值范围**: 字符长度1-128位 
        :type registry_name: str
        :param registry_id: **参数解释**: 仓库ID **取值范围**: 字符长度1-64位 
        :type registry_id: str
        :param registry_type: **参数解释**: 镜像仓类型，不传默认返回所有类型。如果要查询多个类型，可以使用逗号分隔。 **取值范围**: - Harbor harbor - Jfrog jfrog - SwrPrivate swr私有 - SwrShared  swr共享 - SwrEnterprise  swr企业 - Other  其他仓库 
        :type registry_type: str
        :param registry_addr: **参数解释**: 镜像仓地址 **取值范围**: 字符长度1-256位 
        :type registry_addr: str
        :param status: **参数解释**： 接入状态 **约束限制**： 不涉及 **取值范围**： - success：接入成功 - fail：接入异常 - accessing：接入中  **默认取值**： 不涉及 
        :type status: str
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._registry_name = None
        self._registry_id = None
        self._registry_type = None
        self._registry_addr = None
        self._status = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if registry_name is not None:
            self.registry_name = registry_name
        if registry_id is not None:
            self.registry_id = registry_id
        if registry_type is not None:
            self.registry_type = registry_type
        if registry_addr is not None:
            self.registry_addr = registry_addr
        if status is not None:
            self.status = status

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListRegistryRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListRegistryRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListRegistryRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListRegistryRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListRegistryRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListRegistryRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListRegistryRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListRegistryRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListRegistryRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListRegistryRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRegistryRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListRegistryRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def registry_name(self):
        r"""Gets the registry_name of this ListRegistryRequest.

        **参数解释**: 仓库名称 **取值范围**: 字符长度1-128位 

        :return: The registry_name of this ListRegistryRequest.
        :rtype: str
        """
        return self._registry_name

    @registry_name.setter
    def registry_name(self, registry_name):
        r"""Sets the registry_name of this ListRegistryRequest.

        **参数解释**: 仓库名称 **取值范围**: 字符长度1-128位 

        :param registry_name: The registry_name of this ListRegistryRequest.
        :type registry_name: str
        """
        self._registry_name = registry_name

    @property
    def registry_id(self):
        r"""Gets the registry_id of this ListRegistryRequest.

        **参数解释**: 仓库ID **取值范围**: 字符长度1-64位 

        :return: The registry_id of this ListRegistryRequest.
        :rtype: str
        """
        return self._registry_id

    @registry_id.setter
    def registry_id(self, registry_id):
        r"""Sets the registry_id of this ListRegistryRequest.

        **参数解释**: 仓库ID **取值范围**: 字符长度1-64位 

        :param registry_id: The registry_id of this ListRegistryRequest.
        :type registry_id: str
        """
        self._registry_id = registry_id

    @property
    def registry_type(self):
        r"""Gets the registry_type of this ListRegistryRequest.

        **参数解释**: 镜像仓类型，不传默认返回所有类型。如果要查询多个类型，可以使用逗号分隔。 **取值范围**: - Harbor harbor - Jfrog jfrog - SwrPrivate swr私有 - SwrShared  swr共享 - SwrEnterprise  swr企业 - Other  其他仓库 

        :return: The registry_type of this ListRegistryRequest.
        :rtype: str
        """
        return self._registry_type

    @registry_type.setter
    def registry_type(self, registry_type):
        r"""Sets the registry_type of this ListRegistryRequest.

        **参数解释**: 镜像仓类型，不传默认返回所有类型。如果要查询多个类型，可以使用逗号分隔。 **取值范围**: - Harbor harbor - Jfrog jfrog - SwrPrivate swr私有 - SwrShared  swr共享 - SwrEnterprise  swr企业 - Other  其他仓库 

        :param registry_type: The registry_type of this ListRegistryRequest.
        :type registry_type: str
        """
        self._registry_type = registry_type

    @property
    def registry_addr(self):
        r"""Gets the registry_addr of this ListRegistryRequest.

        **参数解释**: 镜像仓地址 **取值范围**: 字符长度1-256位 

        :return: The registry_addr of this ListRegistryRequest.
        :rtype: str
        """
        return self._registry_addr

    @registry_addr.setter
    def registry_addr(self, registry_addr):
        r"""Sets the registry_addr of this ListRegistryRequest.

        **参数解释**: 镜像仓地址 **取值范围**: 字符长度1-256位 

        :param registry_addr: The registry_addr of this ListRegistryRequest.
        :type registry_addr: str
        """
        self._registry_addr = registry_addr

    @property
    def status(self):
        r"""Gets the status of this ListRegistryRequest.

        **参数解释**： 接入状态 **约束限制**： 不涉及 **取值范围**： - success：接入成功 - fail：接入异常 - accessing：接入中  **默认取值**： 不涉及 

        :return: The status of this ListRegistryRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListRegistryRequest.

        **参数解释**： 接入状态 **约束限制**： 不涉及 **取值范围**： - success：接入成功 - fail：接入异常 - accessing：接入中  **默认取值**： 不涉及 

        :param status: The status of this ListRegistryRequest.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ListRegistryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
