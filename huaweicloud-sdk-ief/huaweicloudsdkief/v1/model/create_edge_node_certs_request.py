# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEdgeNodeCertsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'ief_instance_id': 'str',
        'body': 'Cert'
    }

    attribute_map = {
        'node_id': 'node_id',
        'ief_instance_id': 'ief-instance-id',
        'body': 'body'
    }

    def __init__(self, node_id=None, ief_instance_id=None, body=None):
        r"""CreateEdgeNodeCertsRequest

        The model defined in huaweicloud sdk

        :param node_id: 边缘节点ID
        :type node_id: str
        :param ief_instance_id: 铂金版实例ID，专业版实例为空值
        :type ief_instance_id: str
        :param body: Body of the CreateEdgeNodeCertsRequest
        :type body: :class:`huaweicloudsdkief.v1.Cert`
        """
        
        

        self._node_id = None
        self._ief_instance_id = None
        self._body = None
        self.discriminator = None

        self.node_id = node_id
        if ief_instance_id is not None:
            self.ief_instance_id = ief_instance_id
        if body is not None:
            self.body = body

    @property
    def node_id(self):
        r"""Gets the node_id of this CreateEdgeNodeCertsRequest.

        边缘节点ID

        :return: The node_id of this CreateEdgeNodeCertsRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this CreateEdgeNodeCertsRequest.

        边缘节点ID

        :param node_id: The node_id of this CreateEdgeNodeCertsRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def ief_instance_id(self):
        r"""Gets the ief_instance_id of this CreateEdgeNodeCertsRequest.

        铂金版实例ID，专业版实例为空值

        :return: The ief_instance_id of this CreateEdgeNodeCertsRequest.
        :rtype: str
        """
        return self._ief_instance_id

    @ief_instance_id.setter
    def ief_instance_id(self, ief_instance_id):
        r"""Sets the ief_instance_id of this CreateEdgeNodeCertsRequest.

        铂金版实例ID，专业版实例为空值

        :param ief_instance_id: The ief_instance_id of this CreateEdgeNodeCertsRequest.
        :type ief_instance_id: str
        """
        self._ief_instance_id = ief_instance_id

    @property
    def body(self):
        r"""Gets the body of this CreateEdgeNodeCertsRequest.

        :return: The body of this CreateEdgeNodeCertsRequest.
        :rtype: :class:`huaweicloudsdkief.v1.Cert`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateEdgeNodeCertsRequest.

        :param body: The body of this CreateEdgeNodeCertsRequest.
        :type body: :class:`huaweicloudsdkief.v1.Cert`
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
        if not isinstance(other, CreateEdgeNodeCertsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
