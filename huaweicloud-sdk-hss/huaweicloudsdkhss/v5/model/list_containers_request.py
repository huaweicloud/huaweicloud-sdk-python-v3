# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListContainersRequest:

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
        'container_name': 'str',
        'pod_name': 'str',
        'image_name': 'str',
        'cluster_container': 'bool',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'container_name': 'container_name',
        'pod_name': 'pod_name',
        'image_name': 'image_name',
        'cluster_container': 'cluster_container',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, enterprise_project_id=None, container_name=None, pod_name=None, image_name=None, cluster_container=None, limit=None, offset=None):
        r"""ListContainersRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param container_name: **参数解释**: 容器名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type container_name: str
        :param pod_name: **参数解释**: 所属Pod名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type pod_name: str
        :param image_name: **参数解释**: 镜像名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 
        :type image_name: str
        :param cluster_container: **参数解释**: 是否是集群纳管的容器 **约束限制**: 不涉及 **取值范围**:   - true：是集群纳管的容器。   - false：不是集群纳管的容器。 **默认取值**: false 
        :type cluster_container: bool
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param offset: **参数解释**: 指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 取值0-2000000 **默认取值**: 0 
        :type offset: int
        """
        
        

        self._enterprise_project_id = None
        self._container_name = None
        self._pod_name = None
        self._image_name = None
        self._cluster_container = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if container_name is not None:
            self.container_name = container_name
        if pod_name is not None:
            self.pod_name = pod_name
        if image_name is not None:
            self.image_name = image_name
        if cluster_container is not None:
            self.cluster_container = cluster_container
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListContainersRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListContainersRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListContainersRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListContainersRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def container_name(self):
        r"""Gets the container_name of this ListContainersRequest.

        **参数解释**: 容器名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The container_name of this ListContainersRequest.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        r"""Sets the container_name of this ListContainersRequest.

        **参数解释**: 容器名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param container_name: The container_name of this ListContainersRequest.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def pod_name(self):
        r"""Gets the pod_name of this ListContainersRequest.

        **参数解释**: 所属Pod名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The pod_name of this ListContainersRequest.
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        r"""Sets the pod_name of this ListContainersRequest.

        **参数解释**: 所属Pod名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param pod_name: The pod_name of this ListContainersRequest.
        :type pod_name: str
        """
        self._pod_name = pod_name

    @property
    def image_name(self):
        r"""Gets the image_name of this ListContainersRequest.

        **参数解释**: 镜像名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :return: The image_name of this ListContainersRequest.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        r"""Sets the image_name of this ListContainersRequest.

        **参数解释**: 镜像名称 **约束限制**: 不涉及 **取值范围**: 字符长度0-128位 **默认取值**: 不涉及 

        :param image_name: The image_name of this ListContainersRequest.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def cluster_container(self):
        r"""Gets the cluster_container of this ListContainersRequest.

        **参数解释**: 是否是集群纳管的容器 **约束限制**: 不涉及 **取值范围**:   - true：是集群纳管的容器。   - false：不是集群纳管的容器。 **默认取值**: false 

        :return: The cluster_container of this ListContainersRequest.
        :rtype: bool
        """
        return self._cluster_container

    @cluster_container.setter
    def cluster_container(self, cluster_container):
        r"""Sets the cluster_container of this ListContainersRequest.

        **参数解释**: 是否是集群纳管的容器 **约束限制**: 不涉及 **取值范围**:   - true：是集群纳管的容器。   - false：不是集群纳管的容器。 **默认取值**: false 

        :param cluster_container: The cluster_container of this ListContainersRequest.
        :type cluster_container: bool
        """
        self._cluster_container = cluster_container

    @property
    def limit(self):
        r"""Gets the limit of this ListContainersRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListContainersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListContainersRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListContainersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListContainersRequest.

        **参数解释**: 指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 取值0-2000000 **默认取值**: 0 

        :return: The offset of this ListContainersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListContainersRequest.

        **参数解释**: 指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 取值0-2000000 **默认取值**: 0 

        :param offset: The offset of this ListContainersRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListContainersRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
