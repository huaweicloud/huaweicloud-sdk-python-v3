# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResendReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group': 'str',
        'client_id': 'str',
        'msg_id_list': 'list[str]'
    }

    attribute_map = {
        'group': 'group',
        'client_id': 'client_id',
        'msg_id_list': 'msg_id_list'
    }

    def __init__(self, group=None, client_id=None, msg_id_list=None):
        """ResendReq

        The model defined in huaweicloud sdk

        :param group: Group ID。
        :type group: str
        :param client_id: 客户端ID。
        :type client_id: str
        :param msg_id_list: 消息列表。
        :type msg_id_list: list[str]
        """
        
        

        self._group = None
        self._client_id = None
        self._msg_id_list = None
        self.discriminator = None

        if group is not None:
            self.group = group
        if client_id is not None:
            self.client_id = client_id
        if msg_id_list is not None:
            self.msg_id_list = msg_id_list

    @property
    def group(self):
        """Gets the group of this ResendReq.

        Group ID。

        :return: The group of this ResendReq.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this ResendReq.

        Group ID。

        :param group: The group of this ResendReq.
        :type group: str
        """
        self._group = group

    @property
    def client_id(self):
        """Gets the client_id of this ResendReq.

        客户端ID。

        :return: The client_id of this ResendReq.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this ResendReq.

        客户端ID。

        :param client_id: The client_id of this ResendReq.
        :type client_id: str
        """
        self._client_id = client_id

    @property
    def msg_id_list(self):
        """Gets the msg_id_list of this ResendReq.

        消息列表。

        :return: The msg_id_list of this ResendReq.
        :rtype: list[str]
        """
        return self._msg_id_list

    @msg_id_list.setter
    def msg_id_list(self, msg_id_list):
        """Sets the msg_id_list of this ResendReq.

        消息列表。

        :param msg_id_list: The msg_id_list of this ResendReq.
        :type msg_id_list: list[str]
        """
        self._msg_id_list = msg_id_list

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
        if not isinstance(other, ResendReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
