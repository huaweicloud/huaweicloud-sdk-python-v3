# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyProtectScope:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_name': 'str',
        'cluster_id': 'str',
        'images': 'list[str]',
        'namespaces': 'list[str]',
        'labels': 'list[str]'
    }

    attribute_map = {
        'cluster_name': 'cluster_name',
        'cluster_id': 'cluster_id',
        'images': 'images',
        'namespaces': 'namespaces',
        'labels': 'labels'
    }

    def __init__(self, cluster_name=None, cluster_id=None, images=None, namespaces=None, labels=None):
        r"""PolicyProtectScope

        The model defined in huaweicloud sdk

        :param cluster_name: 集群名称
        :type cluster_name: str
        :param cluster_id: 集群id
        :type cluster_id: str
        :param images: 防护镜像
        :type images: list[str]
        :param namespaces: 防护namespace
        :type namespaces: list[str]
        :param labels: 防护labels
        :type labels: list[str]
        """
        
        

        self._cluster_name = None
        self._cluster_id = None
        self._images = None
        self._namespaces = None
        self._labels = None
        self.discriminator = None

        self.cluster_name = cluster_name
        self.cluster_id = cluster_id
        self.images = images
        self.namespaces = namespaces
        self.labels = labels

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this PolicyProtectScope.

        集群名称

        :return: The cluster_name of this PolicyProtectScope.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this PolicyProtectScope.

        集群名称

        :param cluster_name: The cluster_name of this PolicyProtectScope.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this PolicyProtectScope.

        集群id

        :return: The cluster_id of this PolicyProtectScope.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this PolicyProtectScope.

        集群id

        :param cluster_id: The cluster_id of this PolicyProtectScope.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def images(self):
        r"""Gets the images of this PolicyProtectScope.

        防护镜像

        :return: The images of this PolicyProtectScope.
        :rtype: list[str]
        """
        return self._images

    @images.setter
    def images(self, images):
        r"""Sets the images of this PolicyProtectScope.

        防护镜像

        :param images: The images of this PolicyProtectScope.
        :type images: list[str]
        """
        self._images = images

    @property
    def namespaces(self):
        r"""Gets the namespaces of this PolicyProtectScope.

        防护namespace

        :return: The namespaces of this PolicyProtectScope.
        :rtype: list[str]
        """
        return self._namespaces

    @namespaces.setter
    def namespaces(self, namespaces):
        r"""Sets the namespaces of this PolicyProtectScope.

        防护namespace

        :param namespaces: The namespaces of this PolicyProtectScope.
        :type namespaces: list[str]
        """
        self._namespaces = namespaces

    @property
    def labels(self):
        r"""Gets the labels of this PolicyProtectScope.

        防护labels

        :return: The labels of this PolicyProtectScope.
        :rtype: list[str]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this PolicyProtectScope.

        防护labels

        :param labels: The labels of this PolicyProtectScope.
        :type labels: list[str]
        """
        self._labels = labels

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
        if not isinstance(other, PolicyProtectScope):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
