# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeResult:

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
        'error_message': 'str',
        'error_code': 'str'
    }

    attribute_map = {
        'node_id': 'node_id',
        'error_message': 'error_message',
        'error_code': 'error_code'
    }

    def __init__(self, node_id=None, error_message=None, error_code=None):
        r"""NodeResult

        The model defined in huaweicloud sdk

        :param node_id: 部署的节点ID
        :type node_id: str
        :param error_message: 部署到该节点失败时，返回的错误信息
        :type error_message: str
        :param error_code: 部署到该节点失败时，返回的错误码
        :type error_code: str
        """
        
        

        self._node_id = None
        self._error_message = None
        self._error_code = None
        self.discriminator = None

        self.node_id = node_id
        if error_message is not None:
            self.error_message = error_message
        if error_code is not None:
            self.error_code = error_code

    @property
    def node_id(self):
        r"""Gets the node_id of this NodeResult.

        部署的节点ID

        :return: The node_id of this NodeResult.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this NodeResult.

        部署的节点ID

        :param node_id: The node_id of this NodeResult.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def error_message(self):
        r"""Gets the error_message of this NodeResult.

        部署到该节点失败时，返回的错误信息

        :return: The error_message of this NodeResult.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this NodeResult.

        部署到该节点失败时，返回的错误信息

        :param error_message: The error_message of this NodeResult.
        :type error_message: str
        """
        self._error_message = error_message

    @property
    def error_code(self):
        r"""Gets the error_code of this NodeResult.

        部署到该节点失败时，返回的错误码

        :return: The error_code of this NodeResult.
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        r"""Sets the error_code of this NodeResult.

        部署到该节点失败时，返回的错误码

        :param error_code: The error_code of this NodeResult.
        :type error_code: str
        """
        self._error_code = error_code

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
        if not isinstance(other, NodeResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
