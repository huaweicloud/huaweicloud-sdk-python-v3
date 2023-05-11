# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Version:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version_metadata': 'VersionMetadata',
        'secret_binary': 'str',
        'secret_string': 'str'
    }

    attribute_map = {
        'version_metadata': 'version_metadata',
        'secret_binary': 'secret_binary',
        'secret_string': 'secret_string'
    }

    def __init__(self, version_metadata=None, secret_binary=None, secret_string=None):
        """Version

        The model defined in huaweicloud sdk

        :param version_metadata: 
        :type version_metadata: :class:`huaweicloudsdkcsms.v1.VersionMetadata`
        :param secret_binary: 二进制类型凭据在base64编码后的明文，凭据管理服务将其加密后，存入凭据的初始版本中。  类型：base64编码的二进制数据对象。 
        :type secret_binary: str
        :param secret_string: 文本类型凭据的明文，凭据管理服务将其加密后，存入凭据的初始版本中。
        :type secret_string: str
        """
        
        

        self._version_metadata = None
        self._secret_binary = None
        self._secret_string = None
        self.discriminator = None

        if version_metadata is not None:
            self.version_metadata = version_metadata
        if secret_binary is not None:
            self.secret_binary = secret_binary
        if secret_string is not None:
            self.secret_string = secret_string

    @property
    def version_metadata(self):
        """Gets the version_metadata of this Version.

        :return: The version_metadata of this Version.
        :rtype: :class:`huaweicloudsdkcsms.v1.VersionMetadata`
        """
        return self._version_metadata

    @version_metadata.setter
    def version_metadata(self, version_metadata):
        """Sets the version_metadata of this Version.

        :param version_metadata: The version_metadata of this Version.
        :type version_metadata: :class:`huaweicloudsdkcsms.v1.VersionMetadata`
        """
        self._version_metadata = version_metadata

    @property
    def secret_binary(self):
        """Gets the secret_binary of this Version.

        二进制类型凭据在base64编码后的明文，凭据管理服务将其加密后，存入凭据的初始版本中。  类型：base64编码的二进制数据对象。 

        :return: The secret_binary of this Version.
        :rtype: str
        """
        return self._secret_binary

    @secret_binary.setter
    def secret_binary(self, secret_binary):
        """Sets the secret_binary of this Version.

        二进制类型凭据在base64编码后的明文，凭据管理服务将其加密后，存入凭据的初始版本中。  类型：base64编码的二进制数据对象。 

        :param secret_binary: The secret_binary of this Version.
        :type secret_binary: str
        """
        self._secret_binary = secret_binary

    @property
    def secret_string(self):
        """Gets the secret_string of this Version.

        文本类型凭据的明文，凭据管理服务将其加密后，存入凭据的初始版本中。

        :return: The secret_string of this Version.
        :rtype: str
        """
        return self._secret_string

    @secret_string.setter
    def secret_string(self, secret_string):
        """Sets the secret_string of this Version.

        文本类型凭据的明文，凭据管理服务将其加密后，存入凭据的初始版本中。

        :param secret_string: The secret_string of this Version.
        :type secret_string: str
        """
        self._secret_string = secret_string

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
        if not isinstance(other, Version):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
