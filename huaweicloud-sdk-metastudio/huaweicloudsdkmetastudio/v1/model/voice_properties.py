# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VoiceProperties:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_tag': 'str',
        'sex': 'str',
        'language': 'str'
    }

    attribute_map = {
        'job_tag': 'job_tag',
        'sex': 'sex',
        'language': 'language'
    }

    def __init__(self, job_tag=None, sex=None, language=None):
        r"""VoiceProperties

        The model defined in huaweicloud sdk

        :param job_tag: 任务标签，为Flexus版声音的配置。   * ECOMMERCE: 电商   * NEWS: 新闻   * MARKETING: 营销
        :type job_tag: str
        :param sex: 语音性别，是男性声音还是女性声音，为Flexus版声音的配置。 * FEMALE: 女性 * MALE: 男性
        :type sex: str
        :param language: 训练语言，当前仅支持中文，为Flexus版声音的配置。 * CN: 中文 * EN: 英文
        :type language: str
        """
        
        

        self._job_tag = None
        self._sex = None
        self._language = None
        self.discriminator = None

        self.job_tag = job_tag
        self.sex = sex
        self.language = language

    @property
    def job_tag(self):
        r"""Gets the job_tag of this VoiceProperties.

        任务标签，为Flexus版声音的配置。   * ECOMMERCE: 电商   * NEWS: 新闻   * MARKETING: 营销

        :return: The job_tag of this VoiceProperties.
        :rtype: str
        """
        return self._job_tag

    @job_tag.setter
    def job_tag(self, job_tag):
        r"""Sets the job_tag of this VoiceProperties.

        任务标签，为Flexus版声音的配置。   * ECOMMERCE: 电商   * NEWS: 新闻   * MARKETING: 营销

        :param job_tag: The job_tag of this VoiceProperties.
        :type job_tag: str
        """
        self._job_tag = job_tag

    @property
    def sex(self):
        r"""Gets the sex of this VoiceProperties.

        语音性别，是男性声音还是女性声音，为Flexus版声音的配置。 * FEMALE: 女性 * MALE: 男性

        :return: The sex of this VoiceProperties.
        :rtype: str
        """
        return self._sex

    @sex.setter
    def sex(self, sex):
        r"""Sets the sex of this VoiceProperties.

        语音性别，是男性声音还是女性声音，为Flexus版声音的配置。 * FEMALE: 女性 * MALE: 男性

        :param sex: The sex of this VoiceProperties.
        :type sex: str
        """
        self._sex = sex

    @property
    def language(self):
        r"""Gets the language of this VoiceProperties.

        训练语言，当前仅支持中文，为Flexus版声音的配置。 * CN: 中文 * EN: 英文

        :return: The language of this VoiceProperties.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this VoiceProperties.

        训练语言，当前仅支持中文，为Flexus版声音的配置。 * CN: 中文 * EN: 英文

        :param language: The language of this VoiceProperties.
        :type language: str
        """
        self._language = language

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
        if not isinstance(other, VoiceProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
