# coding: utf-8

import pprint
import re

import six





class UpdatePublicationRequestDTO:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'publish_name': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'dept_list': 'list[str]',
        'device_list': 'list[str]',
        'program_list': 'list[str]'
    }

    attribute_map = {
        'publish_name': 'publishName',
        'start_time': 'startTime',
        'end_time': 'endTime',
        'dept_list': 'deptList',
        'device_list': 'deviceList',
        'program_list': 'programList'
    }

    def __init__(self, publish_name=None, start_time=None, end_time=None, dept_list=None, device_list=None, program_list=None):
        """UpdatePublicationRequestDTO - a model defined in huaweicloud sdk"""
        
        

        self._publish_name = None
        self._start_time = None
        self._end_time = None
        self._dept_list = None
        self._device_list = None
        self._program_list = None
        self.discriminator = None

        if publish_name is not None:
            self.publish_name = publish_name
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if dept_list is not None:
            self.dept_list = dept_list
        if device_list is not None:
            self.device_list = device_list
        if program_list is not None:
            self.program_list = program_list

    @property
    def publish_name(self):
        """Gets the publish_name of this UpdatePublicationRequestDTO.

        发布名称

        :return: The publish_name of this UpdatePublicationRequestDTO.
        :rtype: str
        """
        return self._publish_name

    @publish_name.setter
    def publish_name(self, publish_name):
        """Sets the publish_name of this UpdatePublicationRequestDTO.

        发布名称

        :param publish_name: The publish_name of this UpdatePublicationRequestDTO.
        :type: str
        """
        self._publish_name = publish_name

    @property
    def start_time(self):
        """Gets the start_time of this UpdatePublicationRequestDTO.

        开始时间

        :return: The start_time of this UpdatePublicationRequestDTO.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        """Sets the start_time of this UpdatePublicationRequestDTO.

        开始时间

        :param start_time: The start_time of this UpdatePublicationRequestDTO.
        :type: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        """Gets the end_time of this UpdatePublicationRequestDTO.

        结束时间

        :return: The end_time of this UpdatePublicationRequestDTO.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this UpdatePublicationRequestDTO.

        结束时间

        :param end_time: The end_time of this UpdatePublicationRequestDTO.
        :type: int
        """
        self._end_time = end_time

    @property
    def dept_list(self):
        """Gets the dept_list of this UpdatePublicationRequestDTO.

        发布到部门编码列表

        :return: The dept_list of this UpdatePublicationRequestDTO.
        :rtype: list[str]
        """
        return self._dept_list

    @dept_list.setter
    def dept_list(self, dept_list):
        """Sets the dept_list of this UpdatePublicationRequestDTO.

        发布到部门编码列表

        :param dept_list: The dept_list of this UpdatePublicationRequestDTO.
        :type: list[str]
        """
        self._dept_list = dept_list

    @property
    def device_list(self):
        """Gets the device_list of this UpdatePublicationRequestDTO.

        发布到设备用户ID列表

        :return: The device_list of this UpdatePublicationRequestDTO.
        :rtype: list[str]
        """
        return self._device_list

    @device_list.setter
    def device_list(self, device_list):
        """Sets the device_list of this UpdatePublicationRequestDTO.

        发布到设备用户ID列表

        :param device_list: The device_list of this UpdatePublicationRequestDTO.
        :type: list[str]
        """
        self._device_list = device_list

    @property
    def program_list(self):
        """Gets the program_list of this UpdatePublicationRequestDTO.

        发布节目ID列表

        :return: The program_list of this UpdatePublicationRequestDTO.
        :rtype: list[str]
        """
        return self._program_list

    @program_list.setter
    def program_list(self, program_list):
        """Sets the program_list of this UpdatePublicationRequestDTO.

        发布节目ID列表

        :param program_list: The program_list of this UpdatePublicationRequestDTO.
        :type: list[str]
        """
        self._program_list = program_list

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
        if not isinstance(other, UpdatePublicationRequestDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
