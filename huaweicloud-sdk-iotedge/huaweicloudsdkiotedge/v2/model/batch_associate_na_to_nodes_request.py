# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchAssociateNaToNodesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'na_id': 'str',
        'action': 'str',
        'body': 'AuthorizeNa2NodesRequestDTO'
    }

    attribute_map = {
        'na_id': 'na_id',
        'action': 'action',
        'body': 'body'
    }

    def __init__(self, na_id=None, action=None, body=None):
        """BatchAssociateNaToNodesRequest

        The model defined in huaweicloud sdk

        :param na_id: 北向数据接收端点ID
        :type na_id: str
        :param action: 批量删除delete，批量添加add
        :type action: str
        :param body: Body of the BatchAssociateNaToNodesRequest
        :type body: :class:`huaweicloudsdkiotedge.v2.AuthorizeNa2NodesRequestDTO`
        """
        
        

        self._na_id = None
        self._action = None
        self._body = None
        self.discriminator = None

        self.na_id = na_id
        self.action = action
        if body is not None:
            self.body = body

    @property
    def na_id(self):
        """Gets the na_id of this BatchAssociateNaToNodesRequest.

        北向数据接收端点ID

        :return: The na_id of this BatchAssociateNaToNodesRequest.
        :rtype: str
        """
        return self._na_id

    @na_id.setter
    def na_id(self, na_id):
        """Sets the na_id of this BatchAssociateNaToNodesRequest.

        北向数据接收端点ID

        :param na_id: The na_id of this BatchAssociateNaToNodesRequest.
        :type na_id: str
        """
        self._na_id = na_id

    @property
    def action(self):
        """Gets the action of this BatchAssociateNaToNodesRequest.

        批量删除delete，批量添加add

        :return: The action of this BatchAssociateNaToNodesRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this BatchAssociateNaToNodesRequest.

        批量删除delete，批量添加add

        :param action: The action of this BatchAssociateNaToNodesRequest.
        :type action: str
        """
        self._action = action

    @property
    def body(self):
        """Gets the body of this BatchAssociateNaToNodesRequest.

        :return: The body of this BatchAssociateNaToNodesRequest.
        :rtype: :class:`huaweicloudsdkiotedge.v2.AuthorizeNa2NodesRequestDTO`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this BatchAssociateNaToNodesRequest.

        :param body: The body of this BatchAssociateNaToNodesRequest.
        :type body: :class:`huaweicloudsdkiotedge.v2.AuthorizeNa2NodesRequestDTO`
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
        if not isinstance(other, BatchAssociateNaToNodesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
