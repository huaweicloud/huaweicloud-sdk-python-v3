# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestPicLayout:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'switch_time': 'int',
        'pic_num': 'int',
        'lay_out_name': 'str',
        'image_type': 'str',
        'uuid': 'str',
        'subscriber_in_pics': 'list[PicInfoNotify]'
    }

    attribute_map = {
        'switch_time': 'switchTime',
        'pic_num': 'picNum',
        'lay_out_name': 'layOutName',
        'image_type': 'imageType',
        'uuid': 'uuid',
        'subscriber_in_pics': 'subscriberInPics'
    }

    def __init__(self, switch_time=None, pic_num=None, lay_out_name=None, image_type=None, uuid=None, subscriber_in_pics=None):
        """RestPicLayout

        The model defined in huaweicloud sdk

        :param switch_time: 多画面轮询时间，单位秒。
        :type switch_time: int
        :param pic_num: 多画面画面数量。
        :type pic_num: int
        :param lay_out_name: 多画面布局名称。
        :type lay_out_name: str
        :param image_type: 画面类型。
        :type image_type: str
        :param uuid: 布局UUID。
        :type uuid: str
        :param subscriber_in_pics: 子画面列表。
        :type subscriber_in_pics: list[:class:`huaweicloudsdkmeeting.v1.PicInfoNotify`]
        """
        
        

        self._switch_time = None
        self._pic_num = None
        self._lay_out_name = None
        self._image_type = None
        self._uuid = None
        self._subscriber_in_pics = None
        self.discriminator = None

        if switch_time is not None:
            self.switch_time = switch_time
        if pic_num is not None:
            self.pic_num = pic_num
        if lay_out_name is not None:
            self.lay_out_name = lay_out_name
        if image_type is not None:
            self.image_type = image_type
        if uuid is not None:
            self.uuid = uuid
        if subscriber_in_pics is not None:
            self.subscriber_in_pics = subscriber_in_pics

    @property
    def switch_time(self):
        """Gets the switch_time of this RestPicLayout.

        多画面轮询时间，单位秒。

        :return: The switch_time of this RestPicLayout.
        :rtype: int
        """
        return self._switch_time

    @switch_time.setter
    def switch_time(self, switch_time):
        """Sets the switch_time of this RestPicLayout.

        多画面轮询时间，单位秒。

        :param switch_time: The switch_time of this RestPicLayout.
        :type switch_time: int
        """
        self._switch_time = switch_time

    @property
    def pic_num(self):
        """Gets the pic_num of this RestPicLayout.

        多画面画面数量。

        :return: The pic_num of this RestPicLayout.
        :rtype: int
        """
        return self._pic_num

    @pic_num.setter
    def pic_num(self, pic_num):
        """Sets the pic_num of this RestPicLayout.

        多画面画面数量。

        :param pic_num: The pic_num of this RestPicLayout.
        :type pic_num: int
        """
        self._pic_num = pic_num

    @property
    def lay_out_name(self):
        """Gets the lay_out_name of this RestPicLayout.

        多画面布局名称。

        :return: The lay_out_name of this RestPicLayout.
        :rtype: str
        """
        return self._lay_out_name

    @lay_out_name.setter
    def lay_out_name(self, lay_out_name):
        """Sets the lay_out_name of this RestPicLayout.

        多画面布局名称。

        :param lay_out_name: The lay_out_name of this RestPicLayout.
        :type lay_out_name: str
        """
        self._lay_out_name = lay_out_name

    @property
    def image_type(self):
        """Gets the image_type of this RestPicLayout.

        画面类型。

        :return: The image_type of this RestPicLayout.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        """Sets the image_type of this RestPicLayout.

        画面类型。

        :param image_type: The image_type of this RestPicLayout.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def uuid(self):
        """Gets the uuid of this RestPicLayout.

        布局UUID。

        :return: The uuid of this RestPicLayout.
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this RestPicLayout.

        布局UUID。

        :param uuid: The uuid of this RestPicLayout.
        :type uuid: str
        """
        self._uuid = uuid

    @property
    def subscriber_in_pics(self):
        """Gets the subscriber_in_pics of this RestPicLayout.

        子画面列表。

        :return: The subscriber_in_pics of this RestPicLayout.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.PicInfoNotify`]
        """
        return self._subscriber_in_pics

    @subscriber_in_pics.setter
    def subscriber_in_pics(self, subscriber_in_pics):
        """Sets the subscriber_in_pics of this RestPicLayout.

        子画面列表。

        :param subscriber_in_pics: The subscriber_in_pics of this RestPicLayout.
        :type subscriber_in_pics: list[:class:`huaweicloudsdkmeeting.v1.PicInfoNotify`]
        """
        self._subscriber_in_pics = subscriber_in_pics

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
        if not isinstance(other, RestPicLayout):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
