# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StatisticParticipateDataItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'time': 'str',
        'conf_user_name': 'str',
        'conf_user_account': 'str',
        'conf_user_dept_name': 'str',
        'conf_user_count': 'str',
        'conf_user_duration': 'str',
        'conf_hard_terminal_name': 'str',
        'conf_hard_terminal_model': 'str',
        'conf_hard_terminal_user_id': 'str',
        'conf_hard_terminal_count': 'str',
        'conf_hard_terminal_duration': 'str',
        'device_type': 'str',
        'device_version': 'str',
        'device_attendance_count': 'str'
    }

    attribute_map = {
        'time': 'time',
        'conf_user_name': 'confUserName',
        'conf_user_account': 'confUserAccount',
        'conf_user_dept_name': 'confUserDeptName',
        'conf_user_count': 'confUserCount',
        'conf_user_duration': 'confUserDuration',
        'conf_hard_terminal_name': 'confHardTerminalName',
        'conf_hard_terminal_model': 'confHardTerminalModel',
        'conf_hard_terminal_user_id': 'confHardTerminalUserId',
        'conf_hard_terminal_count': 'confHardTerminalCount',
        'conf_hard_terminal_duration': 'confHardTerminalDuration',
        'device_type': 'deviceType',
        'device_version': 'deviceVersion',
        'device_attendance_count': 'deviceAttendanceCount'
    }

    def __init__(self, time=None, conf_user_name=None, conf_user_account=None, conf_user_dept_name=None, conf_user_count=None, conf_user_duration=None, conf_hard_terminal_name=None, conf_hard_terminal_model=None, conf_hard_terminal_user_id=None, conf_hard_terminal_count=None, conf_hard_terminal_duration=None, device_type=None, device_version=None, device_attendance_count=None):
        """StatisticParticipateDataItem

        The model defined in huaweicloud sdk

        :param time: 日期/月份。
        :type time: str
        :param conf_user_name: 与会用户名称。 category &#x3D; user_participate_info时有效。
        :type conf_user_name: str
        :param conf_user_account: 与会用户账户。 category &#x3D; user_participate_info时有效。
        :type conf_user_account: str
        :param conf_user_dept_name: 与会用户所属部门。 category &#x3D; user_participate_info时有效。
        :type conf_user_dept_name: str
        :param conf_user_count: 用户与会数。 category &#x3D; user_participate_info时有效。
        :type conf_user_count: str
        :param conf_user_duration: 用户与会时长(秒)。 category &#x3D; user_participate_info时有效。
        :type conf_user_duration: str
        :param conf_hard_terminal_name: 与会硬件终端名称。 category &#x3D; hard_terminal_participate_info时有效。
        :type conf_hard_terminal_name: str
        :param conf_hard_terminal_model: 与会硬件终端型号。 category &#x3D; hard_terminal_participate_info时有效。
        :type conf_hard_terminal_model: str
        :param conf_hard_terminal_user_id: 与会硬件终端的用户ID。 category &#x3D; hard_terminal_participate_info时有效。
        :type conf_hard_terminal_user_id: str
        :param conf_hard_terminal_count: 硬件终端与会数。 category &#x3D; hard_terminal_participate_info时有效。
        :type conf_hard_terminal_count: str
        :param conf_hard_terminal_duration: 硬件终端与会时长(秒)。 category &#x3D; hard_terminal_participate_info时有效。
        :type conf_hard_terminal_duration: str
        :param device_type: 与会设备类型。 category &#x3D; participant_type_info时有效。
        :type device_type: str
        :param device_version: 与会设备版本。 category &#x3D; participant_type_info时有效。
        :type device_version: str
        :param device_attendance_count: 设备与会数。 category &#x3D; participant_type_info时有效。
        :type device_attendance_count: str
        """
        
        

        self._time = None
        self._conf_user_name = None
        self._conf_user_account = None
        self._conf_user_dept_name = None
        self._conf_user_count = None
        self._conf_user_duration = None
        self._conf_hard_terminal_name = None
        self._conf_hard_terminal_model = None
        self._conf_hard_terminal_user_id = None
        self._conf_hard_terminal_count = None
        self._conf_hard_terminal_duration = None
        self._device_type = None
        self._device_version = None
        self._device_attendance_count = None
        self.discriminator = None

        if time is not None:
            self.time = time
        if conf_user_name is not None:
            self.conf_user_name = conf_user_name
        if conf_user_account is not None:
            self.conf_user_account = conf_user_account
        if conf_user_dept_name is not None:
            self.conf_user_dept_name = conf_user_dept_name
        if conf_user_count is not None:
            self.conf_user_count = conf_user_count
        if conf_user_duration is not None:
            self.conf_user_duration = conf_user_duration
        if conf_hard_terminal_name is not None:
            self.conf_hard_terminal_name = conf_hard_terminal_name
        if conf_hard_terminal_model is not None:
            self.conf_hard_terminal_model = conf_hard_terminal_model
        if conf_hard_terminal_user_id is not None:
            self.conf_hard_terminal_user_id = conf_hard_terminal_user_id
        if conf_hard_terminal_count is not None:
            self.conf_hard_terminal_count = conf_hard_terminal_count
        if conf_hard_terminal_duration is not None:
            self.conf_hard_terminal_duration = conf_hard_terminal_duration
        if device_type is not None:
            self.device_type = device_type
        if device_version is not None:
            self.device_version = device_version
        if device_attendance_count is not None:
            self.device_attendance_count = device_attendance_count

    @property
    def time(self):
        """Gets the time of this StatisticParticipateDataItem.

        日期/月份。

        :return: The time of this StatisticParticipateDataItem.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this StatisticParticipateDataItem.

        日期/月份。

        :param time: The time of this StatisticParticipateDataItem.
        :type time: str
        """
        self._time = time

    @property
    def conf_user_name(self):
        """Gets the conf_user_name of this StatisticParticipateDataItem.

        与会用户名称。 category = user_participate_info时有效。

        :return: The conf_user_name of this StatisticParticipateDataItem.
        :rtype: str
        """
        return self._conf_user_name

    @conf_user_name.setter
    def conf_user_name(self, conf_user_name):
        """Sets the conf_user_name of this StatisticParticipateDataItem.

        与会用户名称。 category = user_participate_info时有效。

        :param conf_user_name: The conf_user_name of this StatisticParticipateDataItem.
        :type conf_user_name: str
        """
        self._conf_user_name = conf_user_name

    @property
    def conf_user_account(self):
        """Gets the conf_user_account of this StatisticParticipateDataItem.

        与会用户账户。 category = user_participate_info时有效。

        :return: The conf_user_account of this StatisticParticipateDataItem.
        :rtype: str
        """
        return self._conf_user_account

    @conf_user_account.setter
    def conf_user_account(self, conf_user_account):
        """Sets the conf_user_account of this StatisticParticipateDataItem.

        与会用户账户。 category = user_participate_info时有效。

        :param conf_user_account: The conf_user_account of this StatisticParticipateDataItem.
        :type conf_user_account: str
        """
        self._conf_user_account = conf_user_account

    @property
    def conf_user_dept_name(self):
        """Gets the conf_user_dept_name of this StatisticParticipateDataItem.

        与会用户所属部门。 category = user_participate_info时有效。

        :return: The conf_user_dept_name of this StatisticParticipateDataItem.
        :rtype: str
        """
        return self._conf_user_dept_name

    @conf_user_dept_name.setter
    def conf_user_dept_name(self, conf_user_dept_name):
        """Sets the conf_user_dept_name of this StatisticParticipateDataItem.

        与会用户所属部门。 category = user_participate_info时有效。

        :param conf_user_dept_name: The conf_user_dept_name of this StatisticParticipateDataItem.
        :type conf_user_dept_name: str
        """
        self._conf_user_dept_name = conf_user_dept_name

    @property
    def conf_user_count(self):
        """Gets the conf_user_count of this StatisticParticipateDataItem.

        用户与会数。 category = user_participate_info时有效。

        :return: The conf_user_count of this StatisticParticipateDataItem.
        :rtype: str
        """
        return self._conf_user_count

    @conf_user_count.setter
    def conf_user_count(self, conf_user_count):
        """Sets the conf_user_count of this StatisticParticipateDataItem.

        用户与会数。 category = user_participate_info时有效。

        :param conf_user_count: The conf_user_count of this StatisticParticipateDataItem.
        :type conf_user_count: str
        """
        self._conf_user_count = conf_user_count

    @property
    def conf_user_duration(self):
        """Gets the conf_user_duration of this StatisticParticipateDataItem.

        用户与会时长(秒)。 category = user_participate_info时有效。

        :return: The conf_user_duration of this StatisticParticipateDataItem.
        :rtype: str
        """
        return self._conf_user_duration

    @conf_user_duration.setter
    def conf_user_duration(self, conf_user_duration):
        """Sets the conf_user_duration of this StatisticParticipateDataItem.

        用户与会时长(秒)。 category = user_participate_info时有效。

        :param conf_user_duration: The conf_user_duration of this StatisticParticipateDataItem.
        :type conf_user_duration: str
        """
        self._conf_user_duration = conf_user_duration

    @property
    def conf_hard_terminal_name(self):
        """Gets the conf_hard_terminal_name of this StatisticParticipateDataItem.

        与会硬件终端名称。 category = hard_terminal_participate_info时有效。

        :return: The conf_hard_terminal_name of this StatisticParticipateDataItem.
        :rtype: str
        """
        return self._conf_hard_terminal_name

    @conf_hard_terminal_name.setter
    def conf_hard_terminal_name(self, conf_hard_terminal_name):
        """Sets the conf_hard_terminal_name of this StatisticParticipateDataItem.

        与会硬件终端名称。 category = hard_terminal_participate_info时有效。

        :param conf_hard_terminal_name: The conf_hard_terminal_name of this StatisticParticipateDataItem.
        :type conf_hard_terminal_name: str
        """
        self._conf_hard_terminal_name = conf_hard_terminal_name

    @property
    def conf_hard_terminal_model(self):
        """Gets the conf_hard_terminal_model of this StatisticParticipateDataItem.

        与会硬件终端型号。 category = hard_terminal_participate_info时有效。

        :return: The conf_hard_terminal_model of this StatisticParticipateDataItem.
        :rtype: str
        """
        return self._conf_hard_terminal_model

    @conf_hard_terminal_model.setter
    def conf_hard_terminal_model(self, conf_hard_terminal_model):
        """Sets the conf_hard_terminal_model of this StatisticParticipateDataItem.

        与会硬件终端型号。 category = hard_terminal_participate_info时有效。

        :param conf_hard_terminal_model: The conf_hard_terminal_model of this StatisticParticipateDataItem.
        :type conf_hard_terminal_model: str
        """
        self._conf_hard_terminal_model = conf_hard_terminal_model

    @property
    def conf_hard_terminal_user_id(self):
        """Gets the conf_hard_terminal_user_id of this StatisticParticipateDataItem.

        与会硬件终端的用户ID。 category = hard_terminal_participate_info时有效。

        :return: The conf_hard_terminal_user_id of this StatisticParticipateDataItem.
        :rtype: str
        """
        return self._conf_hard_terminal_user_id

    @conf_hard_terminal_user_id.setter
    def conf_hard_terminal_user_id(self, conf_hard_terminal_user_id):
        """Sets the conf_hard_terminal_user_id of this StatisticParticipateDataItem.

        与会硬件终端的用户ID。 category = hard_terminal_participate_info时有效。

        :param conf_hard_terminal_user_id: The conf_hard_terminal_user_id of this StatisticParticipateDataItem.
        :type conf_hard_terminal_user_id: str
        """
        self._conf_hard_terminal_user_id = conf_hard_terminal_user_id

    @property
    def conf_hard_terminal_count(self):
        """Gets the conf_hard_terminal_count of this StatisticParticipateDataItem.

        硬件终端与会数。 category = hard_terminal_participate_info时有效。

        :return: The conf_hard_terminal_count of this StatisticParticipateDataItem.
        :rtype: str
        """
        return self._conf_hard_terminal_count

    @conf_hard_terminal_count.setter
    def conf_hard_terminal_count(self, conf_hard_terminal_count):
        """Sets the conf_hard_terminal_count of this StatisticParticipateDataItem.

        硬件终端与会数。 category = hard_terminal_participate_info时有效。

        :param conf_hard_terminal_count: The conf_hard_terminal_count of this StatisticParticipateDataItem.
        :type conf_hard_terminal_count: str
        """
        self._conf_hard_terminal_count = conf_hard_terminal_count

    @property
    def conf_hard_terminal_duration(self):
        """Gets the conf_hard_terminal_duration of this StatisticParticipateDataItem.

        硬件终端与会时长(秒)。 category = hard_terminal_participate_info时有效。

        :return: The conf_hard_terminal_duration of this StatisticParticipateDataItem.
        :rtype: str
        """
        return self._conf_hard_terminal_duration

    @conf_hard_terminal_duration.setter
    def conf_hard_terminal_duration(self, conf_hard_terminal_duration):
        """Sets the conf_hard_terminal_duration of this StatisticParticipateDataItem.

        硬件终端与会时长(秒)。 category = hard_terminal_participate_info时有效。

        :param conf_hard_terminal_duration: The conf_hard_terminal_duration of this StatisticParticipateDataItem.
        :type conf_hard_terminal_duration: str
        """
        self._conf_hard_terminal_duration = conf_hard_terminal_duration

    @property
    def device_type(self):
        """Gets the device_type of this StatisticParticipateDataItem.

        与会设备类型。 category = participant_type_info时有效。

        :return: The device_type of this StatisticParticipateDataItem.
        :rtype: str
        """
        return self._device_type

    @device_type.setter
    def device_type(self, device_type):
        """Sets the device_type of this StatisticParticipateDataItem.

        与会设备类型。 category = participant_type_info时有效。

        :param device_type: The device_type of this StatisticParticipateDataItem.
        :type device_type: str
        """
        self._device_type = device_type

    @property
    def device_version(self):
        """Gets the device_version of this StatisticParticipateDataItem.

        与会设备版本。 category = participant_type_info时有效。

        :return: The device_version of this StatisticParticipateDataItem.
        :rtype: str
        """
        return self._device_version

    @device_version.setter
    def device_version(self, device_version):
        """Sets the device_version of this StatisticParticipateDataItem.

        与会设备版本。 category = participant_type_info时有效。

        :param device_version: The device_version of this StatisticParticipateDataItem.
        :type device_version: str
        """
        self._device_version = device_version

    @property
    def device_attendance_count(self):
        """Gets the device_attendance_count of this StatisticParticipateDataItem.

        设备与会数。 category = participant_type_info时有效。

        :return: The device_attendance_count of this StatisticParticipateDataItem.
        :rtype: str
        """
        return self._device_attendance_count

    @device_attendance_count.setter
    def device_attendance_count(self, device_attendance_count):
        """Sets the device_attendance_count of this StatisticParticipateDataItem.

        设备与会数。 category = participant_type_info时有效。

        :param device_attendance_count: The device_attendance_count of this StatisticParticipateDataItem.
        :type device_attendance_count: str
        """
        self._device_attendance_count = device_attendance_count

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
        if not isinstance(other, StatisticParticipateDataItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
