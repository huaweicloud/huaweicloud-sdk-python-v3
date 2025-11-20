# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TranscodeDetailInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'stream_name': 'str',
        'template': 'str',
        'code_rate_format': 'str',
        'duration': 'int'
    }

    attribute_map = {
        'stream_name': 'stream_name',
        'template': 'template',
        'code_rate_format': 'code_rate_format',
        'duration': 'duration'
    }

    def __init__(self, stream_name=None, template=None, code_rate_format=None, duration=None):
        r"""TranscodeDetailInfo

        The model defined in huaweicloud sdk

        :param stream_name: 流名
        :type stream_name: str
        :param template: 转码模板
        :type template: str
        :param code_rate_format: 转码格式（H264/H265）
        :type code_rate_format: str
        :param duration: 转码时长
        :type duration: int
        """
        
        

        self._stream_name = None
        self._template = None
        self._code_rate_format = None
        self._duration = None
        self.discriminator = None

        if stream_name is not None:
            self.stream_name = stream_name
        if template is not None:
            self.template = template
        if code_rate_format is not None:
            self.code_rate_format = code_rate_format
        if duration is not None:
            self.duration = duration

    @property
    def stream_name(self):
        r"""Gets the stream_name of this TranscodeDetailInfo.

        流名

        :return: The stream_name of this TranscodeDetailInfo.
        :rtype: str
        """
        return self._stream_name

    @stream_name.setter
    def stream_name(self, stream_name):
        r"""Sets the stream_name of this TranscodeDetailInfo.

        流名

        :param stream_name: The stream_name of this TranscodeDetailInfo.
        :type stream_name: str
        """
        self._stream_name = stream_name

    @property
    def template(self):
        r"""Gets the template of this TranscodeDetailInfo.

        转码模板

        :return: The template of this TranscodeDetailInfo.
        :rtype: str
        """
        return self._template

    @template.setter
    def template(self, template):
        r"""Sets the template of this TranscodeDetailInfo.

        转码模板

        :param template: The template of this TranscodeDetailInfo.
        :type template: str
        """
        self._template = template

    @property
    def code_rate_format(self):
        r"""Gets the code_rate_format of this TranscodeDetailInfo.

        转码格式（H264/H265）

        :return: The code_rate_format of this TranscodeDetailInfo.
        :rtype: str
        """
        return self._code_rate_format

    @code_rate_format.setter
    def code_rate_format(self, code_rate_format):
        r"""Sets the code_rate_format of this TranscodeDetailInfo.

        转码格式（H264/H265）

        :param code_rate_format: The code_rate_format of this TranscodeDetailInfo.
        :type code_rate_format: str
        """
        self._code_rate_format = code_rate_format

    @property
    def duration(self):
        r"""Gets the duration of this TranscodeDetailInfo.

        转码时长

        :return: The duration of this TranscodeDetailInfo.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this TranscodeDetailInfo.

        转码时长

        :param duration: The duration of this TranscodeDetailInfo.
        :type duration: int
        """
        self._duration = duration

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
        if not isinstance(other, TranscodeDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
