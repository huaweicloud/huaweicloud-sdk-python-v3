# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAppAccessKeyListRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'key_name': 'str',
        'sort_key': 'str',
        'sort_dir': 'str'
    }

    attribute_map = {
        'app_id': 'app_id',
        'limit': 'limit',
        'offset': 'offset',
        'key_name': 'key_name',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, app_id=None, limit=None, offset=None, key_name=None, sort_key=None, sort_dir=None):
        r"""ShowAppAccessKeyListRequest

        The model defined in huaweicloud sdk

        :param app_id: 应用ID
        :type app_id: str
        :param limit: 指定查询返回记录条数，默认值10
        :type limit: int
        :param offset: 索引位置，从offset指定的下一条数据开始查询默认值为0
        :type offset: int
        :param key_name: 访问密钥名称
        :type key_name: str
        :param sort_key: 排序属性，目前支持以下属性： - **create_time** : 应用的创建时间（默认）
        :type sort_key: str
        :param sort_dir: 排序方向，支持以下值： - **DESC** : 降序（默认） - **ASC** : 升序
        :type sort_dir: str
        """
        
        

        self._app_id = None
        self._limit = None
        self._offset = None
        self._key_name = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        self.app_id = app_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if key_name is not None:
            self.key_name = key_name
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir

    @property
    def app_id(self):
        r"""Gets the app_id of this ShowAppAccessKeyListRequest.

        应用ID

        :return: The app_id of this ShowAppAccessKeyListRequest.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this ShowAppAccessKeyListRequest.

        应用ID

        :param app_id: The app_id of this ShowAppAccessKeyListRequest.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def limit(self):
        r"""Gets the limit of this ShowAppAccessKeyListRequest.

        指定查询返回记录条数，默认值10

        :return: The limit of this ShowAppAccessKeyListRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowAppAccessKeyListRequest.

        指定查询返回记录条数，默认值10

        :param limit: The limit of this ShowAppAccessKeyListRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowAppAccessKeyListRequest.

        索引位置，从offset指定的下一条数据开始查询默认值为0

        :return: The offset of this ShowAppAccessKeyListRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowAppAccessKeyListRequest.

        索引位置，从offset指定的下一条数据开始查询默认值为0

        :param offset: The offset of this ShowAppAccessKeyListRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def key_name(self):
        r"""Gets the key_name of this ShowAppAccessKeyListRequest.

        访问密钥名称

        :return: The key_name of this ShowAppAccessKeyListRequest.
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        r"""Sets the key_name of this ShowAppAccessKeyListRequest.

        访问密钥名称

        :param key_name: The key_name of this ShowAppAccessKeyListRequest.
        :type key_name: str
        """
        self._key_name = key_name

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ShowAppAccessKeyListRequest.

        排序属性，目前支持以下属性： - **create_time** : 应用的创建时间（默认）

        :return: The sort_key of this ShowAppAccessKeyListRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ShowAppAccessKeyListRequest.

        排序属性，目前支持以下属性： - **create_time** : 应用的创建时间（默认）

        :param sort_key: The sort_key of this ShowAppAccessKeyListRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ShowAppAccessKeyListRequest.

        排序方向，支持以下值： - **DESC** : 降序（默认） - **ASC** : 升序

        :return: The sort_dir of this ShowAppAccessKeyListRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ShowAppAccessKeyListRequest.

        排序方向，支持以下值： - **DESC** : 降序（默认） - **ASC** : 升序

        :param sort_dir: The sort_dir of this ShowAppAccessKeyListRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

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
        if not isinstance(other, ShowAppAccessKeyListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
