# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TranscodeInfoResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_name': 'str',
        'progress': 'int',
        'start_time': 'str',
        'waiting_time': 'int',
        'process_time': 'int'
    }

    attribute_map = {
        'template_name': 'template_name',
        'progress': 'progress',
        'start_time': 'start_time',
        'waiting_time': 'waiting_time',
        'process_time': 'process_time'
    }

    def __init__(self, template_name=None, progress=None, start_time=None, waiting_time=None, process_time=None):
        r"""TranscodeInfoResult

        The model defined in huaweicloud sdk

        :param template_name: 转码模板名 
        :type template_name: str
        :param progress: 转码进度 
        :type progress: int
        :param start_time: 转码开始处理时间，格式按照RFC3339，UTC时间，如2020-09-01T18:50:20Z 
        :type start_time: str
        :param waiting_time: 等待时长，单位为秒，当值为非-1时有效 
        :type waiting_time: int
        :param process_time: 处理时长，单位为秒，当值为非-1时有效 
        :type process_time: int
        """
        
        

        self._template_name = None
        self._progress = None
        self._start_time = None
        self._waiting_time = None
        self._process_time = None
        self.discriminator = None

        if template_name is not None:
            self.template_name = template_name
        if progress is not None:
            self.progress = progress
        if start_time is not None:
            self.start_time = start_time
        if waiting_time is not None:
            self.waiting_time = waiting_time
        if process_time is not None:
            self.process_time = process_time

    @property
    def template_name(self):
        r"""Gets the template_name of this TranscodeInfoResult.

        转码模板名 

        :return: The template_name of this TranscodeInfoResult.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this TranscodeInfoResult.

        转码模板名 

        :param template_name: The template_name of this TranscodeInfoResult.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def progress(self):
        r"""Gets the progress of this TranscodeInfoResult.

        转码进度 

        :return: The progress of this TranscodeInfoResult.
        :rtype: int
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        r"""Sets the progress of this TranscodeInfoResult.

        转码进度 

        :param progress: The progress of this TranscodeInfoResult.
        :type progress: int
        """
        self._progress = progress

    @property
    def start_time(self):
        r"""Gets the start_time of this TranscodeInfoResult.

        转码开始处理时间，格式按照RFC3339，UTC时间，如2020-09-01T18:50:20Z 

        :return: The start_time of this TranscodeInfoResult.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this TranscodeInfoResult.

        转码开始处理时间，格式按照RFC3339，UTC时间，如2020-09-01T18:50:20Z 

        :param start_time: The start_time of this TranscodeInfoResult.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def waiting_time(self):
        r"""Gets the waiting_time of this TranscodeInfoResult.

        等待时长，单位为秒，当值为非-1时有效 

        :return: The waiting_time of this TranscodeInfoResult.
        :rtype: int
        """
        return self._waiting_time

    @waiting_time.setter
    def waiting_time(self, waiting_time):
        r"""Sets the waiting_time of this TranscodeInfoResult.

        等待时长，单位为秒，当值为非-1时有效 

        :param waiting_time: The waiting_time of this TranscodeInfoResult.
        :type waiting_time: int
        """
        self._waiting_time = waiting_time

    @property
    def process_time(self):
        r"""Gets the process_time of this TranscodeInfoResult.

        处理时长，单位为秒，当值为非-1时有效 

        :return: The process_time of this TranscodeInfoResult.
        :rtype: int
        """
        return self._process_time

    @process_time.setter
    def process_time(self, process_time):
        r"""Sets the process_time of this TranscodeInfoResult.

        处理时长，单位为秒，当值为非-1时有效 

        :param process_time: The process_time of this TranscodeInfoResult.
        :type process_time: int
        """
        self._process_time = process_time

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
        if not isinstance(other, TranscodeInfoResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
