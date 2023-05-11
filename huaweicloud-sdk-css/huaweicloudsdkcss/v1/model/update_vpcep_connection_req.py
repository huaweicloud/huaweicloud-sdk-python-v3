# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateVpcepConnectionReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'endpoint_id_list': 'list[str]'
    }

    attribute_map = {
        'action': 'action',
        'endpoint_id_list': 'endpointIdList'
    }

    def __init__(self, action=None, endpoint_id_list=None):
        """UpdateVpcepConnectionReq

        The model defined in huaweicloud sdk

        :param action: 期望的操作行为。 - receive: 允许连接 - reject: 拒绝连接
        :type action: str
        :param endpoint_id_list: 终端节点ID列表。
        :type endpoint_id_list: list[str]
        """
        
        

        self._action = None
        self._endpoint_id_list = None
        self.discriminator = None

        self.action = action
        self.endpoint_id_list = endpoint_id_list

    @property
    def action(self):
        """Gets the action of this UpdateVpcepConnectionReq.

        期望的操作行为。 - receive: 允许连接 - reject: 拒绝连接

        :return: The action of this UpdateVpcepConnectionReq.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this UpdateVpcepConnectionReq.

        期望的操作行为。 - receive: 允许连接 - reject: 拒绝连接

        :param action: The action of this UpdateVpcepConnectionReq.
        :type action: str
        """
        self._action = action

    @property
    def endpoint_id_list(self):
        """Gets the endpoint_id_list of this UpdateVpcepConnectionReq.

        终端节点ID列表。

        :return: The endpoint_id_list of this UpdateVpcepConnectionReq.
        :rtype: list[str]
        """
        return self._endpoint_id_list

    @endpoint_id_list.setter
    def endpoint_id_list(self, endpoint_id_list):
        """Sets the endpoint_id_list of this UpdateVpcepConnectionReq.

        终端节点ID列表。

        :param endpoint_id_list: The endpoint_id_list of this UpdateVpcepConnectionReq.
        :type endpoint_id_list: list[str]
        """
        self._endpoint_id_list = endpoint_id_list

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
        if not isinstance(other, UpdateVpcepConnectionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
