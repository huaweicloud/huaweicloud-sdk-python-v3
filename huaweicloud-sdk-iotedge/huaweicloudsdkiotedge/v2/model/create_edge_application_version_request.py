# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEdgeApplicationVersionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'edge_app_id': 'str',
        'body': 'CreateEdgeApplicationVersionDTO'
    }

    attribute_map = {
        'edge_app_id': 'edge_app_id',
        'body': 'body'
    }

    def __init__(self, edge_app_id=None, body=None):
        """CreateEdgeApplicationVersionRequest

        The model defined in huaweicloud sdk

        :param edge_app_id: 应用ID，应用唯一。
        :type edge_app_id: str
        :param body: Body of the CreateEdgeApplicationVersionRequest
        :type body: :class:`huaweicloudsdkiotedge.v2.CreateEdgeApplicationVersionDTO`
        """
        
        

        self._edge_app_id = None
        self._body = None
        self.discriminator = None

        self.edge_app_id = edge_app_id
        if body is not None:
            self.body = body

    @property
    def edge_app_id(self):
        """Gets the edge_app_id of this CreateEdgeApplicationVersionRequest.

        应用ID，应用唯一。

        :return: The edge_app_id of this CreateEdgeApplicationVersionRequest.
        :rtype: str
        """
        return self._edge_app_id

    @edge_app_id.setter
    def edge_app_id(self, edge_app_id):
        """Sets the edge_app_id of this CreateEdgeApplicationVersionRequest.

        应用ID，应用唯一。

        :param edge_app_id: The edge_app_id of this CreateEdgeApplicationVersionRequest.
        :type edge_app_id: str
        """
        self._edge_app_id = edge_app_id

    @property
    def body(self):
        """Gets the body of this CreateEdgeApplicationVersionRequest.

        :return: The body of this CreateEdgeApplicationVersionRequest.
        :rtype: :class:`huaweicloudsdkiotedge.v2.CreateEdgeApplicationVersionDTO`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this CreateEdgeApplicationVersionRequest.

        :param body: The body of this CreateEdgeApplicationVersionRequest.
        :type body: :class:`huaweicloudsdkiotedge.v2.CreateEdgeApplicationVersionDTO`
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
        if not isinstance(other, CreateEdgeApplicationVersionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
