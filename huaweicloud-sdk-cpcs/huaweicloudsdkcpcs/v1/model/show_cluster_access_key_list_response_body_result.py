# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowClusterAccessKeyListResponseBodyResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_key_id': 'str',
        'status': 'str',
        'app_name': 'str',
        'access_key': 'str',
        'key_name': 'str',
        'create_time': 'int'
    }

    attribute_map = {
        'access_key_id': 'access_key_id',
        'status': 'status',
        'app_name': 'app_name',
        'access_key': 'access_key',
        'key_name': 'key_name',
        'create_time': 'create_time'
    }

    def __init__(self, access_key_id=None, status=None, app_name=None, access_key=None, key_name=None, create_time=None):
        r"""ShowClusterAccessKeyListResponseBodyResult

        The model defined in huaweicloud sdk

        :param access_key_id: 访问密钥ID
        :type access_key_id: str
        :param status: 访问密钥状态
        :type status: str
        :param app_name: 访问密钥所属的应用名称
        :type app_name: str
        :param access_key: 访问密钥AK
        :type access_key: str
        :param key_name: 访问密钥名称
        :type key_name: str
        :param create_time: 应用的创建时间，UNIX时间戳，单位毫秒
        :type create_time: int
        """
        
        

        self._access_key_id = None
        self._status = None
        self._app_name = None
        self._access_key = None
        self._key_name = None
        self._create_time = None
        self.discriminator = None

        self.access_key_id = access_key_id
        self.status = status
        self.app_name = app_name
        self.access_key = access_key
        self.key_name = key_name
        self.create_time = create_time

    @property
    def access_key_id(self):
        r"""Gets the access_key_id of this ShowClusterAccessKeyListResponseBodyResult.

        访问密钥ID

        :return: The access_key_id of this ShowClusterAccessKeyListResponseBodyResult.
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        r"""Sets the access_key_id of this ShowClusterAccessKeyListResponseBodyResult.

        访问密钥ID

        :param access_key_id: The access_key_id of this ShowClusterAccessKeyListResponseBodyResult.
        :type access_key_id: str
        """
        self._access_key_id = access_key_id

    @property
    def status(self):
        r"""Gets the status of this ShowClusterAccessKeyListResponseBodyResult.

        访问密钥状态

        :return: The status of this ShowClusterAccessKeyListResponseBodyResult.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowClusterAccessKeyListResponseBodyResult.

        访问密钥状态

        :param status: The status of this ShowClusterAccessKeyListResponseBodyResult.
        :type status: str
        """
        self._status = status

    @property
    def app_name(self):
        r"""Gets the app_name of this ShowClusterAccessKeyListResponseBodyResult.

        访问密钥所属的应用名称

        :return: The app_name of this ShowClusterAccessKeyListResponseBodyResult.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ShowClusterAccessKeyListResponseBodyResult.

        访问密钥所属的应用名称

        :param app_name: The app_name of this ShowClusterAccessKeyListResponseBodyResult.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def access_key(self):
        r"""Gets the access_key of this ShowClusterAccessKeyListResponseBodyResult.

        访问密钥AK

        :return: The access_key of this ShowClusterAccessKeyListResponseBodyResult.
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        r"""Sets the access_key of this ShowClusterAccessKeyListResponseBodyResult.

        访问密钥AK

        :param access_key: The access_key of this ShowClusterAccessKeyListResponseBodyResult.
        :type access_key: str
        """
        self._access_key = access_key

    @property
    def key_name(self):
        r"""Gets the key_name of this ShowClusterAccessKeyListResponseBodyResult.

        访问密钥名称

        :return: The key_name of this ShowClusterAccessKeyListResponseBodyResult.
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        r"""Sets the key_name of this ShowClusterAccessKeyListResponseBodyResult.

        访问密钥名称

        :param key_name: The key_name of this ShowClusterAccessKeyListResponseBodyResult.
        :type key_name: str
        """
        self._key_name = key_name

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowClusterAccessKeyListResponseBodyResult.

        应用的创建时间，UNIX时间戳，单位毫秒

        :return: The create_time of this ShowClusterAccessKeyListResponseBodyResult.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowClusterAccessKeyListResponseBodyResult.

        应用的创建时间，UNIX时间戳，单位毫秒

        :param create_time: The create_time of this ShowClusterAccessKeyListResponseBodyResult.
        :type create_time: int
        """
        self._create_time = create_time

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
        if not isinstance(other, ShowClusterAccessKeyListResponseBodyResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
