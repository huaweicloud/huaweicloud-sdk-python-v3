# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ShowBackupPolicyResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'backup_policy': 'BackupPolicy'
    }

    attribute_map = {
        'backup_policy': 'backup_policy'
    }

    def __init__(self, backup_policy=None):
        """ShowBackupPolicyResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._backup_policy = None
        self.discriminator = None

        if backup_policy is not None:
            self.backup_policy = backup_policy

    @property
    def backup_policy(self):
        """Gets the backup_policy of this ShowBackupPolicyResponse.


        :return: The backup_policy of this ShowBackupPolicyResponse.
        :rtype: BackupPolicy
        """
        return self._backup_policy

    @backup_policy.setter
    def backup_policy(self, backup_policy):
        """Sets the backup_policy of this ShowBackupPolicyResponse.


        :param backup_policy: The backup_policy of this ShowBackupPolicyResponse.
        :type: BackupPolicy
        """
        self._backup_policy = backup_policy

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowBackupPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
