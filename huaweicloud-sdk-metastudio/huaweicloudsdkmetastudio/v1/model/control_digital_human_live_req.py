# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ControlDigitalHumanLiveReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'command': 'str',
        'params': 'object'
    }

    attribute_map = {
        'command': 'command',
        'params': 'params'
    }

    def __init__(self, command=None, params=None):
        """ControlDigitalHumanLiveReq

        The model defined in huaweicloud sdk

        :param command: 命令名称。 - BODY_POS_RESET：视觉驱动复位 - HIPS_POS_ADJUST：模型位移调整 - EYE_POS：眼神锁定/解锁 - SKELETON_ROTATION_ADJUST：骨骼旋转 - LOCK_SKELETONS：骨骼锁定 - UNLOCK_SKELETONS：骨骼解锁
        :type command: str
        :param params: 命令参数。
        :type params: object
        """
        
        

        self._command = None
        self._params = None
        self.discriminator = None

        self.command = command
        if params is not None:
            self.params = params

    @property
    def command(self):
        """Gets the command of this ControlDigitalHumanLiveReq.

        命令名称。 - BODY_POS_RESET：视觉驱动复位 - HIPS_POS_ADJUST：模型位移调整 - EYE_POS：眼神锁定/解锁 - SKELETON_ROTATION_ADJUST：骨骼旋转 - LOCK_SKELETONS：骨骼锁定 - UNLOCK_SKELETONS：骨骼解锁

        :return: The command of this ControlDigitalHumanLiveReq.
        :rtype: str
        """
        return self._command

    @command.setter
    def command(self, command):
        """Sets the command of this ControlDigitalHumanLiveReq.

        命令名称。 - BODY_POS_RESET：视觉驱动复位 - HIPS_POS_ADJUST：模型位移调整 - EYE_POS：眼神锁定/解锁 - SKELETON_ROTATION_ADJUST：骨骼旋转 - LOCK_SKELETONS：骨骼锁定 - UNLOCK_SKELETONS：骨骼解锁

        :param command: The command of this ControlDigitalHumanLiveReq.
        :type command: str
        """
        self._command = command

    @property
    def params(self):
        """Gets the params of this ControlDigitalHumanLiveReq.

        命令参数。

        :return: The params of this ControlDigitalHumanLiveReq.
        :rtype: object
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this ControlDigitalHumanLiveReq.

        命令参数。

        :param params: The params of this ControlDigitalHumanLiveReq.
        :type params: object
        """
        self._params = params

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
        if not isinstance(other, ControlDigitalHumanLiveReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
