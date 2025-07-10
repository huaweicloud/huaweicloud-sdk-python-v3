# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubTicketsRequest:

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
        'type': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'ticket_type': 'ticket_type',
        'ticket_id': 'ticket_id',
        'type': 'type',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, ticket_type=None, ticket_id=None, type=None, limit=None, marker=None):
        r"""ListSubTicketsRequest

        The model defined in huaweicloud sdk

        :param ticket_type: 工单类型，此处传固定值change。
        :type ticket_type: str
        :param ticket_id: 变更单工单id
        :type ticket_id: str
        :param type: 资源类型
        :type type: str
        :param limit: 每页显示的条数
        :type limit: int
        :param marker: 上一页数据的最后一条记录的id
        :type marker: str
        """
        
        

        self._ticket_type = None
        self._ticket_id = None
        self._type = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        self.ticket_type = ticket_type
        self.ticket_id = ticket_id
        self.type = type
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def ticket_type(self):
        r"""Gets the ticket_type of this ListSubTicketsRequest.

        工单类型，此处传固定值change。

        :return: The ticket_type of this ListSubTicketsRequest.
        :rtype: str
        """
        return self._ticket_type

    @ticket_type.setter
    def ticket_type(self, ticket_type):
        r"""Sets the ticket_type of this ListSubTicketsRequest.

        工单类型，此处传固定值change。

        :param ticket_type: The ticket_type of this ListSubTicketsRequest.
        :type ticket_type: str
        """
        self._ticket_type = ticket_type

    @property
    def ticket_id(self):
        r"""Gets the ticket_id of this ListSubTicketsRequest.

        变更单工单id

        :return: The ticket_id of this ListSubTicketsRequest.
        :rtype: str
        """
        return self._ticket_id

    @ticket_id.setter
    def ticket_id(self, ticket_id):
        r"""Sets the ticket_id of this ListSubTicketsRequest.

        变更单工单id

        :param ticket_id: The ticket_id of this ListSubTicketsRequest.
        :type ticket_id: str
        """
        self._ticket_id = ticket_id

    @property
    def type(self):
        r"""Gets the type of this ListSubTicketsRequest.

        资源类型

        :return: The type of this ListSubTicketsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListSubTicketsRequest.

        资源类型

        :param type: The type of this ListSubTicketsRequest.
        :type type: str
        """
        self._type = type

    @property
    def limit(self):
        r"""Gets the limit of this ListSubTicketsRequest.

        每页显示的条数

        :return: The limit of this ListSubTicketsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSubTicketsRequest.

        每页显示的条数

        :param limit: The limit of this ListSubTicketsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListSubTicketsRequest.

        上一页数据的最后一条记录的id

        :return: The marker of this ListSubTicketsRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListSubTicketsRequest.

        上一页数据的最后一条记录的id

        :param marker: The marker of this ListSubTicketsRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListSubTicketsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
