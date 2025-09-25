# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProtectInfoQuotaInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'expired_quota_num': 'int',
        'about_to_expire_quota_num': 'int',
        'user_use_enterprise_rate': 'float'
    }

    attribute_map = {
        'expired_quota_num': 'expired_quota_num',
        'about_to_expire_quota_num': 'about_to_expire_quota_num',
        'user_use_enterprise_rate': 'user_use_enterprise_rate'
    }

    def __init__(self, expired_quota_num=None, about_to_expire_quota_num=None, user_use_enterprise_rate=None):
        r"""ProtectInfoQuotaInfo

        The model defined in huaweicloud sdk

        :param expired_quota_num: **参数解释**: 已经到期的配额 **取值范围**: 最小值0，最大值2147483647 
        :type expired_quota_num: int
        :param about_to_expire_quota_num: **参数解释**: 即将到期的配额 **取值范围**: 最小值0，最大值2147483647 
        :type about_to_expire_quota_num: int
        :param user_use_enterprise_rate: **参数解释**: 使用企业版的用户率 **取值范围**: 最小值0，最大值1 
        :type user_use_enterprise_rate: float
        """
        
        

        self._expired_quota_num = None
        self._about_to_expire_quota_num = None
        self._user_use_enterprise_rate = None
        self.discriminator = None

        if expired_quota_num is not None:
            self.expired_quota_num = expired_quota_num
        if about_to_expire_quota_num is not None:
            self.about_to_expire_quota_num = about_to_expire_quota_num
        if user_use_enterprise_rate is not None:
            self.user_use_enterprise_rate = user_use_enterprise_rate

    @property
    def expired_quota_num(self):
        r"""Gets the expired_quota_num of this ProtectInfoQuotaInfo.

        **参数解释**: 已经到期的配额 **取值范围**: 最小值0，最大值2147483647 

        :return: The expired_quota_num of this ProtectInfoQuotaInfo.
        :rtype: int
        """
        return self._expired_quota_num

    @expired_quota_num.setter
    def expired_quota_num(self, expired_quota_num):
        r"""Sets the expired_quota_num of this ProtectInfoQuotaInfo.

        **参数解释**: 已经到期的配额 **取值范围**: 最小值0，最大值2147483647 

        :param expired_quota_num: The expired_quota_num of this ProtectInfoQuotaInfo.
        :type expired_quota_num: int
        """
        self._expired_quota_num = expired_quota_num

    @property
    def about_to_expire_quota_num(self):
        r"""Gets the about_to_expire_quota_num of this ProtectInfoQuotaInfo.

        **参数解释**: 即将到期的配额 **取值范围**: 最小值0，最大值2147483647 

        :return: The about_to_expire_quota_num of this ProtectInfoQuotaInfo.
        :rtype: int
        """
        return self._about_to_expire_quota_num

    @about_to_expire_quota_num.setter
    def about_to_expire_quota_num(self, about_to_expire_quota_num):
        r"""Sets the about_to_expire_quota_num of this ProtectInfoQuotaInfo.

        **参数解释**: 即将到期的配额 **取值范围**: 最小值0，最大值2147483647 

        :param about_to_expire_quota_num: The about_to_expire_quota_num of this ProtectInfoQuotaInfo.
        :type about_to_expire_quota_num: int
        """
        self._about_to_expire_quota_num = about_to_expire_quota_num

    @property
    def user_use_enterprise_rate(self):
        r"""Gets the user_use_enterprise_rate of this ProtectInfoQuotaInfo.

        **参数解释**: 使用企业版的用户率 **取值范围**: 最小值0，最大值1 

        :return: The user_use_enterprise_rate of this ProtectInfoQuotaInfo.
        :rtype: float
        """
        return self._user_use_enterprise_rate

    @user_use_enterprise_rate.setter
    def user_use_enterprise_rate(self, user_use_enterprise_rate):
        r"""Sets the user_use_enterprise_rate of this ProtectInfoQuotaInfo.

        **参数解释**: 使用企业版的用户率 **取值范围**: 最小值0，最大值1 

        :param user_use_enterprise_rate: The user_use_enterprise_rate of this ProtectInfoQuotaInfo.
        :type user_use_enterprise_rate: float
        """
        self._user_use_enterprise_rate = user_use_enterprise_rate

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
        if not isinstance(other, ProtectInfoQuotaInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
