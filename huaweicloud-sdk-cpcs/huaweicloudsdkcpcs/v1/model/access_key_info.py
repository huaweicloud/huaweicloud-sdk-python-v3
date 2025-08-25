# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessKeyInfo:

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
        'key_name': 'str',
        'access_key': 'str',
        'app_name': 'str',
        'status': 'str',
        'create_time': 'int',
        'download_time': 'int',
        'is_downloaded': 'bool',
        'is_imported': 'bool'
    }

    attribute_map = {
        'access_key_id': 'access_key_id',
        'key_name': 'key_name',
        'access_key': 'access_key',
        'app_name': 'app_name',
        'status': 'status',
        'create_time': 'create_time',
        'download_time': 'download_time',
        'is_downloaded': 'is_downloaded',
        'is_imported': 'is_imported'
    }

    def __init__(self, access_key_id=None, key_name=None, access_key=None, app_name=None, status=None, create_time=None, download_time=None, is_downloaded=None, is_imported=None):
        r"""AccessKeyInfo

        The model defined in huaweicloud sdk

        :param access_key_id: 访问密钥ID
        :type access_key_id: str
        :param key_name: 访问密钥名称
        :type key_name: str
        :param access_key: 访问密钥AK
        :type access_key: str
        :param app_name: 访问密钥所属的应用名称
        :type app_name: str
        :param status: 访问密钥状态
        :type status: str
        :param create_time: 应用的创建时间，UNIX时间戳，单位毫秒
        :type create_time: int
        :param download_time: 下载时间
        :type download_time: int
        :param is_downloaded: 是否下载
        :type is_downloaded: bool
        :param is_imported: 是否导入
        :type is_imported: bool
        """
        
        

        self._access_key_id = None
        self._key_name = None
        self._access_key = None
        self._app_name = None
        self._status = None
        self._create_time = None
        self._download_time = None
        self._is_downloaded = None
        self._is_imported = None
        self.discriminator = None

        self.access_key_id = access_key_id
        self.key_name = key_name
        self.access_key = access_key
        self.app_name = app_name
        self.status = status
        self.create_time = create_time
        if download_time is not None:
            self.download_time = download_time
        self.is_downloaded = is_downloaded
        self.is_imported = is_imported

    @property
    def access_key_id(self):
        r"""Gets the access_key_id of this AccessKeyInfo.

        访问密钥ID

        :return: The access_key_id of this AccessKeyInfo.
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        r"""Sets the access_key_id of this AccessKeyInfo.

        访问密钥ID

        :param access_key_id: The access_key_id of this AccessKeyInfo.
        :type access_key_id: str
        """
        self._access_key_id = access_key_id

    @property
    def key_name(self):
        r"""Gets the key_name of this AccessKeyInfo.

        访问密钥名称

        :return: The key_name of this AccessKeyInfo.
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        r"""Sets the key_name of this AccessKeyInfo.

        访问密钥名称

        :param key_name: The key_name of this AccessKeyInfo.
        :type key_name: str
        """
        self._key_name = key_name

    @property
    def access_key(self):
        r"""Gets the access_key of this AccessKeyInfo.

        访问密钥AK

        :return: The access_key of this AccessKeyInfo.
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        r"""Sets the access_key of this AccessKeyInfo.

        访问密钥AK

        :param access_key: The access_key of this AccessKeyInfo.
        :type access_key: str
        """
        self._access_key = access_key

    @property
    def app_name(self):
        r"""Gets the app_name of this AccessKeyInfo.

        访问密钥所属的应用名称

        :return: The app_name of this AccessKeyInfo.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this AccessKeyInfo.

        访问密钥所属的应用名称

        :param app_name: The app_name of this AccessKeyInfo.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def status(self):
        r"""Gets the status of this AccessKeyInfo.

        访问密钥状态

        :return: The status of this AccessKeyInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AccessKeyInfo.

        访问密钥状态

        :param status: The status of this AccessKeyInfo.
        :type status: str
        """
        self._status = status

    @property
    def create_time(self):
        r"""Gets the create_time of this AccessKeyInfo.

        应用的创建时间，UNIX时间戳，单位毫秒

        :return: The create_time of this AccessKeyInfo.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AccessKeyInfo.

        应用的创建时间，UNIX时间戳，单位毫秒

        :param create_time: The create_time of this AccessKeyInfo.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def download_time(self):
        r"""Gets the download_time of this AccessKeyInfo.

        下载时间

        :return: The download_time of this AccessKeyInfo.
        :rtype: int
        """
        return self._download_time

    @download_time.setter
    def download_time(self, download_time):
        r"""Sets the download_time of this AccessKeyInfo.

        下载时间

        :param download_time: The download_time of this AccessKeyInfo.
        :type download_time: int
        """
        self._download_time = download_time

    @property
    def is_downloaded(self):
        r"""Gets the is_downloaded of this AccessKeyInfo.

        是否下载

        :return: The is_downloaded of this AccessKeyInfo.
        :rtype: bool
        """
        return self._is_downloaded

    @is_downloaded.setter
    def is_downloaded(self, is_downloaded):
        r"""Sets the is_downloaded of this AccessKeyInfo.

        是否下载

        :param is_downloaded: The is_downloaded of this AccessKeyInfo.
        :type is_downloaded: bool
        """
        self._is_downloaded = is_downloaded

    @property
    def is_imported(self):
        r"""Gets the is_imported of this AccessKeyInfo.

        是否导入

        :return: The is_imported of this AccessKeyInfo.
        :rtype: bool
        """
        return self._is_imported

    @is_imported.setter
    def is_imported(self, is_imported):
        r"""Sets the is_imported of this AccessKeyInfo.

        是否导入

        :param is_imported: The is_imported of this AccessKeyInfo.
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
        if not isinstance(other, AccessKeyInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
