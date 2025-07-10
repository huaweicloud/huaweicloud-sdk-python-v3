# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CocUpdateChangeRequestBodyV2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ticket_info': 'CocUpdateChangeRequestBodyV2TicketInfo',
        'sub_tickets': 'list[CocUpdateChangeRequestBodyV2SubTickets]',
        'history_info': 'CocUpdateChangeRequestBodyV2HistoryInfo'
    }

    attribute_map = {
        'ticket_info': 'ticket_info',
        'sub_tickets': 'sub_tickets',
        'history_info': 'history_info'
    }

    def __init__(self, ticket_info=None, sub_tickets=None, history_info=None):
        r"""CocUpdateChangeRequestBodyV2

        The model defined in huaweicloud sdk

        :param ticket_info: 
        :type ticket_info: :class:`huaweicloudsdkcoc.v1.CocUpdateChangeRequestBodyV2TicketInfo`
        :param sub_tickets: 子单信息
        :type sub_tickets: list[:class:`huaweicloudsdkcoc.v1.CocUpdateChangeRequestBodyV2SubTickets`]
        :param history_info: 
        :type history_info: :class:`huaweicloudsdkcoc.v1.CocUpdateChangeRequestBodyV2HistoryInfo`
        """
        
        

        self._ticket_info = None
        self._sub_tickets = None
        self._history_info = None
        self.discriminator = None

        if ticket_info is not None:
            self.ticket_info = ticket_info
        if sub_tickets is not None:
            self.sub_tickets = sub_tickets
        if history_info is not None:
            self.history_info = history_info

    @property
    def ticket_info(self):
        r"""Gets the ticket_info of this CocUpdateChangeRequestBodyV2.

        :return: The ticket_info of this CocUpdateChangeRequestBodyV2.
        :rtype: :class:`huaweicloudsdkcoc.v1.CocUpdateChangeRequestBodyV2TicketInfo`
        """
        return self._ticket_info

    @ticket_info.setter
    def ticket_info(self, ticket_info):
        r"""Sets the ticket_info of this CocUpdateChangeRequestBodyV2.

        :param ticket_info: The ticket_info of this CocUpdateChangeRequestBodyV2.
        :type ticket_info: :class:`huaweicloudsdkcoc.v1.CocUpdateChangeRequestBodyV2TicketInfo`
        """
        self._ticket_info = ticket_info

    @property
    def sub_tickets(self):
        r"""Gets the sub_tickets of this CocUpdateChangeRequestBodyV2.

        子单信息

        :return: The sub_tickets of this CocUpdateChangeRequestBodyV2.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.CocUpdateChangeRequestBodyV2SubTickets`]
        """
        return self._sub_tickets

    @sub_tickets.setter
    def sub_tickets(self, sub_tickets):
        r"""Sets the sub_tickets of this CocUpdateChangeRequestBodyV2.

        子单信息

        :param sub_tickets: The sub_tickets of this CocUpdateChangeRequestBodyV2.
        :type sub_tickets: list[:class:`huaweicloudsdkcoc.v1.CocUpdateChangeRequestBodyV2SubTickets`]
        """
        self._sub_tickets = sub_tickets

    @property
    def history_info(self):
        r"""Gets the history_info of this CocUpdateChangeRequestBodyV2.

        :return: The history_info of this CocUpdateChangeRequestBodyV2.
        :rtype: :class:`huaweicloudsdkcoc.v1.CocUpdateChangeRequestBodyV2HistoryInfo`
        """
        return self._history_info

    @history_info.setter
    def history_info(self, history_info):
        r"""Sets the history_info of this CocUpdateChangeRequestBodyV2.

        :param history_info: The history_info of this CocUpdateChangeRequestBodyV2.
        :type history_info: :class:`huaweicloudsdkcoc.v1.CocUpdateChangeRequestBodyV2HistoryInfo`
        """
        self._history_info = history_info

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
        if not isinstance(other, CocUpdateChangeRequestBodyV2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
