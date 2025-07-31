# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListK8sStatefulSetsRequest:

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
        'statefulset_name': 'str',
        'namespace_name': 'str',
        'cluster_name': 'str',
        'limit': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'statefulset_name': 'statefulset_name',
        'namespace_name': 'namespace_name',
        'cluster_name': 'cluster_name',
        'limit': 'limit'
    }

    def __init__(self, enterprise_project_id=None, offset=None, statefulset_name=None, namespace_name=None, cluster_name=None, limit=None):
        r"""ListK8sStatefulSetsRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param statefulset_name: statefulset名称
        :type statefulset_name: str
        :param namespace_name: 命名空间名称
        :type namespace_name: str
        :param cluster_name: 所属集群名称
        :type cluster_name: str
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._statefulset_name = None
        self._namespace_name = None
        self._cluster_name = None
        self._limit = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if statefulset_name is not None:
            self.statefulset_name = statefulset_name
        if namespace_name is not None:
            self.namespace_name = namespace_name
        if cluster_name is not None:
            self.cluster_name = cluster_name
        self.limit = limit

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListK8sStatefulSetsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListK8sStatefulSetsRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListK8sStatefulSetsRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListK8sStatefulSetsRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListK8sStatefulSetsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListK8sStatefulSetsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListK8sStatefulSetsRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListK8sStatefulSetsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def statefulset_name(self):
        r"""Gets the statefulset_name of this ListK8sStatefulSetsRequest.

        statefulset名称

        :return: The statefulset_name of this ListK8sStatefulSetsRequest.
        :rtype: str
        """
        return self._statefulset_name

    @statefulset_name.setter
    def statefulset_name(self, statefulset_name):
        r"""Sets the statefulset_name of this ListK8sStatefulSetsRequest.

        statefulset名称

        :param statefulset_name: The statefulset_name of this ListK8sStatefulSetsRequest.
        :type statefulset_name: str
        """
        self._statefulset_name = statefulset_name

    @property
    def namespace_name(self):
        r"""Gets the namespace_name of this ListK8sStatefulSetsRequest.

        命名空间名称

        :return: The namespace_name of this ListK8sStatefulSetsRequest.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        r"""Sets the namespace_name of this ListK8sStatefulSetsRequest.

        命名空间名称

        :param namespace_name: The namespace_name of this ListK8sStatefulSetsRequest.
        :type namespace_name: str
        """
        self._namespace_name = namespace_name

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ListK8sStatefulSetsRequest.

        所属集群名称

        :return: The cluster_name of this ListK8sStatefulSetsRequest.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ListK8sStatefulSetsRequest.

        所属集群名称

        :param cluster_name: The cluster_name of this ListK8sStatefulSetsRequest.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def limit(self):
        r"""Gets the limit of this ListK8sStatefulSetsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListK8sStatefulSetsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListK8sStatefulSetsRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListK8sStatefulSetsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListK8sStatefulSetsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
