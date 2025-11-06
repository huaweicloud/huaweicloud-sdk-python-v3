# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestoreRedisDataRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'recovery_info': 'RecoveryInfo'
    }

    attribute_map = {
        'recovery_info': 'recovery_info'
    }

    def __init__(self, recovery_info=None):
        r"""RestoreRedisDataRequestBody

        The model defined in huaweicloud sdk

        :param recovery_info: 
        :type recovery_info: :class:`huaweicloudsdkgaussdbfornosql.v3.RecoveryInfo`
        """
        
        

        self._recovery_info = None
        self.discriminator = None

        if recovery_info is not None:
            self.recovery_info = recovery_info

    @property
    def recovery_info(self):
        r"""Gets the recovery_info of this RestoreRedisDataRequestBody.

        :return: The recovery_info of this RestoreRedisDataRequestBody.
        :rtype: :class:`huaweicloudsdkgaussdbfornosql.v3.RecoveryInfo`
        """
        return self._recovery_info

    @recovery_info.setter
    def recovery_info(self, recovery_info):
        r"""Sets the recovery_info of this RestoreRedisDataRequestBody.

        :param recovery_info: The recovery_info of this RestoreRedisDataRequestBody.
        :type recovery_info: :class:`huaweicloudsdkgaussdbfornosql.v3.RecoveryInfo`
        """
        self._recovery_info = recovery_info

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
        if not isinstance(other, RestoreRedisDataRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
