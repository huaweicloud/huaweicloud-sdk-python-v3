# coding: utf-8

import pprint
import re

import six





class VmrCloudLinkDTO:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'vmr_conf_id': 'str',
        'vmr_name': 'str',
        'user_name': 'str',
        'user_account': 'str',
        'guestpwd': 'str',
        'guest_url': 'str',
        'hostpwd': 'str',
        'host_url': 'str',
        'start_conf_without_host': 'bool',
        'gust_first_notice': 'bool',
        'vmr_pkg_id': 'str',
        'max_parties': 'int',
        'duration': 'int',
        'max_manual_prolong_times': 'int',
        'vmr_mode': 'int',
        'expire_date': 'int',
        'remaining_hours': 'int',
        'status': 'int'
    }

    attribute_map = {
        'id': 'id',
        'vmr_conf_id': 'vmrConfId',
        'vmr_name': 'vmrName',
        'user_name': 'userName',
        'user_account': 'userAccount',
        'guestpwd': 'guestpwd',
        'guest_url': 'guestUrl',
        'hostpwd': 'hostpwd',
        'host_url': 'hostUrl',
        'start_conf_without_host': 'startConfWithoutHost',
        'gust_first_notice': 'gustFirstNotice',
        'vmr_pkg_id': 'vmrPkgId',
        'max_parties': 'maxParties',
        'duration': 'duration',
        'max_manual_prolong_times': 'maxManualProlongTimes',
        'vmr_mode': 'vmrMode',
        'expire_date': 'expireDate',
        'remaining_hours': 'remainingHours',
        'status': 'status'
    }

    def __init__(self, id=None, vmr_conf_id=None, vmr_name=None, user_name=None, user_account=None, guestpwd=None, guest_url=None, hostpwd=None, host_url=None, start_conf_without_host=None, gust_first_notice=None, vmr_pkg_id=None, max_parties=None, duration=None, max_manual_prolong_times=None, vmr_mode=None, expire_date=None, remaining_hours=None, status=None):
        """VmrCloudLinkDTO - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._vmr_conf_id = None
        self._vmr_name = None
        self._user_name = None
        self._user_account = None
        self._guestpwd = None
        self._guest_url = None
        self._hostpwd = None
        self._host_url = None
        self._start_conf_without_host = None
        self._gust_first_notice = None
        self._vmr_pkg_id = None
        self._max_parties = None
        self._duration = None
        self._max_manual_prolong_times = None
        self._vmr_mode = None
        self._expire_date = None
        self._remaining_hours = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if vmr_conf_id is not None:
            self.vmr_conf_id = vmr_conf_id
        if vmr_name is not None:
            self.vmr_name = vmr_name
        if user_name is not None:
            self.user_name = user_name
        if user_account is not None:
            self.user_account = user_account
        if guestpwd is not None:
            self.guestpwd = guestpwd
        if guest_url is not None:
            self.guest_url = guest_url
        if hostpwd is not None:
            self.hostpwd = hostpwd
        if host_url is not None:
            self.host_url = host_url
        if start_conf_without_host is not None:
            self.start_conf_without_host = start_conf_without_host
        if gust_first_notice is not None:
            self.gust_first_notice = gust_first_notice
        if vmr_pkg_id is not None:
            self.vmr_pkg_id = vmr_pkg_id
        if max_parties is not None:
            self.max_parties = max_parties
        if duration is not None:
            self.duration = duration
        if max_manual_prolong_times is not None:
            self.max_manual_prolong_times = max_manual_prolong_times
        if vmr_mode is not None:
            self.vmr_mode = vmr_mode
        if expire_date is not None:
            self.expire_date = expire_date
        if remaining_hours is not None:
            self.remaining_hours = remaining_hours
        if status is not None:
            self.status = status

    @property
    def id(self):
        """Gets the id of this VmrCloudLinkDTO.

        唯一标识

        :return: The id of this VmrCloudLinkDTO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VmrCloudLinkDTO.

        唯一标识

        :param id: The id of this VmrCloudLinkDTO.
        :type: str
        """
        self._id = id

    @property
    def vmr_conf_id(self):
        """Gets the vmr_conf_id of this VmrCloudLinkDTO.

        vmr虚拟会议室Id

        :return: The vmr_conf_id of this VmrCloudLinkDTO.
        :rtype: str
        """
        return self._vmr_conf_id

    @vmr_conf_id.setter
    def vmr_conf_id(self, vmr_conf_id):
        """Sets the vmr_conf_id of this VmrCloudLinkDTO.

        vmr虚拟会议室Id

        :param vmr_conf_id: The vmr_conf_id of this VmrCloudLinkDTO.
        :type: str
        """
        self._vmr_conf_id = vmr_conf_id

    @property
    def vmr_name(self):
        """Gets the vmr_name of this VmrCloudLinkDTO.

        vmr虚拟会议室名称

        :return: The vmr_name of this VmrCloudLinkDTO.
        :rtype: str
        """
        return self._vmr_name

    @vmr_name.setter
    def vmr_name(self, vmr_name):
        """Sets the vmr_name of this VmrCloudLinkDTO.

        vmr虚拟会议室名称

        :param vmr_name: The vmr_name of this VmrCloudLinkDTO.
        :type: str
        """
        self._vmr_name = vmr_name

    @property
    def user_name(self):
        """Gets the user_name of this VmrCloudLinkDTO.

        用户名称

        :return: The user_name of this VmrCloudLinkDTO.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this VmrCloudLinkDTO.

        用户名称

        :param user_name: The user_name of this VmrCloudLinkDTO.
        :type: str
        """
        self._user_name = user_name

    @property
    def user_account(self):
        """Gets the user_account of this VmrCloudLinkDTO.

        用户账号

        :return: The user_account of this VmrCloudLinkDTO.
        :rtype: str
        """
        return self._user_account

    @user_account.setter
    def user_account(self, user_account):
        """Sets the user_account of this VmrCloudLinkDTO.

        用户账号

        :param user_account: The user_account of this VmrCloudLinkDTO.
        :type: str
        """
        self._user_account = user_account

    @property
    def guestpwd(self):
        """Gets the guestpwd of this VmrCloudLinkDTO.

        来宾密码

        :return: The guestpwd of this VmrCloudLinkDTO.
        :rtype: str
        """
        return self._guestpwd

    @guestpwd.setter
    def guestpwd(self, guestpwd):
        """Sets the guestpwd of this VmrCloudLinkDTO.

        来宾密码

        :param guestpwd: The guestpwd of this VmrCloudLinkDTO.
        :type: str
        """
        self._guestpwd = guestpwd

    @property
    def guest_url(self):
        """Gets the guest_url of this VmrCloudLinkDTO.

        来宾与会链接

        :return: The guest_url of this VmrCloudLinkDTO.
        :rtype: str
        """
        return self._guest_url

    @guest_url.setter
    def guest_url(self, guest_url):
        """Sets the guest_url of this VmrCloudLinkDTO.

        来宾与会链接

        :param guest_url: The guest_url of this VmrCloudLinkDTO.
        :type: str
        """
        self._guest_url = guest_url

    @property
    def hostpwd(self):
        """Gets the hostpwd of this VmrCloudLinkDTO.

        主席密码

        :return: The hostpwd of this VmrCloudLinkDTO.
        :rtype: str
        """
        return self._hostpwd

    @hostpwd.setter
    def hostpwd(self, hostpwd):
        """Sets the hostpwd of this VmrCloudLinkDTO.

        主席密码

        :param hostpwd: The hostpwd of this VmrCloudLinkDTO.
        :type: str
        """
        self._hostpwd = hostpwd

    @property
    def host_url(self):
        """Gets the host_url of this VmrCloudLinkDTO.

        主席与会链接

        :return: The host_url of this VmrCloudLinkDTO.
        :rtype: str
        """
        return self._host_url

    @host_url.setter
    def host_url(self, host_url):
        """Sets the host_url of this VmrCloudLinkDTO.

        主席与会链接

        :param host_url: The host_url of this VmrCloudLinkDTO.
        :type: str
        """
        self._host_url = host_url

    @property
    def start_conf_without_host(self):
        """Gets the start_conf_without_host of this VmrCloudLinkDTO.

        允许来宾先入会

        :return: The start_conf_without_host of this VmrCloudLinkDTO.
        :rtype: bool
        """
        return self._start_conf_without_host

    @start_conf_without_host.setter
    def start_conf_without_host(self, start_conf_without_host):
        """Sets the start_conf_without_host of this VmrCloudLinkDTO.

        允许来宾先入会

        :param start_conf_without_host: The start_conf_without_host of this VmrCloudLinkDTO.
        :type: bool
        """
        self._start_conf_without_host = start_conf_without_host

    @property
    def gust_first_notice(self):
        """Gets the gust_first_notice of this VmrCloudLinkDTO.

        来宾先入会发送通知

        :return: The gust_first_notice of this VmrCloudLinkDTO.
        :rtype: bool
        """
        return self._gust_first_notice

    @gust_first_notice.setter
    def gust_first_notice(self, gust_first_notice):
        """Sets the gust_first_notice of this VmrCloudLinkDTO.

        来宾先入会发送通知

        :param gust_first_notice: The gust_first_notice of this VmrCloudLinkDTO.
        :type: bool
        """
        self._gust_first_notice = gust_first_notice

    @property
    def vmr_pkg_id(self):
        """Gets the vmr_pkg_id of this VmrCloudLinkDTO.

        对应的云会议室套餐包ID

        :return: The vmr_pkg_id of this VmrCloudLinkDTO.
        :rtype: str
        """
        return self._vmr_pkg_id

    @vmr_pkg_id.setter
    def vmr_pkg_id(self, vmr_pkg_id):
        """Sets the vmr_pkg_id of this VmrCloudLinkDTO.

        对应的云会议室套餐包ID

        :param vmr_pkg_id: The vmr_pkg_id of this VmrCloudLinkDTO.
        :type: str
        """
        self._vmr_pkg_id = vmr_pkg_id

    @property
    def max_parties(self):
        """Gets the max_parties of this VmrCloudLinkDTO.

        对应的云会议室套餐包最大与会方数

        :return: The max_parties of this VmrCloudLinkDTO.
        :rtype: int
        """
        return self._max_parties

    @max_parties.setter
    def max_parties(self, max_parties):
        """Sets the max_parties of this VmrCloudLinkDTO.

        对应的云会议室套餐包最大与会方数

        :param max_parties: The max_parties of this VmrCloudLinkDTO.
        :type: int
        """
        self._max_parties = max_parties

    @property
    def duration(self):
        """Gets the duration of this VmrCloudLinkDTO.

        对应的云会议室套餐包最大与会时长，若为0，则代表不限制

        :return: The duration of this VmrCloudLinkDTO.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this VmrCloudLinkDTO.

        对应的云会议室套餐包最大与会时长，若为0，则代表不限制

        :param duration: The duration of this VmrCloudLinkDTO.
        :type: int
        """
        self._duration = duration

    @property
    def max_manual_prolong_times(self):
        """Gets the max_manual_prolong_times of this VmrCloudLinkDTO.

        对应的云会议室套餐包最大会议时长时间到后的延长会议次数

        :return: The max_manual_prolong_times of this VmrCloudLinkDTO.
        :rtype: int
        """
        return self._max_manual_prolong_times

    @max_manual_prolong_times.setter
    def max_manual_prolong_times(self, max_manual_prolong_times):
        """Sets the max_manual_prolong_times of this VmrCloudLinkDTO.

        对应的云会议室套餐包最大会议时长时间到后的延长会议次数

        :param max_manual_prolong_times: The max_manual_prolong_times of this VmrCloudLinkDTO.
        :type: int
        """
        self._max_manual_prolong_times = max_manual_prolong_times

    @property
    def vmr_mode(self):
        """Gets the vmr_mode of this VmrCloudLinkDTO.

        VMR模式 * 0：个人 * 1：专用 * 2：网络研讨会 

        :return: The vmr_mode of this VmrCloudLinkDTO.
        :rtype: int
        """
        return self._vmr_mode

    @vmr_mode.setter
    def vmr_mode(self, vmr_mode):
        """Sets the vmr_mode of this VmrCloudLinkDTO.

        VMR模式 * 0：个人 * 1：专用 * 2：网络研讨会 

        :param vmr_mode: The vmr_mode of this VmrCloudLinkDTO.
        :type: int
        """
        self._vmr_mode = vmr_mode

    @property
    def expire_date(self):
        """Gets the expire_date of this VmrCloudLinkDTO.

        到期时间，utc时间戳

        :return: The expire_date of this VmrCloudLinkDTO.
        :rtype: int
        """
        return self._expire_date

    @expire_date.setter
    def expire_date(self, expire_date):
        """Sets the expire_date of this VmrCloudLinkDTO.

        到期时间，utc时间戳

        :param expire_date: The expire_date of this VmrCloudLinkDTO.
        :type: int
        """
        self._expire_date = expire_date

    @property
    def remaining_hours(self):
        """Gets the remaining_hours of this VmrCloudLinkDTO.

        剩余时间（小时，不足按1小时计）

        :return: The remaining_hours of this VmrCloudLinkDTO.
        :rtype: int
        """
        return self._remaining_hours

    @remaining_hours.setter
    def remaining_hours(self, remaining_hours):
        """Sets the remaining_hours of this VmrCloudLinkDTO.

        剩余时间（小时，不足按1小时计）

        :param remaining_hours: The remaining_hours of this VmrCloudLinkDTO.
        :type: int
        """
        self._remaining_hours = remaining_hours

    @property
    def status(self):
        """Gets the status of this VmrCloudLinkDTO.

        vmr虚拟会议室状态。 * 0、正常 * 1、停用 

        :return: The status of this VmrCloudLinkDTO.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this VmrCloudLinkDTO.

        vmr虚拟会议室状态。 * 0、正常 * 1、停用 

        :param status: The status of this VmrCloudLinkDTO.
        :type: int
        """
        self._status = status

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
        if not isinstance(other, VmrCloudLinkDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
