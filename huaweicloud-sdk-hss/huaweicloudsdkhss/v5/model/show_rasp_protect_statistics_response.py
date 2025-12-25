# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRaspProtectStatisticsResponse(SdkResponse):

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
        'anti_tampering_num': 'int'
    }

    attribute_map = {
        'protect_host_num': 'protect_host_num',
        'anti_tampering_num': 'anti_tampering_num'
    }

    def __init__(self, protect_host_num=None, anti_tampering_num=None):
        r"""ShowRaspProtectStatisticsResponse

        The model defined in huaweicloud sdk

        :param protect_host_num: **参数解释** 当前项目（或指定企业项目）下已添加应用防护的云服务器总数，统计范围为所有已启用RASP防护的主机 **取值范围** 取值0-为该项目下云服务器总数量（无上限，实际受账号资源配额限制） 
        :type protect_host_num: int
        :param anti_tampering_num: **参数解释** 近7天内当前项目（或指定企业项目）下RASP防护成功拦截的篡改类攻击总数，与功能介绍中&#39;近七天微服务RASP攻击数量&#39;对应 **取值范围** 取值0-无上限（实际受攻击频次限制） 
        :type anti_tampering_num: int
        """
        
        super().__init__()

        self._protect_host_num = None
        self._anti_tampering_num = None
        self.discriminator = None

        if protect_host_num is not None:
            self.protect_host_num = protect_host_num
        if anti_tampering_num is not None:
            self.anti_tampering_num = anti_tampering_num

    @property
    def protect_host_num(self):
        r"""Gets the protect_host_num of this ShowRaspProtectStatisticsResponse.

        **参数解释** 当前项目（或指定企业项目）下已添加应用防护的云服务器总数，统计范围为所有已启用RASP防护的主机 **取值范围** 取值0-为该项目下云服务器总数量（无上限，实际受账号资源配额限制） 

        :return: The protect_host_num of this ShowRaspProtectStatisticsResponse.
        :rtype: int
        """
        return self._protect_host_num

    @protect_host_num.setter
    def protect_host_num(self, protect_host_num):
        r"""Sets the protect_host_num of this ShowRaspProtectStatisticsResponse.

        **参数解释** 当前项目（或指定企业项目）下已添加应用防护的云服务器总数，统计范围为所有已启用RASP防护的主机 **取值范围** 取值0-为该项目下云服务器总数量（无上限，实际受账号资源配额限制） 

        :param protect_host_num: The protect_host_num of this ShowRaspProtectStatisticsResponse.
        :type protect_host_num: int
        """
        self._protect_host_num = protect_host_num

    @property
    def anti_tampering_num(self):
        r"""Gets the anti_tampering_num of this ShowRaspProtectStatisticsResponse.

        **参数解释** 近7天内当前项目（或指定企业项目）下RASP防护成功拦截的篡改类攻击总数，与功能介绍中'近七天微服务RASP攻击数量'对应 **取值范围** 取值0-无上限（实际受攻击频次限制） 

        :return: The anti_tampering_num of this ShowRaspProtectStatisticsResponse.
        :rtype: int
        """
        return self._anti_tampering_num

    @anti_tampering_num.setter
    def anti_tampering_num(self, anti_tampering_num):
        r"""Sets the anti_tampering_num of this ShowRaspProtectStatisticsResponse.

        **参数解释** 近7天内当前项目（或指定企业项目）下RASP防护成功拦截的篡改类攻击总数，与功能介绍中'近七天微服务RASP攻击数量'对应 **取值范围** 取值0-无上限（实际受攻击频次限制） 

        :param anti_tampering_num: The anti_tampering_num of this ShowRaspProtectStatisticsResponse.
        :type anti_tampering_num: int
        """
        self._anti_tampering_num = anti_tampering_num

    def to_dict(self):
        import warnings
        warnings.warn("ShowRaspProtectStatisticsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowRaspProtectStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
