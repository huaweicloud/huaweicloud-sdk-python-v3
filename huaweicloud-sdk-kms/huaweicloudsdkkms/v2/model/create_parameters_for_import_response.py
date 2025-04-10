# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateParametersForImportResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key_id': 'str',
        'import_token': 'str',
        'expiration_time': 'int',
        'public_key': 'str'
    }

    attribute_map = {
        'key_id': 'key_id',
        'import_token': 'import_token',
        'expiration_time': 'expiration_time',
        'public_key': 'public_key'
    }

    def __init__(self, key_id=None, import_token=None, expiration_time=None, public_key=None):
        r"""CreateParametersForImportResponse

        The model defined in huaweicloud sdk

        :param key_id: 密钥ID。
        :type key_id: str
        :param import_token: 密钥导入令牌。
        :type import_token: str
        :param expiration_time: 导入参数到期时间，时间戳，即从1970年1月1日至该时间的总秒数。
        :type expiration_time: int
        :param public_key: 加密密钥材料的公钥，base64格式。
        :type public_key: str
        """
        
        super(CreateParametersForImportResponse, self).__init__()

        self._key_id = None
        self._import_token = None
        self._expiration_time = None
        self._public_key = None
        self.discriminator = None

        if key_id is not None:
            self.key_id = key_id
        if import_token is not None:
            self.import_token = import_token
        if expiration_time is not None:
            self.expiration_time = expiration_time
        if public_key is not None:
            self.public_key = public_key

    @property
    def key_id(self):
        r"""Gets the key_id of this CreateParametersForImportResponse.

        密钥ID。

        :return: The key_id of this CreateParametersForImportResponse.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        r"""Sets the key_id of this CreateParametersForImportResponse.

        密钥ID。

        :param key_id: The key_id of this CreateParametersForImportResponse.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def import_token(self):
        r"""Gets the import_token of this CreateParametersForImportResponse.

        密钥导入令牌。

        :return: The import_token of this CreateParametersForImportResponse.
        :rtype: str
        """
        return self._import_token

    @import_token.setter
    def import_token(self, import_token):
        r"""Sets the import_token of this CreateParametersForImportResponse.

        密钥导入令牌。

        :param import_token: The import_token of this CreateParametersForImportResponse.
        :type import_token: str
        """
        self._import_token = import_token

    @property
    def expiration_time(self):
        r"""Gets the expiration_time of this CreateParametersForImportResponse.

        导入参数到期时间，时间戳，即从1970年1月1日至该时间的总秒数。

        :return: The expiration_time of this CreateParametersForImportResponse.
        :rtype: int
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        r"""Sets the expiration_time of this CreateParametersForImportResponse.

        导入参数到期时间，时间戳，即从1970年1月1日至该时间的总秒数。

        :param expiration_time: The expiration_time of this CreateParametersForImportResponse.
        :type expiration_time: int
        """
        self._expiration_time = expiration_time

    @property
    def public_key(self):
        r"""Gets the public_key of this CreateParametersForImportResponse.

        加密密钥材料的公钥，base64格式。

        :return: The public_key of this CreateParametersForImportResponse.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        r"""Sets the public_key of this CreateParametersForImportResponse.

        加密密钥材料的公钥，base64格式。

        :param public_key: The public_key of this CreateParametersForImportResponse.
        :type public_key: str
        """
        self._public_key = public_key

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
        if not isinstance(other, CreateParametersForImportResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
