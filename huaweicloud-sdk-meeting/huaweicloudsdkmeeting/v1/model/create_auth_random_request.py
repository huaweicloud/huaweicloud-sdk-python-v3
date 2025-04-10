# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAuthRandomRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('x_password')

    openapi_types = {
        'conf_id': 'str',
        'guest_waiting': 'int',
        'x_password': 'str'
    }

    attribute_map = {
        'conf_id': 'conf_id',
        'guest_waiting': 'guest_waiting',
        'x_password': 'X-Password'
    }

    def __init__(self, conf_id=None, guest_waiting=None, x_password=None):
        r"""CreateAuthRandomRequest

        The model defined in huaweicloud sdk

        :param conf_id: 会议ID
        :type conf_id: str
        :param guest_waiting: 0-不支持来宾会前等待页能力（默认）、1-支持来宾会前等待页能力
        :type guest_waiting: int
        :param x_password: 会议密码
        :type x_password: str
        """
        
        

        self._conf_id = None
        self._guest_waiting = None
        self._x_password = None
        self.discriminator = None

        self.conf_id = conf_id
        if guest_waiting is not None:
            self.guest_waiting = guest_waiting
        if x_password is not None:
            self.x_password = x_password

    @property
    def conf_id(self):
        r"""Gets the conf_id of this CreateAuthRandomRequest.

        会议ID

        :return: The conf_id of this CreateAuthRandomRequest.
        :rtype: str
        """
        return self._conf_id

    @conf_id.setter
    def conf_id(self, conf_id):
        r"""Sets the conf_id of this CreateAuthRandomRequest.

        会议ID

        :param conf_id: The conf_id of this CreateAuthRandomRequest.
        :type conf_id: str
        """
        self._conf_id = conf_id

    @property
    def guest_waiting(self):
        r"""Gets the guest_waiting of this CreateAuthRandomRequest.

        0-不支持来宾会前等待页能力（默认）、1-支持来宾会前等待页能力

        :return: The guest_waiting of this CreateAuthRandomRequest.
        :rtype: int
        """
        return self._guest_waiting

    @guest_waiting.setter
    def guest_waiting(self, guest_waiting):
        r"""Sets the guest_waiting of this CreateAuthRandomRequest.

        0-不支持来宾会前等待页能力（默认）、1-支持来宾会前等待页能力

        :param guest_waiting: The guest_waiting of this CreateAuthRandomRequest.
        :type guest_waiting: int
        """
        self._guest_waiting = guest_waiting

    @property
    def x_password(self):
        r"""Gets the x_password of this CreateAuthRandomRequest.

        会议密码

        :return: The x_password of this CreateAuthRandomRequest.
        :rtype: str
        """
        return self._x_password

    @x_password.setter
    def x_password(self, x_password):
        r"""Sets the x_password of this CreateAuthRandomRequest.

        会议密码

        :param x_password: The x_password of this CreateAuthRandomRequest.
        :type x_password: str
        """
        self._x_password = x_password

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
        if not isinstance(other, CreateAuthRandomRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
