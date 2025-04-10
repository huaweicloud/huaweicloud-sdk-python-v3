# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateIncreBackupPolicy1RequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'incre_backup_policy': 'ShowIncreBackupPolicyRespBodyIncreBackupPolicy'
    }

    attribute_map = {
        'incre_backup_policy': 'incre_backup_policy'
    }

    def __init__(self, incre_backup_policy=None):
        r"""UpdateIncreBackupPolicy1RequestBody

        The model defined in huaweicloud sdk

        :param incre_backup_policy: 
        :type incre_backup_policy: :class:`huaweicloudsdkrds.v3.ShowIncreBackupPolicyRespBodyIncreBackupPolicy`
        """
        
        

        self._incre_backup_policy = None
        self.discriminator = None

        self.incre_backup_policy = incre_backup_policy

    @property
    def incre_backup_policy(self):
        r"""Gets the incre_backup_policy of this UpdateIncreBackupPolicy1RequestBody.

        :return: The incre_backup_policy of this UpdateIncreBackupPolicy1RequestBody.
        :rtype: :class:`huaweicloudsdkrds.v3.ShowIncreBackupPolicyRespBodyIncreBackupPolicy`
        """
        return self._incre_backup_policy

    @incre_backup_policy.setter
    def incre_backup_policy(self, incre_backup_policy):
        r"""Sets the incre_backup_policy of this UpdateIncreBackupPolicy1RequestBody.

        :param incre_backup_policy: The incre_backup_policy of this UpdateIncreBackupPolicy1RequestBody.
        :type incre_backup_policy: :class:`huaweicloudsdkrds.v3.ShowIncreBackupPolicyRespBodyIncreBackupPolicy`
        """
        self._incre_backup_policy = incre_backup_policy

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
        if not isinstance(other, UpdateIncreBackupPolicy1RequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
