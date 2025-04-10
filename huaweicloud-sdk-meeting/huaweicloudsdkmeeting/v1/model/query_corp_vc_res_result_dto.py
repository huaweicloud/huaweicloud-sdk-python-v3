# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryCorpVcResResultDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vmr_pkg_list': 'list[QueryVmrPkgResResultDTO]',
        'te1080p_hard_count': 'int',
        'te720p_hard_count': 'int',
        'te_soft_count': 'int',
        'room_count': 'int',
        'record_capability': 'int',
        'conf_call_count': 'int',
        'live_count': 'int',
        'third_party_hard_count': 'int',
        'hw_vision_count': 'int',
        'idea_hub_count': 'int'
    }

    attribute_map = {
        'vmr_pkg_list': 'vmrPkgList',
        'te1080p_hard_count': 'te1080pHardCount',
        'te720p_hard_count': 'te720pHardCount',
        'te_soft_count': 'teSoftCount',
        'room_count': 'roomCount',
        'record_capability': 'recordCapability',
        'conf_call_count': 'confCallCount',
        'live_count': 'liveCount',
        'third_party_hard_count': 'thirdPartyHardCount',
        'hw_vision_count': 'hwVisionCount',
        'idea_hub_count': 'ideaHubCount'
    }

    def __init__(self, vmr_pkg_list=None, te1080p_hard_count=None, te720p_hard_count=None, te_soft_count=None, room_count=None, record_capability=None, conf_call_count=None, live_count=None, third_party_hard_count=None, hw_vision_count=None, idea_hub_count=None):
        r"""QueryCorpVcResResultDTO

        The model defined in huaweicloud sdk

        :param vmr_pkg_list: 云会议室类型列表。
        :type vmr_pkg_list: list[:class:`huaweicloudsdkmeeting.v1.QueryVmrPkgResResultDTO`]
        :param te1080p_hard_count: 1080P硬终端接入帐号数量。
        :type te1080p_hard_count: int
        :param te720p_hard_count: 720P硬终端接入帐号数量。
        :type te720p_hard_count: int
        :param te_soft_count: 软终端账户数量。
        :type te_soft_count: int
        :param room_count: 电子白板（SmartRooms）接入帐号数量。
        :type room_count: int
        :param record_capability: 录播存储空间 (单位:G)。
        :type record_capability: int
        :param conf_call_count: 会议并发方数量。
        :type conf_call_count: int
        :param live_count: 直播端口数量。
        :type live_count: int
        :param third_party_hard_count: 第三方硬终端接入帐号数量。
        :type third_party_hard_count: int
        :param hw_vision_count: 智慧屏终端接入帐号数量。
        :type hw_vision_count: int
        :param idea_hub_count: IdeaHub终端接入帐号数量。
        :type idea_hub_count: int
        """
        
        

        self._vmr_pkg_list = None
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
        self.discriminator = None

        if vmr_pkg_list is not None:
            self.vmr_pkg_list = vmr_pkg_list
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

    @property
    def vmr_pkg_list(self):
        r"""Gets the vmr_pkg_list of this QueryCorpVcResResultDTO.

        云会议室类型列表。

        :return: The vmr_pkg_list of this QueryCorpVcResResultDTO.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.QueryVmrPkgResResultDTO`]
        """
        return self._vmr_pkg_list

    @vmr_pkg_list.setter
    def vmr_pkg_list(self, vmr_pkg_list):
        r"""Sets the vmr_pkg_list of this QueryCorpVcResResultDTO.

        云会议室类型列表。

        :param vmr_pkg_list: The vmr_pkg_list of this QueryCorpVcResResultDTO.
        :type vmr_pkg_list: list[:class:`huaweicloudsdkmeeting.v1.QueryVmrPkgResResultDTO`]
        """
        self._vmr_pkg_list = vmr_pkg_list

    @property
    def te1080p_hard_count(self):
        r"""Gets the te1080p_hard_count of this QueryCorpVcResResultDTO.

        1080P硬终端接入帐号数量。

        :return: The te1080p_hard_count of this QueryCorpVcResResultDTO.
        :rtype: int
        """
        return self._te1080p_hard_count

    @te1080p_hard_count.setter
    def te1080p_hard_count(self, te1080p_hard_count):
        r"""Sets the te1080p_hard_count of this QueryCorpVcResResultDTO.

        1080P硬终端接入帐号数量。

        :param te1080p_hard_count: The te1080p_hard_count of this QueryCorpVcResResultDTO.
        :type te1080p_hard_count: int
        """
        self._te1080p_hard_count = te1080p_hard_count

    @property
    def te720p_hard_count(self):
        r"""Gets the te720p_hard_count of this QueryCorpVcResResultDTO.

        720P硬终端接入帐号数量。

        :return: The te720p_hard_count of this QueryCorpVcResResultDTO.
        :rtype: int
        """
        return self._te720p_hard_count

    @te720p_hard_count.setter
    def te720p_hard_count(self, te720p_hard_count):
        r"""Sets the te720p_hard_count of this QueryCorpVcResResultDTO.

        720P硬终端接入帐号数量。

        :param te720p_hard_count: The te720p_hard_count of this QueryCorpVcResResultDTO.
        :type te720p_hard_count: int
        """
        self._te720p_hard_count = te720p_hard_count

    @property
    def te_soft_count(self):
        r"""Gets the te_soft_count of this QueryCorpVcResResultDTO.

        软终端账户数量。

        :return: The te_soft_count of this QueryCorpVcResResultDTO.
        :rtype: int
        """
        return self._te_soft_count

    @te_soft_count.setter
    def te_soft_count(self, te_soft_count):
        r"""Sets the te_soft_count of this QueryCorpVcResResultDTO.

        软终端账户数量。

        :param te_soft_count: The te_soft_count of this QueryCorpVcResResultDTO.
        :type te_soft_count: int
        """
        self._te_soft_count = te_soft_count

    @property
    def room_count(self):
        r"""Gets the room_count of this QueryCorpVcResResultDTO.

        电子白板（SmartRooms）接入帐号数量。

        :return: The room_count of this QueryCorpVcResResultDTO.
        :rtype: int
        """
        return self._room_count

    @room_count.setter
    def room_count(self, room_count):
        r"""Sets the room_count of this QueryCorpVcResResultDTO.

        电子白板（SmartRooms）接入帐号数量。

        :param room_count: The room_count of this QueryCorpVcResResultDTO.
        :type room_count: int
        """
        self._room_count = room_count

    @property
    def record_capability(self):
        r"""Gets the record_capability of this QueryCorpVcResResultDTO.

        录播存储空间 (单位:G)。

        :return: The record_capability of this QueryCorpVcResResultDTO.
        :rtype: int
        """
        return self._record_capability

    @record_capability.setter
    def record_capability(self, record_capability):
        r"""Sets the record_capability of this QueryCorpVcResResultDTO.

        录播存储空间 (单位:G)。

        :param record_capability: The record_capability of this QueryCorpVcResResultDTO.
        :type record_capability: int
        """
        self._record_capability = record_capability

    @property
    def conf_call_count(self):
        r"""Gets the conf_call_count of this QueryCorpVcResResultDTO.

        会议并发方数量。

        :return: The conf_call_count of this QueryCorpVcResResultDTO.
        :rtype: int
        """
        return self._conf_call_count

    @conf_call_count.setter
    def conf_call_count(self, conf_call_count):
        r"""Sets the conf_call_count of this QueryCorpVcResResultDTO.

        会议并发方数量。

        :param conf_call_count: The conf_call_count of this QueryCorpVcResResultDTO.
        :type conf_call_count: int
        """
        self._conf_call_count = conf_call_count

    @property
    def live_count(self):
        r"""Gets the live_count of this QueryCorpVcResResultDTO.

        直播端口数量。

        :return: The live_count of this QueryCorpVcResResultDTO.
        :rtype: int
        """
        return self._live_count

    @live_count.setter
    def live_count(self, live_count):
        r"""Sets the live_count of this QueryCorpVcResResultDTO.

        直播端口数量。

        :param live_count: The live_count of this QueryCorpVcResResultDTO.
        :type live_count: int
        """
        self._live_count = live_count

    @property
    def third_party_hard_count(self):
        r"""Gets the third_party_hard_count of this QueryCorpVcResResultDTO.

        第三方硬终端接入帐号数量。

        :return: The third_party_hard_count of this QueryCorpVcResResultDTO.
        :rtype: int
        """
        return self._third_party_hard_count

    @third_party_hard_count.setter
    def third_party_hard_count(self, third_party_hard_count):
        r"""Sets the third_party_hard_count of this QueryCorpVcResResultDTO.

        第三方硬终端接入帐号数量。

        :param third_party_hard_count: The third_party_hard_count of this QueryCorpVcResResultDTO.
        :type third_party_hard_count: int
        """
        self._third_party_hard_count = third_party_hard_count

    @property
    def hw_vision_count(self):
        r"""Gets the hw_vision_count of this QueryCorpVcResResultDTO.

        智慧屏终端接入帐号数量。

        :return: The hw_vision_count of this QueryCorpVcResResultDTO.
        :rtype: int
        """
        return self._hw_vision_count

    @hw_vision_count.setter
    def hw_vision_count(self, hw_vision_count):
        r"""Sets the hw_vision_count of this QueryCorpVcResResultDTO.

        智慧屏终端接入帐号数量。

        :param hw_vision_count: The hw_vision_count of this QueryCorpVcResResultDTO.
        :type hw_vision_count: int
        """
        self._hw_vision_count = hw_vision_count

    @property
    def idea_hub_count(self):
        r"""Gets the idea_hub_count of this QueryCorpVcResResultDTO.

        IdeaHub终端接入帐号数量。

        :return: The idea_hub_count of this QueryCorpVcResResultDTO.
        :rtype: int
        """
        return self._idea_hub_count

    @idea_hub_count.setter
    def idea_hub_count(self, idea_hub_count):
        r"""Sets the idea_hub_count of this QueryCorpVcResResultDTO.

        IdeaHub终端接入帐号数量。

        :param idea_hub_count: The idea_hub_count of this QueryCorpVcResResultDTO.
        :type idea_hub_count: int
        """
        self._idea_hub_count = idea_hub_count

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
        if not isinstance(other, QueryCorpVcResResultDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
