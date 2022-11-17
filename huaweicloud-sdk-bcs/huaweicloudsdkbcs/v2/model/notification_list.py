# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NotificationList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'channel_name': 'str',
        'status': 'str',
        'updated_time': 'str',
        'tc3_need': 'bool',
        'invitor_info': 'InvitorInfo',
        'invitee_info': 'InviteeInfo',
        'hide': 'int',
        'invitee_orgs': 'list[OrganizationV2]',
        'read_status': 'int',
        'cross_version_upgrade': 'str'
    }

    attribute_map = {
        'channel_name': 'channel_name',
        'status': 'status',
        'updated_time': 'updated_time',
        'tc3_need': 'tc3_need',
        'invitor_info': 'invitor_info',
        'invitee_info': 'invitee_info',
        'hide': 'hide',
        'invitee_orgs': 'invitee_orgs',
        'read_status': 'read_status',
        'cross_version_upgrade': 'cross_version_upgrade'
    }

    def __init__(self, channel_name=None, status=None, updated_time=None, tc3_need=None, invitor_info=None, invitee_info=None, hide=None, invitee_orgs=None, read_status=None, cross_version_upgrade=None):
        """NotificationList

        The model defined in huaweicloud sdk

        :param channel_name: 通道名称
        :type channel_name: str
        :param status: 当前状态
        :type status: str
        :param updated_time: 更新时间
        :type updated_time: str
        :param tc3_need: 是否开启可信
        :type tc3_need: bool
        :param invitor_info: 
        :type invitor_info: :class:`huaweicloudsdkbcs.v2.InvitorInfo`
        :param invitee_info: 
        :type invitee_info: :class:`huaweicloudsdkbcs.v2.InviteeInfo`
        :param hide: 是否删除
        :type hide: int
        :param invitee_orgs: 被邀请的组织信息
        :type invitee_orgs: list[:class:`huaweicloudsdkbcs.v2.OrganizationV2`]
        :param read_status: 阅读状态值
        :type read_status: int
        :param cross_version_upgrade: 跨版本进行升级
        :type cross_version_upgrade: str
        """
        
        

        self._channel_name = None
        self._status = None
        self._updated_time = None
        self._tc3_need = None
        self._invitor_info = None
        self._invitee_info = None
        self._hide = None
        self._invitee_orgs = None
        self._read_status = None
        self._cross_version_upgrade = None
        self.discriminator = None

        if channel_name is not None:
            self.channel_name = channel_name
        if status is not None:
            self.status = status
        if updated_time is not None:
            self.updated_time = updated_time
        if tc3_need is not None:
            self.tc3_need = tc3_need
        if invitor_info is not None:
            self.invitor_info = invitor_info
        if invitee_info is not None:
            self.invitee_info = invitee_info
        if hide is not None:
            self.hide = hide
        if invitee_orgs is not None:
            self.invitee_orgs = invitee_orgs
        if read_status is not None:
            self.read_status = read_status
        if cross_version_upgrade is not None:
            self.cross_version_upgrade = cross_version_upgrade

    @property
    def channel_name(self):
        """Gets the channel_name of this NotificationList.

        通道名称

        :return: The channel_name of this NotificationList.
        :rtype: str
        """
        return self._channel_name

    @channel_name.setter
    def channel_name(self, channel_name):
        """Sets the channel_name of this NotificationList.

        通道名称

        :param channel_name: The channel_name of this NotificationList.
        :type channel_name: str
        """
        self._channel_name = channel_name

    @property
    def status(self):
        """Gets the status of this NotificationList.

        当前状态

        :return: The status of this NotificationList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NotificationList.

        当前状态

        :param status: The status of this NotificationList.
        :type status: str
        """
        self._status = status

    @property
    def updated_time(self):
        """Gets the updated_time of this NotificationList.

        更新时间

        :return: The updated_time of this NotificationList.
        :rtype: str
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        """Sets the updated_time of this NotificationList.

        更新时间

        :param updated_time: The updated_time of this NotificationList.
        :type updated_time: str
        """
        self._updated_time = updated_time

    @property
    def tc3_need(self):
        """Gets the tc3_need of this NotificationList.

        是否开启可信

        :return: The tc3_need of this NotificationList.
        :rtype: bool
        """
        return self._tc3_need

    @tc3_need.setter
    def tc3_need(self, tc3_need):
        """Sets the tc3_need of this NotificationList.

        是否开启可信

        :param tc3_need: The tc3_need of this NotificationList.
        :type tc3_need: bool
        """
        self._tc3_need = tc3_need

    @property
    def invitor_info(self):
        """Gets the invitor_info of this NotificationList.

        :return: The invitor_info of this NotificationList.
        :rtype: :class:`huaweicloudsdkbcs.v2.InvitorInfo`
        """
        return self._invitor_info

    @invitor_info.setter
    def invitor_info(self, invitor_info):
        """Sets the invitor_info of this NotificationList.

        :param invitor_info: The invitor_info of this NotificationList.
        :type invitor_info: :class:`huaweicloudsdkbcs.v2.InvitorInfo`
        """
        self._invitor_info = invitor_info

    @property
    def invitee_info(self):
        """Gets the invitee_info of this NotificationList.

        :return: The invitee_info of this NotificationList.
        :rtype: :class:`huaweicloudsdkbcs.v2.InviteeInfo`
        """
        return self._invitee_info

    @invitee_info.setter
    def invitee_info(self, invitee_info):
        """Sets the invitee_info of this NotificationList.

        :param invitee_info: The invitee_info of this NotificationList.
        :type invitee_info: :class:`huaweicloudsdkbcs.v2.InviteeInfo`
        """
        self._invitee_info = invitee_info

    @property
    def hide(self):
        """Gets the hide of this NotificationList.

        是否删除

        :return: The hide of this NotificationList.
        :rtype: int
        """
        return self._hide

    @hide.setter
    def hide(self, hide):
        """Sets the hide of this NotificationList.

        是否删除

        :param hide: The hide of this NotificationList.
        :type hide: int
        """
        self._hide = hide

    @property
    def invitee_orgs(self):
        """Gets the invitee_orgs of this NotificationList.

        被邀请的组织信息

        :return: The invitee_orgs of this NotificationList.
        :rtype: list[:class:`huaweicloudsdkbcs.v2.OrganizationV2`]
        """
        return self._invitee_orgs

    @invitee_orgs.setter
    def invitee_orgs(self, invitee_orgs):
        """Sets the invitee_orgs of this NotificationList.

        被邀请的组织信息

        :param invitee_orgs: The invitee_orgs of this NotificationList.
        :type invitee_orgs: list[:class:`huaweicloudsdkbcs.v2.OrganizationV2`]
        """
        self._invitee_orgs = invitee_orgs

    @property
    def read_status(self):
        """Gets the read_status of this NotificationList.

        阅读状态值

        :return: The read_status of this NotificationList.
        :rtype: int
        """
        return self._read_status

    @read_status.setter
    def read_status(self, read_status):
        """Sets the read_status of this NotificationList.

        阅读状态值

        :param read_status: The read_status of this NotificationList.
        :type read_status: int
        """
        self._read_status = read_status

    @property
    def cross_version_upgrade(self):
        """Gets the cross_version_upgrade of this NotificationList.

        跨版本进行升级

        :return: The cross_version_upgrade of this NotificationList.
        :rtype: str
        """
        return self._cross_version_upgrade

    @cross_version_upgrade.setter
    def cross_version_upgrade(self, cross_version_upgrade):
        """Sets the cross_version_upgrade of this NotificationList.

        跨版本进行升级

        :param cross_version_upgrade: The cross_version_upgrade of this NotificationList.
        :type cross_version_upgrade: str
        """
        self._cross_version_upgrade = cross_version_upgrade

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
        if not isinstance(other, NotificationList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
