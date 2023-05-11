# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StandardReqDataByVideoAndNameAndId:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'verification_name': 'str',
        'verification_id': 'str',
        'video': 'str',
        'actions': 'str',
        'nod_threshold': 'float'
    }

    attribute_map = {
        'verification_name': 'verification_name',
        'verification_id': 'verification_id',
        'video': 'video',
        'actions': 'actions',
        'nod_threshold': 'nod_threshold'
    }

    def __init__(self, verification_name=None, verification_id=None, video=None, actions=None, nod_threshold=None):
        """StandardReqDataByVideoAndNameAndId

        The model defined in huaweicloud sdk

        :param verification_name: 被验证人的姓名。
        :type verification_name: str
        :param verification_id: 被验证人的身份证号码。
        :type verification_id: str
        :param video: 现场拍摄人像视频数据，使用base64编码，要求base64编码后大小不超过10M。
        :type video: str
        :param actions: 动作代码顺序列表，英文逗号（,）分隔。建议单动作，目前支持的动作有： • 1：左摇头 • 2：右摇头 • 3：点头 • 4：嘴部动作
        :type actions: str
        :param nod_threshold: 该参数为点头动作幅度的判断门限，取值范围：[1,90]，默认为10，单位为度。该值设置越大，则越难判断为点头。
        :type nod_threshold: float
        """
        
        

        self._verification_name = None
        self._verification_id = None
        self._video = None
        self._actions = None
        self._nod_threshold = None
        self.discriminator = None

        self.verification_name = verification_name
        self.verification_id = verification_id
        self.video = video
        self.actions = actions
        if nod_threshold is not None:
            self.nod_threshold = nod_threshold

    @property
    def verification_name(self):
        """Gets the verification_name of this StandardReqDataByVideoAndNameAndId.

        被验证人的姓名。

        :return: The verification_name of this StandardReqDataByVideoAndNameAndId.
        :rtype: str
        """
        return self._verification_name

    @verification_name.setter
    def verification_name(self, verification_name):
        """Sets the verification_name of this StandardReqDataByVideoAndNameAndId.

        被验证人的姓名。

        :param verification_name: The verification_name of this StandardReqDataByVideoAndNameAndId.
        :type verification_name: str
        """
        self._verification_name = verification_name

    @property
    def verification_id(self):
        """Gets the verification_id of this StandardReqDataByVideoAndNameAndId.

        被验证人的身份证号码。

        :return: The verification_id of this StandardReqDataByVideoAndNameAndId.
        :rtype: str
        """
        return self._verification_id

    @verification_id.setter
    def verification_id(self, verification_id):
        """Sets the verification_id of this StandardReqDataByVideoAndNameAndId.

        被验证人的身份证号码。

        :param verification_id: The verification_id of this StandardReqDataByVideoAndNameAndId.
        :type verification_id: str
        """
        self._verification_id = verification_id

    @property
    def video(self):
        """Gets the video of this StandardReqDataByVideoAndNameAndId.

        现场拍摄人像视频数据，使用base64编码，要求base64编码后大小不超过10M。

        :return: The video of this StandardReqDataByVideoAndNameAndId.
        :rtype: str
        """
        return self._video

    @video.setter
    def video(self, video):
        """Sets the video of this StandardReqDataByVideoAndNameAndId.

        现场拍摄人像视频数据，使用base64编码，要求base64编码后大小不超过10M。

        :param video: The video of this StandardReqDataByVideoAndNameAndId.
        :type video: str
        """
        self._video = video

    @property
    def actions(self):
        """Gets the actions of this StandardReqDataByVideoAndNameAndId.

        动作代码顺序列表，英文逗号（,）分隔。建议单动作，目前支持的动作有： • 1：左摇头 • 2：右摇头 • 3：点头 • 4：嘴部动作

        :return: The actions of this StandardReqDataByVideoAndNameAndId.
        :rtype: str
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this StandardReqDataByVideoAndNameAndId.

        动作代码顺序列表，英文逗号（,）分隔。建议单动作，目前支持的动作有： • 1：左摇头 • 2：右摇头 • 3：点头 • 4：嘴部动作

        :param actions: The actions of this StandardReqDataByVideoAndNameAndId.
        :type actions: str
        """
        self._actions = actions

    @property
    def nod_threshold(self):
        """Gets the nod_threshold of this StandardReqDataByVideoAndNameAndId.

        该参数为点头动作幅度的判断门限，取值范围：[1,90]，默认为10，单位为度。该值设置越大，则越难判断为点头。

        :return: The nod_threshold of this StandardReqDataByVideoAndNameAndId.
        :rtype: float
        """
        return self._nod_threshold

    @nod_threshold.setter
    def nod_threshold(self, nod_threshold):
        """Sets the nod_threshold of this StandardReqDataByVideoAndNameAndId.

        该参数为点头动作幅度的判断门限，取值范围：[1,90]，默认为10，单位为度。该值设置越大，则越难判断为点头。

        :param nod_threshold: The nod_threshold of this StandardReqDataByVideoAndNameAndId.
        :type nod_threshold: float
        """
        self._nod_threshold = nod_threshold

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
        if not isinstance(other, StandardReqDataByVideoAndNameAndId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
