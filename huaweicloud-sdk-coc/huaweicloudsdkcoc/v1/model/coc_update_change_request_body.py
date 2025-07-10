# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CocUpdateChangeRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ticket_info': 'CocUpdateChangeRequestBodyTicketInfo',
        'sub_tickets': 'list[CocUpdateChangeRequestBodySubTickets]',
        'history_info': 'CocUpdateChangeRequestBodyHistoryInfo'
    }

    attribute_map = {
        'ticket_info': 'ticket_info',
        'sub_tickets': 'sub_tickets',
        'history_info': 'history_info'
    }

    def __init__(self, ticket_info=None, sub_tickets=None, history_info=None):
        r"""CocUpdateChangeRequestBody

        The model defined in huaweicloud sdk

        :param ticket_info: 
        :type ticket_info: :class:`huaweicloudsdkcoc.v1.CocUpdateChangeRequestBodyTicketInfo`
        :param sub_tickets: 变更子单信息。
        :type sub_tickets: list[:class:`huaweicloudsdkcoc.v1.CocUpdateChangeRequestBodySubTickets`]
        :param history_info: 
        :type history_info: :class:`huaweicloudsdkcoc.v1.CocUpdateChangeRequestBodyHistoryInfo`
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
        r"""Gets the ticket_info of this CocUpdateChangeRequestBody.

        :return: The ticket_info of this CocUpdateChangeRequestBody.
        :rtype: :class:`huaweicloudsdkcoc.v1.CocUpdateChangeRequestBodyTicketInfo`
        """
        return self._ticket_info

    @ticket_info.setter
    def ticket_info(self, ticket_info):
        r"""Sets the ticket_info of this CocUpdateChangeRequestBody.

        :param ticket_info: The ticket_info of this CocUpdateChangeRequestBody.
        :type ticket_info: :class:`huaweicloudsdkcoc.v1.CocUpdateChangeRequestBodyTicketInfo`
        """
        self._ticket_info = ticket_info

    @property
    def sub_tickets(self):
        r"""Gets the sub_tickets of this CocUpdateChangeRequestBody.

        变更子单信息。

        :return: The sub_tickets of this CocUpdateChangeRequestBody.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.CocUpdateChangeRequestBodySubTickets`]
        """
        return self._sub_tickets

    @sub_tickets.setter
    def sub_tickets(self, sub_tickets):
        r"""Sets the sub_tickets of this CocUpdateChangeRequestBody.

        变更子单信息。

        :param sub_tickets: The sub_tickets of this CocUpdateChangeRequestBody.
        :type sub_tickets: list[:class:`huaweicloudsdkcoc.v1.CocUpdateChangeRequestBodySubTickets`]
        """
        self._sub_tickets = sub_tickets

    @property
    def history_info(self):
        r"""Gets the history_info of this CocUpdateChangeRequestBody.

        :return: The history_info of this CocUpdateChangeRequestBody.
        :rtype: :class:`huaweicloudsdkcoc.v1.CocUpdateChangeRequestBodyHistoryInfo`
        """
        return self._history_info

    @history_info.setter
    def history_info(self, history_info):
        r"""Sets the history_info of this CocUpdateChangeRequestBody.

        :param history_info: The history_info of this CocUpdateChangeRequestBody.
        :type history_info: :class:`huaweicloudsdkcoc.v1.CocUpdateChangeRequestBodyHistoryInfo`
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
        if not isinstance(other, CocUpdateChangeRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
