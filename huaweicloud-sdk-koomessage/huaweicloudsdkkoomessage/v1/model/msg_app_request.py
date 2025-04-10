# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MsgAppRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_name': 'str',
        'up_link_addr': 'str'
    }

    attribute_map = {
        'app_name': 'app_name',
        'up_link_addr': 'up_link_addr'
    }

    def __init__(self, app_name=None, up_link_addr=None):
        r"""MsgAppRequest

        The model defined in huaweicloud sdk

        :param app_name: 应用名称。
        :type app_name: str
        :param up_link_addr: 上行回调地址。支持通信协议HTTPS/HTTP。
        :type up_link_addr: str
        """
        
        

        self._app_name = None
        self._up_link_addr = None
        self.discriminator = None

        self.app_name = app_name
        if up_link_addr is not None:
            self.up_link_addr = up_link_addr

    @property
    def app_name(self):
        r"""Gets the app_name of this MsgAppRequest.

        应用名称。

        :return: The app_name of this MsgAppRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this MsgAppRequest.

        应用名称。

        :param app_name: The app_name of this MsgAppRequest.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def up_link_addr(self):
        r"""Gets the up_link_addr of this MsgAppRequest.

        上行回调地址。支持通信协议HTTPS/HTTP。

        :return: The up_link_addr of this MsgAppRequest.
        :rtype: str
        """
        return self._up_link_addr

    @up_link_addr.setter
    def up_link_addr(self, up_link_addr):
        r"""Sets the up_link_addr of this MsgAppRequest.

        上行回调地址。支持通信协议HTTPS/HTTP。

        :param up_link_addr: The up_link_addr of this MsgAppRequest.
        :type up_link_addr: str
        """
        self._up_link_addr = up_link_addr

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
        if not isinstance(other, MsgAppRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
