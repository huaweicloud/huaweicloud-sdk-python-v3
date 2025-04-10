# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateMixParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'layout_template': 'str',
        'background_image': 'str',
        'default_user_background_image': 'str',
        'screen_background_image': 'str',
        'max_idle_time': 'int',
        'layout_panes': 'list[MixLayoutPane]',
        'user_background_images': 'list[MixUserBackgroundImage]'
    }

    attribute_map = {
        'layout_template': 'layout_template',
        'background_image': 'background_image',
        'default_user_background_image': 'default_user_background_image',
        'screen_background_image': 'screen_background_image',
        'max_idle_time': 'max_idle_time',
        'layout_panes': 'layout_panes',
        'user_background_images': 'user_background_images'
    }

    def __init__(self, layout_template=None, background_image=None, default_user_background_image=None, screen_background_image=None, max_idle_time=None, layout_panes=None, user_background_images=None):
        r"""UpdateMixParam

        The model defined in huaweicloud sdk

        :param layout_template: 视频布局模板编号，仅支持自定义模板之间的更新。
        :type layout_template: str
        :param background_image: 画布背景图地址，图片先上传obs。默认使用等比缩放裁剪，保证铺满。格式s3://bucket/object
        :type background_image: str
        :param default_user_background_image: 默认用户背景图地址，图片先上传obs，格式s3://bucket/object。默认使用等比缩放裁剪，保证铺满。
        :type default_user_background_image: str
        :param screen_background_image: 共享屏幕的背景图地址，图片先上传obs，格式s3://bucket/object。  在一大多小的布局场景下，无论大窗是显示非指定用户（屏幕共享人的桌面）还是指定用户的共享桌面，都通过该字段指定背景图。 
        :type screen_background_image: str
        :param max_idle_time: 最长空闲频道时间。  取值范围：[5，43200]，默认值为30。  单位：秒。  如果频道内无连麦方的状态持续超过该时间，录制程序会自动退出。退出后，再次调用start请求，会产生新的录制任务。  连麦方指：joiner或者publisher的用户。 
        :type max_idle_time: int
        :param layout_panes: 需要混流的视频列表。若不需要视频混流，则可不传递该参数。
        :type layout_panes: list[:class:`huaweicloudsdkcloudrtc.v2.MixLayoutPane`]
        :param user_background_images: 指定用户背景图，优先级大于default_user_background_image
        :type user_background_images: list[:class:`huaweicloudsdkcloudrtc.v2.MixUserBackgroundImage`]
        """
        
        

        self._layout_template = None
        self._background_image = None
        self._default_user_background_image = None
        self._screen_background_image = None
        self._max_idle_time = None
        self._layout_panes = None
        self._user_background_images = None
        self.discriminator = None

        if layout_template is not None:
            self.layout_template = layout_template
        if background_image is not None:
            self.background_image = background_image
        if default_user_background_image is not None:
            self.default_user_background_image = default_user_background_image
        if screen_background_image is not None:
            self.screen_background_image = screen_background_image
        if max_idle_time is not None:
            self.max_idle_time = max_idle_time
        if layout_panes is not None:
            self.layout_panes = layout_panes
        if user_background_images is not None:
            self.user_background_images = user_background_images

    @property
    def layout_template(self):
        r"""Gets the layout_template of this UpdateMixParam.

        视频布局模板编号，仅支持自定义模板之间的更新。

        :return: The layout_template of this UpdateMixParam.
        :rtype: str
        """
        return self._layout_template

    @layout_template.setter
    def layout_template(self, layout_template):
        r"""Sets the layout_template of this UpdateMixParam.

        视频布局模板编号，仅支持自定义模板之间的更新。

        :param layout_template: The layout_template of this UpdateMixParam.
        :type layout_template: str
        """
        self._layout_template = layout_template

    @property
    def background_image(self):
        r"""Gets the background_image of this UpdateMixParam.

        画布背景图地址，图片先上传obs。默认使用等比缩放裁剪，保证铺满。格式s3://bucket/object

        :return: The background_image of this UpdateMixParam.
        :rtype: str
        """
        return self._background_image

    @background_image.setter
    def background_image(self, background_image):
        r"""Sets the background_image of this UpdateMixParam.

        画布背景图地址，图片先上传obs。默认使用等比缩放裁剪，保证铺满。格式s3://bucket/object

        :param background_image: The background_image of this UpdateMixParam.
        :type background_image: str
        """
        self._background_image = background_image

    @property
    def default_user_background_image(self):
        r"""Gets the default_user_background_image of this UpdateMixParam.

        默认用户背景图地址，图片先上传obs，格式s3://bucket/object。默认使用等比缩放裁剪，保证铺满。

        :return: The default_user_background_image of this UpdateMixParam.
        :rtype: str
        """
        return self._default_user_background_image

    @default_user_background_image.setter
    def default_user_background_image(self, default_user_background_image):
        r"""Sets the default_user_background_image of this UpdateMixParam.

        默认用户背景图地址，图片先上传obs，格式s3://bucket/object。默认使用等比缩放裁剪，保证铺满。

        :param default_user_background_image: The default_user_background_image of this UpdateMixParam.
        :type default_user_background_image: str
        """
        self._default_user_background_image = default_user_background_image

    @property
    def screen_background_image(self):
        r"""Gets the screen_background_image of this UpdateMixParam.

        共享屏幕的背景图地址，图片先上传obs，格式s3://bucket/object。  在一大多小的布局场景下，无论大窗是显示非指定用户（屏幕共享人的桌面）还是指定用户的共享桌面，都通过该字段指定背景图。 

        :return: The screen_background_image of this UpdateMixParam.
        :rtype: str
        """
        return self._screen_background_image

    @screen_background_image.setter
    def screen_background_image(self, screen_background_image):
        r"""Sets the screen_background_image of this UpdateMixParam.

        共享屏幕的背景图地址，图片先上传obs，格式s3://bucket/object。  在一大多小的布局场景下，无论大窗是显示非指定用户（屏幕共享人的桌面）还是指定用户的共享桌面，都通过该字段指定背景图。 

        :param screen_background_image: The screen_background_image of this UpdateMixParam.
        :type screen_background_image: str
        """
        self._screen_background_image = screen_background_image

    @property
    def max_idle_time(self):
        r"""Gets the max_idle_time of this UpdateMixParam.

        最长空闲频道时间。  取值范围：[5，43200]，默认值为30。  单位：秒。  如果频道内无连麦方的状态持续超过该时间，录制程序会自动退出。退出后，再次调用start请求，会产生新的录制任务。  连麦方指：joiner或者publisher的用户。 

        :return: The max_idle_time of this UpdateMixParam.
        :rtype: int
        """
        return self._max_idle_time

    @max_idle_time.setter
    def max_idle_time(self, max_idle_time):
        r"""Sets the max_idle_time of this UpdateMixParam.

        最长空闲频道时间。  取值范围：[5，43200]，默认值为30。  单位：秒。  如果频道内无连麦方的状态持续超过该时间，录制程序会自动退出。退出后，再次调用start请求，会产生新的录制任务。  连麦方指：joiner或者publisher的用户。 

        :param max_idle_time: The max_idle_time of this UpdateMixParam.
        :type max_idle_time: int
        """
        self._max_idle_time = max_idle_time

    @property
    def layout_panes(self):
        r"""Gets the layout_panes of this UpdateMixParam.

        需要混流的视频列表。若不需要视频混流，则可不传递该参数。

        :return: The layout_panes of this UpdateMixParam.
        :rtype: list[:class:`huaweicloudsdkcloudrtc.v2.MixLayoutPane`]
        """
        return self._layout_panes

    @layout_panes.setter
    def layout_panes(self, layout_panes):
        r"""Sets the layout_panes of this UpdateMixParam.

        需要混流的视频列表。若不需要视频混流，则可不传递该参数。

        :param layout_panes: The layout_panes of this UpdateMixParam.
        :type layout_panes: list[:class:`huaweicloudsdkcloudrtc.v2.MixLayoutPane`]
        """
        self._layout_panes = layout_panes

    @property
    def user_background_images(self):
        r"""Gets the user_background_images of this UpdateMixParam.

        指定用户背景图，优先级大于default_user_background_image

        :return: The user_background_images of this UpdateMixParam.
        :rtype: list[:class:`huaweicloudsdkcloudrtc.v2.MixUserBackgroundImage`]
        """
        return self._user_background_images

    @user_background_images.setter
    def user_background_images(self, user_background_images):
        r"""Sets the user_background_images of this UpdateMixParam.

        指定用户背景图，优先级大于default_user_background_image

        :param user_background_images: The user_background_images of this UpdateMixParam.
        :type user_background_images: list[:class:`huaweicloudsdkcloudrtc.v2.MixUserBackgroundImage`]
        """
        self._user_background_images = user_background_images

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
        if not isinstance(other, UpdateMixParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
