# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VideoConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'background_id': 'str',
        'logo_id': 'str',
        'show_subtitles': 'bool',
        'resolution_type': 'int'
    }

    attribute_map = {
        'background_id': 'background_id',
        'logo_id': 'logo_id',
        'show_subtitles': 'show_subtitles',
        'resolution_type': 'resolution_type'
    }

    def __init__(self, background_id=None, logo_id=None, show_subtitles=None, resolution_type=None):
        r"""VideoConfig

        The model defined in huaweicloud sdk

        :param background_id: 背景id
        :type background_id: str
        :param logo_id: 图标id
        :type logo_id: str
        :param show_subtitles: 是否显示字幕 默认：false
        :type show_subtitles: bool
        :param resolution_type: 画面分辨率： 0: 宽屏landscape（默认） 1: 竖屏portrait
        :type resolution_type: int
        """
        
        

        self._background_id = None
        self._logo_id = None
        self._show_subtitles = None
        self._resolution_type = None
        self.discriminator = None

        self.background_id = background_id
        if logo_id is not None:
            self.logo_id = logo_id
        if show_subtitles is not None:
            self.show_subtitles = show_subtitles
        if resolution_type is not None:
            self.resolution_type = resolution_type

    @property
    def background_id(self):
        r"""Gets the background_id of this VideoConfig.

        背景id

        :return: The background_id of this VideoConfig.
        :rtype: str
        """
        return self._background_id

    @background_id.setter
    def background_id(self, background_id):
        r"""Sets the background_id of this VideoConfig.

        背景id

        :param background_id: The background_id of this VideoConfig.
        :type background_id: str
        """
        self._background_id = background_id

    @property
    def logo_id(self):
        r"""Gets the logo_id of this VideoConfig.

        图标id

        :return: The logo_id of this VideoConfig.
        :rtype: str
        """
        return self._logo_id

    @logo_id.setter
    def logo_id(self, logo_id):
        r"""Sets the logo_id of this VideoConfig.

        图标id

        :param logo_id: The logo_id of this VideoConfig.
        :type logo_id: str
        """
        self._logo_id = logo_id

    @property
    def show_subtitles(self):
        r"""Gets the show_subtitles of this VideoConfig.

        是否显示字幕 默认：false

        :return: The show_subtitles of this VideoConfig.
        :rtype: bool
        """
        return self._show_subtitles

    @show_subtitles.setter
    def show_subtitles(self, show_subtitles):
        r"""Sets the show_subtitles of this VideoConfig.

        是否显示字幕 默认：false

        :param show_subtitles: The show_subtitles of this VideoConfig.
        :type show_subtitles: bool
        """
        self._show_subtitles = show_subtitles

    @property
    def resolution_type(self):
        r"""Gets the resolution_type of this VideoConfig.

        画面分辨率： 0: 宽屏landscape（默认） 1: 竖屏portrait

        :return: The resolution_type of this VideoConfig.
        :rtype: int
        """
        return self._resolution_type

    @resolution_type.setter
    def resolution_type(self, resolution_type):
        r"""Sets the resolution_type of this VideoConfig.

        画面分辨率： 0: 宽屏landscape（默认） 1: 竖屏portrait

        :param resolution_type: The resolution_type of this VideoConfig.
        :type resolution_type: int
        """
        self._resolution_type = resolution_type

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
        if not isinstance(other, VideoConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
