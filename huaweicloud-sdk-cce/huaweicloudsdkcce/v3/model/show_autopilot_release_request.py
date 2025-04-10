# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAutopilotReleaseRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'namespace': 'str',
        'cluster_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'namespace': 'namespace',
        'cluster_id': 'cluster_id'
    }

    def __init__(self, name=None, namespace=None, cluster_id=None):
        r"""ShowAutopilotReleaseRequest

        The model defined in huaweicloud sdk

        :param name: 模板实例名称
        :type name: str
        :param namespace: 模板实例所在的命名空间
        :type namespace: str
        :param cluster_id: 集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。
        :type cluster_id: str
        """
        
        

        self._name = None
        self._namespace = None
        self._cluster_id = None
        self.discriminator = None

        self.name = name
        self.namespace = namespace
        self.cluster_id = cluster_id

    @property
    def name(self):
        r"""Gets the name of this ShowAutopilotReleaseRequest.

        模板实例名称

        :return: The name of this ShowAutopilotReleaseRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowAutopilotReleaseRequest.

        模板实例名称

        :param name: The name of this ShowAutopilotReleaseRequest.
        :type name: str
        """
        self._name = name

    @property
    def namespace(self):
        r"""Gets the namespace of this ShowAutopilotReleaseRequest.

        模板实例所在的命名空间

        :return: The namespace of this ShowAutopilotReleaseRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ShowAutopilotReleaseRequest.

        模板实例所在的命名空间

        :param namespace: The namespace of this ShowAutopilotReleaseRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ShowAutopilotReleaseRequest.

        集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :return: The cluster_id of this ShowAutopilotReleaseRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ShowAutopilotReleaseRequest.

        集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :param cluster_id: The cluster_id of this ShowAutopilotReleaseRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

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
        if not isinstance(other, ShowAutopilotReleaseRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
