# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCocTicketOperationHistoriesRequest:

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
        'body': 'ListTicketParams'
    }

    attribute_map = {
        'ticket_type': 'ticket_type',
        'body': 'body'
    }

    def __init__(self, ticket_type=None, body=None):
        r"""ListCocTicketOperationHistoriesRequest

        The model defined in huaweicloud sdk

        :param ticket_type: 需要查询的工单类型，事件单传值为incident，问题单传值为issues_mgmt。
        :type ticket_type: str
        :param body: Body of the ListCocTicketOperationHistoriesRequest
        :type body: :class:`huaweicloudsdkcoc.v1.ListTicketParams`
        """
        
        

        self._ticket_type = None
        self._body = None
        self.discriminator = None

        self.ticket_type = ticket_type
        if body is not None:
            self.body = body

    @property
    def ticket_type(self):
        r"""Gets the ticket_type of this ListCocTicketOperationHistoriesRequest.

        需要查询的工单类型，事件单传值为incident，问题单传值为issues_mgmt。

        :return: The ticket_type of this ListCocTicketOperationHistoriesRequest.
        :rtype: str
        """
        return self._ticket_type

    @ticket_type.setter
    def ticket_type(self, ticket_type):
        r"""Sets the ticket_type of this ListCocTicketOperationHistoriesRequest.

        需要查询的工单类型，事件单传值为incident，问题单传值为issues_mgmt。

        :param ticket_type: The ticket_type of this ListCocTicketOperationHistoriesRequest.
        :type ticket_type: str
        """
        self._ticket_type = ticket_type

    @property
    def body(self):
        r"""Gets the body of this ListCocTicketOperationHistoriesRequest.

        :return: The body of this ListCocTicketOperationHistoriesRequest.
        :rtype: :class:`huaweicloudsdkcoc.v1.ListTicketParams`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ListCocTicketOperationHistoriesRequest.

        :param body: The body of this ListCocTicketOperationHistoriesRequest.
        :type body: :class:`huaweicloudsdkcoc.v1.ListTicketParams`
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
        if not isinstance(other, ListCocTicketOperationHistoriesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
