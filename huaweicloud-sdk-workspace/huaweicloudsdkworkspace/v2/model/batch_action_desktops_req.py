# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchActionDesktopsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_ids': 'list[str]',
        'op_type': 'str',
        'type': 'str'
    }

    attribute_map = {
        'desktop_ids': 'desktop_ids',
        'op_type': 'op_type',
        'type': 'type'
    }

    def __init__(self, desktop_ids=None, op_type=None, type=None):
        """BatchActionDesktopsReq

        The model defined in huaweicloud sdk

        :param desktop_ids: 操作的桌面ID列表。
        :type desktop_ids: list[str]
        :param op_type: 操作类型。 -os-start 启动。 -reboot 重启。 -os-stop 关机。 -os-hibernate 休眠。
        :type op_type: str
        :param type: SOFT：普通操作；HARD：强制操作。例如type为HARD，op_type为os-stop代表强制关机。
        :type type: str
        """
        
        

        self._desktop_ids = None
        self._op_type = None
        self._type = None
        self.discriminator = None

        self.desktop_ids = desktop_ids
        self.op_type = op_type
        if type is not None:
            self.type = type

    @property
    def desktop_ids(self):
        """Gets the desktop_ids of this BatchActionDesktopsReq.

        操作的桌面ID列表。

        :return: The desktop_ids of this BatchActionDesktopsReq.
        :rtype: list[str]
        """
        return self._desktop_ids

    @desktop_ids.setter
    def desktop_ids(self, desktop_ids):
        """Sets the desktop_ids of this BatchActionDesktopsReq.

        操作的桌面ID列表。

        :param desktop_ids: The desktop_ids of this BatchActionDesktopsReq.
        :type desktop_ids: list[str]
        """
        self._desktop_ids = desktop_ids

    @property
    def op_type(self):
        """Gets the op_type of this BatchActionDesktopsReq.

        操作类型。 -os-start 启动。 -reboot 重启。 -os-stop 关机。 -os-hibernate 休眠。

        :return: The op_type of this BatchActionDesktopsReq.
        :rtype: str
        """
        return self._op_type

    @op_type.setter
    def op_type(self, op_type):
        """Sets the op_type of this BatchActionDesktopsReq.

        操作类型。 -os-start 启动。 -reboot 重启。 -os-stop 关机。 -os-hibernate 休眠。

        :param op_type: The op_type of this BatchActionDesktopsReq.
        :type op_type: str
        """
        self._op_type = op_type

    @property
    def type(self):
        """Gets the type of this BatchActionDesktopsReq.

        SOFT：普通操作；HARD：强制操作。例如type为HARD，op_type为os-stop代表强制关机。

        :return: The type of this BatchActionDesktopsReq.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BatchActionDesktopsReq.

        SOFT：普通操作；HARD：强制操作。例如type为HARD，op_type为os-stop代表强制关机。

        :param type: The type of this BatchActionDesktopsReq.
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
        if not isinstance(other, BatchActionDesktopsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
