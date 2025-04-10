# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfirmSmarLiveRoomReq:

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
        'script_version': 'str'
    }

    attribute_map = {
        'action': 'action',
        'script_version': 'script_version'
    }

    def __init__(self, action=None, script_version=None):
        r"""ConfirmSmarLiveRoomReq

        The model defined in huaweicloud sdk

        :param action: 确认操作。 * confirm: 确认。 * reject: 拒绝。
        :type action: str
        :param script_version: 剧本版本。从查询直播间详情接口中获取。
        :type script_version: str
        """
        
        

        self._action = None
        self._script_version = None
        self.discriminator = None

        if action is not None:
            self.action = action
        if script_version is not None:
            self.script_version = script_version

    @property
    def action(self):
        r"""Gets the action of this ConfirmSmarLiveRoomReq.

        确认操作。 * confirm: 确认。 * reject: 拒绝。

        :return: The action of this ConfirmSmarLiveRoomReq.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ConfirmSmarLiveRoomReq.

        确认操作。 * confirm: 确认。 * reject: 拒绝。

        :param action: The action of this ConfirmSmarLiveRoomReq.
        :type action: str
        """
        self._action = action

    @property
    def script_version(self):
        r"""Gets the script_version of this ConfirmSmarLiveRoomReq.

        剧本版本。从查询直播间详情接口中获取。

        :return: The script_version of this ConfirmSmarLiveRoomReq.
        :rtype: str
        """
        return self._script_version

    @script_version.setter
    def script_version(self, script_version):
        r"""Sets the script_version of this ConfirmSmarLiveRoomReq.

        剧本版本。从查询直播间详情接口中获取。

        :param script_version: The script_version of this ConfirmSmarLiveRoomReq.
        :type script_version: str
        """
        self._script_version = script_version

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
        if not isinstance(other, ConfirmSmarLiveRoomReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
