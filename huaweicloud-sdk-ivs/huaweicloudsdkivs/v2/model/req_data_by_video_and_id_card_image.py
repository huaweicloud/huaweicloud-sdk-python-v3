# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ReqDataByVideoAndIdCardImage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'idcard_image1': 'str',
        'idcard_image2': 'str',
        'video': 'str',
        'actions': 'str',
        'nod_threshold': 'float',
        'detail': 'bool'
    }

    attribute_map = {
        'idcard_image1': 'idcard_image1',
        'idcard_image2': 'idcard_image2',
        'video': 'video',
        'actions': 'actions',
        'nod_threshold': 'nod_threshold',
        'detail': 'detail'
    }

    def __init__(self, idcard_image1=None, idcard_image2=None, video=None, actions=None, nod_threshold=None, detail=None):
        r"""ReqDataByVideoAndIdCardImage

        The model defined in huaweicloud sdk

        :param idcard_image1: 身份证人像面图像数据，使用base64编码，要求base64编码后大小不超过4M。图像各边的像素大小在300到4000之间，支持JPG格式。
        :type idcard_image1: str
        :param idcard_image2: 身份证国徽面图像数据，使用base64编码，要求base64编码后大小不超过4M。图像各边的像素大小在300到4000之间，支持JPG格式。
        :type idcard_image2: str
        :param video: 现场拍摄人像视频数据，使用base64编码，要求base64编码后大小不超过10M。
        :type video: str
        :param actions: 动作代码顺序列表，英文逗号（,）分隔。建议单动作，目前支持的动作有： • 1：左摇头 • 2：右摇头 • 3：点头 • 4：嘴部动作
        :type actions: str
        :param nod_threshold: 该参数为点头动作幅度的判断门限，取值范围：[1,90]，默认为10，单位为度。该值设置越大，则越难判断为点头。
        :type nod_threshold: float
        :param detail: 响应参数similarity是否详细显示，默认为false。 - true表示响应中的similarity为0~1000的小数。 - false表示响应中的similarity为0~100的整数。
        :type detail: bool
        """
        
        

        self._idcard_image1 = None
        self._idcard_image2 = None
        self._video = None
        self._actions = None
        self._nod_threshold = None
        self._detail = None
        self.discriminator = None

        self.idcard_image1 = idcard_image1
        if idcard_image2 is not None:
            self.idcard_image2 = idcard_image2
        self.video = video
        self.actions = actions
        if nod_threshold is not None:
            self.nod_threshold = nod_threshold
        if detail is not None:
            self.detail = detail

    @property
    def idcard_image1(self):
        r"""Gets the idcard_image1 of this ReqDataByVideoAndIdCardImage.

        身份证人像面图像数据，使用base64编码，要求base64编码后大小不超过4M。图像各边的像素大小在300到4000之间，支持JPG格式。

        :return: The idcard_image1 of this ReqDataByVideoAndIdCardImage.
        :rtype: str
        """
        return self._idcard_image1

    @idcard_image1.setter
    def idcard_image1(self, idcard_image1):
        r"""Sets the idcard_image1 of this ReqDataByVideoAndIdCardImage.

        身份证人像面图像数据，使用base64编码，要求base64编码后大小不超过4M。图像各边的像素大小在300到4000之间，支持JPG格式。

        :param idcard_image1: The idcard_image1 of this ReqDataByVideoAndIdCardImage.
        :type idcard_image1: str
        """
        self._idcard_image1 = idcard_image1

    @property
    def idcard_image2(self):
        r"""Gets the idcard_image2 of this ReqDataByVideoAndIdCardImage.

        身份证国徽面图像数据，使用base64编码，要求base64编码后大小不超过4M。图像各边的像素大小在300到4000之间，支持JPG格式。

        :return: The idcard_image2 of this ReqDataByVideoAndIdCardImage.
        :rtype: str
        """
        return self._idcard_image2

    @idcard_image2.setter
    def idcard_image2(self, idcard_image2):
        r"""Sets the idcard_image2 of this ReqDataByVideoAndIdCardImage.

        身份证国徽面图像数据，使用base64编码，要求base64编码后大小不超过4M。图像各边的像素大小在300到4000之间，支持JPG格式。

        :param idcard_image2: The idcard_image2 of this ReqDataByVideoAndIdCardImage.
        :type idcard_image2: str
        """
        self._idcard_image2 = idcard_image2

    @property
    def video(self):
        r"""Gets the video of this ReqDataByVideoAndIdCardImage.

        现场拍摄人像视频数据，使用base64编码，要求base64编码后大小不超过10M。

        :return: The video of this ReqDataByVideoAndIdCardImage.
        :rtype: str
        """
        return self._video

    @video.setter
    def video(self, video):
        r"""Sets the video of this ReqDataByVideoAndIdCardImage.

        现场拍摄人像视频数据，使用base64编码，要求base64编码后大小不超过10M。

        :param video: The video of this ReqDataByVideoAndIdCardImage.
        :type video: str
        """
        self._video = video

    @property
    def actions(self):
        r"""Gets the actions of this ReqDataByVideoAndIdCardImage.

        动作代码顺序列表，英文逗号（,）分隔。建议单动作，目前支持的动作有： • 1：左摇头 • 2：右摇头 • 3：点头 • 4：嘴部动作

        :return: The actions of this ReqDataByVideoAndIdCardImage.
        :rtype: str
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this ReqDataByVideoAndIdCardImage.

        动作代码顺序列表，英文逗号（,）分隔。建议单动作，目前支持的动作有： • 1：左摇头 • 2：右摇头 • 3：点头 • 4：嘴部动作

        :param actions: The actions of this ReqDataByVideoAndIdCardImage.
        :type actions: str
        """
        self._actions = actions

    @property
    def nod_threshold(self):
        r"""Gets the nod_threshold of this ReqDataByVideoAndIdCardImage.

        该参数为点头动作幅度的判断门限，取值范围：[1,90]，默认为10，单位为度。该值设置越大，则越难判断为点头。

        :return: The nod_threshold of this ReqDataByVideoAndIdCardImage.
        :rtype: float
        """
        return self._nod_threshold

    @nod_threshold.setter
    def nod_threshold(self, nod_threshold):
        r"""Sets the nod_threshold of this ReqDataByVideoAndIdCardImage.

        该参数为点头动作幅度的判断门限，取值范围：[1,90]，默认为10，单位为度。该值设置越大，则越难判断为点头。

        :param nod_threshold: The nod_threshold of this ReqDataByVideoAndIdCardImage.
        :type nod_threshold: float
        """
        self._nod_threshold = nod_threshold

    @property
    def detail(self):
        r"""Gets the detail of this ReqDataByVideoAndIdCardImage.

        响应参数similarity是否详细显示，默认为false。 - true表示响应中的similarity为0~1000的小数。 - false表示响应中的similarity为0~100的整数。

        :return: The detail of this ReqDataByVideoAndIdCardImage.
        :rtype: bool
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        r"""Sets the detail of this ReqDataByVideoAndIdCardImage.

        响应参数similarity是否详细显示，默认为false。 - true表示响应中的similarity为0~1000的小数。 - false表示响应中的similarity为0~100的整数。

        :param detail: The detail of this ReqDataByVideoAndIdCardImage.
        :type detail: bool
        """
        self._detail = detail

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
        if not isinstance(other, ReqDataByVideoAndIdCardImage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
