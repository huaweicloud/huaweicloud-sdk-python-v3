# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupEncryptRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'kms_key_id': 'str',
        'encryption_status': 'str'
    }

    attribute_map = {
        'type': 'type',
        'kms_key_id': 'kms_key_id',
        'encryption_status': 'encryption_status'
    }

    def __init__(self, type=None, kms_key_id=None, encryption_status=None):
        """BackupEncryptRequest

        The model defined in huaweicloud sdk

        :param type: 加密类型。当前只支持kms。 开启加密时必传，关闭加密时不传。 不区分大小写。
        :type type: str
        :param kms_key_id: kms加密ID。加密时必传，关闭加密时候不传。
        :type kms_key_id: str
        :param encryption_status: 开启或关闭加密。不区分大小写。
        :type encryption_status: str
        """
        
        

        self._type = None
        self._kms_key_id = None
        self._encryption_status = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if kms_key_id is not None:
            self.kms_key_id = kms_key_id
        self.encryption_status = encryption_status

    @property
    def type(self):
        """Gets the type of this BackupEncryptRequest.

        加密类型。当前只支持kms。 开启加密时必传，关闭加密时不传。 不区分大小写。

        :return: The type of this BackupEncryptRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BackupEncryptRequest.

        加密类型。当前只支持kms。 开启加密时必传，关闭加密时不传。 不区分大小写。

        :param type: The type of this BackupEncryptRequest.
        :type type: str
        """
        self._type = type

    @property
    def kms_key_id(self):
        """Gets the kms_key_id of this BackupEncryptRequest.

        kms加密ID。加密时必传，关闭加密时候不传。

        :return: The kms_key_id of this BackupEncryptRequest.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """Sets the kms_key_id of this BackupEncryptRequest.

        kms加密ID。加密时必传，关闭加密时候不传。

        :param kms_key_id: The kms_key_id of this BackupEncryptRequest.
        :type kms_key_id: str
        """
        self._kms_key_id = kms_key_id

    @property
    def encryption_status(self):
        """Gets the encryption_status of this BackupEncryptRequest.

        开启或关闭加密。不区分大小写。

        :return: The encryption_status of this BackupEncryptRequest.
        :rtype: str
        """
        return self._encryption_status

    @encryption_status.setter
    def encryption_status(self, encryption_status):
        """Sets the encryption_status of this BackupEncryptRequest.

        开启或关闭加密。不区分大小写。

        :param encryption_status: The encryption_status of this BackupEncryptRequest.
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
        if not isinstance(other, BackupEncryptRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
