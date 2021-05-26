# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowSpResourceResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'te1080p_hard_count': 'ResDetailDTO',
        'te720p_hard_count': 'ResDetailDTO',
        'te_soft_count': 'ResDetailDTO',
        'room_count': 'ResDetailDTO',
        'record_capability': 'ResDetailDTO',
        'conf_call_count': 'ResDetailDTO',
        'live_count': 'ResDetailDTO',
        'corp_count': 'ResDetailDTO',
        'third_party_hard_count': 'ResDetailDTO',
        'hw_vision_count': 'ResDetailDTO',
        'idea_hub_count': 'ResDetailDTO',
        'enable_pstn': 'bool',
        'enable_sms': 'bool',
        'group_list': 'list[QueryCorpGroupDTO]'
    }

    attribute_map = {
        'te1080p_hard_count': 'te1080pHardCount',
        'te720p_hard_count': 'te720pHardCount',
        'te_soft_count': 'teSoftCount',
        'room_count': 'roomCount',
        'record_capability': 'recordCapability',
        'conf_call_count': 'confCallCount',
        'live_count': 'liveCount',
        'corp_count': 'corpCount',
        'third_party_hard_count': 'thirdPartyHardCount',
        'hw_vision_count': 'hwVisionCount',
        'idea_hub_count': 'ideaHubCount',
        'enable_pstn': 'enablePstn',
        'enable_sms': 'enableSMS',
        'group_list': 'groupList'
    }

    def __init__(self, te1080p_hard_count=None, te720p_hard_count=None, te_soft_count=None, room_count=None, record_capability=None, conf_call_count=None, live_count=None, corp_count=None, third_party_hard_count=None, hw_vision_count=None, idea_hub_count=None, enable_pstn=None, enable_sms=None, group_list=None):
        """ShowSpResourceResponse - a model defined in huaweicloud sdk"""
        
        super(ShowSpResourceResponse, self).__init__()

        self._te1080p_hard_count = None
        self._te720p_hard_count = None
        self._te_soft_count = None
        self._room_count = None
        self._record_capability = None
        self._conf_call_count = None
        self._live_count = None
        self._corp_count = None
        self._third_party_hard_count = None
        self._hw_vision_count = None
        self._idea_hub_count = None
        self._enable_pstn = None
        self._enable_sms = None
        self._group_list = None
        self.discriminator = None

        if te1080p_hard_count is not None:
            self.te1080p_hard_count = te1080p_hard_count
        if te720p_hard_count is not None:
            self.te720p_hard_count = te720p_hard_count
        if te_soft_count is not None:
            self.te_soft_count = te_soft_count
        if room_count is not None:
            self.room_count = room_count
        if record_capability is not None:
            self.record_capability = record_capability
        if conf_call_count is not None:
            self.conf_call_count = conf_call_count
        if live_count is not None:
            self.live_count = live_count
        if corp_count is not None:
            self.corp_count = corp_count
        if third_party_hard_count is not None:
            self.third_party_hard_count = third_party_hard_count
        if hw_vision_count is not None:
            self.hw_vision_count = hw_vision_count
        if idea_hub_count is not None:
            self.idea_hub_count = idea_hub_count
        if enable_pstn is not None:
            self.enable_pstn = enable_pstn
        if enable_sms is not None:
            self.enable_sms = enable_sms
        if group_list is not None:
            self.group_list = group_list

    @property
    def te1080p_hard_count(self):
        """Gets the te1080p_hard_count of this ShowSpResourceResponse.


        :return: The te1080p_hard_count of this ShowSpResourceResponse.
        :rtype: ResDetailDTO
        """
        return self._te1080p_hard_count

    @te1080p_hard_count.setter
    def te1080p_hard_count(self, te1080p_hard_count):
        """Sets the te1080p_hard_count of this ShowSpResourceResponse.


        :param te1080p_hard_count: The te1080p_hard_count of this ShowSpResourceResponse.
        :type: ResDetailDTO
        """
        self._te1080p_hard_count = te1080p_hard_count

    @property
    def te720p_hard_count(self):
        """Gets the te720p_hard_count of this ShowSpResourceResponse.


        :return: The te720p_hard_count of this ShowSpResourceResponse.
        :rtype: ResDetailDTO
        """
        return self._te720p_hard_count

    @te720p_hard_count.setter
    def te720p_hard_count(self, te720p_hard_count):
        """Sets the te720p_hard_count of this ShowSpResourceResponse.


        :param te720p_hard_count: The te720p_hard_count of this ShowSpResourceResponse.
        :type: ResDetailDTO
        """
        self._te720p_hard_count = te720p_hard_count

    @property
    def te_soft_count(self):
        """Gets the te_soft_count of this ShowSpResourceResponse.


        :return: The te_soft_count of this ShowSpResourceResponse.
        :rtype: ResDetailDTO
        """
        return self._te_soft_count

    @te_soft_count.setter
    def te_soft_count(self, te_soft_count):
        """Sets the te_soft_count of this ShowSpResourceResponse.


        :param te_soft_count: The te_soft_count of this ShowSpResourceResponse.
        :type: ResDetailDTO
        """
        self._te_soft_count = te_soft_count

    @property
    def room_count(self):
        """Gets the room_count of this ShowSpResourceResponse.


        :return: The room_count of this ShowSpResourceResponse.
        :rtype: ResDetailDTO
        """
        return self._room_count

    @room_count.setter
    def room_count(self, room_count):
        """Sets the room_count of this ShowSpResourceResponse.


        :param room_count: The room_count of this ShowSpResourceResponse.
        :type: ResDetailDTO
        """
        self._room_count = room_count

    @property
    def record_capability(self):
        """Gets the record_capability of this ShowSpResourceResponse.


        :return: The record_capability of this ShowSpResourceResponse.
        :rtype: ResDetailDTO
        """
        return self._record_capability

    @record_capability.setter
    def record_capability(self, record_capability):
        """Sets the record_capability of this ShowSpResourceResponse.


        :param record_capability: The record_capability of this ShowSpResourceResponse.
        :type: ResDetailDTO
        """
        self._record_capability = record_capability

    @property
    def conf_call_count(self):
        """Gets the conf_call_count of this ShowSpResourceResponse.


        :return: The conf_call_count of this ShowSpResourceResponse.
        :rtype: ResDetailDTO
        """
        return self._conf_call_count

    @conf_call_count.setter
    def conf_call_count(self, conf_call_count):
        """Sets the conf_call_count of this ShowSpResourceResponse.


        :param conf_call_count: The conf_call_count of this ShowSpResourceResponse.
        :type: ResDetailDTO
        """
        self._conf_call_count = conf_call_count

    @property
    def live_count(self):
        """Gets the live_count of this ShowSpResourceResponse.


        :return: The live_count of this ShowSpResourceResponse.
        :rtype: ResDetailDTO
        """
        return self._live_count

    @live_count.setter
    def live_count(self, live_count):
        """Sets the live_count of this ShowSpResourceResponse.


        :param live_count: The live_count of this ShowSpResourceResponse.
        :type: ResDetailDTO
        """
        self._live_count = live_count

    @property
    def corp_count(self):
        """Gets the corp_count of this ShowSpResourceResponse.


        :return: The corp_count of this ShowSpResourceResponse.
        :rtype: ResDetailDTO
        """
        return self._corp_count

    @corp_count.setter
    def corp_count(self, corp_count):
        """Sets the corp_count of this ShowSpResourceResponse.


        :param corp_count: The corp_count of this ShowSpResourceResponse.
        :type: ResDetailDTO
        """
        self._corp_count = corp_count

    @property
    def third_party_hard_count(self):
        """Gets the third_party_hard_count of this ShowSpResourceResponse.


        :return: The third_party_hard_count of this ShowSpResourceResponse.
        :rtype: ResDetailDTO
        """
        return self._third_party_hard_count

    @third_party_hard_count.setter
    def third_party_hard_count(self, third_party_hard_count):
        """Sets the third_party_hard_count of this ShowSpResourceResponse.


        :param third_party_hard_count: The third_party_hard_count of this ShowSpResourceResponse.
        :type: ResDetailDTO
        """
        self._third_party_hard_count = third_party_hard_count

    @property
    def hw_vision_count(self):
        """Gets the hw_vision_count of this ShowSpResourceResponse.


        :return: The hw_vision_count of this ShowSpResourceResponse.
        :rtype: ResDetailDTO
        """
        return self._hw_vision_count

    @hw_vision_count.setter
    def hw_vision_count(self, hw_vision_count):
        """Sets the hw_vision_count of this ShowSpResourceResponse.


        :param hw_vision_count: The hw_vision_count of this ShowSpResourceResponse.
        :type: ResDetailDTO
        """
        self._hw_vision_count = hw_vision_count

    @property
    def idea_hub_count(self):
        """Gets the idea_hub_count of this ShowSpResourceResponse.


        :return: The idea_hub_count of this ShowSpResourceResponse.
        :rtype: ResDetailDTO
        """
        return self._idea_hub_count

    @idea_hub_count.setter
    def idea_hub_count(self, idea_hub_count):
        """Sets the idea_hub_count of this ShowSpResourceResponse.


        :param idea_hub_count: The idea_hub_count of this ShowSpResourceResponse.
        :type: ResDetailDTO
        """
        self._idea_hub_count = idea_hub_count

    @property
    def enable_pstn(self):
        """Gets the enable_pstn of this ShowSpResourceResponse.

        在创建SP的时候设置的pstn权限开关

        :return: The enable_pstn of this ShowSpResourceResponse.
        :rtype: bool
        """
        return self._enable_pstn

    @enable_pstn.setter
    def enable_pstn(self, enable_pstn):
        """Sets the enable_pstn of this ShowSpResourceResponse.

        在创建SP的时候设置的pstn权限开关

        :param enable_pstn: The enable_pstn of this ShowSpResourceResponse.
        :type: bool
        """
        self._enable_pstn = enable_pstn

    @property
    def enable_sms(self):
        """Gets the enable_sms of this ShowSpResourceResponse.

        在创建SP的时候设置发送短信开关

        :return: The enable_sms of this ShowSpResourceResponse.
        :rtype: bool
        """
        return self._enable_sms

    @enable_sms.setter
    def enable_sms(self, enable_sms):
        """Sets the enable_sms of this ShowSpResourceResponse.

        在创建SP的时候设置发送短信开关

        :param enable_sms: The enable_sms of this ShowSpResourceResponse.
        :type: bool
        """
        self._enable_sms = enable_sms

    @property
    def group_list(self):
        """Gets the group_list of this ShowSpResourceResponse.

        sp管理员绑定的分组列表

        :return: The group_list of this ShowSpResourceResponse.
        :rtype: list[QueryCorpGroupDTO]
        """
        return self._group_list

    @group_list.setter
    def group_list(self, group_list):
        """Sets the group_list of this ShowSpResourceResponse.

        sp管理员绑定的分组列表

        :param group_list: The group_list of this ShowSpResourceResponse.
        :type: list[QueryCorpGroupDTO]
        """
        self._group_list = group_list

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
        if not isinstance(other, ShowSpResourceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
