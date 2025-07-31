# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIacFileRisksRequest:

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
        'file_id': 'str',
        'risk_name': 'str',
        'risk_level': 'str',
        'risk_category': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'file_id': 'file_id',
        'risk_name': 'risk_name',
        'risk_level': 'risk_level',
        'risk_category': 'risk_category'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, file_id=None, risk_name=None, risk_level=None, risk_category=None):
        r"""ListIacFileRisksRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param file_id: **参数解释**: 文件ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64  **默认取值**: 不涉及 
        :type file_id: str
        :param risk_name: 风险名称
        :type risk_name: str
        :param risk_level: **参数解释**: 风险程度 **约束限制**: 不涉及 **取值范围**: - high ：高危 - medium ：中危 - low ：低危 - tips ：提示  **默认取值**: 不涉及 
        :type risk_level: str
        :param risk_category: **参数解释**: 风险分类 **约束限制**: 不涉及 **取值范围**: k8s yaml的风险分类，包含如下：   - control_plane：控制平面   - access_control：访问控制   - network：网络   - workload：工作负载   - secrets：密钥管理   - node_escape：节点逃逸  **默认取值**: 不涉及 
        :type risk_category: str
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._file_id = None
        self._risk_name = None
        self._risk_level = None
        self._risk_category = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.offset = offset
        self.limit = limit
        self.file_id = file_id
        if risk_name is not None:
            self.risk_name = risk_name
        if risk_level is not None:
            self.risk_level = risk_level
        if risk_category is not None:
            self.risk_category = risk_category

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListIacFileRisksRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListIacFileRisksRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListIacFileRisksRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListIacFileRisksRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListIacFileRisksRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :return: The offset of this ListIacFileRisksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListIacFileRisksRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :param offset: The offset of this ListIacFileRisksRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListIacFileRisksRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListIacFileRisksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListIacFileRisksRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListIacFileRisksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def file_id(self):
        r"""Gets the file_id of this ListIacFileRisksRequest.

        **参数解释**: 文件ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64  **默认取值**: 不涉及 

        :return: The file_id of this ListIacFileRisksRequest.
        :rtype: str
        """
        return self._file_id

    @file_id.setter
    def file_id(self, file_id):
        r"""Sets the file_id of this ListIacFileRisksRequest.

        **参数解释**: 文件ID **约束限制**: 不涉及 **取值范围**: 字符长度1-64  **默认取值**: 不涉及 

        :param file_id: The file_id of this ListIacFileRisksRequest.
        :type file_id: str
        """
        self._file_id = file_id

    @property
    def risk_name(self):
        r"""Gets the risk_name of this ListIacFileRisksRequest.

        风险名称

        :return: The risk_name of this ListIacFileRisksRequest.
        :rtype: str
        """
        return self._risk_name

    @risk_name.setter
    def risk_name(self, risk_name):
        r"""Sets the risk_name of this ListIacFileRisksRequest.

        风险名称

        :param risk_name: The risk_name of this ListIacFileRisksRequest.
        :type risk_name: str
        """
        self._risk_name = risk_name

    @property
    def risk_level(self):
        r"""Gets the risk_level of this ListIacFileRisksRequest.

        **参数解释**: 风险程度 **约束限制**: 不涉及 **取值范围**: - high ：高危 - medium ：中危 - low ：低危 - tips ：提示  **默认取值**: 不涉及 

        :return: The risk_level of this ListIacFileRisksRequest.
        :rtype: str
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        r"""Sets the risk_level of this ListIacFileRisksRequest.

        **参数解释**: 风险程度 **约束限制**: 不涉及 **取值范围**: - high ：高危 - medium ：中危 - low ：低危 - tips ：提示  **默认取值**: 不涉及 

        :param risk_level: The risk_level of this ListIacFileRisksRequest.
        :type risk_level: str
        """
        self._risk_level = risk_level

    @property
    def risk_category(self):
        r"""Gets the risk_category of this ListIacFileRisksRequest.

        **参数解释**: 风险分类 **约束限制**: 不涉及 **取值范围**: k8s yaml的风险分类，包含如下：   - control_plane：控制平面   - access_control：访问控制   - network：网络   - workload：工作负载   - secrets：密钥管理   - node_escape：节点逃逸  **默认取值**: 不涉及 

        :return: The risk_category of this ListIacFileRisksRequest.
        :rtype: str
        """
        return self._risk_category

    @risk_category.setter
    def risk_category(self, risk_category):
        r"""Sets the risk_category of this ListIacFileRisksRequest.

        **参数解释**: 风险分类 **约束限制**: 不涉及 **取值范围**: k8s yaml的风险分类，包含如下：   - control_plane：控制平面   - access_control：访问控制   - network：网络   - workload：工作负载   - secrets：密钥管理   - node_escape：节点逃逸  **默认取值**: 不涉及 

        :param risk_category: The risk_category of this ListIacFileRisksRequest.
        :type risk_category: str
        """
        self._risk_category = risk_category

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
        if not isinstance(other, ListIacFileRisksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
