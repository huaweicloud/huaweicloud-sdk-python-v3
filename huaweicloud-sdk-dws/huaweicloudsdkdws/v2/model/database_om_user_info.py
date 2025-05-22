# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatabaseOmUserInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'om_user_status': 'str',
        'om_user_expires_time': 'int'
    }

    attribute_map = {
        'om_user_status': 'om_user_status',
        'om_user_expires_time': 'om_user_expires_time'
    }

    def __init__(self, om_user_status=None, om_user_expires_time=None):
        r"""DatabaseOmUserInfo

        The model defined in huaweicloud sdk

        :param om_user_status: **参数解释**： 运维账户状态。 **取值范围**： on、off
        :type om_user_status: str
        :param om_user_expires_time: **参数解释**： 运维账户过期状态。格式是有效的时间戳。 **取值范围**： 不涉及。
        :type om_user_expires_time: int
        """
        
        

        self._om_user_status = None
        self._om_user_expires_time = None
        self.discriminator = None

        if om_user_status is not None:
            self.om_user_status = om_user_status
        if om_user_expires_time is not None:
            self.om_user_expires_time = om_user_expires_time

    @property
    def om_user_status(self):
        r"""Gets the om_user_status of this DatabaseOmUserInfo.

        **参数解释**： 运维账户状态。 **取值范围**： on、off

        :return: The om_user_status of this DatabaseOmUserInfo.
        :rtype: str
        """
        return self._om_user_status

    @om_user_status.setter
    def om_user_status(self, om_user_status):
        r"""Sets the om_user_status of this DatabaseOmUserInfo.

        **参数解释**： 运维账户状态。 **取值范围**： on、off

        :param om_user_status: The om_user_status of this DatabaseOmUserInfo.
        :type om_user_status: str
        """
        self._om_user_status = om_user_status

    @property
    def om_user_expires_time(self):
        r"""Gets the om_user_expires_time of this DatabaseOmUserInfo.

        **参数解释**： 运维账户过期状态。格式是有效的时间戳。 **取值范围**： 不涉及。

        :return: The om_user_expires_time of this DatabaseOmUserInfo.
        :rtype: int
        """
        return self._om_user_expires_time

    @om_user_expires_time.setter
    def om_user_expires_time(self, om_user_expires_time):
        r"""Sets the om_user_expires_time of this DatabaseOmUserInfo.

        **参数解释**： 运维账户过期状态。格式是有效的时间戳。 **取值范围**： 不涉及。

        :param om_user_expires_time: The om_user_expires_time of this DatabaseOmUserInfo.
        :type om_user_expires_time: int
        """
        self._om_user_expires_time = om_user_expires_time

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
        if not isinstance(other, DatabaseOmUserInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
