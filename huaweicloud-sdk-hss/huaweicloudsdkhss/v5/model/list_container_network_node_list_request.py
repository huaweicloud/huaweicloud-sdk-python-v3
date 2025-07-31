# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListContainerNetworkNodeListRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'enterprise_project_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'query_field': 'str',
        'query_value': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'enterprise_project_id': 'enterprise_project_id',
        'limit': 'limit',
        'offset': 'offset',
        'query_field': 'query_field',
        'query_value': 'query_value'
    }

    def __init__(self, cluster_id=None, enterprise_project_id=None, limit=None, offset=None, query_field=None, query_value=None):
        r"""ListContainerNetworkNodeListRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID
        :type cluster_id: str
        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 
        :type offset: int
        :param query_field: 查询字段
        :type query_field: str
        :param query_value: 查询字段值
        :type query_value: str
        """
        
        

        self._cluster_id = None
        self._enterprise_project_id = None
        self._limit = None
        self._offset = None
        self._query_field = None
        self._query_value = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.limit = limit
        self.offset = offset
        if query_field is not None:
            self.query_field = query_field
        if query_value is not None:
            self.query_value = query_value

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListContainerNetworkNodeListRequest.

        集群ID

        :return: The cluster_id of this ListContainerNetworkNodeListRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListContainerNetworkNodeListRequest.

        集群ID

        :param cluster_id: The cluster_id of this ListContainerNetworkNodeListRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListContainerNetworkNodeListRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListContainerNetworkNodeListRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListContainerNetworkNodeListRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListContainerNetworkNodeListRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def limit(self):
        r"""Gets the limit of this ListContainerNetworkNodeListRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListContainerNetworkNodeListRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListContainerNetworkNodeListRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListContainerNetworkNodeListRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListContainerNetworkNodeListRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :return: The offset of this ListContainerNetworkNodeListRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListContainerNetworkNodeListRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 不涉及 

        :param offset: The offset of this ListContainerNetworkNodeListRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def query_field(self):
        r"""Gets the query_field of this ListContainerNetworkNodeListRequest.

        查询字段

        :return: The query_field of this ListContainerNetworkNodeListRequest.
        :rtype: str
        """
        return self._query_field

    @query_field.setter
    def query_field(self, query_field):
        r"""Sets the query_field of this ListContainerNetworkNodeListRequest.

        查询字段

        :param query_field: The query_field of this ListContainerNetworkNodeListRequest.
        :type query_field: str
        """
        self._query_field = query_field

    @property
    def query_value(self):
        r"""Gets the query_value of this ListContainerNetworkNodeListRequest.

        查询字段值

        :return: The query_value of this ListContainerNetworkNodeListRequest.
        :rtype: str
        """
        return self._query_value

    @query_value.setter
    def query_value(self, query_value):
        r"""Sets the query_value of this ListContainerNetworkNodeListRequest.

        查询字段值

        :param query_value: The query_value of this ListContainerNetworkNodeListRequest.
        :type query_value: str
        """
        self._query_value = query_value

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
        if not isinstance(other, ListContainerNetworkNodeListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
