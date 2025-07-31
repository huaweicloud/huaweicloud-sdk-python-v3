# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterItemResponseInfo:

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
        'cluster_ns': 'list[str]',
        'cluster_labels': 'list[str]',
        'protect_status': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'cluster_name': 'cluster_name',
        'cluster_ns': 'cluster_ns',
        'cluster_labels': 'cluster_labels',
        'protect_status': 'protect_status'
    }

    def __init__(self, cluster_id=None, cluster_name=None, cluster_ns=None, cluster_labels=None, protect_status=None):
        r"""ClusterItemResponseInfo

        The model defined in huaweicloud sdk

        :param cluster_id: 集群id
        :type cluster_id: str
        :param cluster_name: 集群名称
        :type cluster_name: str
        :param cluster_ns: 集群命名空间
        :type cluster_ns: list[str]
        :param cluster_labels: 集群标签
        :type cluster_labels: list[str]
        :param protect_status: 集群防护状态 | - \&quot;0\&quot; unprotected - \&quot;1\&quot; plugin error - \&quot;2\&quot; protected with policy - \&quot;3\&quot; deploy policy failed - \&quot;4\&quot; protected without policy - \&quot;5\&quot; uninstall failed - \&quot;6\&quot; uninstall - \&quot;7\&quot; installing
        :type protect_status: str
        """
        
        

        self._cluster_id = None
        self._cluster_name = None
        self._cluster_ns = None
        self._cluster_labels = None
        self._protect_status = None
        self.discriminator = None

        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if cluster_ns is not None:
            self.cluster_ns = cluster_ns
        if cluster_labels is not None:
            self.cluster_labels = cluster_labels
        if protect_status is not None:
            self.protect_status = protect_status

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ClusterItemResponseInfo.

        集群id

        :return: The cluster_id of this ClusterItemResponseInfo.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ClusterItemResponseInfo.

        集群id

        :param cluster_id: The cluster_id of this ClusterItemResponseInfo.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_name(self):
        r"""Gets the cluster_name of this ClusterItemResponseInfo.

        集群名称

        :return: The cluster_name of this ClusterItemResponseInfo.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        r"""Sets the cluster_name of this ClusterItemResponseInfo.

        集群名称

        :param cluster_name: The cluster_name of this ClusterItemResponseInfo.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def cluster_ns(self):
        r"""Gets the cluster_ns of this ClusterItemResponseInfo.

        集群命名空间

        :return: The cluster_ns of this ClusterItemResponseInfo.
        :rtype: list[str]
        """
        return self._cluster_ns

    @cluster_ns.setter
    def cluster_ns(self, cluster_ns):
        r"""Sets the cluster_ns of this ClusterItemResponseInfo.

        集群命名空间

        :param cluster_ns: The cluster_ns of this ClusterItemResponseInfo.
        :type cluster_ns: list[str]
        """
        self._cluster_ns = cluster_ns

    @property
    def cluster_labels(self):
        r"""Gets the cluster_labels of this ClusterItemResponseInfo.

        集群标签

        :return: The cluster_labels of this ClusterItemResponseInfo.
        :rtype: list[str]
        """
        return self._cluster_labels

    @cluster_labels.setter
    def cluster_labels(self, cluster_labels):
        r"""Sets the cluster_labels of this ClusterItemResponseInfo.

        集群标签

        :param cluster_labels: The cluster_labels of this ClusterItemResponseInfo.
        :type cluster_labels: list[str]
        """
        self._cluster_labels = cluster_labels

    @property
    def protect_status(self):
        r"""Gets the protect_status of this ClusterItemResponseInfo.

        集群防护状态 | - \"0\" unprotected - \"1\" plugin error - \"2\" protected with policy - \"3\" deploy policy failed - \"4\" protected without policy - \"5\" uninstall failed - \"6\" uninstall - \"7\" installing

        :return: The protect_status of this ClusterItemResponseInfo.
        :rtype: str
        """
        return self._protect_status

    @protect_status.setter
    def protect_status(self, protect_status):
        r"""Sets the protect_status of this ClusterItemResponseInfo.

        集群防护状态 | - \"0\" unprotected - \"1\" plugin error - \"2\" protected with policy - \"3\" deploy policy failed - \"4\" protected without policy - \"5\" uninstall failed - \"6\" uninstall - \"7\" installing

        :param protect_status: The protect_status of this ClusterItemResponseInfo.
        :type protect_status: str
        """
        self._protect_status = protect_status

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
        if not isinstance(other, ClusterItemResponseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
