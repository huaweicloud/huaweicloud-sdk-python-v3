# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTicketRequest:

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
        'ticket_id': 'str',
        'body': 'CocUpdateChangeRequestBody'
    }

    attribute_map = {
        'ticket_type': 'ticket_type',
        'ticket_id': 'ticket_id',
        'body': 'body'
    }

    def __init__(self, ticket_type=None, ticket_id=None, body=None):
        r"""UpdateTicketRequest

        The model defined in huaweicloud sdk

        :param ticket_type: 需要修改的工单类型，此处需传递固定值change，表示更新变更单状态。
        :type ticket_type: str
        :param ticket_id: 变更单工单单号。
        :type ticket_id: str
        :param body: Body of the UpdateTicketRequest
        :type body: :class:`huaweicloudsdkcoc.v1.CocUpdateChangeRequestBody`
        """
        
        

        self._ticket_type = None
        self._ticket_id = None
        self._body = None
        self.discriminator = None

        self.ticket_type = ticket_type
        self.ticket_id = ticket_id
        if body is not None:
            self.body = body

    @property
    def ticket_type(self):
        r"""Gets the ticket_type of this UpdateTicketRequest.

        需要修改的工单类型，此处需传递固定值change，表示更新变更单状态。

        :return: The ticket_type of this UpdateTicketRequest.
        :rtype: str
        """
        return self._ticket_type

    @ticket_type.setter
    def ticket_type(self, ticket_type):
        r"""Sets the ticket_type of this UpdateTicketRequest.

        需要修改的工单类型，此处需传递固定值change，表示更新变更单状态。

        :param ticket_type: The ticket_type of this UpdateTicketRequest.
        :type ticket_type: str
        """
        self._ticket_type = ticket_type

    @property
    def ticket_id(self):
        r"""Gets the ticket_id of this UpdateTicketRequest.

        变更单工单单号。

        :return: The ticket_id of this UpdateTicketRequest.
        :rtype: str
        """
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, ticket_id):
        r"""Sets the ticket_id of this UpdateTicketRequest.

        变更单工单单号。

        :param ticket_id: The ticket_id of this UpdateTicketRequest.
        :type ticket_id: str
        """
        self._ticket_id = ticket_id

    @property
    def body(self):
        r"""Gets the body of this UpdateTicketRequest.

        :return: The body of this UpdateTicketRequest.
        :rtype: :class:`huaweicloudsdkcoc.v1.CocUpdateChangeRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateTicketRequest.

        :param body: The body of this UpdateTicketRequest.
        :type body: :class:`huaweicloudsdkcoc.v1.CocUpdateChangeRequestBody`
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
        if not isinstance(other, UpdateTicketRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
