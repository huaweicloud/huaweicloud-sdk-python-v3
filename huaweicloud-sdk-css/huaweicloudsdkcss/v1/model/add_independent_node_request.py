# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddIndependentNodeRequest:

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
        'type': 'str',
        'body': 'IndependentReq'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'type': 'type',
        'body': 'body'
    }

    def __init__(self, cluster_id=None, type=None, body=None):
        r"""AddIndependentNodeRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 指定需要独立master或client的集群ID。
        :type cluster_id: str
        :param type: 指定待新增独立节点类型。 - ess-master：Master节点。 - ess-client：Client节点。
        :type type: str
        :param body: Body of the AddIndependentNodeRequest
        :type body: :class:`huaweicloudsdkcss.v1.IndependentReq`
        """
        
        

        self._cluster_id = None
        self._type = None
        self._body = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.type = type
        if body is not None:
            self.body = body

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this AddIndependentNodeRequest.

        指定需要独立master或client的集群ID。

        :return: The cluster_id of this AddIndependentNodeRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this AddIndependentNodeRequest.

        指定需要独立master或client的集群ID。

        :param cluster_id: The cluster_id of this AddIndependentNodeRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def type(self):
        r"""Gets the type of this AddIndependentNodeRequest.

        指定待新增独立节点类型。 - ess-master：Master节点。 - ess-client：Client节点。

        :return: The type of this AddIndependentNodeRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AddIndependentNodeRequest.

        指定待新增独立节点类型。 - ess-master：Master节点。 - ess-client：Client节点。

        :param type: The type of this AddIndependentNodeRequest.
        :type type: str
        """
        self._type = type

    @property
    def body(self):
        r"""Gets the body of this AddIndependentNodeRequest.

        :return: The body of this AddIndependentNodeRequest.
        :rtype: :class:`huaweicloudsdkcss.v1.IndependentReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this AddIndependentNodeRequest.

        :param body: The body of this AddIndependentNodeRequest.
        :type body: :class:`huaweicloudsdkcss.v1.IndependentReq`
        """
        self._body = body

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
        if not isinstance(other, AddIndependentNodeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
