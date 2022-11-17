# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MultiPicDisplayDO:

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
        'subscriber_in_pics': 'list[PicInfoNotify]',
        'switch_time': 'str',
        'pic_layout_info': 'PicLayoutInfo'
    }

    attribute_map = {
        'manual_set': 'manualSet',
        'image_type': 'imageType',
        'subscriber_in_pics': 'subscriberInPics',
        'switch_time': 'switchTime',
        'pic_layout_info': 'picLayoutInfo'
    }

    def __init__(self, manual_set=None, image_type=None, subscriber_in_pics=None, switch_time=None, pic_layout_info=None):
        """MultiPicDisplayDO

        The model defined in huaweicloud sdk

        :param manual_set: 是否为手工设置多画面。 * 0 ：系统自动多画面 * 1 ：手工设置多画面 
        :type manual_set: int
        :param image_type: 画面类型。取值范围: * Single: 单画面 * Two: 二画面 * Three: 三画面， Three-2: 三画面-2， Three-3: 三画面-3， Three-4: 三画面-4 * Four: 四画面， Four-2: 四画面-2， Four-3: 四画面-3 * Five: 五画面， Five-2: 五画面-2 * Six: 六画面， Six-2: 六画面-2， Six-3: 六画面-3， Six-4: 六画面-4， Six-5: 六画面-5 * Seven: 七画面， Seven-2: 七画面-2， Seven-3: 七画面-3， Seven-4: 七画面-4 * Eight: 八画面， Eight-2: 八画面-2， Eight-3: 八画面-3， Eight-4: 八画面-4 * Nine: 九画面 * Ten: 十画面， Ten-2: 十画面-2， Ten-3: 十画面-3， Ten-4: 十画面-4， Ten-5: 十画面-5， Ten-6: 十画面-6 * Thirteen: 十三画面， Thirteen-2: 十三画面-2， Thirteen-3: 十三画面-3，Thirteen-4: 十三画面-4， Thirteen-5: 十三画面-5， ThirteenR: 十三画面R， ThirteenM: 十三画面M * Sixteen: 十六画面 * Seventeen: 十七画面 * Twenty-Five: 二十五画面 * Custom: 自定义多画面（当前不支持） 
        :type image_type: str
        :param subscriber_in_pics: 子画面列表。
        :type subscriber_in_pics: list[:class:`huaweicloudsdkmeeting.v1.PicInfoNotify`]
        :param switch_time: 表示轮询间隔，单位：秒。当同一个子画面中包含有多个视频源时，此参数有效。
        :type switch_time: str
        :param pic_layout_info: 
        :type pic_layout_info: :class:`huaweicloudsdkmeeting.v1.PicLayoutInfo`
        """
        
        

        self._manual_set = None
        self._image_type = None
        self._subscriber_in_pics = None
        self._switch_time = None
        self._pic_layout_info = None
        self.discriminator = None

        if manual_set is not None:
            self.manual_set = manual_set
        if image_type is not None:
            self.image_type = image_type
        if subscriber_in_pics is not None:
            self.subscriber_in_pics = subscriber_in_pics
        if switch_time is not None:
            self.switch_time = switch_time
        if pic_layout_info is not None:
            self.pic_layout_info = pic_layout_info

    @property
    def manual_set(self):
        """Gets the manual_set of this MultiPicDisplayDO.

        是否为手工设置多画面。 * 0 ：系统自动多画面 * 1 ：手工设置多画面 

        :return: The manual_set of this MultiPicDisplayDO.
        :rtype: int
        """
        return self._manual_set

    @manual_set.setter
    def manual_set(self, manual_set):
        """Sets the manual_set of this MultiPicDisplayDO.

        是否为手工设置多画面。 * 0 ：系统自动多画面 * 1 ：手工设置多画面 

        :param manual_set: The manual_set of this MultiPicDisplayDO.
        :type manual_set: int
        """
        self._manual_set = manual_set

    @property
    def image_type(self):
        """Gets the image_type of this MultiPicDisplayDO.

        画面类型。取值范围: * Single: 单画面 * Two: 二画面 * Three: 三画面， Three-2: 三画面-2， Three-3: 三画面-3， Three-4: 三画面-4 * Four: 四画面， Four-2: 四画面-2， Four-3: 四画面-3 * Five: 五画面， Five-2: 五画面-2 * Six: 六画面， Six-2: 六画面-2， Six-3: 六画面-3， Six-4: 六画面-4， Six-5: 六画面-5 * Seven: 七画面， Seven-2: 七画面-2， Seven-3: 七画面-3， Seven-4: 七画面-4 * Eight: 八画面， Eight-2: 八画面-2， Eight-3: 八画面-3， Eight-4: 八画面-4 * Nine: 九画面 * Ten: 十画面， Ten-2: 十画面-2， Ten-3: 十画面-3， Ten-4: 十画面-4， Ten-5: 十画面-5， Ten-6: 十画面-6 * Thirteen: 十三画面， Thirteen-2: 十三画面-2， Thirteen-3: 十三画面-3，Thirteen-4: 十三画面-4， Thirteen-5: 十三画面-5， ThirteenR: 十三画面R， ThirteenM: 十三画面M * Sixteen: 十六画面 * Seventeen: 十七画面 * Twenty-Five: 二十五画面 * Custom: 自定义多画面（当前不支持） 

        :return: The image_type of this MultiPicDisplayDO.
        :rtype: str
        """
        return self._image_type

    @image_type.setter
    def image_type(self, image_type):
        """Sets the image_type of this MultiPicDisplayDO.

        画面类型。取值范围: * Single: 单画面 * Two: 二画面 * Three: 三画面， Three-2: 三画面-2， Three-3: 三画面-3， Three-4: 三画面-4 * Four: 四画面， Four-2: 四画面-2， Four-3: 四画面-3 * Five: 五画面， Five-2: 五画面-2 * Six: 六画面， Six-2: 六画面-2， Six-3: 六画面-3， Six-4: 六画面-4， Six-5: 六画面-5 * Seven: 七画面， Seven-2: 七画面-2， Seven-3: 七画面-3， Seven-4: 七画面-4 * Eight: 八画面， Eight-2: 八画面-2， Eight-3: 八画面-3， Eight-4: 八画面-4 * Nine: 九画面 * Ten: 十画面， Ten-2: 十画面-2， Ten-3: 十画面-3， Ten-4: 十画面-4， Ten-5: 十画面-5， Ten-6: 十画面-6 * Thirteen: 十三画面， Thirteen-2: 十三画面-2， Thirteen-3: 十三画面-3，Thirteen-4: 十三画面-4， Thirteen-5: 十三画面-5， ThirteenR: 十三画面R， ThirteenM: 十三画面M * Sixteen: 十六画面 * Seventeen: 十七画面 * Twenty-Five: 二十五画面 * Custom: 自定义多画面（当前不支持） 

        :param image_type: The image_type of this MultiPicDisplayDO.
        :type image_type: str
        """
        self._image_type = image_type

    @property
    def subscriber_in_pics(self):
        """Gets the subscriber_in_pics of this MultiPicDisplayDO.

        子画面列表。

        :return: The subscriber_in_pics of this MultiPicDisplayDO.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.PicInfoNotify`]
        """
        return self._subscriber_in_pics

    @subscriber_in_pics.setter
    def subscriber_in_pics(self, subscriber_in_pics):
        """Sets the subscriber_in_pics of this MultiPicDisplayDO.

        子画面列表。

        :param subscriber_in_pics: The subscriber_in_pics of this MultiPicDisplayDO.
        :type subscriber_in_pics: list[:class:`huaweicloudsdkmeeting.v1.PicInfoNotify`]
        """
        self._subscriber_in_pics = subscriber_in_pics

    @property
    def switch_time(self):
        """Gets the switch_time of this MultiPicDisplayDO.

        表示轮询间隔，单位：秒。当同一个子画面中包含有多个视频源时，此参数有效。

        :return: The switch_time of this MultiPicDisplayDO.
        :rtype: str
        """
        return self._switch_time

    @switch_time.setter
    def switch_time(self, switch_time):
        """Sets the switch_time of this MultiPicDisplayDO.

        表示轮询间隔，单位：秒。当同一个子画面中包含有多个视频源时，此参数有效。

        :param switch_time: The switch_time of this MultiPicDisplayDO.
        :type switch_time: str
        """
        self._switch_time = switch_time

    @property
    def pic_layout_info(self):
        """Gets the pic_layout_info of this MultiPicDisplayDO.

        :return: The pic_layout_info of this MultiPicDisplayDO.
        :rtype: :class:`huaweicloudsdkmeeting.v1.PicLayoutInfo`
        """
        return self._pic_layout_info

    @pic_layout_info.setter
    def pic_layout_info(self, pic_layout_info):
        """Sets the pic_layout_info of this MultiPicDisplayDO.

        :param pic_layout_info: The pic_layout_info of this MultiPicDisplayDO.
        :type pic_layout_info: :class:`huaweicloudsdkmeeting.v1.PicLayoutInfo`
        """
        self._pic_layout_info = pic_layout_info

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
        if not isinstance(other, MultiPicDisplayDO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
