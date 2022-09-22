# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestSwitchModeReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'switch_mode': 'str',
        'image_type': 'int'
    }

    attribute_map = {
        'switch_mode': 'switchMode',
        'image_type': 'imageType'
    }

    def __init__(self, switch_mode=None, image_type=None):
        """RestSwitchModeReqBody

        The model defined in huaweicloud sdk

        :param switch_mode: 会议显示策略。 - Fixed: 固定广播与会者 - VAS: 声控切换
        :type switch_mode: str
        :param image_type: 画面类型。单画面设置只针对声控模式。 - 0: 单画面 - 1: 多画面
        :type image_type: int
        """
        
        

        self._switch_mode = None
        self._image_type = None
        self.discriminator = None

        self.switch_mode = switch_mode
        self.image_type = image_type

    @property
    def switch_mode(self):
        """Gets the switch_mode of this RestSwitchModeReqBody.

        会议显示策略。 - Fixed: 固定广播与会者 - VAS: 声控切换

        :return: The switch_mode of this RestSwitchModeReqBody.
        :rtype: str
        """
        return self._switch_mode

    @switch_mode.setter
    def switch_mode(self, switch_mode):
        """Sets the switch_mode of this RestSwitchModeReqBody.

        会议显示策略。 - Fixed: 固定广播与会者 - VAS: 声控切换

        :param switch_mode: The switch_mode of this RestSwitchModeReqBody.
        :type switch_mode: str
        """
        self._switch_mode = switch_mode

    @property
    def image_type(self):
        """Gets the image_type of this RestSwitchModeReqBody.

        画面类型。单画面设置只针对声控模式。 - 0: 单画面 - 1: 多画面

        :return: The image_type of this RestSwitchModeReqBody.
        :rtype: int
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        """Sets the image_type of this RestSwitchModeReqBody.

        画面类型。单画面设置只针对声控模式。 - 0: 单画面 - 1: 多画面

        :param image_type: The image_type of this RestSwitchModeReqBody.
        :type image_type: int
        """
        self._image_type = image_type

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
        if not isinstance(other, RestSwitchModeReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
