# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCorpResourceResponse(SdkResponse):

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
        'third_party_hard_count': 'ResDetailDTO',
        'hw_vision_count': 'ResDetailDTO',
        'idea_hub_count': 'ResDetailDTO',
        'vmr': 'list[QueryVmrPkgResResultDTO]',
        'enable_pstn': 'bool',
        'enable_sms': 'bool',
        'enable_hybrid_cloud': 'bool',
        'enable_cloud_disk': 'bool',
        'enable_uc': 'bool',
        'enable_ai_minutes': 'bool',
        'single_conf_call_count': 'int',
        'conf_length': 'int'
    }

    attribute_map = {
        'te1080p_hard_count': 'te1080pHardCount',
        'te720p_hard_count': 'te720pHardCount',
        'te_soft_count': 'teSoftCount',
        'room_count': 'roomCount',
        'record_capability': 'recordCapability',
        'conf_call_count': 'confCallCount',
        'live_count': 'liveCount',
        'third_party_hard_count': 'thirdPartyHardCount',
        'hw_vision_count': 'hwVisionCount',
        'idea_hub_count': 'ideaHubCount',
        'vmr': 'vmr',
        'enable_pstn': 'enablePstn',
        'enable_sms': 'enableSMS',
        'enable_hybrid_cloud': 'enableHybridCloud',
        'enable_cloud_disk': 'enableCloudDisk',
        'enable_uc': 'enableUc',
        'enable_ai_minutes': 'enableAiMinutes',
        'single_conf_call_count': 'singleConfCallCount',
        'conf_length': 'confLength'
    }

    def __init__(self, te1080p_hard_count=None, te720p_hard_count=None, te_soft_count=None, room_count=None, record_capability=None, conf_call_count=None, live_count=None, third_party_hard_count=None, hw_vision_count=None, idea_hub_count=None, vmr=None, enable_pstn=None, enable_sms=None, enable_hybrid_cloud=None, enable_cloud_disk=None, enable_uc=None, enable_ai_minutes=None, single_conf_call_count=None, conf_length=None):
        """ShowCorpResourceResponse

        The model defined in huaweicloud sdk

        :param te1080p_hard_count: 
        :type te1080p_hard_count: :class:`huaweicloudsdkmeeting.v1.ResDetailDTO`
        :param te720p_hard_count: 
        :type te720p_hard_count: :class:`huaweicloudsdkmeeting.v1.ResDetailDTO`
        :param te_soft_count: 
        :type te_soft_count: :class:`huaweicloudsdkmeeting.v1.ResDetailDTO`
        :param room_count: 
        :type room_count: :class:`huaweicloudsdkmeeting.v1.ResDetailDTO`
        :param record_capability: 
        :type record_capability: :class:`huaweicloudsdkmeeting.v1.ResDetailDTO`
        :param conf_call_count: 
        :type conf_call_count: :class:`huaweicloudsdkmeeting.v1.ResDetailDTO`
        :param live_count: 
        :type live_count: :class:`huaweicloudsdkmeeting.v1.ResDetailDTO`
        :param third_party_hard_count: 
        :type third_party_hard_count: :class:`huaweicloudsdkmeeting.v1.ResDetailDTO`
        :param hw_vision_count: 
        :type hw_vision_count: :class:`huaweicloudsdkmeeting.v1.ResDetailDTO`
        :param idea_hub_count: 
        :type idea_hub_count: :class:`huaweicloudsdkmeeting.v1.ResDetailDTO`
        :param vmr: 查询云会议室套餐包分配数量结果。
        :type vmr: list[:class:`huaweicloudsdkmeeting.v1.QueryVmrPkgResResultDTO`]
        :param enable_pstn: 在创建企业的时候设置的pstn权限开关。
        :type enable_pstn: bool
        :param enable_sms: 企业是否通过短信形式发送会议通知。
        :type enable_sms: bool
        :param enable_hybrid_cloud: 企业是否开启混合云模式。
        :type enable_hybrid_cloud: bool
        :param enable_cloud_disk: 是否开启云盘。
        :type enable_cloud_disk: bool
        :param enable_uc: 是否开启UC功能。
        :type enable_uc: bool
        :param enable_ai_minutes: 是否开启Ai会议纪要。
        :type enable_ai_minutes: bool
        :param single_conf_call_count: 单会议并发呼叫数。
        :type single_conf_call_count: int
        :param conf_length: 会议时长。
        :type conf_length: int
        """
        
        super(ShowCorpResourceResponse, self).__init__()

        self._te1080p_hard_count = None
        self._te720p_hard_count = None
        self._te_soft_count = None
        self._room_count = None
        self._record_capability = None
        self._conf_call_count = None
        self._live_count = None
        self._third_party_hard_count = None
        self._hw_vision_count = None
        self._idea_hub_count = None
        self._vmr = None
        self._enable_pstn = None
        self._enable_sms = None
        self._enable_hybrid_cloud = None
        self._enable_cloud_disk = None
        self._enable_uc = None
        self._enable_ai_minutes = None
        self._single_conf_call_count = None
        self._conf_length = None
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
        if third_party_hard_count is not None:
            self.third_party_hard_count = third_party_hard_count
        if hw_vision_count is not None:
            self.hw_vision_count = hw_vision_count
        if idea_hub_count is not None:
            self.idea_hub_count = idea_hub_count
        if vmr is not None:
            self.vmr = vmr
        if enable_pstn is not None:
            self.enable_pstn = enable_pstn
        if enable_sms is not None:
            self.enable_sms = enable_sms
        if enable_hybrid_cloud is not None:
            self.enable_hybrid_cloud = enable_hybrid_cloud
        if enable_cloud_disk is not None:
            self.enable_cloud_disk = enable_cloud_disk
        if enable_uc is not None:
            self.enable_uc = enable_uc
        if enable_ai_minutes is not None:
            self.enable_ai_minutes = enable_ai_minutes
        if single_conf_call_count is not None:
            self.single_conf_call_count = single_conf_call_count
        if conf_length is not None:
            self.conf_length = conf_length

    @property
    def te1080p_hard_count(self):
        """Gets the te1080p_hard_count of this ShowCorpResourceResponse.


        :return: The te1080p_hard_count of this ShowCorpResourceResponse.
        :rtype: :class:`huaweicloudsdkmeeting.v1.ResDetailDTO`
        """
        return self._te1080p_hard_count

    @te1080p_hard_count.setter
    def te1080p_hard_count(self, te1080p_hard_count):
        """Sets the te1080p_hard_count of this ShowCorpResourceResponse.


        :param te1080p_hard_count: The te1080p_hard_count of this ShowCorpResourceResponse.
        :type te1080p_hard_count: :class:`huaweicloudsdkmeeting.v1.ResDetailDTO`
        """
        self._te1080p_hard_count = te1080p_hard_count

    @property
    def te720p_hard_count(self):
        """Gets the te720p_hard_count of this ShowCorpResourceResponse.


        :return: The te720p_hard_count of this ShowCorpResourceResponse.
        :rtype: :class:`huaweicloudsdkmeeting.v1.ResDetailDTO`
        """
        return self._te720p_hard_count

    @te720p_hard_count.setter
    def te720p_hard_count(self, te720p_hard_count):
        """Sets the te720p_hard_count of this ShowCorpResourceResponse.


        :param te720p_hard_count: The te720p_hard_count of this ShowCorpResourceResponse.
        :type te720p_hard_count: :class:`huaweicloudsdkmeeting.v1.ResDetailDTO`
        """
        self._te720p_hard_count = te720p_hard_count

    @property
    def te_soft_count(self):
        """Gets the te_soft_count of this ShowCorpResourceResponse.


        :return: The te_soft_count of this ShowCorpResourceResponse.
        :rtype: :class:`huaweicloudsdkmeeting.v1.ResDetailDTO`
        """
        return self._te_soft_count

    @te_soft_count.setter
    def te_soft_count(self, te_soft_count):
        """Sets the te_soft_count of this ShowCorpResourceResponse.


        :param te_soft_count: The te_soft_count of this ShowCorpResourceResponse.
        :type te_soft_count: :class:`huaweicloudsdkmeeting.v1.ResDetailDTO`
        """
        self._te_soft_count = te_soft_count

    @property
    def room_count(self):
        """Gets the room_count of this ShowCorpResourceResponse.


        :return: The room_count of this ShowCorpResourceResponse.
        :rtype: :class:`huaweicloudsdkmeeting.v1.ResDetailDTO`
        """
        return self._room_count

    @room_count.setter
    def room_count(self, room_count):
        """Sets the room_count of this ShowCorpResourceResponse.


        :param room_count: The room_count of this ShowCorpResourceResponse.
        :type room_count: :class:`huaweicloudsdkmeeting.v1.ResDetailDTO`
        """
        self._room_count = room_count

    @property
    def record_capability(self):
        """Gets the record_capability of this ShowCorpResourceResponse.


        :return: The record_capability of this ShowCorpResourceResponse.
        :rtype: :class:`huaweicloudsdkmeeting.v1.ResDetailDTO`
        """
        return self._record_capability

    @record_capability.setter
    def record_capability(self, record_capability):
        """Sets the record_capability of this ShowCorpResourceResponse.


        :param record_capability: The record_capability of this ShowCorpResourceResponse.
        :type record_capability: :class:`huaweicloudsdkmeeting.v1.ResDetailDTO`
        """
        self._record_capability = record_capability

    @property
    def conf_call_count(self):
        """Gets the conf_call_count of this ShowCorpResourceResponse.


        :return: The conf_call_count of this ShowCorpResourceResponse.
        :rtype: :class:`huaweicloudsdkmeeting.v1.ResDetailDTO`
        """
        return self._conf_call_count

    @conf_call_count.setter
    def conf_call_count(self, conf_call_count):
        """Sets the conf_call_count of this ShowCorpResourceResponse.


        :param conf_call_count: The conf_call_count of this ShowCorpResourceResponse.
        :type conf_call_count: :class:`huaweicloudsdkmeeting.v1.ResDetailDTO`
        """
        self._conf_call_count = conf_call_count

    @property
    def live_count(self):
        """Gets the live_count of this ShowCorpResourceResponse.


        :return: The live_count of this ShowCorpResourceResponse.
        :rtype: :class:`huaweicloudsdkmeeting.v1.ResDetailDTO`
        """
        return self._live_count

    @live_count.setter
    def live_count(self, live_count):
        """Sets the live_count of this ShowCorpResourceResponse.


        :param live_count: The live_count of this ShowCorpResourceResponse.
        :type live_count: :class:`huaweicloudsdkmeeting.v1.ResDetailDTO`
        """
        self._live_count = live_count

    @property
    def third_party_hard_count(self):
        """Gets the third_party_hard_count of this ShowCorpResourceResponse.


        :return: The third_party_hard_count of this ShowCorpResourceResponse.
        :rtype: :class:`huaweicloudsdkmeeting.v1.ResDetailDTO`
        """
        return self._third_party_hard_count

    @third_party_hard_count.setter
    def third_party_hard_count(self, third_party_hard_count):
        """Sets the third_party_hard_count of this ShowCorpResourceResponse.


        :param third_party_hard_count: The third_party_hard_count of this ShowCorpResourceResponse.
        :type third_party_hard_count: :class:`huaweicloudsdkmeeting.v1.ResDetailDTO`
        """
        self._third_party_hard_count = third_party_hard_count

    @property
    def hw_vision_count(self):
        """Gets the hw_vision_count of this ShowCorpResourceResponse.


        :return: The hw_vision_count of this ShowCorpResourceResponse.
        :rtype: :class:`huaweicloudsdkmeeting.v1.ResDetailDTO`
        """
        return self._hw_vision_count

    @hw_vision_count.setter
    def hw_vision_count(self, hw_vision_count):
        """Sets the hw_vision_count of this ShowCorpResourceResponse.


        :param hw_vision_count: The hw_vision_count of this ShowCorpResourceResponse.
        :type hw_vision_count: :class:`huaweicloudsdkmeeting.v1.ResDetailDTO`
        """
        self._hw_vision_count = hw_vision_count

    @property
    def idea_hub_count(self):
        """Gets the idea_hub_count of this ShowCorpResourceResponse.


        :return: The idea_hub_count of this ShowCorpResourceResponse.
        :rtype: :class:`huaweicloudsdkmeeting.v1.ResDetailDTO`
        """
        return self._idea_hub_count

    @idea_hub_count.setter
    def idea_hub_count(self, idea_hub_count):
        """Sets the idea_hub_count of this ShowCorpResourceResponse.


        :param idea_hub_count: The idea_hub_count of this ShowCorpResourceResponse.
        :type idea_hub_count: :class:`huaweicloudsdkmeeting.v1.ResDetailDTO`
        """
        self._idea_hub_count = idea_hub_count

    @property
    def vmr(self):
        """Gets the vmr of this ShowCorpResourceResponse.

        查询云会议室套餐包分配数量结果。

        :return: The vmr of this ShowCorpResourceResponse.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.QueryVmrPkgResResultDTO`]
        """
        return self._vmr

    @vmr.setter
    def vmr(self, vmr):
        """Sets the vmr of this ShowCorpResourceResponse.

        查询云会议室套餐包分配数量结果。

        :param vmr: The vmr of this ShowCorpResourceResponse.
        :type vmr: list[:class:`huaweicloudsdkmeeting.v1.QueryVmrPkgResResultDTO`]
        """
        self._vmr = vmr

    @property
    def enable_pstn(self):
        """Gets the enable_pstn of this ShowCorpResourceResponse.

        在创建企业的时候设置的pstn权限开关。

        :return: The enable_pstn of this ShowCorpResourceResponse.
        :rtype: bool
        """
        return self._enable_pstn

    @enable_pstn.setter
    def enable_pstn(self, enable_pstn):
        """Sets the enable_pstn of this ShowCorpResourceResponse.

        在创建企业的时候设置的pstn权限开关。

        :param enable_pstn: The enable_pstn of this ShowCorpResourceResponse.
        :type enable_pstn: bool
        """
        self._enable_pstn = enable_pstn

    @property
    def enable_sms(self):
        """Gets the enable_sms of this ShowCorpResourceResponse.

        企业是否通过短信形式发送会议通知。

        :return: The enable_sms of this ShowCorpResourceResponse.
        :rtype: bool
        """
        return self._enable_sms

    @enable_sms.setter
    def enable_sms(self, enable_sms):
        """Sets the enable_sms of this ShowCorpResourceResponse.

        企业是否通过短信形式发送会议通知。

        :param enable_sms: The enable_sms of this ShowCorpResourceResponse.
        :type enable_sms: bool
        """
        self._enable_sms = enable_sms

    @property
    def enable_hybrid_cloud(self):
        """Gets the enable_hybrid_cloud of this ShowCorpResourceResponse.

        企业是否开启混合云模式。

        :return: The enable_hybrid_cloud of this ShowCorpResourceResponse.
        :rtype: bool
        """
        return self._enable_hybrid_cloud

    @enable_hybrid_cloud.setter
    def enable_hybrid_cloud(self, enable_hybrid_cloud):
        """Sets the enable_hybrid_cloud of this ShowCorpResourceResponse.

        企业是否开启混合云模式。

        :param enable_hybrid_cloud: The enable_hybrid_cloud of this ShowCorpResourceResponse.
        :type enable_hybrid_cloud: bool
        """
        self._enable_hybrid_cloud = enable_hybrid_cloud

    @property
    def enable_cloud_disk(self):
        """Gets the enable_cloud_disk of this ShowCorpResourceResponse.

        是否开启云盘。

        :return: The enable_cloud_disk of this ShowCorpResourceResponse.
        :rtype: bool
        """
        return self._enable_cloud_disk

    @enable_cloud_disk.setter
    def enable_cloud_disk(self, enable_cloud_disk):
        """Sets the enable_cloud_disk of this ShowCorpResourceResponse.

        是否开启云盘。

        :param enable_cloud_disk: The enable_cloud_disk of this ShowCorpResourceResponse.
        :type enable_cloud_disk: bool
        """
        self._enable_cloud_disk = enable_cloud_disk

    @property
    def enable_uc(self):
        """Gets the enable_uc of this ShowCorpResourceResponse.

        是否开启UC功能。

        :return: The enable_uc of this ShowCorpResourceResponse.
        :rtype: bool
        """
        return self._enable_uc

    @enable_uc.setter
    def enable_uc(self, enable_uc):
        """Sets the enable_uc of this ShowCorpResourceResponse.

        是否开启UC功能。

        :param enable_uc: The enable_uc of this ShowCorpResourceResponse.
        :type enable_uc: bool
        """
        self._enable_uc = enable_uc

    @property
    def enable_ai_minutes(self):
        """Gets the enable_ai_minutes of this ShowCorpResourceResponse.

        是否开启Ai会议纪要。

        :return: The enable_ai_minutes of this ShowCorpResourceResponse.
        :rtype: bool
        """
        return self._enable_ai_minutes

    @enable_ai_minutes.setter
    def enable_ai_minutes(self, enable_ai_minutes):
        """Sets the enable_ai_minutes of this ShowCorpResourceResponse.

        是否开启Ai会议纪要。

        :param enable_ai_minutes: The enable_ai_minutes of this ShowCorpResourceResponse.
        :type enable_ai_minutes: bool
        """
        self._enable_ai_minutes = enable_ai_minutes

    @property
    def single_conf_call_count(self):
        """Gets the single_conf_call_count of this ShowCorpResourceResponse.

        单会议并发呼叫数。

        :return: The single_conf_call_count of this ShowCorpResourceResponse.
        :rtype: int
        """
        return self._single_conf_call_count

    @single_conf_call_count.setter
    def single_conf_call_count(self, single_conf_call_count):
        """Sets the single_conf_call_count of this ShowCorpResourceResponse.

        单会议并发呼叫数。

        :param single_conf_call_count: The single_conf_call_count of this ShowCorpResourceResponse.
        :type single_conf_call_count: int
        """
        self._single_conf_call_count = single_conf_call_count

    @property
    def conf_length(self):
        """Gets the conf_length of this ShowCorpResourceResponse.

        会议时长。

        :return: The conf_length of this ShowCorpResourceResponse.
        :rtype: int
        """
        return self._conf_length

    @conf_length.setter
    def conf_length(self, conf_length):
        """Sets the conf_length of this ShowCorpResourceResponse.

        会议时长。

        :param conf_length: The conf_length of this ShowCorpResourceResponse.
        :type conf_length: int
        """
        self._conf_length = conf_length

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
        if not isinstance(other, ShowCorpResourceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
