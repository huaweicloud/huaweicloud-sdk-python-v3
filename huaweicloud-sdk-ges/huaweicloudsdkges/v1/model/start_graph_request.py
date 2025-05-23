# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StartGraphRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'graph_id': 'str',
        'action_id': 'str',
        'body': 'StartGraphReq'
    }

    attribute_map = {
        'graph_id': 'graph_id',
        'action_id': 'action_id',
        'body': 'body'
    }

    def __init__(self, graph_id=None, action_id=None, body=None):
        r"""StartGraphRequest

        The model defined in huaweicloud sdk

        :param graph_id: 图ID。
        :type graph_id: str
        :param action_id: 图actionId
        :type action_id: str
        :param body: Body of the StartGraphRequest
        :type body: :class:`huaweicloudsdkges.v1.StartGraphReq`
        """
        
        

        self._graph_id = None
        self._action_id = None
        self._body = None
        self.discriminator = None

        self.graph_id = graph_id
        self.action_id = action_id
        if body is not None:
            self.body = body

    @property
    def graph_id(self):
        r"""Gets the graph_id of this StartGraphRequest.

        图ID。

        :return: The graph_id of this StartGraphRequest.
        :rtype: str
        """
        return self._graph_id

    @graph_id.setter
    def graph_id(self, graph_id):
        r"""Sets the graph_id of this StartGraphRequest.

        图ID。

        :param graph_id: The graph_id of this StartGraphRequest.
        :type graph_id: str
        """
        self._graph_id = graph_id

    @property
    def action_id(self):
        r"""Gets the action_id of this StartGraphRequest.

        图actionId

        :return: The action_id of this StartGraphRequest.
        :rtype: str
        """
        return self._action_id

    @action_id.setter
    def action_id(self, action_id):
        r"""Sets the action_id of this StartGraphRequest.

        图actionId

        :param action_id: The action_id of this StartGraphRequest.
        :type action_id: str
        """
        self._action_id = action_id

    @property
    def body(self):
        r"""Gets the body of this StartGraphRequest.

        :return: The body of this StartGraphRequest.
        :rtype: :class:`huaweicloudsdkges.v1.StartGraphReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this StartGraphRequest.

        :param body: The body of this StartGraphRequest.
        :type body: :class:`huaweicloudsdkges.v1.StartGraphReq`
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
        if not isinstance(other, StartGraphRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
