# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAudienceCountInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'show_audience_mode': 'int',
        'base_audience_count': 'int',
        'multiple': 'float'
    }

    attribute_map = {
        'show_audience_mode': 'showAudienceMode',
        'base_audience_count': 'baseAudienceCount',
        'multiple': 'multiple'
    }

    def __init__(self, show_audience_mode=None, base_audience_count=None, multiple=None):
        """ShowAudienceCountInfo

        The model defined in huaweicloud sdk

        :param show_audience_mode: 观众显示策略。 * 0：不显示 * 1：倍增显示与会人数。基于实时与会人数或累计与会人次（假设为N），可以再进行倍增设置。支持设置倍增倍数X和基础人数Y，设置后，显示的人数为：N*X+Y 
        :type show_audience_mode: int
        :param base_audience_count: 基础人数。范围是0~10000。
        :type base_audience_count: int
        :param multiple: 倍增倍数。范围是1~10, 支持设置到小数点后1位。
        :type multiple: float
        """
        
        

        self._show_audience_mode = None
        self._base_audience_count = None
        self._multiple = None
        self.discriminator = None

        if show_audience_mode is not None:
            self.show_audience_mode = show_audience_mode
        if base_audience_count is not None:
            self.base_audience_count = base_audience_count
        if multiple is not None:
            self.multiple = multiple

    @property
    def show_audience_mode(self):
        """Gets the show_audience_mode of this ShowAudienceCountInfo.

        观众显示策略。 * 0：不显示 * 1：倍增显示与会人数。基于实时与会人数或累计与会人次（假设为N），可以再进行倍增设置。支持设置倍增倍数X和基础人数Y，设置后，显示的人数为：N*X+Y 

        :return: The show_audience_mode of this ShowAudienceCountInfo.
        :rtype: int
        """
        return self._show_audience_mode

    @show_audience_mode.setter
    def show_audience_mode(self, show_audience_mode):
        """Sets the show_audience_mode of this ShowAudienceCountInfo.

        观众显示策略。 * 0：不显示 * 1：倍增显示与会人数。基于实时与会人数或累计与会人次（假设为N），可以再进行倍增设置。支持设置倍增倍数X和基础人数Y，设置后，显示的人数为：N*X+Y 

        :param show_audience_mode: The show_audience_mode of this ShowAudienceCountInfo.
        :type show_audience_mode: int
        """
        self._show_audience_mode = show_audience_mode

    @property
    def base_audience_count(self):
        """Gets the base_audience_count of this ShowAudienceCountInfo.

        基础人数。范围是0~10000。

        :return: The base_audience_count of this ShowAudienceCountInfo.
        :rtype: int
        """
        return self._base_audience_count

    @base_audience_count.setter
    def base_audience_count(self, base_audience_count):
        """Sets the base_audience_count of this ShowAudienceCountInfo.

        基础人数。范围是0~10000。

        :param base_audience_count: The base_audience_count of this ShowAudienceCountInfo.
        :type base_audience_count: int
        """
        self._base_audience_count = base_audience_count

    @property
    def multiple(self):
        """Gets the multiple of this ShowAudienceCountInfo.

        倍增倍数。范围是1~10, 支持设置到小数点后1位。

        :return: The multiple of this ShowAudienceCountInfo.
        :rtype: float
        """
        return self._multiple

    @multiple.setter
    def multiple(self, multiple):
        """Sets the multiple of this ShowAudienceCountInfo.

        倍增倍数。范围是1~10, 支持设置到小数点后1位。

        :param multiple: The multiple of this ShowAudienceCountInfo.
        :type multiple: float
        """
        self._multiple = multiple

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
        if not isinstance(other, ShowAudienceCountInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
