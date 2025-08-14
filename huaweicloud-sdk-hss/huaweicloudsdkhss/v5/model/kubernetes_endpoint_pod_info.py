# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KubernetesEndpointPodInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'endpoint_id': 'str',
        'pod_ip': 'str',
        'pod_name': 'str',
        'available': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'endpoint_id': 'endpoint_id',
        'pod_ip': 'pod_ip',
        'pod_name': 'pod_name',
        'available': 'available'
    }

    def __init__(self, id=None, endpoint_id=None, pod_ip=None, pod_name=None, available=None):
        r"""KubernetesEndpointPodInfo

        The model defined in huaweicloud sdk

        :param id: ID
        :type id: str
        :param endpoint_id: 关联端点ID
        :type endpoint_id: str
        :param pod_ip: pod IP
        :type pod_ip: str
        :param pod_name: Pod名称
        :type pod_name: str
        :param available: 是否可用
        :type available: bool
        """
        
        

        self._id = None
        self._endpoint_id = None
        self._pod_ip = None
        self._pod_name = None
        self._available = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if endpoint_id is not None:
            self.endpoint_id = endpoint_id
        if pod_ip is not None:
            self.pod_ip = pod_ip
        if pod_name is not None:
            self.pod_name = pod_name
        if available is not None:
            self.available = available

    @property
    def id(self):
        r"""Gets the id of this KubernetesEndpointPodInfo.

        ID

        :return: The id of this KubernetesEndpointPodInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this KubernetesEndpointPodInfo.

        ID

        :param id: The id of this KubernetesEndpointPodInfo.
        :type id: str
        """
        self._id = id

    @property
    def endpoint_id(self):
        r"""Gets the endpoint_id of this KubernetesEndpointPodInfo.

        关联端点ID

        :return: The endpoint_id of this KubernetesEndpointPodInfo.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        r"""Sets the endpoint_id of this KubernetesEndpointPodInfo.

        关联端点ID

        :param endpoint_id: The endpoint_id of this KubernetesEndpointPodInfo.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

    @property
    def pod_ip(self):
        r"""Gets the pod_ip of this KubernetesEndpointPodInfo.

        pod IP

        :return: The pod_ip of this KubernetesEndpointPodInfo.
        :rtype: str
        """
        return self._pod_ip

    @pod_ip.setter
    def pod_ip(self, pod_ip):
        r"""Sets the pod_ip of this KubernetesEndpointPodInfo.

        pod IP

        :param pod_ip: The pod_ip of this KubernetesEndpointPodInfo.
        :type pod_ip: str
        """
        self._pod_ip = pod_ip

    @property
    def pod_name(self):
        r"""Gets the pod_name of this KubernetesEndpointPodInfo.

        Pod名称

        :return: The pod_name of this KubernetesEndpointPodInfo.
        :rtype: str
        """
        return self._pod_name

    @pod_name.setter
    def pod_name(self, pod_name):
        r"""Sets the pod_name of this KubernetesEndpointPodInfo.

        Pod名称

        :param pod_name: The pod_name of this KubernetesEndpointPodInfo.
        :type pod_name: str
        """
        self._pod_name = pod_name

    @property
    def available(self):
        r"""Gets the available of this KubernetesEndpointPodInfo.

        是否可用

        :return: The available of this KubernetesEndpointPodInfo.
        :rtype: bool
        """
        return self._available

    @available.setter
    def available(self, available):
        r"""Sets the available of this KubernetesEndpointPodInfo.

        是否可用

        :param available: The available of this KubernetesEndpointPodInfo.
        :type available: bool
        """
        self._available = available

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
        if not isinstance(other, KubernetesEndpointPodInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
