# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DesktopPoolActionReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'op_type': 'str',
        'type': 'str'
    }

    attribute_map = {
        'op_type': 'op_type',
        'type': 'type'
    }

    def __init__(self, op_type=None, type=None):
        r"""DesktopPoolActionReq

        The model defined in huaweicloud sdk

        :param op_type: 操作类型。 -os-start 开机。 -os-stop 关机。 -reboot 重启。 -hibernate 休眠。
        :type op_type: str
        :param type: 执行类型。例如type为HARD，op_type为os-stop代表强制关机。 - SOFT：普通操作。 - HARD：强制操作。
        :type type: str
        """
        
        

        self._op_type = None
        self._type = None
        self.discriminator = None

        self.op_type = op_type
        if type is not None:
            self.type = type

    @property
    def op_type(self):
        r"""Gets the op_type of this DesktopPoolActionReq.

        操作类型。 -os-start 开机。 -os-stop 关机。 -reboot 重启。 -hibernate 休眠。

        :return: The op_type of this DesktopPoolActionReq.
        :rtype: str
        """
        return self._op_type

    @op_type.setter
    def op_type(self, op_type):
        r"""Sets the op_type of this DesktopPoolActionReq.

        操作类型。 -os-start 开机。 -os-stop 关机。 -reboot 重启。 -hibernate 休眠。

        :param op_type: The op_type of this DesktopPoolActionReq.
        :type op_type: str
        """
        self._op_type = op_type

    @property
    def type(self):
        r"""Gets the type of this DesktopPoolActionReq.

        执行类型。例如type为HARD，op_type为os-stop代表强制关机。 - SOFT：普通操作。 - HARD：强制操作。

        :return: The type of this DesktopPoolActionReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this DesktopPoolActionReq.

        执行类型。例如type为HARD，op_type为os-stop代表强制关机。 - SOFT：普通操作。 - HARD：强制操作。

        :param type: The type of this DesktopPoolActionReq.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, DesktopPoolActionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
