# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTranscodeTaskDetailResponse(SdkResponse):

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
        'start_time': 'str',
        'end_time': 'str',
        'transcode_detail_list': 'list[TranscodeDetailInfo]',
        'x_request_id': 'str'
    }

    attribute_map = {
        'domain': 'domain',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'transcode_detail_list': 'transcode_detail_list',
        'x_request_id': 'X-Request-Id'
    }

    def __init__(self, domain=None, start_time=None, end_time=None, transcode_detail_list=None, x_request_id=None):
        r"""ListTranscodeTaskDetailResponse

        The model defined in huaweicloud sdk

        :param domain: 推流域名
        :type domain: str
        :param start_time: 采样开始时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。
        :type start_time: str
        :param end_time: 采样结束时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。
        :type end_time: str
        :param transcode_detail_list: 流粒度转码明细
        :type transcode_detail_list: list[:class:`huaweicloudsdklive.v2.TranscodeDetailInfo`]
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super().__init__()

        self._domain = None
        self._start_time = None
        self._end_time = None
        self._transcode_detail_list = None
        self._x_request_id = None
        self.discriminator = None

        if domain is not None:
            self.domain = domain
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if transcode_detail_list is not None:
            self.transcode_detail_list = transcode_detail_list
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def domain(self):
        r"""Gets the domain of this ListTranscodeTaskDetailResponse.

        推流域名

        :return: The domain of this ListTranscodeTaskDetailResponse.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        r"""Sets the domain of this ListTranscodeTaskDetailResponse.

        推流域名

        :param domain: The domain of this ListTranscodeTaskDetailResponse.
        :type domain: str
        """
        self._domain = domain

    @property
    def start_time(self):
        r"""Gets the start_time of this ListTranscodeTaskDetailResponse.

        采样开始时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。

        :return: The start_time of this ListTranscodeTaskDetailResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListTranscodeTaskDetailResponse.

        采样开始时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。

        :param start_time: The start_time of this ListTranscodeTaskDetailResponse.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListTranscodeTaskDetailResponse.

        采样结束时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。

        :return: The end_time of this ListTranscodeTaskDetailResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListTranscodeTaskDetailResponse.

        采样结束时间。日期格式按照ISO8601表示法，并使用UTC时间。 格式为：YYYY-MM-DDThh:mm:ssZ。

        :param end_time: The end_time of this ListTranscodeTaskDetailResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def transcode_detail_list(self):
        r"""Gets the transcode_detail_list of this ListTranscodeTaskDetailResponse.

        流粒度转码明细

        :return: The transcode_detail_list of this ListTranscodeTaskDetailResponse.
        :rtype: list[:class:`huaweicloudsdklive.v2.TranscodeDetailInfo`]
        """
        return self._transcode_detail_list

    @transcode_detail_list.setter
    def transcode_detail_list(self, transcode_detail_list):
        r"""Sets the transcode_detail_list of this ListTranscodeTaskDetailResponse.

        流粒度转码明细

        :param transcode_detail_list: The transcode_detail_list of this ListTranscodeTaskDetailResponse.
        :type transcode_detail_list: list[:class:`huaweicloudsdklive.v2.TranscodeDetailInfo`]
        """
        self._transcode_detail_list = transcode_detail_list

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this ListTranscodeTaskDetailResponse.

        :return: The x_request_id of this ListTranscodeTaskDetailResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this ListTranscodeTaskDetailResponse.

        :param x_request_id: The x_request_id of this ListTranscodeTaskDetailResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

    def to_dict(self):
        import warnings
        warnings.warn("ListTranscodeTaskDetailResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListTranscodeTaskDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
