# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Resources:

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
        'cluster_name': 'str',
        'images': 'str',
        'labels': 'str',
        'namespace': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'images': 'images',
        'labels': 'labels',
        'namespace': 'namespace'
    }

    def __init__(self, cluster_id=None, cluster_name=None, images=None, labels=None, namespace=None):
        r"""Resources

        The model defined in huaweicloud sdk

        :param cluster_id: 集群id
        :type cluster_id: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param images: 镜像
        :type images: str
        :param labels: 标签
        :type labels: str
        :param namespace: 命名空间
        :type namespace: str
        """
        
        

        self._cluster_id = None
        self._cluster_name = None
        self._images = None
        self._labels = None
        self._namespace = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if images is not None:
            self.images = images
        if labels is not None:
            self.labels = labels
        if namespace is not None:
            self.namespace = namespace

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this Resources.

        集群id

        :return: The cluster_id of this Resources.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this Resources.

        集群id

        :param cluster_id: The cluster_id of this Resources.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this Resources.

        集群名称

        :return: The cluster_name of this Resources.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this Resources.

        集群名称

        :param cluster_name: The cluster_name of this Resources.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def images(self):
        r"""Gets the images of this Resources.

        镜像

        :return: The images of this Resources.
        :rtype: str
        """
        return self._images

    @images.setter
    def images(self, images):
        r"""Sets the images of this Resources.

        镜像

        :param images: The images of this Resources.
        :type images: str
        """
        self._images = images

    @property
    def labels(self):
        r"""Gets the labels of this Resources.

        标签

        :return: The labels of this Resources.
        :rtype: str
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this Resources.

        标签

        :param labels: The labels of this Resources.
        :type labels: str
        """
        self._labels = labels

    @property
    def namespace(self):
        r"""Gets the namespace of this Resources.

        命名空间

        :return: The namespace of this Resources.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this Resources.

        命名空间

        :param namespace: The namespace of this Resources.
        :type namespace: str
        """
        self._namespace = namespace

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
        if not isinstance(other, Resources):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
