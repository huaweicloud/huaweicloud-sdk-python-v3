# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateClusterPolicyInstanceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'clusterid': 'str',
        'body': 'UCSConstraintRequest'
    }

    attribute_map = {
        'clusterid': 'clusterid',
        'body': 'body'
    }

    def __init__(self, clusterid=None, body=None):
        r"""CreateClusterPolicyInstanceRequest

        The model defined in huaweicloud sdk

        :param clusterid: 集群id
        :type clusterid: str
        :param body: Body of the CreateClusterPolicyInstanceRequest
        :type body: :class:`huaweicloudsdkucs.v1.UCSConstraintRequest`
        """
        
        

        self._clusterid = None
        self._body = None
        self.discriminator = None

        self.clusterid = clusterid
        if body is not None:
            self.body = body

    @property
    def clusterid(self):
        r"""Gets the clusterid of this CreateClusterPolicyInstanceRequest.

        集群id

        :return: The clusterid of this CreateClusterPolicyInstanceRequest.
        :rtype: str
        """
        return self._clusterid

    @clusterid.setter
    def clusterid(self, clusterid):
        r"""Sets the clusterid of this CreateClusterPolicyInstanceRequest.

        集群id

        :param clusterid: The clusterid of this CreateClusterPolicyInstanceRequest.
        :type clusterid: str
        """
        self._clusterid = clusterid

    @property
    def body(self):
        r"""Gets the body of this CreateClusterPolicyInstanceRequest.

        :return: The body of this CreateClusterPolicyInstanceRequest.
        :rtype: :class:`huaweicloudsdkucs.v1.UCSConstraintRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateClusterPolicyInstanceRequest.

        :param body: The body of this CreateClusterPolicyInstanceRequest.
        :type body: :class:`huaweicloudsdkucs.v1.UCSConstraintRequest`
        """
        self._body = body

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
        if not isinstance(other, CreateClusterPolicyInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
