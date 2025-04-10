# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MixLayoutPane:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'user_id': 'str',
        'video_type': 'str',
        'x': 'float',
        'y': 'float',
        'width': 'float',
        'height': 'float',
        'zorder': 'int',
        'crop_mode': 'str',
        'filling_policy': 'str'
    }

    attribute_map = {
        'id': 'id',
        'user_id': 'user_id',
        'video_type': 'video_type',
        'x': 'x',
        'y': 'y',
        'width': 'width',
        'height': 'height',
        'zorder': 'zorder',
        'crop_mode': 'crop_mode',
        'filling_policy': 'filling_policy'
    }

    def __init__(self, id=None, user_id=None, video_type=None, x=None, y=None, width=None, height=None, zorder=None, crop_mode=None, filling_policy=None):
        r"""MixLayoutPane

        The model defined in huaweicloud sdk

        :param id: 窗口id，从1开始编号
        :type id: int
        :param user_id: 加入房间的用户id
        :type user_id: str
        :param video_type: 标识视频流的类型，可选摄像头流或者屏幕分享流。  - CAMERASTREAM：摄像头视频流 - SCREENSTREAM：屏幕分享视频流  默认为CAMERASTREAM。 
        :type video_type: str
        :param x: 坐标x，归一化百分比，画布上该画面左上角的横坐标的相对值，范围是 [0.0,1.0]。从左到右布局，0.0在最左端，1.0在最右端，小数取值范围在float内，自定义布局场景下填写本字段。
        :type x: float
        :param y: 坐标y，归一化百分比，画布上该画面左上角的纵坐标的相对值，范围是 [0.0,1.0]。从上到下布局，0.0在最上端，1.0在最下端，小数取值范围在float内，自定义布局场景下填写本字段。
        :type y: float
        :param width: 窗格宽，归一化百分比，小数取值范围在float内，自定义布局场景下填写本字段。
        :type width: float
        :param height: 窗格高，归一化百分比，小数取值范围在float内，自定义布局场景下填写本字段。
        :type height: float
        :param zorder: 叠放顺序，0为最底层，1层在0层之上，以此类推，最大支持25层，自定义布局场景下填写本字段。
        :type zorder: int
        :param crop_mode: 裁剪模式，自定义布局场景下填写本字段，支持两种模式：   - KEEP_RATIO_PADDING ：保持比例留边。   - KEEP_RATIO_CROP ：保持比例裁剪。 
        :type crop_mode: str
        :param filling_policy: 填充策略，仅限屏幕共享模板(包括screen_share_right、screen_share_left)场景下填写本字段，支持两种模式：   - FIXED_USER ：固定用户填充。   - SHARED_SCREEN ：共享屏幕填充。 
        :type filling_policy: str
        """
        
        

        self._id = None
        self._user_id = None
        self._video_type = None
        self._x = None
        self._y = None
        self._width = None
        self._height = None
        self._zorder = None
        self._crop_mode = None
        self._filling_policy = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if user_id is not None:
            self.user_id = user_id
        if video_type is not None:
            self.video_type = video_type
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if zorder is not None:
            self.zorder = zorder
        if crop_mode is not None:
            self.crop_mode = crop_mode
        if filling_policy is not None:
            self.filling_policy = filling_policy

    @property
    def id(self):
        r"""Gets the id of this MixLayoutPane.

        窗口id，从1开始编号

        :return: The id of this MixLayoutPane.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this MixLayoutPane.

        窗口id，从1开始编号

        :param id: The id of this MixLayoutPane.
        :type id: int
        """
        self._id = id

    @property
    def user_id(self):
        r"""Gets the user_id of this MixLayoutPane.

        加入房间的用户id

        :return: The user_id of this MixLayoutPane.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this MixLayoutPane.

        加入房间的用户id

        :param user_id: The user_id of this MixLayoutPane.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def video_type(self):
        r"""Gets the video_type of this MixLayoutPane.

        标识视频流的类型，可选摄像头流或者屏幕分享流。  - CAMERASTREAM：摄像头视频流 - SCREENSTREAM：屏幕分享视频流  默认为CAMERASTREAM。 

        :return: The video_type of this MixLayoutPane.
        :rtype: str
        """
        return self._video_type

    @video_type.setter
    def video_type(self, video_type):
        r"""Sets the video_type of this MixLayoutPane.

        标识视频流的类型，可选摄像头流或者屏幕分享流。  - CAMERASTREAM：摄像头视频流 - SCREENSTREAM：屏幕分享视频流  默认为CAMERASTREAM。 

        :param video_type: The video_type of this MixLayoutPane.
        :type video_type: str
        """
        self._video_type = video_type

    @property
    def x(self):
        r"""Gets the x of this MixLayoutPane.

        坐标x，归一化百分比，画布上该画面左上角的横坐标的相对值，范围是 [0.0,1.0]。从左到右布局，0.0在最左端，1.0在最右端，小数取值范围在float内，自定义布局场景下填写本字段。

        :return: The x of this MixLayoutPane.
        :rtype: float
        """
        return self._x

    @x.setter
    def x(self, x):
        r"""Sets the x of this MixLayoutPane.

        坐标x，归一化百分比，画布上该画面左上角的横坐标的相对值，范围是 [0.0,1.0]。从左到右布局，0.0在最左端，1.0在最右端，小数取值范围在float内，自定义布局场景下填写本字段。

        :param x: The x of this MixLayoutPane.
        :type x: float
        """
        self._x = x

    @property
    def y(self):
        r"""Gets the y of this MixLayoutPane.

        坐标y，归一化百分比，画布上该画面左上角的纵坐标的相对值，范围是 [0.0,1.0]。从上到下布局，0.0在最上端，1.0在最下端，小数取值范围在float内，自定义布局场景下填写本字段。

        :return: The y of this MixLayoutPane.
        :rtype: float
        """
        return self._y

    @y.setter
    def y(self, y):
        r"""Sets the y of this MixLayoutPane.

        坐标y，归一化百分比，画布上该画面左上角的纵坐标的相对值，范围是 [0.0,1.0]。从上到下布局，0.0在最上端，1.0在最下端，小数取值范围在float内，自定义布局场景下填写本字段。

        :param y: The y of this MixLayoutPane.
        :type y: float
        """
        self._y = y

    @property
    def width(self):
        r"""Gets the width of this MixLayoutPane.

        窗格宽，归一化百分比，小数取值范围在float内，自定义布局场景下填写本字段。

        :return: The width of this MixLayoutPane.
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        r"""Sets the width of this MixLayoutPane.

        窗格宽，归一化百分比，小数取值范围在float内，自定义布局场景下填写本字段。

        :param width: The width of this MixLayoutPane.
        :type width: float
        """
        self._width = width

    @property
    def height(self):
        r"""Gets the height of this MixLayoutPane.

        窗格高，归一化百分比，小数取值范围在float内，自定义布局场景下填写本字段。

        :return: The height of this MixLayoutPane.
        :rtype: float
        """
        return self._height

    @height.setter
    def height(self, height):
        r"""Sets the height of this MixLayoutPane.

        窗格高，归一化百分比，小数取值范围在float内，自定义布局场景下填写本字段。

        :param height: The height of this MixLayoutPane.
        :type height: float
        """
        self._height = height

    @property
    def zorder(self):
        r"""Gets the zorder of this MixLayoutPane.

        叠放顺序，0为最底层，1层在0层之上，以此类推，最大支持25层，自定义布局场景下填写本字段。

        :return: The zorder of this MixLayoutPane.
        :rtype: int
        """
        return self._zorder

    @zorder.setter
    def zorder(self, zorder):
        r"""Sets the zorder of this MixLayoutPane.

        叠放顺序，0为最底层，1层在0层之上，以此类推，最大支持25层，自定义布局场景下填写本字段。

        :param zorder: The zorder of this MixLayoutPane.
        :type zorder: int
        """
        self._zorder = zorder

    @property
    def crop_mode(self):
        r"""Gets the crop_mode of this MixLayoutPane.

        裁剪模式，自定义布局场景下填写本字段，支持两种模式：   - KEEP_RATIO_PADDING ：保持比例留边。   - KEEP_RATIO_CROP ：保持比例裁剪。 

        :return: The crop_mode of this MixLayoutPane.
        :rtype: str
        """
        return self._crop_mode

    @crop_mode.setter
    def crop_mode(self, crop_mode):
        r"""Sets the crop_mode of this MixLayoutPane.

        裁剪模式，自定义布局场景下填写本字段，支持两种模式：   - KEEP_RATIO_PADDING ：保持比例留边。   - KEEP_RATIO_CROP ：保持比例裁剪。 

        :param crop_mode: The crop_mode of this MixLayoutPane.
        :type crop_mode: str
        """
        self._crop_mode = crop_mode

    @property
    def filling_policy(self):
        r"""Gets the filling_policy of this MixLayoutPane.

        填充策略，仅限屏幕共享模板(包括screen_share_right、screen_share_left)场景下填写本字段，支持两种模式：   - FIXED_USER ：固定用户填充。   - SHARED_SCREEN ：共享屏幕填充。 

        :return: The filling_policy of this MixLayoutPane.
        :rtype: str
        """
        return self._filling_policy

    @filling_policy.setter
    def filling_policy(self, filling_policy):
        r"""Sets the filling_policy of this MixLayoutPane.

        填充策略，仅限屏幕共享模板(包括screen_share_right、screen_share_left)场景下填写本字段，支持两种模式：   - FIXED_USER ：固定用户填充。   - SHARED_SCREEN ：共享屏幕填充。 

        :param filling_policy: The filling_policy of this MixLayoutPane.
        :type filling_policy: str
        """
        self._filling_policy = filling_policy

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
        if not isinstance(other, MixLayoutPane):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
