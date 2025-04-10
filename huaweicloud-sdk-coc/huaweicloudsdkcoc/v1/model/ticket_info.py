# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TicketInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ticket_id': 'str',
        'ticket_type': 'str',
        'target_id': 'str',
        'scope_id': 'str'
    }

    attribute_map = {
        'ticket_id': 'ticket_id',
        'ticket_type': 'ticket_type',
        'target_id': 'target_id',
        'scope_id': 'scope_id'
    }

    def __init__(self, ticket_id=None, ticket_type=None, target_id=None, scope_id=None):
        r"""TicketInfo

        The model defined in huaweicloud sdk

        :param ticket_id: 四号单id
        :type ticket_id: str
        :param ticket_type: 四号单类型，可选CHANGE/INCIDENT/ALARM/WARROOM
        :type ticket_type: str
        :param target_id: 四号单关联的应用id
        :type target_id: str
        :param scope_id: region id
        :type scope_id: str
        """
        
        

        self._ticket_id = None
        self._ticket_type = None
        self._target_id = None
        self._scope_id = None
        self.discriminator = None

        if ticket_id is not None:
            self.ticket_id = ticket_id
        if ticket_type is not None:
            self.ticket_type = ticket_type
        if target_id is not None:
            self.target_id = target_id
        if scope_id is not None:
            self.scope_id = scope_id

    @property
    def ticket_id(self):
        r"""Gets the ticket_id of this TicketInfo.

        四号单id

        :return: The ticket_id of this TicketInfo.
        :rtype: str
        """
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, ticket_id):
        r"""Sets the ticket_id of this TicketInfo.

        四号单id

        :param ticket_id: The ticket_id of this TicketInfo.
        :type ticket_id: str
        """
        self._ticket_id = ticket_id

    @property
    def ticket_type(self):
        r"""Gets the ticket_type of this TicketInfo.

        四号单类型，可选CHANGE/INCIDENT/ALARM/WARROOM

        :return: The ticket_type of this TicketInfo.
        :rtype: str
        """
        return self._ticket_type

    @ticket_type.setter
    def ticket_type(self, ticket_type):
        r"""Sets the ticket_type of this TicketInfo.

        四号单类型，可选CHANGE/INCIDENT/ALARM/WARROOM

        :param ticket_type: The ticket_type of this TicketInfo.
        :type ticket_type: str
        """
        self._ticket_type = ticket_type

    @property
    def target_id(self):
        r"""Gets the target_id of this TicketInfo.

        四号单关联的应用id

        :return: The target_id of this TicketInfo.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        r"""Sets the target_id of this TicketInfo.

        四号单关联的应用id

        :param target_id: The target_id of this TicketInfo.
        :type target_id: str
        """
        self._target_id = target_id

    @property
    def scope_id(self):
        r"""Gets the scope_id of this TicketInfo.

        region id

        :return: The scope_id of this TicketInfo.
        :rtype: str
        """
        return self._scope_id

    @scope_id.setter
    def scope_id(self, scope_id):
        r"""Sets the scope_id of this TicketInfo.

        region id

        :param scope_id: The scope_id of this TicketInfo.
        :type scope_id: str
        """
        self._scope_id = scope_id

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
        if not isinstance(other, TicketInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
