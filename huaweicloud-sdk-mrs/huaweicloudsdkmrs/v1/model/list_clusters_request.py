# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListClustersRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'str',
        'page_size': 'str',
        'current_page': 'str',
        'cluster_name': 'str',
        'cluster_state': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'tags': 'tags',
        'page_size': 'pageSize',
        'current_page': 'currentPage',
        'cluster_name': 'clusterName',
        'cluster_state': 'clusterState',
        'enterprise_project_id': 'enterpriseProjectId'
    }

    def __init__(self, tags=None, page_size=None, current_page=None, cluster_name=None, cluster_state=None, enterprise_project_id=None):
        """ListClustersRequest

        The model defined in huaweicloud sdk

        :param tags: 可以通过集群的标签来搜索指定标签的集群，当指定多个tag进行查询时，标签之间是与的关系。  - tags参数的格式为tags&#x3D;k1*v1,k2*v2,k3*v3 - 当标签的value为空时，格式为tags&#x3D;k1,k2,k3*v3
        :type tags: str
        :param page_size: 分页查询每页返回的最大集群数量。  取值范围：[1～2147483646]
        :type page_size: str
        :param current_page: 当前查询页码。
        :type current_page: str
        :param cluster_name: 集群名称。
        :type cluster_name: str
        :param cluster_state: 根据集群状态查询集群列表。 - existing：查询现有集群列表，包括除“已删除”、包周期集群的“订单处理中”和“准备中”状态外的所有集群。 - history：查询历史集群列表，包括所有“已删除”、删除集群失败、集群删除虚拟机失败、删除集群更新数据库失败等状态的集群。 - starting：查询启动中的集群列表。 - running：查询运行中的集群列表。 - terminated：查询已删除的集群列表。 - failed：查询失败的集群列表。 - abnormal：查询异常的集群列表。 - terminating：查询删除中的集群列表。 - frozen：查询已冻结的集群列表。 - scaling-out：查询扩容中的集群列表。 - scaling-in：查询缩容中的集群列表。
        :type cluster_state: str
        :param enterprise_project_id: 通过企业项目ID来搜索指定项目的集群。  该参数默认设置为0，表示为default企业项目。  获取方式请参见《企业管理API参考》的“查询企业项目列表”响应消息表“enterprise_project字段数据结构说明”的“id”。
        :type enterprise_project_id: str
        """
        
        

        self._tags = None
        self._page_size = None
        self._current_page = None
        self._cluster_name = None
        self._cluster_state = None
        self._enterprise_project_id = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        if page_size is not None:
            self.page_size = page_size
        if current_page is not None:
            self.current_page = current_page
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if cluster_state is not None:
            self.cluster_state = cluster_state
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        """Gets the tags of this ListClustersRequest.

        可以通过集群的标签来搜索指定标签的集群，当指定多个tag进行查询时，标签之间是与的关系。  - tags参数的格式为tags=k1*v1,k2*v2,k3*v3 - 当标签的value为空时，格式为tags=k1,k2,k3*v3

        :return: The tags of this ListClustersRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListClustersRequest.

        可以通过集群的标签来搜索指定标签的集群，当指定多个tag进行查询时，标签之间是与的关系。  - tags参数的格式为tags=k1*v1,k2*v2,k3*v3 - 当标签的value为空时，格式为tags=k1,k2,k3*v3

        :param tags: The tags of this ListClustersRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def page_size(self):
        """Gets the page_size of this ListClustersRequest.

        分页查询每页返回的最大集群数量。  取值范围：[1～2147483646]

        :return: The page_size of this ListClustersRequest.
        :rtype: str
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        """Sets the page_size of this ListClustersRequest.

        分页查询每页返回的最大集群数量。  取值范围：[1～2147483646]

        :param page_size: The page_size of this ListClustersRequest.
        :type page_size: str
        """
        self._page_size = page_size

    @property
    def current_page(self):
        """Gets the current_page of this ListClustersRequest.

        当前查询页码。

        :return: The current_page of this ListClustersRequest.
        :rtype: str
        """
        return self._current_page

    @current_page.setter
    def current_page(self, current_page):
        """Sets the current_page of this ListClustersRequest.

        当前查询页码。

        :param current_page: The current_page of this ListClustersRequest.
        :type current_page: str
        """
        self._current_page = current_page

    @property
    def cluster_name(self):
        """Gets the cluster_name of this ListClustersRequest.

        集群名称。

        :return: The cluster_name of this ListClustersRequest.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this ListClustersRequest.

        集群名称。

        :param cluster_name: The cluster_name of this ListClustersRequest.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def cluster_state(self):
        """Gets the cluster_state of this ListClustersRequest.

        根据集群状态查询集群列表。 - existing：查询现有集群列表，包括除“已删除”、包周期集群的“订单处理中”和“准备中”状态外的所有集群。 - history：查询历史集群列表，包括所有“已删除”、删除集群失败、集群删除虚拟机失败、删除集群更新数据库失败等状态的集群。 - starting：查询启动中的集群列表。 - running：查询运行中的集群列表。 - terminated：查询已删除的集群列表。 - failed：查询失败的集群列表。 - abnormal：查询异常的集群列表。 - terminating：查询删除中的集群列表。 - frozen：查询已冻结的集群列表。 - scaling-out：查询扩容中的集群列表。 - scaling-in：查询缩容中的集群列表。

        :return: The cluster_state of this ListClustersRequest.
        :rtype: str
        """
        return self._cluster_state

    @cluster_state.setter
    def cluster_state(self, cluster_state):
        """Sets the cluster_state of this ListClustersRequest.

        根据集群状态查询集群列表。 - existing：查询现有集群列表，包括除“已删除”、包周期集群的“订单处理中”和“准备中”状态外的所有集群。 - history：查询历史集群列表，包括所有“已删除”、删除集群失败、集群删除虚拟机失败、删除集群更新数据库失败等状态的集群。 - starting：查询启动中的集群列表。 - running：查询运行中的集群列表。 - terminated：查询已删除的集群列表。 - failed：查询失败的集群列表。 - abnormal：查询异常的集群列表。 - terminating：查询删除中的集群列表。 - frozen：查询已冻结的集群列表。 - scaling-out：查询扩容中的集群列表。 - scaling-in：查询缩容中的集群列表。

        :param cluster_state: The cluster_state of this ListClustersRequest.
        :type cluster_state: str
        """
        self._cluster_state = cluster_state

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this ListClustersRequest.

        通过企业项目ID来搜索指定项目的集群。  该参数默认设置为0，表示为default企业项目。  获取方式请参见《企业管理API参考》的“查询企业项目列表”响应消息表“enterprise_project字段数据结构说明”的“id”。

        :return: The enterprise_project_id of this ListClustersRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListClustersRequest.

        通过企业项目ID来搜索指定项目的集群。  该参数默认设置为0，表示为default企业项目。  获取方式请参见《企业管理API参考》的“查询企业项目列表”响应消息表“enterprise_project字段数据结构说明”的“id”。

        :param enterprise_project_id: The enterprise_project_id of this ListClustersRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, ListClustersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
