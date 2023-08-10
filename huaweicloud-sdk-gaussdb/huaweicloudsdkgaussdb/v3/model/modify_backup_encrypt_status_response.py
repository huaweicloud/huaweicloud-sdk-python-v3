# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyBackupEncryptStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'encryption_status': 'str'
    }

    attribute_map = {
        'encryption_status': 'encryption_status'
    }

    def __init__(self, encryption_status=None):
        """ModifyBackupEncryptStatusResponse

        The model defined in huaweicloud sdk

        :param encryption_status: 备份加密状态。
        :type encryption_status: str
        """
        
        super(ModifyBackupEncryptStatusResponse, self).__init__()

        self._encryption_status = None
        self.discriminator = None

        if encryption_status is not None:
            self.encryption_status = encryption_status

    @property
    def encryption_status(self):
        """Gets the encryption_status of this ModifyBackupEncryptStatusResponse.

        备份加密状态。

        :return: The encryption_status of this ModifyBackupEncryptStatusResponse.
        :rtype: str
        """
        return self._encryption_status

    @encryption_status.setter
    def encryption_status(self, encryption_status):
        """Sets the encryption_status of this ModifyBackupEncryptStatusResponse.

        备份加密状态。

        :param encryption_status: The encryption_status of this ModifyBackupEncryptStatusResponse.
        :type encryption_status: str
        """
        self._encryption_status = encryption_status

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
        if not isinstance(other, ModifyBackupEncryptStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
