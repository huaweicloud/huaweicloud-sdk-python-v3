# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FailReasons:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'reason': 'str',
        'host_id': 'str'
    }

    attribute_map = {
        'reason': 'reason',
        'host_id': 'host_id'
    }

    def __init__(self, reason=None, host_id=None):
        r"""FailReasons

        The model defined in huaweicloud sdk

        :param reason: **参数解释** 原因 **取值范围** 长度1-100 
        :type reason: str
        :param host_id: **参数解释** 主机ID **取值范围** 长度1-64 
        :type host_id: str
        """
        
        

        self._reason = None
        self._host_id = None
        self.discriminator = None

        if reason is not None:
            self.reason = reason
        if host_id is not None:
            self.host_id = host_id

    @property
    def reason(self):
        r"""Gets the reason of this FailReasons.

        **参数解释** 原因 **取值范围** 长度1-100 

        :return: The reason of this FailReasons.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this FailReasons.

        **参数解释** 原因 **取值范围** 长度1-100 

        :param reason: The reason of this FailReasons.
        :type reason: str
        """
        self._reason = reason

    @property
    def host_id(self):
        r"""Gets the host_id of this FailReasons.

        **参数解释** 主机ID **取值范围** 长度1-64 

        :return: The host_id of this FailReasons.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        r"""Sets the host_id of this FailReasons.

        **参数解释** 主机ID **取值范围** 长度1-64 

        :param host_id: The host_id of this FailReasons.
        :type host_id: str
        """
        self._host_id = host_id

    def to_dict(self):
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
        if not isinstance(other, FailReasons):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
