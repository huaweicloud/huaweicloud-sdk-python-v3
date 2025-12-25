# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateShortJobReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'job_type': 'str',
        'language': 'str'
    }

    attribute_map = {
        'job_type': 'job_type',
        'language': 'language'
    }

    def __init__(self, job_type=None, language=None):
        r"""CreateShortJobReq

        The model defined in huaweicloud sdk

        :param job_type: 短任务类型。 * VOICE_ASSESS: 声音质量检测
        :type job_type: str
        :param language: 语言。 * CN: 中文 * EN: 英文
        :type language: str
        """
        
        

        self._job_type = None
        self._language = None
        self.discriminator = None

        self.job_type = job_type
        if language is not None:
            self.language = language

    @property
    def job_type(self):
        r"""Gets the job_type of this CreateShortJobReq.

        短任务类型。 * VOICE_ASSESS: 声音质量检测

        :return: The job_type of this CreateShortJobReq.
        :rtype: str
        """
        return self._job_type

    @job_type.setter
    def job_type(self, job_type):
        r"""Sets the job_type of this CreateShortJobReq.

        短任务类型。 * VOICE_ASSESS: 声音质量检测

        :param job_type: The job_type of this CreateShortJobReq.
        :type job_type: str
        """
        self._job_type = job_type

    @property
    def language(self):
        r"""Gets the language of this CreateShortJobReq.

        语言。 * CN: 中文 * EN: 英文

        :return: The language of this CreateShortJobReq.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this CreateShortJobReq.

        语言。 * CN: 中文 * EN: 英文

        :param language: The language of this CreateShortJobReq.
        :type language: str
        """
        self._language = language

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreateShortJobReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
