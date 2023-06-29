# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LogoffDesktopsReq:

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
        'message': 'str'
    }

    attribute_map = {
        'desktop_ids': 'desktop_ids',
        'message': 'message'
    }

    def __init__(self, desktop_ids=None, message=None):
        """LogoffDesktopsReq

        The model defined in huaweicloud sdk

        :param desktop_ids: 计算机id列表。
        :type desktop_ids: list[str]
        :param message: 下发注销桌面任务时，给用户发送的提示信息。
        :type message: str
        """
        
        

        self._desktop_ids = None
        self._message = None
        self.discriminator = None

        if desktop_ids is not None:
            self.desktop_ids = desktop_ids
        if message is not None:
            self.message = message

    @property
    def desktop_ids(self):
        """Gets the desktop_ids of this LogoffDesktopsReq.

        计算机id列表。

        :return: The desktop_ids of this LogoffDesktopsReq.
        :rtype: list[str]
        """
        return self._desktop_ids

    @desktop_ids.setter
    def desktop_ids(self, desktop_ids):
        """Sets the desktop_ids of this LogoffDesktopsReq.

        计算机id列表。

        :param desktop_ids: The desktop_ids of this LogoffDesktopsReq.
        :type desktop_ids: list[str]
        """
        self._desktop_ids = desktop_ids

    @property
    def message(self):
        """Gets the message of this LogoffDesktopsReq.

        下发注销桌面任务时，给用户发送的提示信息。

        :return: The message of this LogoffDesktopsReq.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this LogoffDesktopsReq.

        下发注销桌面任务时，给用户发送的提示信息。

        :param message: The message of this LogoffDesktopsReq.
        :type message: str
        """
        self._message = message

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
        if not isinstance(other, LogoffDesktopsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
