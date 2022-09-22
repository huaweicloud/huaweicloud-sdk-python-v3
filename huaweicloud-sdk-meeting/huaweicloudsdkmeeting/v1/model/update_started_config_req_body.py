# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateStartedConfigReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'lock_sharing': 'int',
        'call_in_restriction': 'int'
    }

    attribute_map = {
        'lock_sharing': 'lockSharing',
        'call_in_restriction': 'callInRestriction'
    }

    def __init__(self, lock_sharing=None, call_in_restriction=None):
        """UpdateStartedConfigReqBody

        The model defined in huaweicloud sdk

        :param lock_sharing: 锁定共享标志位。 * 0: 不锁定 * 1: 锁定 
        :type lock_sharing: int
        :param call_in_restriction: 允许加入会议的范围。 - 0: 所有用户 - 2: 企业内用户 - 3: 被邀请用户 
        :type call_in_restriction: int
        """
        
        

        self._lock_sharing = None
        self._call_in_restriction = None
        self.discriminator = None

        if lock_sharing is not None:
            self.lock_sharing = lock_sharing
        if call_in_restriction is not None:
            self.call_in_restriction = call_in_restriction

    @property
    def lock_sharing(self):
        """Gets the lock_sharing of this UpdateStartedConfigReqBody.

        锁定共享标志位。 * 0: 不锁定 * 1: 锁定 

        :return: The lock_sharing of this UpdateStartedConfigReqBody.
        :rtype: int
        """
        return self._lock_sharing

    @lock_sharing.setter
    def lock_sharing(self, lock_sharing):
        """Sets the lock_sharing of this UpdateStartedConfigReqBody.

        锁定共享标志位。 * 0: 不锁定 * 1: 锁定 

        :param lock_sharing: The lock_sharing of this UpdateStartedConfigReqBody.
        :type lock_sharing: int
        """
        self._lock_sharing = lock_sharing

    @property
    def call_in_restriction(self):
        """Gets the call_in_restriction of this UpdateStartedConfigReqBody.

        允许加入会议的范围。 - 0: 所有用户 - 2: 企业内用户 - 3: 被邀请用户 

        :return: The call_in_restriction of this UpdateStartedConfigReqBody.
        :rtype: int
        """
        return self._call_in_restriction

    @call_in_restriction.setter
    def call_in_restriction(self, call_in_restriction):
        """Sets the call_in_restriction of this UpdateStartedConfigReqBody.

        允许加入会议的范围。 - 0: 所有用户 - 2: 企业内用户 - 3: 被邀请用户 

        :param call_in_restriction: The call_in_restriction of this UpdateStartedConfigReqBody.
        :type call_in_restriction: int
        """
        self._call_in_restriction = call_in_restriction

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
        if not isinstance(other, UpdateStartedConfigReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
