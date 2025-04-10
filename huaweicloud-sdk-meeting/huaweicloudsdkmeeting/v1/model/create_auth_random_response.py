# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAuthRandomResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'random': 'str',
        'subject': 'str',
        'conf_mode': 'str',
        'webinar': 'bool',
        'need_password': 'bool',
        'support_applets': 'bool'
    }

    attribute_map = {
        'random': 'random',
        'subject': 'subject',
        'conf_mode': 'conf_mode',
        'webinar': 'webinar',
        'need_password': 'need_password',
        'support_applets': 'support_applets'
    }

    def __init__(self, random=None, subject=None, conf_mode=None, webinar=None, need_password=None, support_applets=None):
        r"""CreateAuthRandomResponse

        The model defined in huaweicloud sdk

        :param random: 鉴权随机数
        :type random: str
        :param subject: 会议主题
        :type subject: str
        :param conf_mode: 会议类型模型。 * COMMON：MCU会议 * RTC：MMR会议 
        :type conf_mode: str
        :param webinar: 是否为网络研讨会
        :type webinar: bool
        :param need_password: 是否需要密码
        :type need_password: bool
        :param support_applets: 是否支持小程序
        :type support_applets: bool
        """
        
        super(CreateAuthRandomResponse, self).__init__()

        self._random = None
        self._subject = None
        self._conf_mode = None
        self._webinar = None
        self._need_password = None
        self._support_applets = None
        self.discriminator = None

        if random is not None:
            self.random = random
        if subject is not None:
            self.subject = subject
        if conf_mode is not None:
            self.conf_mode = conf_mode
        if webinar is not None:
            self.webinar = webinar
        if need_password is not None:
            self.need_password = need_password
        if support_applets is not None:
            self.support_applets = support_applets

    @property
    def random(self):
        r"""Gets the random of this CreateAuthRandomResponse.

        鉴权随机数

        :return: The random of this CreateAuthRandomResponse.
        :rtype: str
        """
        return self._random

    @random.setter
    def random(self, random):
        r"""Sets the random of this CreateAuthRandomResponse.

        鉴权随机数

        :param random: The random of this CreateAuthRandomResponse.
        :type random: str
        """
        self._random = random

    @property
    def subject(self):
        r"""Gets the subject of this CreateAuthRandomResponse.

        会议主题

        :return: The subject of this CreateAuthRandomResponse.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        r"""Sets the subject of this CreateAuthRandomResponse.

        会议主题

        :param subject: The subject of this CreateAuthRandomResponse.
        :type subject: str
        """
        self._subject = subject

    @property
    def conf_mode(self):
        r"""Gets the conf_mode of this CreateAuthRandomResponse.

        会议类型模型。 * COMMON：MCU会议 * RTC：MMR会议 

        :return: The conf_mode of this CreateAuthRandomResponse.
        :rtype: str
        """
        return self._conf_mode

    @conf_mode.setter
    def conf_mode(self, conf_mode):
        r"""Sets the conf_mode of this CreateAuthRandomResponse.

        会议类型模型。 * COMMON：MCU会议 * RTC：MMR会议 

        :param conf_mode: The conf_mode of this CreateAuthRandomResponse.
        :type conf_mode: str
        """
        self._conf_mode = conf_mode

    @property
    def webinar(self):
        r"""Gets the webinar of this CreateAuthRandomResponse.

        是否为网络研讨会

        :return: The webinar of this CreateAuthRandomResponse.
        :rtype: bool
        """
        return self._webinar

    @webinar.setter
    def webinar(self, webinar):
        r"""Sets the webinar of this CreateAuthRandomResponse.

        是否为网络研讨会

        :param webinar: The webinar of this CreateAuthRandomResponse.
        :type webinar: bool
        """
        self._webinar = webinar

    @property
    def need_password(self):
        r"""Gets the need_password of this CreateAuthRandomResponse.

        是否需要密码

        :return: The need_password of this CreateAuthRandomResponse.
        :rtype: bool
        """
        return self._need_password

    @need_password.setter
    def need_password(self, need_password):
        r"""Sets the need_password of this CreateAuthRandomResponse.

        是否需要密码

        :param need_password: The need_password of this CreateAuthRandomResponse.
        :type need_password: bool
        """
        self._need_password = need_password

    @property
    def support_applets(self):
        r"""Gets the support_applets of this CreateAuthRandomResponse.

        是否支持小程序

        :return: The support_applets of this CreateAuthRandomResponse.
        :rtype: bool
        """
        return self._support_applets

    @support_applets.setter
    def support_applets(self, support_applets):
        r"""Sets the support_applets of this CreateAuthRandomResponse.

        是否支持小程序

        :param support_applets: The support_applets of this CreateAuthRandomResponse.
        :type support_applets: bool
        """
        self._support_applets = support_applets

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
        if not isinstance(other, CreateAuthRandomResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
