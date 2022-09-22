# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CycleSubConfConfigDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'call_in_restriction': 'int',
        'audience_call_in_restriction': 'int',
        'allow_guest_start_conf': 'bool',
        'enable_waiting_room': 'bool',
        'show_audience_count_info': 'ShowAudienceCountInfo'
    }

    attribute_map = {
        'call_in_restriction': 'callInRestriction',
        'audience_call_in_restriction': 'audienceCallInRestriction',
        'allow_guest_start_conf': 'allowGuestStartConf',
        'enable_waiting_room': 'enableWaitingRoom',
        'show_audience_count_info': 'showAudienceCountInfo'
    }

    def __init__(self, call_in_restriction=None, audience_call_in_restriction=None, allow_guest_start_conf=None, enable_waiting_room=None, show_audience_count_info=None):
        """CycleSubConfConfigDTO

        The model defined in huaweicloud sdk

        :param call_in_restriction: 允许加入会议的范围。 - 0: 所有用户 - 2: 企业内用户 - 3: 被邀请用户 
        :type call_in_restriction: int
        :param audience_call_in_restriction: 允许加入网络研讨会的观众范围。 - 0：所有用户 - 2：企业内用户和被邀请用户 
        :type audience_call_in_restriction: int
        :param allow_guest_start_conf: 是否允许来宾启动会议。 - false:禁止来宾启动会议 - true：允许来宾启动会议 &gt; 仅随机会议ID的会议生效。 
        :type allow_guest_start_conf: bool
        :param enable_waiting_room: 是否启用等候室。
        :type enable_waiting_room: bool
        :param show_audience_count_info: 
        :type show_audience_count_info: :class:`huaweicloudsdkmeeting.v1.ShowAudienceCountInfo`
        """
        
        

        self._call_in_restriction = None
        self._audience_call_in_restriction = None
        self._allow_guest_start_conf = None
        self._enable_waiting_room = None
        self._show_audience_count_info = None
        self.discriminator = None

        if call_in_restriction is not None:
            self.call_in_restriction = call_in_restriction
        if audience_call_in_restriction is not None:
            self.audience_call_in_restriction = audience_call_in_restriction
        if allow_guest_start_conf is not None:
            self.allow_guest_start_conf = allow_guest_start_conf
        if enable_waiting_room is not None:
            self.enable_waiting_room = enable_waiting_room
        if show_audience_count_info is not None:
            self.show_audience_count_info = show_audience_count_info

    @property
    def call_in_restriction(self):
        """Gets the call_in_restriction of this CycleSubConfConfigDTO.

        允许加入会议的范围。 - 0: 所有用户 - 2: 企业内用户 - 3: 被邀请用户 

        :return: The call_in_restriction of this CycleSubConfConfigDTO.
        :rtype: int
        """
        return self._call_in_restriction

    @call_in_restriction.setter
    def call_in_restriction(self, call_in_restriction):
        """Sets the call_in_restriction of this CycleSubConfConfigDTO.

        允许加入会议的范围。 - 0: 所有用户 - 2: 企业内用户 - 3: 被邀请用户 

        :param call_in_restriction: The call_in_restriction of this CycleSubConfConfigDTO.
        :type call_in_restriction: int
        """
        self._call_in_restriction = call_in_restriction

    @property
    def audience_call_in_restriction(self):
        """Gets the audience_call_in_restriction of this CycleSubConfConfigDTO.

        允许加入网络研讨会的观众范围。 - 0：所有用户 - 2：企业内用户和被邀请用户 

        :return: The audience_call_in_restriction of this CycleSubConfConfigDTO.
        :rtype: int
        """
        return self._audience_call_in_restriction

    @audience_call_in_restriction.setter
    def audience_call_in_restriction(self, audience_call_in_restriction):
        """Sets the audience_call_in_restriction of this CycleSubConfConfigDTO.

        允许加入网络研讨会的观众范围。 - 0：所有用户 - 2：企业内用户和被邀请用户 

        :param audience_call_in_restriction: The audience_call_in_restriction of this CycleSubConfConfigDTO.
        :type audience_call_in_restriction: int
        """
        self._audience_call_in_restriction = audience_call_in_restriction

    @property
    def allow_guest_start_conf(self):
        """Gets the allow_guest_start_conf of this CycleSubConfConfigDTO.

        是否允许来宾启动会议。 - false:禁止来宾启动会议 - true：允许来宾启动会议 > 仅随机会议ID的会议生效。 

        :return: The allow_guest_start_conf of this CycleSubConfConfigDTO.
        :rtype: bool
        """
        return self._allow_guest_start_conf

    @allow_guest_start_conf.setter
    def allow_guest_start_conf(self, allow_guest_start_conf):
        """Sets the allow_guest_start_conf of this CycleSubConfConfigDTO.

        是否允许来宾启动会议。 - false:禁止来宾启动会议 - true：允许来宾启动会议 > 仅随机会议ID的会议生效。 

        :param allow_guest_start_conf: The allow_guest_start_conf of this CycleSubConfConfigDTO.
        :type allow_guest_start_conf: bool
        """
        self._allow_guest_start_conf = allow_guest_start_conf

    @property
    def enable_waiting_room(self):
        """Gets the enable_waiting_room of this CycleSubConfConfigDTO.

        是否启用等候室。

        :return: The enable_waiting_room of this CycleSubConfConfigDTO.
        :rtype: bool
        """
        return self._enable_waiting_room

    @enable_waiting_room.setter
    def enable_waiting_room(self, enable_waiting_room):
        """Sets the enable_waiting_room of this CycleSubConfConfigDTO.

        是否启用等候室。

        :param enable_waiting_room: The enable_waiting_room of this CycleSubConfConfigDTO.
        :type enable_waiting_room: bool
        """
        self._enable_waiting_room = enable_waiting_room

    @property
    def show_audience_count_info(self):
        """Gets the show_audience_count_info of this CycleSubConfConfigDTO.


        :return: The show_audience_count_info of this CycleSubConfConfigDTO.
        :rtype: :class:`huaweicloudsdkmeeting.v1.ShowAudienceCountInfo`
        """
        return self._show_audience_count_info

    @show_audience_count_info.setter
    def show_audience_count_info(self, show_audience_count_info):
        """Sets the show_audience_count_info of this CycleSubConfConfigDTO.


        :param show_audience_count_info: The show_audience_count_info of this CycleSubConfConfigDTO.
        :type show_audience_count_info: :class:`huaweicloudsdkmeeting.v1.ShowAudienceCountInfo`
        """
        self._show_audience_count_info = show_audience_count_info

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
        if not isinstance(other, CycleSubConfConfigDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
