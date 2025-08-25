# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAccessKeyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_key': 'str',
        'secret_key': 'str',
        'app_id': 'str',
        'key_name': 'str',
        'is_imported': 'bool'
    }

    attribute_map = {
        'access_key': 'access_key',
        'secret_key': 'secret_key',
        'app_id': 'app_id',
        'key_name': 'key_name',
        'is_imported': 'is_imported'
    }

    def __init__(self, access_key=None, secret_key=None, app_id=None, key_name=None, is_imported=None):
        r"""ShowAccessKeyResponse

        The model defined in huaweicloud sdk

        :param access_key: 访问密钥的access key
        :type access_key: str
        :param secret_key: 访问密钥的secret key
        :type secret_key: str
        :param app_id: 应用id
        :type app_id: str
        :param key_name: 密钥名称
        :type key_name: str
        :param is_imported: 是否导入
        :type is_imported: bool
        """
        
        super(ShowAccessKeyResponse, self).__init__()

        self._access_key = None
        self._secret_key = None
        self._app_id = None
        self._key_name = None
        self._is_imported = None
        self.discriminator = None

        if access_key is not None:
            self.access_key = access_key
        if secret_key is not None:
            self.secret_key = secret_key
        if app_id is not None:
            self.app_id = app_id
        if key_name is not None:
            self.key_name = key_name
        if is_imported is not None:
            self.is_imported = is_imported

    @property
    def access_key(self):
        r"""Gets the access_key of this ShowAccessKeyResponse.

        访问密钥的access key

        :return: The access_key of this ShowAccessKeyResponse.
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        r"""Sets the access_key of this ShowAccessKeyResponse.

        访问密钥的access key

        :param access_key: The access_key of this ShowAccessKeyResponse.
        :type access_key: str
        """
        self._access_key = access_key

    @property
    def secret_key(self):
        r"""Gets the secret_key of this ShowAccessKeyResponse.

        访问密钥的secret key

        :return: The secret_key of this ShowAccessKeyResponse.
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        r"""Sets the secret_key of this ShowAccessKeyResponse.

        访问密钥的secret key

        :param secret_key: The secret_key of this ShowAccessKeyResponse.
        :type secret_key: str
        """
        self._secret_key = secret_key

    @property
    def app_id(self):
        r"""Gets the app_id of this ShowAccessKeyResponse.

        应用id

        :return: The app_id of this ShowAccessKeyResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this ShowAccessKeyResponse.

        应用id

        :param app_id: The app_id of this ShowAccessKeyResponse.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def key_name(self):
        r"""Gets the key_name of this ShowAccessKeyResponse.

        密钥名称

        :return: The key_name of this ShowAccessKeyResponse.
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        r"""Sets the key_name of this ShowAccessKeyResponse.

        密钥名称

        :param key_name: The key_name of this ShowAccessKeyResponse.
        :type key_name: str
        """
        self._key_name = key_name

    @property
    def is_imported(self):
        r"""Gets the is_imported of this ShowAccessKeyResponse.

        是否导入

        :return: The is_imported of this ShowAccessKeyResponse.
        :rtype: bool
        """
        return self._is_imported

    @is_imported.setter
    def is_imported(self, is_imported):
        r"""Sets the is_imported of this ShowAccessKeyResponse.

        是否导入

        :param is_imported: The is_imported of this ShowAccessKeyResponse.
        :type is_imported: bool
        """
        self._is_imported = is_imported

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
        if not isinstance(other, ShowAccessKeyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
