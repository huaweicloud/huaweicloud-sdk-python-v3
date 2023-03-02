# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoCoverAnalysisinference:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'gif_ratenum': 'int',
        'gif_rateden': 'int',
        'gif_long_side': 'int',
        'gif_short_side': 'int'
    }

    attribute_map = {
        'gif_ratenum': 'gif_ratenum',
        'gif_rateden': 'gif_rateden',
        'gif_long_side': 'gif_long_side',
        'gif_short_side': 'gif_short_side'
    }

    def __init__(self, gif_ratenum=None, gif_rateden=None, gif_long_side=None, gif_short_side=None):
        """VideoCoverAnalysisinference

        The model defined in huaweicloud sdk

        :param gif_ratenum: 动态封面帧率分子
        :type gif_ratenum: int
        :param gif_rateden: 动态封面帧率分母
        :type gif_rateden: int
        :param gif_long_side: 动态封面长边长度
        :type gif_long_side: int
        :param gif_short_side: 动态封面短边长度
        :type gif_short_side: int
        """
        
        

        self._gif_ratenum = None
        self._gif_rateden = None
        self._gif_long_side = None
        self._gif_short_side = None
        self.discriminator = None

        if gif_ratenum is not None:
            self.gif_ratenum = gif_ratenum
        if gif_rateden is not None:
            self.gif_rateden = gif_rateden
        if gif_long_side is not None:
            self.gif_long_side = gif_long_side
        if gif_short_side is not None:
            self.gif_short_side = gif_short_side

    @property
    def gif_ratenum(self):
        """Gets the gif_ratenum of this VideoCoverAnalysisinference.

        动态封面帧率分子

        :return: The gif_ratenum of this VideoCoverAnalysisinference.
        :rtype: int
        """
        return self._gif_ratenum

    @gif_ratenum.setter
    def gif_ratenum(self, gif_ratenum):
        """Sets the gif_ratenum of this VideoCoverAnalysisinference.

        动态封面帧率分子

        :param gif_ratenum: The gif_ratenum of this VideoCoverAnalysisinference.
        :type gif_ratenum: int
        """
        self._gif_ratenum = gif_ratenum

    @property
    def gif_rateden(self):
        """Gets the gif_rateden of this VideoCoverAnalysisinference.

        动态封面帧率分母

        :return: The gif_rateden of this VideoCoverAnalysisinference.
        :rtype: int
        """
        return self._gif_rateden

    @gif_rateden.setter
    def gif_rateden(self, gif_rateden):
        """Sets the gif_rateden of this VideoCoverAnalysisinference.

        动态封面帧率分母

        :param gif_rateden: The gif_rateden of this VideoCoverAnalysisinference.
        :type gif_rateden: int
        """
        self._gif_rateden = gif_rateden

    @property
    def gif_long_side(self):
        """Gets the gif_long_side of this VideoCoverAnalysisinference.

        动态封面长边长度

        :return: The gif_long_side of this VideoCoverAnalysisinference.
        :rtype: int
        """
        return self._gif_long_side

    @gif_long_side.setter
    def gif_long_side(self, gif_long_side):
        """Sets the gif_long_side of this VideoCoverAnalysisinference.

        动态封面长边长度

        :param gif_long_side: The gif_long_side of this VideoCoverAnalysisinference.
        :type gif_long_side: int
        """
        self._gif_long_side = gif_long_side

    @property
    def gif_short_side(self):
        """Gets the gif_short_side of this VideoCoverAnalysisinference.

        动态封面短边长度

        :return: The gif_short_side of this VideoCoverAnalysisinference.
        :rtype: int
        """
        return self._gif_short_side

    @gif_short_side.setter
    def gif_short_side(self, gif_short_side):
        """Sets the gif_short_side of this VideoCoverAnalysisinference.

        动态封面短边长度

        :param gif_short_side: The gif_short_side of this VideoCoverAnalysisinference.
        :type gif_short_side: int
        """
        self._gif_short_side = gif_short_side

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
        if not isinstance(other, VideoCoverAnalysisinference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
