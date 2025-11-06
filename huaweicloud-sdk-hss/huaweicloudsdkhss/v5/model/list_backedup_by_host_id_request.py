# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBackedupByHostIdRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'enterprise_project_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'host_id': 'str',
        'status': 'str',
        'name': 'str',
        'last_days': 'int'
    }

    attribute_map = {
        'region': 'region',
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'host_id': 'host_id',
        'status': 'status',
        'name': 'name',
        'last_days': 'last_days'
    }

    def __init__(self, region=None, enterprise_project_id=None, offset=None, limit=None, host_id=None, status=None, name=None, last_days=None):
        r"""ListBackedupByHostIdRequest

        The model defined in huaweicloud sdk

        :param region: **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 
        :type region: str
        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param host_id: **参数解释**: 主机ID **约束限制**: 不涉及 **取值范围**: 字符长度0-64位 **默认取值**: 不涉及 
        :type host_id: str
        :param status: **参数解释**: 状态 **约束限制**: 不涉及 **取值范围**: - available：可用 - protecting：保护中 - deleting：删除中 - restoring：恢复中 - error：异常 - waiting_protect：等待保护 - waiting_delete：等待删除 - waiting_restore：等待恢复  **默认取值**: 不涉及 
        :type status: str
        :param name: **参数解释**: 备份名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-65535位 **默认取值**: 不涉及 
        :type name: str
        :param last_days: **参数解释**: 查询时间范围 **约束限制**: 不涉及 **取值范围**: 取值1-30 **默认取值**: 不涉及 
        :type last_days: int
        """
        
        

        self._region = None
        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._host_id = None
        self._status = None
        self._name = None
        self._last_days = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.offset = offset
        self.limit = limit
        self.host_id = host_id
        if status is not None:
            self.status = status
        if name is not None:
            self.name = name
        if last_days is not None:
            self.last_days = last_days

    @property
    def region(self):
        r"""Gets the region of this ListBackedupByHostIdRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :return: The region of this ListBackedupByHostIdRequest.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ListBackedupByHostIdRequest.

        **参数解释**: 区域ID，用于查询目的区域内的资产。获取方式请参见[获取区域ID](hss_02_0026.xml)。 **约束限制**: 不涉及 **取值范围**: 字符长度1-128位 **默认取值**: 不涉及 

        :param region: The region of this ListBackedupByHostIdRequest.
        :type region: str
        """
        self._region = region

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListBackedupByHostIdRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListBackedupByHostIdRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListBackedupByHostIdRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListBackedupByHostIdRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListBackedupByHostIdRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :return: The offset of this ListBackedupByHostIdRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListBackedupByHostIdRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :param offset: The offset of this ListBackedupByHostIdRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListBackedupByHostIdRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListBackedupByHostIdRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListBackedupByHostIdRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListBackedupByHostIdRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def host_id(self):
        r"""Gets the host_id of this ListBackedupByHostIdRequest.

        **参数解释**: 主机ID **约束限制**: 不涉及 **取值范围**: 字符长度0-64位 **默认取值**: 不涉及 

        :return: The host_id of this ListBackedupByHostIdRequest.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this ListBackedupByHostIdRequest.

        **参数解释**: 主机ID **约束限制**: 不涉及 **取值范围**: 字符长度0-64位 **默认取值**: 不涉及 

        :param host_id: The host_id of this ListBackedupByHostIdRequest.
        :type host_id: str
        """
        self._host_id = host_id

    @property
    def status(self):
        r"""Gets the status of this ListBackedupByHostIdRequest.

        **参数解释**: 状态 **约束限制**: 不涉及 **取值范围**: - available：可用 - protecting：保护中 - deleting：删除中 - restoring：恢复中 - error：异常 - waiting_protect：等待保护 - waiting_delete：等待删除 - waiting_restore：等待恢复  **默认取值**: 不涉及 

        :return: The status of this ListBackedupByHostIdRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListBackedupByHostIdRequest.

        **参数解释**: 状态 **约束限制**: 不涉及 **取值范围**: - available：可用 - protecting：保护中 - deleting：删除中 - restoring：恢复中 - error：异常 - waiting_protect：等待保护 - waiting_delete：等待删除 - waiting_restore：等待恢复  **默认取值**: 不涉及 

        :param status: The status of this ListBackedupByHostIdRequest.
        :type status: str
        """
        self._status = status

    @property
    def name(self):
        r"""Gets the name of this ListBackedupByHostIdRequest.

        **参数解释**: 备份名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-65535位 **默认取值**: 不涉及 

        :return: The name of this ListBackedupByHostIdRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListBackedupByHostIdRequest.

        **参数解释**: 备份名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-65535位 **默认取值**: 不涉及 

        :param name: The name of this ListBackedupByHostIdRequest.
        :type name: str
        """
        self._name = name

    @property
    def last_days(self):
        r"""Gets the last_days of this ListBackedupByHostIdRequest.

        **参数解释**: 查询时间范围 **约束限制**: 不涉及 **取值范围**: 取值1-30 **默认取值**: 不涉及 

        :return: The last_days of this ListBackedupByHostIdRequest.
        :rtype: int
        """
        return self._last_days

    @last_days.setter
    def last_days(self, last_days):
        r"""Sets the last_days of this ListBackedupByHostIdRequest.

        **参数解释**: 查询时间范围 **约束限制**: 不涉及 **取值范围**: 取值1-30 **默认取值**: 不涉及 

        :param last_days: The last_days of this ListBackedupByHostIdRequest.
        :type last_days: int
        """
        self._last_days = last_days

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
        if not isinstance(other, ListBackedupByHostIdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
