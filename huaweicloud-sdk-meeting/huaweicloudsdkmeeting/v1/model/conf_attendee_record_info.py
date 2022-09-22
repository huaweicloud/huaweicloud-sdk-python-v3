# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfAttendeeRecordInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'display_name': 'str',
        'call_number': 'str',
        'device_type': 'str',
        'join_time': 'int',
        'left_time': 'int',
        'media_type': 'str',
        'dept_name': 'str'
    }

    attribute_map = {
        'display_name': 'displayName',
        'call_number': 'callNumber',
        'device_type': 'deviceType',
        'join_time': 'joinTime',
        'left_time': 'leftTime',
        'media_type': 'mediaType',
        'dept_name': 'deptName'
    }

    def __init__(self, display_name=None, call_number=None, device_type=None, join_time=None, left_time=None, media_type=None, dept_name=None):
        """ConfAttendeeRecordInfo

        The model defined in huaweicloud sdk

        :param display_name: 与会者名称。
        :type display_name: str
        :param call_number: 号码。
        :type call_number: str
        :param device_type: 设备类型。
        :type device_type: str
        :param join_time: 入会时间（UTC时间，单位毫秒）。
        :type join_time: int
        :param left_time: 离会时间（UTC时间，单位毫秒）。
        :type left_time: int
        :param media_type: 媒体类型。
        :type media_type: str
        :param dept_name: 部门名称。
        :type dept_name: str
        """
        
        

        self._display_name = None
        self._call_number = None
        self._device_type = None
        self._join_time = None
        self._left_time = None
        self._media_type = None
        self._dept_name = None
        self.discriminator = None

        if display_name is not None:
            self.display_name = display_name
        if call_number is not None:
            self.call_number = call_number
        if device_type is not None:
            self.device_type = device_type
        if join_time is not None:
            self.join_time = join_time
        if left_time is not None:
            self.left_time = left_time
        if media_type is not None:
            self.media_type = media_type
        if dept_name is not None:
            self.dept_name = dept_name

    @property
    def display_name(self):
        """Gets the display_name of this ConfAttendeeRecordInfo.

        与会者名称。

        :return: The display_name of this ConfAttendeeRecordInfo.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ConfAttendeeRecordInfo.

        与会者名称。

        :param display_name: The display_name of this ConfAttendeeRecordInfo.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def call_number(self):
        """Gets the call_number of this ConfAttendeeRecordInfo.

        号码。

        :return: The call_number of this ConfAttendeeRecordInfo.
        :rtype: str
        """
        return self._call_number

    @call_number.setter
    def call_number(self, call_number):
        """Sets the call_number of this ConfAttendeeRecordInfo.

        号码。

        :param call_number: The call_number of this ConfAttendeeRecordInfo.
        :type call_number: str
        """
        self._call_number = call_number

    @property
    def device_type(self):
        """Gets the device_type of this ConfAttendeeRecordInfo.

        设备类型。

        :return: The device_type of this ConfAttendeeRecordInfo.
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this ConfAttendeeRecordInfo.

        设备类型。

        :param device_type: The device_type of this ConfAttendeeRecordInfo.
        :type device_type: str
        """
        self._device_type = device_type

    @property
    def join_time(self):
        """Gets the join_time of this ConfAttendeeRecordInfo.

        入会时间（UTC时间，单位毫秒）。

        :return: The join_time of this ConfAttendeeRecordInfo.
        :rtype: int
        """
        return self._join_time

    @join_time.setter
    def join_time(self, join_time):
        """Sets the join_time of this ConfAttendeeRecordInfo.

        入会时间（UTC时间，单位毫秒）。

        :param join_time: The join_time of this ConfAttendeeRecordInfo.
        :type join_time: int
        """
        self._join_time = join_time

    @property
    def left_time(self):
        """Gets the left_time of this ConfAttendeeRecordInfo.

        离会时间（UTC时间，单位毫秒）。

        :return: The left_time of this ConfAttendeeRecordInfo.
        :rtype: int
        """
        return self._left_time

    @left_time.setter
    def left_time(self, left_time):
        """Sets the left_time of this ConfAttendeeRecordInfo.

        离会时间（UTC时间，单位毫秒）。

        :param left_time: The left_time of this ConfAttendeeRecordInfo.
        :type left_time: int
        """
        self._left_time = left_time

    @property
    def media_type(self):
        """Gets the media_type of this ConfAttendeeRecordInfo.

        媒体类型。

        :return: The media_type of this ConfAttendeeRecordInfo.
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this ConfAttendeeRecordInfo.

        媒体类型。

        :param media_type: The media_type of this ConfAttendeeRecordInfo.
        :type media_type: str
        """
        self._media_type = media_type

    @property
    def dept_name(self):
        """Gets the dept_name of this ConfAttendeeRecordInfo.

        部门名称。

        :return: The dept_name of this ConfAttendeeRecordInfo.
        :rtype: str
        """
        return self._dept_name

    @dept_name.setter
    def dept_name(self, dept_name):
        """Sets the dept_name of this ConfAttendeeRecordInfo.

        部门名称。

        :param dept_name: The dept_name of this ConfAttendeeRecordInfo.
        :type dept_name: str
        """
        self._dept_name = dept_name

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
        if not isinstance(other, ConfAttendeeRecordInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
