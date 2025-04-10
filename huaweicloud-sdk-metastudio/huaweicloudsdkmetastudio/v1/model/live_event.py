# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LiveEvent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'timestamp': 'int',
        'type': 'int',
        'content': 'str'
    }

    attribute_map = {
        'timestamp': 'timestamp',
        'type': 'type',
        'content': 'content'
    }

    def __init__(self, timestamp=None, type=None, content=None):
        r"""LiveEvent

        The model defined in huaweicloud sdk

        :param timestamp: **参数解释**： 事件戳。从1970-01-01 00:00:00:000开始的毫秒数
        :type timestamp: int
        :param type: **参数解释**： 事件类型。 * 1 弹幕信息 * 2 用户入场 * 3 用户点赞 * 4 用户送礼 * 5 用户订阅\\关注 * 6 房间观看人数
        :type type: int
        :param content: 事件内容。 事件类型不同，content内容也不同，定义如下所示： - type&#x3D;1 弹幕信息   content定义：     * user:用户，json     * content: string,弹幕内容     user定义：     * userId：用户id，string     * name：用户姓名，string     * level：用户平台等级，int     * badge：用户牌子名称，string     * badgeLevel：牌子等级，int     举例：   &#x60;&#x60;&#x60;json   {     \&quot;timestamp\&quot;: 1694481224245,     \&quot;type\&quot;: 1,     \&quot;content\&quot;: \&quot;{\\\&quot;user\\\&quot;:{\\\&quot;userId\\\&quot;:\\\&quot;2027271526\\\&quot;,\\\&quot;name\\\&quot;:\\\&quot;***\\\&quot;,\\\&quot;level\\\&quot;:17,\\\&quot;badge\\\&quot;:\\\&quot;\\\&quot;,\\\&quot;badgeLevel\\\&quot;:0},\\\&quot;content\\\&quot;:\\\&quot;***\\\&quot;}\&quot;   }   &#x60;&#x60;&#x60; - type&#x3D;2 用户入场   content定义：     * user:用户，json     举例：   &#x60;&#x60;&#x60;json   {     \&quot;timestamp\&quot;: 1694481227655,     \&quot;type\&quot;: 2,     \&quot;content\&quot;: \&quot;{\\\&quot;user\\\&quot;:{\\\&quot;userId\\\&quot;:\\\&quot;2978899271\\\&quot;,\\\&quot;name\\\&quot;:\\\&quot;***\\\&quot;,\\\&quot;level\\\&quot;:1,\\\&quot;badge\\\&quot;:\\\&quot;\\\&quot;,\\\&quot;badgeLevel\\\&quot;:0}}\&quot;   }   &#x60;&#x60;&#x60; - type&#x3D;3 用户点赞    content定义：     * user：用户，json     举例：   &#x60;&#x60;&#x60;json   {     \&quot;timestamp\&quot;: 1694481227655,     \&quot;type\&quot;: 2,     \&quot;content\&quot;: \&quot;{\\\&quot;user\\\&quot;:{\\\&quot;userId\\\&quot;:\\\&quot;2978899271\\\&quot;,\\\&quot;name\\\&quot;:\\\&quot;***\\\&quot;,\\\&quot;level\\\&quot;:1,\\\&quot;badge\\\&quot;:\\\&quot;\\\&quot;,\\\&quot;badgeLevel\\\&quot;:0}}\&quot;   }   &#x60;&#x60;&#x60; - type&#x3D;4 用户送礼   content定义：     * user：用户，json     * gift：礼物信息,json     gift定义：     * giftName：礼物名称，string     * giftNum：礼物数量，int     * totalValue：此处礼物总价值，int     * giftValue：单个礼物价值，int     举例：   &#x60;&#x60;&#x60;json   {     \&quot;timestamp\&quot;: 1690531652862,     \&quot;type\&quot;: 4,     \&quot;content\&quot;: \&quot;{\\\&quot;gift\\\&quot;:{\\\&quot;giftName\\\&quot;:\\\&quot;小星星\\\&quot;,\\\&quot;giftNum\\\&quot;:10,\\\&quot;totalValue\\\&quot;:10,\\\&quot;giftValue\\\&quot;:3},\\\&quot;user\\\&quot;:{\\\&quot;userId\\\&quot;:\\\&quot;douyin_95882940927\\\&quot;,\\\&quot;name\\\&quot;:\\\&quot;纯爱战士熙熙\\\&quot;,\\\&quot;level\\\&quot;:2,\\\&quot;badge\\\&quot;:\\\&quot;\\\&quot;,\\\&quot;badgeLevel\\\&quot;:0}}\&quot;   }   &#x60;&#x60;&#x60; - type&#x3D;5 用户订阅    暂未使用 - type&#x3D;6 房间观看人数   content定义：     * numberOfViewers：房间观看人数，int     举例：   &#x60;&#x60;&#x60;json   {     \&quot;timestamp\&quot;: 1694481236886,     \&quot;type\&quot;: 6,     \&quot;content\&quot;: \&quot;{\\\&quot;numberOfViewers\\\&quot;:5466}\&quot;   }   &#x60;&#x60;&#x60;
        :type content: str
        """
        
        

        self._timestamp = None
        self._type = None
        self._content = None
        self.discriminator = None

        self.timestamp = timestamp
        if type is not None:
            self.type = type
        if content is not None:
            self.content = content

    @property
    def timestamp(self):
        r"""Gets the timestamp of this LiveEvent.

        **参数解释**： 事件戳。从1970-01-01 00:00:00:000开始的毫秒数

        :return: The timestamp of this LiveEvent.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this LiveEvent.

        **参数解释**： 事件戳。从1970-01-01 00:00:00:000开始的毫秒数

        :param timestamp: The timestamp of this LiveEvent.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def type(self):
        r"""Gets the type of this LiveEvent.

        **参数解释**： 事件类型。 * 1 弹幕信息 * 2 用户入场 * 3 用户点赞 * 4 用户送礼 * 5 用户订阅\\关注 * 6 房间观看人数

        :return: The type of this LiveEvent.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this LiveEvent.

        **参数解释**： 事件类型。 * 1 弹幕信息 * 2 用户入场 * 3 用户点赞 * 4 用户送礼 * 5 用户订阅\\关注 * 6 房间观看人数

        :param type: The type of this LiveEvent.
        :type type: int
        """
        self._type = type

    @property
    def content(self):
        r"""Gets the content of this LiveEvent.

        事件内容。 事件类型不同，content内容也不同，定义如下所示： - type=1 弹幕信息   content定义：     * user:用户，json     * content: string,弹幕内容     user定义：     * userId：用户id，string     * name：用户姓名，string     * level：用户平台等级，int     * badge：用户牌子名称，string     * badgeLevel：牌子等级，int     举例：   ```json   {     \"timestamp\": 1694481224245,     \"type\": 1,     \"content\": \"{\\\"user\\\":{\\\"userId\\\":\\\"2027271526\\\",\\\"name\\\":\\\"***\\\",\\\"level\\\":17,\\\"badge\\\":\\\"\\\",\\\"badgeLevel\\\":0},\\\"content\\\":\\\"***\\\"}\"   }   ``` - type=2 用户入场   content定义：     * user:用户，json     举例：   ```json   {     \"timestamp\": 1694481227655,     \"type\": 2,     \"content\": \"{\\\"user\\\":{\\\"userId\\\":\\\"2978899271\\\",\\\"name\\\":\\\"***\\\",\\\"level\\\":1,\\\"badge\\\":\\\"\\\",\\\"badgeLevel\\\":0}}\"   }   ``` - type=3 用户点赞    content定义：     * user：用户，json     举例：   ```json   {     \"timestamp\": 1694481227655,     \"type\": 2,     \"content\": \"{\\\"user\\\":{\\\"userId\\\":\\\"2978899271\\\",\\\"name\\\":\\\"***\\\",\\\"level\\\":1,\\\"badge\\\":\\\"\\\",\\\"badgeLevel\\\":0}}\"   }   ``` - type=4 用户送礼   content定义：     * user：用户，json     * gift：礼物信息,json     gift定义：     * giftName：礼物名称，string     * giftNum：礼物数量，int     * totalValue：此处礼物总价值，int     * giftValue：单个礼物价值，int     举例：   ```json   {     \"timestamp\": 1690531652862,     \"type\": 4,     \"content\": \"{\\\"gift\\\":{\\\"giftName\\\":\\\"小星星\\\",\\\"giftNum\\\":10,\\\"totalValue\\\":10,\\\"giftValue\\\":3},\\\"user\\\":{\\\"userId\\\":\\\"douyin_95882940927\\\",\\\"name\\\":\\\"纯爱战士熙熙\\\",\\\"level\\\":2,\\\"badge\\\":\\\"\\\",\\\"badgeLevel\\\":0}}\"   }   ``` - type=5 用户订阅    暂未使用 - type=6 房间观看人数   content定义：     * numberOfViewers：房间观看人数，int     举例：   ```json   {     \"timestamp\": 1694481236886,     \"type\": 6,     \"content\": \"{\\\"numberOfViewers\\\":5466}\"   }   ```

        :return: The content of this LiveEvent.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        r"""Sets the content of this LiveEvent.

        事件内容。 事件类型不同，content内容也不同，定义如下所示： - type=1 弹幕信息   content定义：     * user:用户，json     * content: string,弹幕内容     user定义：     * userId：用户id，string     * name：用户姓名，string     * level：用户平台等级，int     * badge：用户牌子名称，string     * badgeLevel：牌子等级，int     举例：   ```json   {     \"timestamp\": 1694481224245,     \"type\": 1,     \"content\": \"{\\\"user\\\":{\\\"userId\\\":\\\"2027271526\\\",\\\"name\\\":\\\"***\\\",\\\"level\\\":17,\\\"badge\\\":\\\"\\\",\\\"badgeLevel\\\":0},\\\"content\\\":\\\"***\\\"}\"   }   ``` - type=2 用户入场   content定义：     * user:用户，json     举例：   ```json   {     \"timestamp\": 1694481227655,     \"type\": 2,     \"content\": \"{\\\"user\\\":{\\\"userId\\\":\\\"2978899271\\\",\\\"name\\\":\\\"***\\\",\\\"level\\\":1,\\\"badge\\\":\\\"\\\",\\\"badgeLevel\\\":0}}\"   }   ``` - type=3 用户点赞    content定义：     * user：用户，json     举例：   ```json   {     \"timestamp\": 1694481227655,     \"type\": 2,     \"content\": \"{\\\"user\\\":{\\\"userId\\\":\\\"2978899271\\\",\\\"name\\\":\\\"***\\\",\\\"level\\\":1,\\\"badge\\\":\\\"\\\",\\\"badgeLevel\\\":0}}\"   }   ``` - type=4 用户送礼   content定义：     * user：用户，json     * gift：礼物信息,json     gift定义：     * giftName：礼物名称，string     * giftNum：礼物数量，int     * totalValue：此处礼物总价值，int     * giftValue：单个礼物价值，int     举例：   ```json   {     \"timestamp\": 1690531652862,     \"type\": 4,     \"content\": \"{\\\"gift\\\":{\\\"giftName\\\":\\\"小星星\\\",\\\"giftNum\\\":10,\\\"totalValue\\\":10,\\\"giftValue\\\":3},\\\"user\\\":{\\\"userId\\\":\\\"douyin_95882940927\\\",\\\"name\\\":\\\"纯爱战士熙熙\\\",\\\"level\\\":2,\\\"badge\\\":\\\"\\\",\\\"badgeLevel\\\":0}}\"   }   ``` - type=5 用户订阅    暂未使用 - type=6 房间观看人数   content定义：     * numberOfViewers：房间观看人数，int     举例：   ```json   {     \"timestamp\": 1694481236886,     \"type\": 6,     \"content\": \"{\\\"numberOfViewers\\\":5466}\"   }   ```

        :param content: The content of this LiveEvent.
        :type content: str
        """
        self._content = content

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
        if not isinstance(other, LiveEvent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
