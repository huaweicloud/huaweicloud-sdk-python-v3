# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RebootCbhRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_id': 'str',
        'reboot_type': 'str'
    }

    attribute_map = {
        'server_id': 'server_id',
        'reboot_type': 'reboot_type'
    }

    def __init__(self, server_id=None, reboot_type=None):
        r"""RebootCbhRequestBody

        The model defined in huaweicloud sdk

        :param server_id: 云堡垒机实例ID，使用UUID格式表示。
        :type server_id: str
        :param reboot_type: 重启方式，不区分大小写。 - SOFT：普通重启，关闭虚拟机服务 - HARD：强制重启，重启虚拟机
        :type reboot_type: str
        """
        
        

        self._server_id = None
        self._reboot_type = None
        self.discriminator = None

        self.server_id = server_id
        self.reboot_type = reboot_type

    @property
    def server_id(self):
        r"""Gets the server_id of this RebootCbhRequestBody.

        云堡垒机实例ID，使用UUID格式表示。

        :return: The server_id of this RebootCbhRequestBody.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this RebootCbhRequestBody.

        云堡垒机实例ID，使用UUID格式表示。

        :param server_id: The server_id of this RebootCbhRequestBody.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def reboot_type(self):
        r"""Gets the reboot_type of this RebootCbhRequestBody.

        重启方式，不区分大小写。 - SOFT：普通重启，关闭虚拟机服务 - HARD：强制重启，重启虚拟机

        :return: The reboot_type of this RebootCbhRequestBody.
        :rtype: str
        """
        return self._reboot_type

    @reboot_type.setter
    def reboot_type(self, reboot_type):
        r"""Sets the reboot_type of this RebootCbhRequestBody.

        重启方式，不区分大小写。 - SOFT：普通重启，关闭虚拟机服务 - HARD：强制重启，重启虚拟机

        :param reboot_type: The reboot_type of this RebootCbhRequestBody.
        :type reboot_type: str
        """
        self._reboot_type = reboot_type

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
        if not isinstance(other, RebootCbhRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
