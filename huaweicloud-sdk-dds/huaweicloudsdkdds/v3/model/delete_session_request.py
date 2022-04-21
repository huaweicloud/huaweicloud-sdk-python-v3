# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteSessionRequest:

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
        'body': 'DeleteSessionRequestBody'
    }

    attribute_map = {
        'node_id': 'node_id',
        'body': 'body'
    }

    def __init__(self, node_id=None, body=None):
        """DeleteSessionRequest

        The model defined in huaweicloud sdk

        :param node_id: 节点ID。允许查询的节点如下： 集群下面的 mongos节点以及 副本集、单节点实例下面的所有节点。
        :type node_id: str
        :param body: Body of the DeleteSessionRequest
        :type body: :class:`huaweicloudsdkdds.v3.DeleteSessionRequestBody`
        """
        
        

        self._node_id = None
        self._body = None
        self.discriminator = None

        self.node_id = node_id
        if body is not None:
            self.body = body

    @property
    def node_id(self):
        """Gets the node_id of this DeleteSessionRequest.

        节点ID。允许查询的节点如下： 集群下面的 mongos节点以及 副本集、单节点实例下面的所有节点。

        :return: The node_id of this DeleteSessionRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this DeleteSessionRequest.

        节点ID。允许查询的节点如下： 集群下面的 mongos节点以及 副本集、单节点实例下面的所有节点。

        :param node_id: The node_id of this DeleteSessionRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def body(self):
        """Gets the body of this DeleteSessionRequest.


        :return: The body of this DeleteSessionRequest.
        :rtype: :class:`huaweicloudsdkdds.v3.DeleteSessionRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this DeleteSessionRequest.


        :param body: The body of this DeleteSessionRequest.
        :type body: :class:`huaweicloudsdkdds.v3.DeleteSessionRequestBody`
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
        if not isinstance(other, DeleteSessionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
