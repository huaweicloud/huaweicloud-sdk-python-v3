# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTicketInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ticket_type': 'str',
        'ticket_id': 'str'
    }

    attribute_map = {
        'ticket_type': 'ticket_type',
        'ticket_id': 'ticket_id'
    }

    def __init__(self, ticket_type=None, ticket_id=None):
        r"""ShowTicketInfoRequest

        The model defined in huaweicloud sdk

        :param ticket_type: 工单类型
        :type ticket_type: str
        :param ticket_id: ID of Ticket
        :type ticket_id: str
        """
        
        

        self._ticket_type = None
        self._ticket_id = None
        self.discriminator = None

        self.ticket_type = ticket_type
        self.ticket_id = ticket_id

    @property
    def ticket_type(self):
        r"""Gets the ticket_type of this ShowTicketInfoRequest.

        工单类型

        :return: The ticket_type of this ShowTicketInfoRequest.
        :rtype: str
        """
        return self._ticket_type

    @ticket_type.setter
    def ticket_type(self, ticket_type):
        r"""Sets the ticket_type of this ShowTicketInfoRequest.

        工单类型

        :param ticket_type: The ticket_type of this ShowTicketInfoRequest.
        :type ticket_type: str
        """
        self._ticket_type = ticket_type

    @property
    def ticket_id(self):
        r"""Gets the ticket_id of this ShowTicketInfoRequest.

        ID of Ticket

        :return: The ticket_id of this ShowTicketInfoRequest.
        :rtype: str
        """
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, ticket_id):
        r"""Sets the ticket_id of this ShowTicketInfoRequest.

        ID of Ticket

        :param ticket_id: The ticket_id of this ShowTicketInfoRequest.
        :type ticket_id: str
        """
        self._ticket_id = ticket_id

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
        if not isinstance(other, ShowTicketInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
