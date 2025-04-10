# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Operation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'operation_id': 'str',
        'operation_action': 'str',
        'dependent_actions': 'list[str]'
    }

    attribute_map = {
        'operation_id': 'operation_id',
        'operation_action': 'operation_action',
        'dependent_actions': 'dependent_actions'
    }

    def __init__(self, operation_id=None, operation_action=None, dependent_actions=None):
        r"""Operation

        The model defined in huaweicloud sdk

        :param operation_id: OpenAPI的操作标识符。
        :type operation_id: str
        :param operation_action: 三段式的授权项名称，例如\&quot;iam:policies:createV5\&quot;。
        :type operation_action: str
        :param dependent_actions: 该操作可能需要的其他授权项授权。
        :type dependent_actions: list[str]
        """
        
        

        self._operation_id = None
        self._operation_action = None
        self._dependent_actions = None
        self.discriminator = None

        self.operation_id = operation_id
        self.operation_action = operation_action
        if dependent_actions is not None:
            self.dependent_actions = dependent_actions

    @property
    def operation_id(self):
        r"""Gets the operation_id of this Operation.

        OpenAPI的操作标识符。

        :return: The operation_id of this Operation.
        :rtype: str
        """
        return self._operation_id

    @operation_id.setter
    def operation_id(self, operation_id):
        r"""Sets the operation_id of this Operation.

        OpenAPI的操作标识符。

        :param operation_id: The operation_id of this Operation.
        :type operation_id: str
        """
        self._operation_id = operation_id

    @property
    def operation_action(self):
        r"""Gets the operation_action of this Operation.

        三段式的授权项名称，例如\"iam:policies:createV5\"。

        :return: The operation_action of this Operation.
        :rtype: str
        """
        return self._operation_action

    @operation_action.setter
    def operation_action(self, operation_action):
        r"""Sets the operation_action of this Operation.

        三段式的授权项名称，例如\"iam:policies:createV5\"。

        :param operation_action: The operation_action of this Operation.
        :type operation_action: str
        """
        self._operation_action = operation_action

    @property
    def dependent_actions(self):
        r"""Gets the dependent_actions of this Operation.

        该操作可能需要的其他授权项授权。

        :return: The dependent_actions of this Operation.
        :rtype: list[str]
        """
        return self._dependent_actions

    @dependent_actions.setter
    def dependent_actions(self, dependent_actions):
        r"""Sets the dependent_actions of this Operation.

        该操作可能需要的其他授权项授权。

        :param dependent_actions: The dependent_actions of this Operation.
        :type dependent_actions: list[str]
        """
        self._dependent_actions = dependent_actions

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
        if not isinstance(other, Operation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
