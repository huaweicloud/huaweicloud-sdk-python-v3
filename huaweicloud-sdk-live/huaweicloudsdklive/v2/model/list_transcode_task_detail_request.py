# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTranscodeTaskDetailRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain': 'str',
        'stream_name_list': 'list[str]',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'stream_name_list': 'stream_name_list',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, domain=None, stream_name_list=None, start_time=None, end_time=None):
        r"""ListTranscodeTaskDetailRequest

        The model defined in huaweicloud sdk

        :param domain: 推流域名。 
        :type domain: str
        :param stream_name_list: 流名列表，以逗号分隔，最多支持查询100个流名。 如果不传入流名，则查询域名下所有转码流的数据。 
        :type stream_name_list: list[str]
        :param start_time: 起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度1天，最大查询周期14天。  若参数为空，默认查询1天数据。 
        :type start_time: str
        :param end_time: 结束时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度1天，最大查询周期14天。  若参数为空，默认为当前时间。结束时间需大于起始时间。 
        :type end_time: str
        """
        
        

        self._domain = None
        self._stream_name_list = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        self.domain = domain
        if stream_name_list is not None:
            self.stream_name_list = stream_name_list
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def domain(self):
        r"""Gets the domain of this ListTranscodeTaskDetailRequest.

        推流域名。 

        :return: The domain of this ListTranscodeTaskDetailRequest.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this ListTranscodeTaskDetailRequest.

        推流域名。 

        :param domain: The domain of this ListTranscodeTaskDetailRequest.
        :type domain: str
        """
        self._domain = domain

    @property
    def stream_name_list(self):
        r"""Gets the stream_name_list of this ListTranscodeTaskDetailRequest.

        流名列表，以逗号分隔，最多支持查询100个流名。 如果不传入流名，则查询域名下所有转码流的数据。 

        :return: The stream_name_list of this ListTranscodeTaskDetailRequest.
        :rtype: list[str]
        """
        return self._stream_name_list

    @stream_name_list.setter
    def stream_name_list(self, stream_name_list):
        r"""Sets the stream_name_list of this ListTranscodeTaskDetailRequest.

        流名列表，以逗号分隔，最多支持查询100个流名。 如果不传入流名，则查询域名下所有转码流的数据。 

        :param stream_name_list: The stream_name_list of this ListTranscodeTaskDetailRequest.
        :type stream_name_list: list[str]
        """
        self._stream_name_list = stream_name_list

    @property
    def start_time(self):
        r"""Gets the start_time of this ListTranscodeTaskDetailRequest.

        起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度1天，最大查询周期14天。  若参数为空，默认查询1天数据。 

        :return: The start_time of this ListTranscodeTaskDetailRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListTranscodeTaskDetailRequest.

        起始时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度1天，最大查询周期14天。  若参数为空，默认查询1天数据。 

        :param start_time: The start_time of this ListTranscodeTaskDetailRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListTranscodeTaskDetailRequest.

        结束时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度1天，最大查询周期14天。  若参数为空，默认为当前时间。结束时间需大于起始时间。 

        :return: The end_time of this ListTranscodeTaskDetailRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListTranscodeTaskDetailRequest.

        结束时间。日期格式按照ISO8601表示法，并使用UTC时间。  格式为：YYYY-MM-DDThh:mm:ssZ。最大查询跨度1天，最大查询周期14天。  若参数为空，默认为当前时间。结束时间需大于起始时间。 

        :param end_time: The end_time of this ListTranscodeTaskDetailRequest.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, ListTranscodeTaskDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
