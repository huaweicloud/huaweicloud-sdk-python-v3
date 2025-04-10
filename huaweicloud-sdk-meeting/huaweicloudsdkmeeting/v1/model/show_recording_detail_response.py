# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRecordingDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'conf_uuid': 'str',
        'conf_id': 'str',
        'url': 'list[str]',
        'rcd_time': 'int',
        'rcd_size': 'int',
        'subject': 'str',
        'scheduser_name': 'str',
        'start_time': 'str',
        'is_decode_finish': 'bool',
        'decode_end_time': 'int',
        'available': 'bool',
        'record_auth_type': 'int'
    }

    attribute_map = {
        'conf_uuid': 'confUUID',
        'conf_id': 'confID',
        'url': 'url',
        'rcd_time': 'rcdTime',
        'rcd_size': 'rcdSize',
        'subject': 'subject',
        'scheduser_name': 'scheduserName',
        'start_time': 'startTime',
        'is_decode_finish': 'isDecodeFinish',
        'decode_end_time': 'decodeEndTime',
        'available': 'available',
        'record_auth_type': 'recordAuthType'
    }

    def __init__(self, conf_uuid=None, conf_id=None, url=None, rcd_time=None, rcd_size=None, subject=None, scheduser_name=None, start_time=None, is_decode_finish=None, decode_end_time=None, available=None, record_auth_type=None):
        r"""ShowRecordingDetailResponse

        The model defined in huaweicloud sdk

        :param conf_uuid: 会议UUID。
        :type conf_uuid: str
        :param conf_id: 会议ID。
        :type conf_id: str
        :param url: 录播观看地址。
        :type url: list[str]
        :param rcd_time: 录制时长（单位秒）。
        :type rcd_time: int
        :param rcd_size: 录制文件大小（MB）。
        :type rcd_size: int
        :param subject: 会议主题。
        :type subject: str
        :param scheduser_name: 会议预订者名称。
        :type scheduser_name: str
        :param start_time: 会议开始时间。
        :type start_time: str
        :param is_decode_finish: 录制文件是否转码完成。
        :type is_decode_finish: bool
        :param decode_end_time: 录制文件预计转码完成时间。
        :type decode_end_time: int
        :param available: 录播文件是否可观看。
        :type available: bool
        :param record_auth_type: 观看/下载录播的鉴权方式。 - 0: 可通过链接观看/下载 - 1: 企业用户可观看/下载 - 2: 与会者可观看/下载
        :type record_auth_type: int
        """
        
        super(ShowRecordingDetailResponse, self).__init__()

        self._conf_uuid = None
        self._conf_id = None
        self._url = None
        self._rcd_time = None
        self._rcd_size = None
        self._subject = None
        self._scheduser_name = None
        self._start_time = None
        self._is_decode_finish = None
        self._decode_end_time = None
        self._available = None
        self._record_auth_type = None
        self.discriminator = None

        if conf_uuid is not None:
            self.conf_uuid = conf_uuid
        if conf_id is not None:
            self.conf_id = conf_id
        if url is not None:
            self.url = url
        if rcd_time is not None:
            self.rcd_time = rcd_time
        if rcd_size is not None:
            self.rcd_size = rcd_size
        if subject is not None:
            self.subject = subject
        if scheduser_name is not None:
            self.scheduser_name = scheduser_name
        if start_time is not None:
            self.start_time = start_time
        if is_decode_finish is not None:
            self.is_decode_finish = is_decode_finish
        if decode_end_time is not None:
            self.decode_end_time = decode_end_time
        if available is not None:
            self.available = available
        if record_auth_type is not None:
            self.record_auth_type = record_auth_type

    @property
    def conf_uuid(self):
        r"""Gets the conf_uuid of this ShowRecordingDetailResponse.

        会议UUID。

        :return: The conf_uuid of this ShowRecordingDetailResponse.
        :rtype: str
        """
        return self._conf_uuid

    @conf_uuid.setter
    def conf_uuid(self, conf_uuid):
        r"""Sets the conf_uuid of this ShowRecordingDetailResponse.

        会议UUID。

        :param conf_uuid: The conf_uuid of this ShowRecordingDetailResponse.
        :type conf_uuid: str
        """
        self._conf_uuid = conf_uuid

    @property
    def conf_id(self):
        r"""Gets the conf_id of this ShowRecordingDetailResponse.

        会议ID。

        :return: The conf_id of this ShowRecordingDetailResponse.
        :rtype: str
        """
        return self._conf_id

    @conf_id.setter
    def conf_id(self, conf_id):
        r"""Sets the conf_id of this ShowRecordingDetailResponse.

        会议ID。

        :param conf_id: The conf_id of this ShowRecordingDetailResponse.
        :type conf_id: str
        """
        self._conf_id = conf_id

    @property
    def url(self):
        r"""Gets the url of this ShowRecordingDetailResponse.

        录播观看地址。

        :return: The url of this ShowRecordingDetailResponse.
        :rtype: list[str]
        """
        return self._url

    @url.setter
    def url(self, url):
        r"""Sets the url of this ShowRecordingDetailResponse.

        录播观看地址。

        :param url: The url of this ShowRecordingDetailResponse.
        :type url: list[str]
        """
        self._url = url

    @property
    def rcd_time(self):
        r"""Gets the rcd_time of this ShowRecordingDetailResponse.

        录制时长（单位秒）。

        :return: The rcd_time of this ShowRecordingDetailResponse.
        :rtype: int
        """
        return self._rcd_time

    @rcd_time.setter
    def rcd_time(self, rcd_time):
        r"""Sets the rcd_time of this ShowRecordingDetailResponse.

        录制时长（单位秒）。

        :param rcd_time: The rcd_time of this ShowRecordingDetailResponse.
        :type rcd_time: int
        """
        self._rcd_time = rcd_time

    @property
    def rcd_size(self):
        r"""Gets the rcd_size of this ShowRecordingDetailResponse.

        录制文件大小（MB）。

        :return: The rcd_size of this ShowRecordingDetailResponse.
        :rtype: int
        """
        return self._rcd_size

    @rcd_size.setter
    def rcd_size(self, rcd_size):
        r"""Sets the rcd_size of this ShowRecordingDetailResponse.

        录制文件大小（MB）。

        :param rcd_size: The rcd_size of this ShowRecordingDetailResponse.
        :type rcd_size: int
        """
        self._rcd_size = rcd_size

    @property
    def subject(self):
        r"""Gets the subject of this ShowRecordingDetailResponse.

        会议主题。

        :return: The subject of this ShowRecordingDetailResponse.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        r"""Sets the subject of this ShowRecordingDetailResponse.

        会议主题。

        :param subject: The subject of this ShowRecordingDetailResponse.
        :type subject: str
        """
        self._subject = subject

    @property
    def scheduser_name(self):
        r"""Gets the scheduser_name of this ShowRecordingDetailResponse.

        会议预订者名称。

        :return: The scheduser_name of this ShowRecordingDetailResponse.
        :rtype: str
        """
        return self._scheduser_name

    @scheduser_name.setter
    def scheduser_name(self, scheduser_name):
        r"""Sets the scheduser_name of this ShowRecordingDetailResponse.

        会议预订者名称。

        :param scheduser_name: The scheduser_name of this ShowRecordingDetailResponse.
        :type scheduser_name: str
        """
        self._scheduser_name = scheduser_name

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowRecordingDetailResponse.

        会议开始时间。

        :return: The start_time of this ShowRecordingDetailResponse.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowRecordingDetailResponse.

        会议开始时间。

        :param start_time: The start_time of this ShowRecordingDetailResponse.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def is_decode_finish(self):
        r"""Gets the is_decode_finish of this ShowRecordingDetailResponse.

        录制文件是否转码完成。

        :return: The is_decode_finish of this ShowRecordingDetailResponse.
        :rtype: bool
        """
        return self._is_decode_finish

    @is_decode_finish.setter
    def is_decode_finish(self, is_decode_finish):
        r"""Sets the is_decode_finish of this ShowRecordingDetailResponse.

        录制文件是否转码完成。

        :param is_decode_finish: The is_decode_finish of this ShowRecordingDetailResponse.
        :type is_decode_finish: bool
        """
        self._is_decode_finish = is_decode_finish

    @property
    def decode_end_time(self):
        r"""Gets the decode_end_time of this ShowRecordingDetailResponse.

        录制文件预计转码完成时间。

        :return: The decode_end_time of this ShowRecordingDetailResponse.
        :rtype: int
        """
        return self._decode_end_time

    @decode_end_time.setter
    def decode_end_time(self, decode_end_time):
        r"""Sets the decode_end_time of this ShowRecordingDetailResponse.

        录制文件预计转码完成时间。

        :param decode_end_time: The decode_end_time of this ShowRecordingDetailResponse.
        :type decode_end_time: int
        """
        self._decode_end_time = decode_end_time

    @property
    def available(self):
        r"""Gets the available of this ShowRecordingDetailResponse.

        录播文件是否可观看。

        :return: The available of this ShowRecordingDetailResponse.
        :rtype: bool
        """
        return self._available

    @available.setter
    def available(self, available):
        r"""Sets the available of this ShowRecordingDetailResponse.

        录播文件是否可观看。

        :param available: The available of this ShowRecordingDetailResponse.
        :type available: bool
        """
        self._available = available

    @property
    def record_auth_type(self):
        r"""Gets the record_auth_type of this ShowRecordingDetailResponse.

        观看/下载录播的鉴权方式。 - 0: 可通过链接观看/下载 - 1: 企业用户可观看/下载 - 2: 与会者可观看/下载

        :return: The record_auth_type of this ShowRecordingDetailResponse.
        :rtype: int
        """
        return self._record_auth_type

    @record_auth_type.setter
    def record_auth_type(self, record_auth_type):
        r"""Sets the record_auth_type of this ShowRecordingDetailResponse.

        观看/下载录播的鉴权方式。 - 0: 可通过链接观看/下载 - 1: 企业用户可观看/下载 - 2: 与会者可观看/下载

        :param record_auth_type: The record_auth_type of this ShowRecordingDetailResponse.
        :type record_auth_type: int
        """
        self._record_auth_type = record_auth_type

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
        if not isinstance(other, ShowRecordingDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
