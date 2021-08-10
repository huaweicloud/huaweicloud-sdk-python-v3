# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowQuotaResponseBodyQuotas:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'quota_limit': 'int',
        'type': 'str',
        'used': 'int',
        'user_domain_id': 'str'
    }

    attribute_map = {
        'quota_limit': 'quota_limit',
        'type': 'type',
        'used': 'used',
        'user_domain_id': 'user_domain_id'
    }

    def __init__(self, quota_limit=None, type=None, used=None, user_domain_id=None):
        """ShowQuotaResponseBodyQuotas - a model defined in huaweicloud sdk"""
        
        

        self._quota_limit = None
        self._type = None
        self._used = None
        self._user_domain_id = None
        self.discriminator = None

        if quota_limit is not None:
            self.quota_limit = quota_limit
        if type is not None:
            self.type = type
        if used is not None:
            self.used = used
        if user_domain_id is not None:
            self.user_domain_id = user_domain_id

    @property
    def quota_limit(self):
        """Gets the quota_limit of this ShowQuotaResponseBodyQuotas.

        配额上限

        :return: The quota_limit of this ShowQuotaResponseBodyQuotas.
        :rtype: int
        """
        return self._quota_limit

    @quota_limit.setter
    def quota_limit(self, quota_limit):
        """Sets the quota_limit of this ShowQuotaResponseBodyQuotas.

        配额上限

        :param quota_limit: The quota_limit of this ShowQuotaResponseBodyQuotas.
        :type: int
        """
        self._quota_limit = quota_limit

    @property
    def type(self):
        """Gets the type of this ShowQuotaResponseBodyQuotas.

        配额类型

        :return: The type of this ShowQuotaResponseBodyQuotas.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowQuotaResponseBodyQuotas.

        配额类型

        :param type: The type of this ShowQuotaResponseBodyQuotas.
        :type: str
        """
        self._type = type

    @property
    def used(self):
        """Gets the used of this ShowQuotaResponseBodyQuotas.

        已使用配额数

        :return: The used of this ShowQuotaResponseBodyQuotas.
        :rtype: int
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this ShowQuotaResponseBodyQuotas.

        已使用配额数

        :param used: The used of this ShowQuotaResponseBodyQuotas.
        :type: int
        """
        self._used = used

    @property
    def user_domain_id(self):
        """Gets the user_domain_id of this ShowQuotaResponseBodyQuotas.

        域名所属用户的domain_id。

        :return: The user_domain_id of this ShowQuotaResponseBodyQuotas.
        :rtype: str
        """
        return self._user_domain_id

    @user_domain_id.setter
    def user_domain_id(self, user_domain_id):
        """Sets the user_domain_id of this ShowQuotaResponseBodyQuotas.

        域名所属用户的domain_id。

        :param user_domain_id: The user_domain_id of this ShowQuotaResponseBodyQuotas.
        :type: str
        """
        self._user_domain_id = user_domain_id

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
        if not isinstance(other, ShowQuotaResponseBodyQuotas):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
