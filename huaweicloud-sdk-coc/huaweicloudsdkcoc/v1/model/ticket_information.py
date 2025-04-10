# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TicketInformation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ticket_infos': 'list[TicketInfo]'
    }

    attribute_map = {
        'ticket_infos': 'ticket_infos'
    }

    def __init__(self, ticket_infos=None):
        r"""TicketInformation

        The model defined in huaweicloud sdk

        :param ticket_infos: 选择的四号提权单信息
        :type ticket_infos: list[:class:`huaweicloudsdkcoc.v1.TicketInfo`]
        """
        
        

        self._ticket_infos = None
        self.discriminator = None

        if ticket_infos is not None:
            self.ticket_infos = ticket_infos

    @property
    def ticket_infos(self):
        r"""Gets the ticket_infos of this TicketInformation.

        选择的四号提权单信息

        :return: The ticket_infos of this TicketInformation.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.TicketInfo`]
        """
        return self._ticket_infos

    @ticket_infos.setter
    def ticket_infos(self, ticket_infos):
        r"""Sets the ticket_infos of this TicketInformation.

        选择的四号提权单信息

        :param ticket_infos: The ticket_infos of this TicketInformation.
        :type ticket_infos: list[:class:`huaweicloudsdkcoc.v1.TicketInfo`]
        """
        self._ticket_infos = ticket_infos

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
        if not isinstance(other, TicketInformation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
