# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWtpProtectStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protect_host_num': 'int',
        'protect_success_host_num': 'int',
        'protect_fail_host_num': 'int',
        'anti_tampering_num': 'int'
    }

    attribute_map = {
        'protect_host_num': 'protect_host_num',
        'protect_success_host_num': 'protect_success_host_num',
        'protect_fail_host_num': 'protect_fail_host_num',
        'anti_tampering_num': 'anti_tampering_num'
    }

    def __init__(self, protect_host_num=None, protect_success_host_num=None, protect_fail_host_num=None, anti_tampering_num=None):
        r"""ShowWtpProtectStatisticsResponse

        The model defined in huaweicloud sdk

        :param protect_host_num: **参数解释**: 防护服务器总数，包含防护状态是防护中、部分防护、防护暂停、防护失败、防护中断和开启中共6中状态的服务器总数 **取值范围**: 最小值0，最大值1000000 
        :type protect_host_num: int
        :param protect_success_host_num: **参数解释**: 防护状态为防护中的服务器总数 **取值范围**: 最小值0，最大值1000000 
        :type protect_success_host_num: int
        :param protect_fail_host_num: **参数解释**: 防护状态为防护失败的服务器总数 **取值范围**: 最小值0，最大值1000000 
        :type protect_fail_host_num: int
        :param anti_tampering_num: **参数解释**: 近168小时防护事件数 **取值范围**: 最小值0，最大值50000000 
        :type anti_tampering_num: int
        """
        
        super(ShowWtpProtectStatisticsResponse, self).__init__()

        self._protect_host_num = None
        self._protect_success_host_num = None
        self._protect_fail_host_num = None
        self._anti_tampering_num = None
        self.discriminator = None

        if protect_host_num is not None:
            self.protect_host_num = protect_host_num
        if protect_success_host_num is not None:
            self.protect_success_host_num = protect_success_host_num
        if protect_fail_host_num is not None:
            self.protect_fail_host_num = protect_fail_host_num
        if anti_tampering_num is not None:
            self.anti_tampering_num = anti_tampering_num

    @property
    def protect_host_num(self):
        r"""Gets the protect_host_num of this ShowWtpProtectStatisticsResponse.

        **参数解释**: 防护服务器总数，包含防护状态是防护中、部分防护、防护暂停、防护失败、防护中断和开启中共6中状态的服务器总数 **取值范围**: 最小值0，最大值1000000 

        :return: The protect_host_num of this ShowWtpProtectStatisticsResponse.
        :rtype: int
        """
        return self._protect_host_num

    @protect_host_num.setter
    def protect_host_num(self, protect_host_num):
        r"""Sets the protect_host_num of this ShowWtpProtectStatisticsResponse.

        **参数解释**: 防护服务器总数，包含防护状态是防护中、部分防护、防护暂停、防护失败、防护中断和开启中共6中状态的服务器总数 **取值范围**: 最小值0，最大值1000000 

        :param protect_host_num: The protect_host_num of this ShowWtpProtectStatisticsResponse.
        :type protect_host_num: int
        """
        self._protect_host_num = protect_host_num

    @property
    def protect_success_host_num(self):
        r"""Gets the protect_success_host_num of this ShowWtpProtectStatisticsResponse.

        **参数解释**: 防护状态为防护中的服务器总数 **取值范围**: 最小值0，最大值1000000 

        :return: The protect_success_host_num of this ShowWtpProtectStatisticsResponse.
        :rtype: int
        """
        return self._protect_success_host_num

    @protect_success_host_num.setter
    def protect_success_host_num(self, protect_success_host_num):
        r"""Sets the protect_success_host_num of this ShowWtpProtectStatisticsResponse.

        **参数解释**: 防护状态为防护中的服务器总数 **取值范围**: 最小值0，最大值1000000 

        :param protect_success_host_num: The protect_success_host_num of this ShowWtpProtectStatisticsResponse.
        :type protect_success_host_num: int
        """
        self._protect_success_host_num = protect_success_host_num

    @property
    def protect_fail_host_num(self):
        r"""Gets the protect_fail_host_num of this ShowWtpProtectStatisticsResponse.

        **参数解释**: 防护状态为防护失败的服务器总数 **取值范围**: 最小值0，最大值1000000 

        :return: The protect_fail_host_num of this ShowWtpProtectStatisticsResponse.
        :rtype: int
        """
        return self._protect_fail_host_num

    @protect_fail_host_num.setter
    def protect_fail_host_num(self, protect_fail_host_num):
        r"""Sets the protect_fail_host_num of this ShowWtpProtectStatisticsResponse.

        **参数解释**: 防护状态为防护失败的服务器总数 **取值范围**: 最小值0，最大值1000000 

        :param protect_fail_host_num: The protect_fail_host_num of this ShowWtpProtectStatisticsResponse.
        :type protect_fail_host_num: int
        """
        self._protect_fail_host_num = protect_fail_host_num

    @property
    def anti_tampering_num(self):
        r"""Gets the anti_tampering_num of this ShowWtpProtectStatisticsResponse.

        **参数解释**: 近168小时防护事件数 **取值范围**: 最小值0，最大值50000000 

        :return: The anti_tampering_num of this ShowWtpProtectStatisticsResponse.
        :rtype: int
        """
        return self._anti_tampering_num

    @anti_tampering_num.setter
    def anti_tampering_num(self, anti_tampering_num):
        r"""Sets the anti_tampering_num of this ShowWtpProtectStatisticsResponse.

        **参数解释**: 近168小时防护事件数 **取值范围**: 最小值0，最大值50000000 

        :param anti_tampering_num: The anti_tampering_num of this ShowWtpProtectStatisticsResponse.
        :type anti_tampering_num: int
        """
        self._anti_tampering_num = anti_tampering_num

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
        if not isinstance(other, ShowWtpProtectStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
