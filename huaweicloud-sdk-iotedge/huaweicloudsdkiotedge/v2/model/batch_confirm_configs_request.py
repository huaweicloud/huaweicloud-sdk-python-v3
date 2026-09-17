# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchConfirmConfigsRequest:

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
        'ia_id': 'str',
        'action': 'str',
        'body': 'ConfirmIaConfigsRequestBody'
    }

    attribute_map = {
        'node_id': 'node_id',
        'ia_id': 'ia_id',
        'action': 'action',
        'body': 'body'
    }

    def __init__(self, node_id=None, ia_id=None, action=None, body=None):
        r"""BatchConfirmConfigsRequest

        The model defined in huaweicloud sdk

        :param node_id: 边缘节点ID
        :type node_id: str
        :param ia_id: 边侧第三方应用的模块ID
        :type ia_id: str
        :param action: confirm
        :type action: str
        :param body: Body of the BatchConfirmConfigsRequest
        :type body: :class:`huaweicloudsdkiotedge.v2.ConfirmIaConfigsRequestBody`
        """
        
        

        self._node_id = None
        self._ia_id = None
        self._action = None
        self._body = None
        self.discriminator = None

        self.node_id = node_id
        self.ia_id = ia_id
        self.action = action
        if body is not None:
            self.body = body

    @property
    def node_id(self):
        r"""Gets the node_id of this BatchConfirmConfigsRequest.

        边缘节点ID

        :return: The node_id of this BatchConfirmConfigsRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this BatchConfirmConfigsRequest.

        边缘节点ID

        :param node_id: The node_id of this BatchConfirmConfigsRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def ia_id(self):
        r"""Gets the ia_id of this BatchConfirmConfigsRequest.

        边侧第三方应用的模块ID

        :return: The ia_id of this BatchConfirmConfigsRequest.
        :rtype: str
        """
        return self._ia_id

    @ia_id.setter
    def ia_id(self, ia_id):
        r"""Sets the ia_id of this BatchConfirmConfigsRequest.

        边侧第三方应用的模块ID

        :param ia_id: The ia_id of this BatchConfirmConfigsRequest.
        :type ia_id: str
        """
        self._ia_id = ia_id

    @property
    def action(self):
        r"""Gets the action of this BatchConfirmConfigsRequest.

        confirm

        :return: The action of this BatchConfirmConfigsRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this BatchConfirmConfigsRequest.

        confirm

        :param action: The action of this BatchConfirmConfigsRequest.
        :type action: str
        """
        self._action = action

    @property
    def body(self):
        r"""Gets the body of this BatchConfirmConfigsRequest.

        :return: The body of this BatchConfirmConfigsRequest.
        :rtype: :class:`huaweicloudsdkiotedge.v2.ConfirmIaConfigsRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this BatchConfirmConfigsRequest.

        :param body: The body of this BatchConfirmConfigsRequest.
        :type body: :class:`huaweicloudsdkiotedge.v2.ConfirmIaConfigsRequestBody`
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
        if not isinstance(other, BatchConfirmConfigsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
