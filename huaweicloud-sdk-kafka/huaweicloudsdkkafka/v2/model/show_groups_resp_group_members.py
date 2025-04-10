# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGroupsRespGroupMembers:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'host': 'str',
        'assignment': 'list[ShowGroupsRespGroupAssignment]',
        'member_id': 'str',
        'client_id': 'str'
    }

    attribute_map = {
        'host': 'host',
        'assignment': 'assignment',
        'member_id': 'member_id',
        'client_id': 'client_id'
    }

    def __init__(self, host=None, assignment=None, member_id=None, client_id=None):
        r"""ShowGroupsRespGroupMembers

        The model defined in huaweicloud sdk

        :param host: 消费组consumer地址。
        :type host: str
        :param assignment: consumer分配到的分区信息。
        :type assignment: list[:class:`huaweicloudsdkkafka.v2.ShowGroupsRespGroupAssignment`]
        :param member_id: 消费组consumer的ID。
        :type member_id: str
        :param client_id: 客户端ID。
        :type client_id: str
        """
        
        

        self._host = None
        self._assignment = None
        self._member_id = None
        self._client_id = None
        self.discriminator = None

        if host is not None:
            self.host = host
        if assignment is not None:
            self.assignment = assignment
        if member_id is not None:
            self.member_id = member_id
        if client_id is not None:
            self.client_id = client_id

    @property
    def host(self):
        r"""Gets the host of this ShowGroupsRespGroupMembers.

        消费组consumer地址。

        :return: The host of this ShowGroupsRespGroupMembers.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        r"""Sets the host of this ShowGroupsRespGroupMembers.

        消费组consumer地址。

        :param host: The host of this ShowGroupsRespGroupMembers.
        :type host: str
        """
        self._host = host

    @property
    def assignment(self):
        r"""Gets the assignment of this ShowGroupsRespGroupMembers.

        consumer分配到的分区信息。

        :return: The assignment of this ShowGroupsRespGroupMembers.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.ShowGroupsRespGroupAssignment`]
        """
        return self._assignment

    @assignment.setter
    def assignment(self, assignment):
        r"""Sets the assignment of this ShowGroupsRespGroupMembers.

        consumer分配到的分区信息。

        :param assignment: The assignment of this ShowGroupsRespGroupMembers.
        :type assignment: list[:class:`huaweicloudsdkkafka.v2.ShowGroupsRespGroupAssignment`]
        """
        self._assignment = assignment

    @property
    def member_id(self):
        r"""Gets the member_id of this ShowGroupsRespGroupMembers.

        消费组consumer的ID。

        :return: The member_id of this ShowGroupsRespGroupMembers.
        :rtype: str
        """
        return self._member_id

    @member_id.setter
    def member_id(self, member_id):
        r"""Sets the member_id of this ShowGroupsRespGroupMembers.

        消费组consumer的ID。

        :param member_id: The member_id of this ShowGroupsRespGroupMembers.
        :type member_id: str
        """
        self._member_id = member_id

    @property
    def client_id(self):
        r"""Gets the client_id of this ShowGroupsRespGroupMembers.

        客户端ID。

        :return: The client_id of this ShowGroupsRespGroupMembers.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        r"""Sets the client_id of this ShowGroupsRespGroupMembers.

        客户端ID。

        :param client_id: The client_id of this ShowGroupsRespGroupMembers.
        :type client_id: str
        """
        self._client_id = client_id

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
        if not isinstance(other, ShowGroupsRespGroupMembers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
