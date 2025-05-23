# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Thumbnail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'quantity': 'int',
        'quantity_time': 'int',
        'time': 'int',
        'dots': 'list[int]',
        'cover_position': 'int',
        'format': 'int',
        'aspect_ratio': 'int',
        'max_length': 'int'
    }

    attribute_map = {
        'type': 'type',
        'quantity': 'quantity',
        'quantity_time': 'quantity_time',
        'time': 'time',
        'dots': 'dots',
        'cover_position': 'cover_position',
        'format': 'format',
        'aspect_ratio': 'aspect_ratio',
        'max_length': 'max_length'
    }

    def __init__(self, type=None, quantity=None, quantity_time=None, time=None, dots=None, cover_position=None, format=None, aspect_ratio=None, max_length=None):
        r"""Thumbnail

        The model defined in huaweicloud sdk

        :param type: 截图类型。  取值如下： - time：每次进行截图的间隔时间。 - dots: 按照指定的时间点截图。 - quantity： 按照指定张数，根据视频时长等分视频截图。
        :type type: str
        :param quantity: **type**取值为quantity时必填。 按照指定张数，根据视频时长等分视频截图。 取值范围：[1,10]之间的整数。
        :type quantity: int
        :param quantity_time: **type**取值为quantity时选填。 按照指定时间间隔取指定张数截图。 取值范围：[0,2147483647]之间的整数。
        :type quantity_time: int
        :param time: 根据时间间隔采样时的时间间隔值。单位：秒。 **type**取值为time时。 默认值：12 取值范围：[0,100]之间的整数。
        :type time: int
        :param dots: **type**取值为dots时必填。指定时间截图时的时间点数组。
        :type dots: list[int]
        :param cover_position: 该值表示指定第几张截图作为封面。  默认值：1。
        :type cover_position: int
        :param format: 截图文件格式。  取值如下： - 1：jpg。  默认值：1 。
        :type format: int
        :param aspect_ratio: 纵横比，图像缩放方式。  取值如下： - 0：自适应（保持原有宽高比）。 - 1：16:9。  默认值：0。
        :type aspect_ratio: int
        :param max_length: 截图最长边的尺寸。  单位：像素。  宽边尺寸按照该尺寸与原始视频像素等比缩放计算。
        :type max_length: int
        """
        
        

        self._type = None
        self._quantity = None
        self._quantity_time = None
        self._time = None
        self._dots = None
        self._cover_position = None
        self._format = None
        self._aspect_ratio = None
        self._max_length = None
        self.discriminator = None

        self.type = type
        if quantity is not None:
            self.quantity = quantity
        if quantity_time is not None:
            self.quantity_time = quantity_time
        if time is not None:
            self.time = time
        if dots is not None:
            self.dots = dots
        if cover_position is not None:
            self.cover_position = cover_position
        if format is not None:
            self.format = format
        if aspect_ratio is not None:
            self.aspect_ratio = aspect_ratio
        if max_length is not None:
            self.max_length = max_length

    @property
    def type(self):
        r"""Gets the type of this Thumbnail.

        截图类型。  取值如下： - time：每次进行截图的间隔时间。 - dots: 按照指定的时间点截图。 - quantity： 按照指定张数，根据视频时长等分视频截图。

        :return: The type of this Thumbnail.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Thumbnail.

        截图类型。  取值如下： - time：每次进行截图的间隔时间。 - dots: 按照指定的时间点截图。 - quantity： 按照指定张数，根据视频时长等分视频截图。

        :param type: The type of this Thumbnail.
        :type type: str
        """
        self._type = type

    @property
    def quantity(self):
        r"""Gets the quantity of this Thumbnail.

        **type**取值为quantity时必填。 按照指定张数，根据视频时长等分视频截图。 取值范围：[1,10]之间的整数。

        :return: The quantity of this Thumbnail.
        :rtype: int
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        r"""Sets the quantity of this Thumbnail.

        **type**取值为quantity时必填。 按照指定张数，根据视频时长等分视频截图。 取值范围：[1,10]之间的整数。

        :param quantity: The quantity of this Thumbnail.
        :type quantity: int
        """
        self._quantity = quantity

    @property
    def quantity_time(self):
        r"""Gets the quantity_time of this Thumbnail.

        **type**取值为quantity时选填。 按照指定时间间隔取指定张数截图。 取值范围：[0,2147483647]之间的整数。

        :return: The quantity_time of this Thumbnail.
        :rtype: int
        """
        return self._quantity_time

    @quantity_time.setter
    def quantity_time(self, quantity_time):
        r"""Sets the quantity_time of this Thumbnail.

        **type**取值为quantity时选填。 按照指定时间间隔取指定张数截图。 取值范围：[0,2147483647]之间的整数。

        :param quantity_time: The quantity_time of this Thumbnail.
        :type quantity_time: int
        """
        self._quantity_time = quantity_time

    @property
    def time(self):
        r"""Gets the time of this Thumbnail.

        根据时间间隔采样时的时间间隔值。单位：秒。 **type**取值为time时。 默认值：12 取值范围：[0,100]之间的整数。

        :return: The time of this Thumbnail.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time):
        r"""Sets the time of this Thumbnail.

        根据时间间隔采样时的时间间隔值。单位：秒。 **type**取值为time时。 默认值：12 取值范围：[0,100]之间的整数。

        :param time: The time of this Thumbnail.
        :type time: int
        """
        self._time = time

    @property
    def dots(self):
        r"""Gets the dots of this Thumbnail.

        **type**取值为dots时必填。指定时间截图时的时间点数组。

        :return: The dots of this Thumbnail.
        :rtype: list[int]
        """
        return self._dots

    @dots.setter
    def dots(self, dots):
        r"""Sets the dots of this Thumbnail.

        **type**取值为dots时必填。指定时间截图时的时间点数组。

        :param dots: The dots of this Thumbnail.
        :type dots: list[int]
        """
        self._dots = dots

    @property
    def cover_position(self):
        r"""Gets the cover_position of this Thumbnail.

        该值表示指定第几张截图作为封面。  默认值：1。

        :return: The cover_position of this Thumbnail.
        :rtype: int
        """
        return self._cover_position

    @cover_position.setter
    def cover_position(self, cover_position):
        r"""Sets the cover_position of this Thumbnail.

        该值表示指定第几张截图作为封面。  默认值：1。

        :param cover_position: The cover_position of this Thumbnail.
        :type cover_position: int
        """
        self._cover_position = cover_position

    @property
    def format(self):
        r"""Gets the format of this Thumbnail.

        截图文件格式。  取值如下： - 1：jpg。  默认值：1 。

        :return: The format of this Thumbnail.
        :rtype: int
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this Thumbnail.

        截图文件格式。  取值如下： - 1：jpg。  默认值：1 。

        :param format: The format of this Thumbnail.
        :type format: int
        """
        self._format = format

    @property
    def aspect_ratio(self):
        r"""Gets the aspect_ratio of this Thumbnail.

        纵横比，图像缩放方式。  取值如下： - 0：自适应（保持原有宽高比）。 - 1：16:9。  默认值：0。

        :return: The aspect_ratio of this Thumbnail.
        :rtype: int
        """
        return self._aspect_ratio

    @aspect_ratio.setter
    def aspect_ratio(self, aspect_ratio):
        r"""Sets the aspect_ratio of this Thumbnail.

        纵横比，图像缩放方式。  取值如下： - 0：自适应（保持原有宽高比）。 - 1：16:9。  默认值：0。

        :param aspect_ratio: The aspect_ratio of this Thumbnail.
        :type aspect_ratio: int
        """
        self._aspect_ratio = aspect_ratio

    @property
    def max_length(self):
        r"""Gets the max_length of this Thumbnail.

        截图最长边的尺寸。  单位：像素。  宽边尺寸按照该尺寸与原始视频像素等比缩放计算。

        :return: The max_length of this Thumbnail.
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        r"""Sets the max_length of this Thumbnail.

        截图最长边的尺寸。  单位：像素。  宽边尺寸按照该尺寸与原始视频像素等比缩放计算。

        :param max_length: The max_length of this Thumbnail.
        :type max_length: int
        """
        self._max_length = max_length

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
        if not isinstance(other, Thumbnail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
