# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListReleasesRequest:

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
        'chart_id': 'str',
        'namespace': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'chart_id': 'chart_id',
        'namespace': 'namespace'
    }

    def __init__(self, cluster_id=None, chart_id=None, namespace=None):
        """ListReleasesRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。
        :type cluster_id: str
        :param chart_id: 模板ID
        :type chart_id: str
        :param namespace: 模板对应的命名空间
        :type namespace: str
        """
        
        

        self._cluster_id = None
        self._chart_id = None
        self._namespace = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if chart_id is not None:
            self.chart_id = chart_id
        if namespace is not None:
            self.namespace = namespace

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ListReleasesRequest.

        集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :return: The cluster_id of this ListReleasesRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ListReleasesRequest.

        集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :param cluster_id: The cluster_id of this ListReleasesRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def chart_id(self):
        """Gets the chart_id of this ListReleasesRequest.

        模板ID

        :return: The chart_id of this ListReleasesRequest.
        :rtype: str
        """
        return self._chart_id

    @chart_id.setter
    def chart_id(self, chart_id):
        """Sets the chart_id of this ListReleasesRequest.

        模板ID

        :param chart_id: The chart_id of this ListReleasesRequest.
        :type chart_id: str
        """
        self._chart_id = chart_id

    @property
    def namespace(self):
        """Gets the namespace of this ListReleasesRequest.

        模板对应的命名空间

        :return: The namespace of this ListReleasesRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ListReleasesRequest.

        模板对应的命名空间

        :param namespace: The namespace of this ListReleasesRequest.
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
        if not isinstance(other, ListReleasesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
