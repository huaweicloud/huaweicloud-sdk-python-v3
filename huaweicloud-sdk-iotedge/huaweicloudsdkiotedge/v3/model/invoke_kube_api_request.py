# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InvokeKubeApiRequest:

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
        'x_forward_target': 'str',
        'x_forward_headers': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'x_forward_target': 'X-Forward-Target',
        'x_forward_headers': 'X-Forward-Headers'
    }

    def __init__(self, cluster_id=None, x_forward_target=None, x_forward_headers=None):
        r"""InvokeKubeApiRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 边缘集群ID
        :type cluster_id: str
        :param x_forward_target: 透传的k8s的API，{method} {uri}?{query_param}
        :type x_forward_target: str
        :param x_forward_headers: 透传的API的header
        :type x_forward_headers: str
        """
        
        

        self._cluster_id = None
        self._x_forward_target = None
        self._x_forward_headers = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.x_forward_target = x_forward_target
        self.x_forward_headers = x_forward_headers

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this InvokeKubeApiRequest.

        边缘集群ID

        :return: The cluster_id of this InvokeKubeApiRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this InvokeKubeApiRequest.

        边缘集群ID

        :param cluster_id: The cluster_id of this InvokeKubeApiRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def x_forward_target(self):
        r"""Gets the x_forward_target of this InvokeKubeApiRequest.

        透传的k8s的API，{method} {uri}?{query_param}

        :return: The x_forward_target of this InvokeKubeApiRequest.
        :rtype: str
        """
        return self._x_forward_target

    @x_forward_target.setter
    def x_forward_target(self, x_forward_target):
        r"""Sets the x_forward_target of this InvokeKubeApiRequest.

        透传的k8s的API，{method} {uri}?{query_param}

        :param x_forward_target: The x_forward_target of this InvokeKubeApiRequest.
        :type x_forward_target: str
        """
        self._x_forward_target = x_forward_target

    @property
    def x_forward_headers(self):
        r"""Gets the x_forward_headers of this InvokeKubeApiRequest.

        透传的API的header

        :return: The x_forward_headers of this InvokeKubeApiRequest.
        :rtype: str
        """
        return self._x_forward_headers

    @x_forward_headers.setter
    def x_forward_headers(self, x_forward_headers):
        r"""Sets the x_forward_headers of this InvokeKubeApiRequest.

        透传的API的header

        :param x_forward_headers: The x_forward_headers of this InvokeKubeApiRequest.
        :type x_forward_headers: str
        """
        self._x_forward_headers = x_forward_headers

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, InvokeKubeApiRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
