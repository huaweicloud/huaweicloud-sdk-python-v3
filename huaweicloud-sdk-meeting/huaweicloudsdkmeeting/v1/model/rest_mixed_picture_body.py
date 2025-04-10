# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestMixedPictureBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'manual_set': 'int',
        'image_type': 'str',
        'subscriber_in_pics': 'list[SubscriberInPic]',
        'switch_time': 'int'
    }

    attribute_map = {
        'manual_set': 'manualSet',
        'image_type': 'imageType',
        'subscriber_in_pics': 'subscriberInPics',
        'switch_time': 'switchTime'
    }

    def __init__(self, manual_set=None, image_type=None, subscriber_in_pics=None, switch_time=None):
        r"""RestMixedPictureBody

        The model defined in huaweicloud sdk

        :param manual_set: 是否为手工设置多画面。 - 0: 系统自动多画面 - 1: 手工设置多画面
        :type manual_set: int
        :param image_type: 多画面数目。手工设置多画面时有效。 - Single: 单画面 - Two: 二画面 - Three: 三画面 - Four: 四画面 - Six: 六画面 - Nine: 九画面 - Sixteen: 十六画面
        :type image_type: str
        :param subscriber_in_pics: 子画面列表（手工设置多画面时必填）。
        :type subscriber_in_pics: list[:class:`huaweicloudsdkmeeting.v1.SubscriberInPic`]
        :param switch_time: 表示轮询间隔。单位：秒。 当同一个子画面中包含有多个与会者时，此参数有效。
        :type switch_time: int
        """
        
        

        self._manual_set = None
        self._image_type = None
        self._subscriber_in_pics = None
        self._switch_time = None
        self.discriminator = None

        self.manual_set = manual_set
        if image_type is not None:
            self.image_type = image_type
        if subscriber_in_pics is not None:
            self.subscriber_in_pics = subscriber_in_pics
        if switch_time is not None:
            self.switch_time = switch_time

    @property
    def manual_set(self):
        r"""Gets the manual_set of this RestMixedPictureBody.

        是否为手工设置多画面。 - 0: 系统自动多画面 - 1: 手工设置多画面

        :return: The manual_set of this RestMixedPictureBody.
        :rtype: int
        """
        return self._manual_set

    @manual_set.setter
    def manual_set(self, manual_set):
        r"""Sets the manual_set of this RestMixedPictureBody.

        是否为手工设置多画面。 - 0: 系统自动多画面 - 1: 手工设置多画面

        :param manual_set: The manual_set of this RestMixedPictureBody.
        :type manual_set: int
        """
        self._manual_set = manual_set

    @property
    def image_type(self):
        r"""Gets the image_type of this RestMixedPictureBody.

        多画面数目。手工设置多画面时有效。 - Single: 单画面 - Two: 二画面 - Three: 三画面 - Four: 四画面 - Six: 六画面 - Nine: 九画面 - Sixteen: 十六画面

        :return: The image_type of this RestMixedPictureBody.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        r"""Sets the image_type of this RestMixedPictureBody.

        多画面数目。手工设置多画面时有效。 - Single: 单画面 - Two: 二画面 - Three: 三画面 - Four: 四画面 - Six: 六画面 - Nine: 九画面 - Sixteen: 十六画面

        :param image_type: The image_type of this RestMixedPictureBody.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def subscriber_in_pics(self):
        r"""Gets the subscriber_in_pics of this RestMixedPictureBody.

        子画面列表（手工设置多画面时必填）。

        :return: The subscriber_in_pics of this RestMixedPictureBody.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.SubscriberInPic`]
        """
        return self._subscriber_in_pics

    @subscriber_in_pics.setter
    def subscriber_in_pics(self, subscriber_in_pics):
        r"""Sets the subscriber_in_pics of this RestMixedPictureBody.

        子画面列表（手工设置多画面时必填）。

        :param subscriber_in_pics: The subscriber_in_pics of this RestMixedPictureBody.
        :type subscriber_in_pics: list[:class:`huaweicloudsdkmeeting.v1.SubscriberInPic`]
        """
        self._subscriber_in_pics = subscriber_in_pics

    @property
    def switch_time(self):
        r"""Gets the switch_time of this RestMixedPictureBody.

        表示轮询间隔。单位：秒。 当同一个子画面中包含有多个与会者时，此参数有效。

        :return: The switch_time of this RestMixedPictureBody.
        :rtype: int
        """
        return self._switch_time

    @switch_time.setter
    def switch_time(self, switch_time):
        r"""Sets the switch_time of this RestMixedPictureBody.

        表示轮询间隔。单位：秒。 当同一个子画面中包含有多个与会者时，此参数有效。

        :param switch_time: The switch_time of this RestMixedPictureBody.
        :type switch_time: int
        """
        self._switch_time = switch_time

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
        if not isinstance(other, RestMixedPictureBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
