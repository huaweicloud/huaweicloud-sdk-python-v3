# coding: utf-8

import pprint
import re

import six





class RecordResultDO:


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
        'available': 'bool'
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
        'available': 'available'
    }

    def __init__(self, conf_uuid=None, conf_id=None, url=None, rcd_time=None, rcd_size=None, subject=None, scheduser_name=None, start_time=None, is_decode_finish=None, decode_end_time=None, available=None):
        """RecordResultDO - a model defined in huaweicloud sdk"""
        
        

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

    @property
    def conf_uuid(self):
        """Gets the conf_uuid of this RecordResultDO.

        会议UUID。

        :return: The conf_uuid of this RecordResultDO.
        :rtype: str
        """
        return self._conf_uuid

    @conf_uuid.setter
    def conf_uuid(self, conf_uuid):
        """Sets the conf_uuid of this RecordResultDO.

        会议UUID。

        :param conf_uuid: The conf_uuid of this RecordResultDO.
        :type: str
        """
        self._conf_uuid = conf_uuid

    @property
    def conf_id(self):
        """Gets the conf_id of this RecordResultDO.

        会议ID。

        :return: The conf_id of this RecordResultDO.
        :rtype: str
        """
        return self._conf_id

    @conf_id.setter
    def conf_id(self, conf_id):
        """Sets the conf_id of this RecordResultDO.

        会议ID。

        :param conf_id: The conf_id of this RecordResultDO.
        :type: str
        """
        self._conf_id = conf_id

    @property
    def url(self):
        """Gets the url of this RecordResultDO.

        点播地址。

        :return: The url of this RecordResultDO.
        :rtype: list[str]
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this RecordResultDO.

        点播地址。

        :param url: The url of this RecordResultDO.
        :type: list[str]
        """
        self._url = url

    @property
    def rcd_time(self):
        """Gets the rcd_time of this RecordResultDO.

        录制时长（单位秒）。

        :return: The rcd_time of this RecordResultDO.
        :rtype: int
        """
        return self._rcd_time

    @rcd_time.setter
    def rcd_time(self, rcd_time):
        """Sets the rcd_time of this RecordResultDO.

        录制时长（单位秒）。

        :param rcd_time: The rcd_time of this RecordResultDO.
        :type: int
        """
        self._rcd_time = rcd_time

    @property
    def rcd_size(self):
        """Gets the rcd_size of this RecordResultDO.

        录制文件大小（MB）。

        :return: The rcd_size of this RecordResultDO.
        :rtype: int
        """
        return self._rcd_size

    @rcd_size.setter
    def rcd_size(self, rcd_size):
        """Sets the rcd_size of this RecordResultDO.

        录制文件大小（MB）。

        :param rcd_size: The rcd_size of this RecordResultDO.
        :type: int
        """
        self._rcd_size = rcd_size

    @property
    def subject(self):
        """Gets the subject of this RecordResultDO.

        会议主题。

        :return: The subject of this RecordResultDO.
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this RecordResultDO.

        会议主题。

        :param subject: The subject of this RecordResultDO.
        :type: str
        """
        self._subject = subject

    @property
    def scheduser_name(self):
        """Gets the scheduser_name of this RecordResultDO.

        会议预订者。

        :return: The scheduser_name of this RecordResultDO.
        :rtype: str
        """
        return self._scheduser_name

    @scheduser_name.setter
    def scheduser_name(self, scheduser_name):
        """Sets the scheduser_name of this RecordResultDO.

        会议预订者。

        :param scheduser_name: The scheduser_name of this RecordResultDO.
        :type: str
        """
        self._scheduser_name = scheduser_name

    @property
    def start_time(self):
        """Gets the start_time of this RecordResultDO.

        会议开始时间。

        :return: The start_time of this RecordResultDO.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this RecordResultDO.

        会议开始时间。

        :param start_time: The start_time of this RecordResultDO.
        :type: str
        """
        self._start_time = start_time

    @property
    def is_decode_finish(self):
        """Gets the is_decode_finish of this RecordResultDO.

        录制文件是否转码完成。

        :return: The is_decode_finish of this RecordResultDO.
        :rtype: bool
        """
        return self._is_decode_finish

    @is_decode_finish.setter
    def is_decode_finish(self, is_decode_finish):
        """Sets the is_decode_finish of this RecordResultDO.

        录制文件是否转码完成。

        :param is_decode_finish: The is_decode_finish of this RecordResultDO.
        :type: bool
        """
        self._is_decode_finish = is_decode_finish

    @property
    def decode_end_time(self):
        """Gets the decode_end_time of this RecordResultDO.

        录制文件预计转码完成时间。

        :return: The decode_end_time of this RecordResultDO.
        :rtype: int
        """
        return self._decode_end_time

    @decode_end_time.setter
    def decode_end_time(self, decode_end_time):
        """Sets the decode_end_time of this RecordResultDO.

        录制文件预计转码完成时间。

        :param decode_end_time: The decode_end_time of this RecordResultDO.
        :type: int
        """
        self._decode_end_time = decode_end_time

    @property
    def available(self):
        """Gets the available of this RecordResultDO.

        录播文件是否可观看。

        :return: The available of this RecordResultDO.
        :rtype: bool
        """
        return self._available

    @available.setter
    def available(self, available):
        """Sets the available of this RecordResultDO.

        录播文件是否可观看。

        :param available: The available of this RecordResultDO.
        :type: bool
        """
        self._available = available

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RecordResultDO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
