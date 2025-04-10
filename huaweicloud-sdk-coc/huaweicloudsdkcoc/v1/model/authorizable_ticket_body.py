# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuthorizableTicketBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'scope_id': 'str',
        'target_id': 'str'
    }

    attribute_map = {
        'type': 'type',
        'scope_id': 'scope_id',
        'target_id': 'target_id'
    }

    def __init__(self, type=None, scope_id=None, target_id=None):
        r"""AuthorizableTicketBody

        The model defined in huaweicloud sdk

        :param type: 可授权单类型
        :type type: str
        :param scope_id: scope ID，一般为region id
        :type scope_id: str
        :param target_id: 目标 ID，一般为应用id
        :type target_id: str
        """
        
        

        self._type = None
        self._scope_id = None
        self._target_id = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if scope_id is not None:
            self.scope_id = scope_id
        if target_id is not None:
            self.target_id = target_id

    @property
    def type(self):
        r"""Gets the type of this AuthorizableTicketBody.

        可授权单类型

        :return: The type of this AuthorizableTicketBody.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AuthorizableTicketBody.

        可授权单类型

        :param type: The type of this AuthorizableTicketBody.
        :type type: str
        """
        self._type = type

    @property
    def scope_id(self):
        r"""Gets the scope_id of this AuthorizableTicketBody.

        scope ID，一般为region id

        :return: The scope_id of this AuthorizableTicketBody.
        :rtype: str
        """
        return self._scope_id

    @scope_id.setter
    def scope_id(self, scope_id):
        r"""Sets the scope_id of this AuthorizableTicketBody.

        scope ID，一般为region id

        :param scope_id: The scope_id of this AuthorizableTicketBody.
        :type scope_id: str
        """
        self._scope_id = scope_id

    @property
    def target_id(self):
        r"""Gets the target_id of this AuthorizableTicketBody.

        目标 ID，一般为应用id

        :return: The target_id of this AuthorizableTicketBody.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        r"""Sets the target_id of this AuthorizableTicketBody.

        目标 ID，一般为应用id

        :param target_id: The target_id of this AuthorizableTicketBody.
        :type target_id: str
        """
        self._target_id = target_id

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
        if not isinstance(other, AuthorizableTicketBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
