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
        """ListContainersRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: 企业项目ID，查询所有企业项目时填写：all_granted_eps
        :type enterprise_project_id: str
        :param container_name: 容器名称
        :type container_name: str
        :param pod_name: 所属Pod名称
        :type pod_name: str
        :param image_name: 镜像名称
        :type image_name: str
        :param cluster_container: 是否是集群纳管的容器
        :type cluster_container: bool
        :param limit: 每页显示个数
        :type limit: int
        :param offset: 偏移量：指定返回记录的开始位置
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
        """Gets the enterprise_project_id of this ListContainersRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :return: The enterprise_project_id of this ListContainersRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this ListContainersRequest.

        企业项目ID，查询所有企业项目时填写：all_granted_eps

        :param enterprise_project_id: The enterprise_project_id of this ListContainersRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def container_name(self):
        """Gets the container_name of this ListContainersRequest.

        容器名称

        :return: The container_name of this ListContainersRequest.
        :rtype: str
        """
        return self._container_name

    @container_name.setter
    def container_name(self, container_name):
        """Sets the container_name of this ListContainersRequest.

        容器名称

        :param container_name: The container_name of this ListContainersRequest.
        :type container_name: str
        """
        self._container_name = container_name

    @property
    def pod_name(self):
        """Gets the pod_name of this ListContainersRequest.

        所属Pod名称

        :return: The pod_name of this ListContainersRequest.
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        """Sets the pod_name of this ListContainersRequest.

        所属Pod名称

        :param pod_name: The pod_name of this ListContainersRequest.
        :type pod_name: str
        """
        self._pod_name = pod_name

    @property
    def image_name(self):
        """Gets the image_name of this ListContainersRequest.

        镜像名称

        :return: The image_name of this ListContainersRequest.
        :rtype: str
        """
        return self._image_name

    @image_name.setter
    def image_name(self, image_name):
        """Sets the image_name of this ListContainersRequest.

        镜像名称

        :param image_name: The image_name of this ListContainersRequest.
        :type image_name: str
        """
        self._image_name = image_name

    @property
    def cluster_container(self):
        """Gets the cluster_container of this ListContainersRequest.

        是否是集群纳管的容器

        :return: The cluster_container of this ListContainersRequest.
        :rtype: bool
        """
        return self._cluster_container

    @cluster_container.setter
    def cluster_container(self, cluster_container):
        """Sets the cluster_container of this ListContainersRequest.

        是否是集群纳管的容器

        :param cluster_container: The cluster_container of this ListContainersRequest.
        :type cluster_container: bool
        """
        self._cluster_container = cluster_container

    @property
    def limit(self):
        """Gets the limit of this ListContainersRequest.

        每页显示个数

        :return: The limit of this ListContainersRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListContainersRequest.

        每页显示个数

        :param limit: The limit of this ListContainersRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListContainersRequest.

        偏移量：指定返回记录的开始位置

        :return: The offset of this ListContainersRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListContainersRequest.

        偏移量：指定返回记录的开始位置

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
