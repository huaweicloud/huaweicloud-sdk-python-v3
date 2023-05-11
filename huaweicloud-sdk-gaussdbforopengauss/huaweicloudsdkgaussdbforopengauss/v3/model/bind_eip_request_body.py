# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BindEIPRequestBody:

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
        'public_ip': 'str',
        'public_ip_id': 'str'
    }

    attribute_map = {
        'action': 'action',
        'public_ip': 'public_ip',
        'public_ip_id': 'public_ip_id'
    }

    def __init__(self, action=None, public_ip=None, public_ip_id=None):
        """BindEIPRequestBody

        The model defined in huaweicloud sdk

        :param action: 操作标识。取值： - BIND，表示绑定弹性公网IP。 - UNBIND，表示解绑弹性公网IP。
        :type action: str
        :param public_ip: 弹性公网IP
        :type public_ip: str
        :param public_ip_id: 弹性公网IP的ID
        :type public_ip_id: str
        """
        
        

        self._action = None
        self._public_ip = None
        self._public_ip_id = None
        self.discriminator = None

        self.action = action
        self.public_ip = public_ip
        self.public_ip_id = public_ip_id

    @property
    def action(self):
        """Gets the action of this BindEIPRequestBody.

        操作标识。取值： - BIND，表示绑定弹性公网IP。 - UNBIND，表示解绑弹性公网IP。

        :return: The action of this BindEIPRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this BindEIPRequestBody.

        操作标识。取值： - BIND，表示绑定弹性公网IP。 - UNBIND，表示解绑弹性公网IP。

        :param action: The action of this BindEIPRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def public_ip(self):
        """Gets the public_ip of this BindEIPRequestBody.

        弹性公网IP

        :return: The public_ip of this BindEIPRequestBody.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this BindEIPRequestBody.

        弹性公网IP

        :param public_ip: The public_ip of this BindEIPRequestBody.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def public_ip_id(self):
        """Gets the public_ip_id of this BindEIPRequestBody.

        弹性公网IP的ID

        :return: The public_ip_id of this BindEIPRequestBody.
        :rtype: str
        """
        return self._public_ip_id

    @public_ip_id.setter
    def public_ip_id(self, public_ip_id):
        """Sets the public_ip_id of this BindEIPRequestBody.

        弹性公网IP的ID

        :param public_ip_id: The public_ip_id of this BindEIPRequestBody.
        :type public_ip_id: str
        """
        self._public_ip_id = public_ip_id

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
        if not isinstance(other, BindEIPRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
