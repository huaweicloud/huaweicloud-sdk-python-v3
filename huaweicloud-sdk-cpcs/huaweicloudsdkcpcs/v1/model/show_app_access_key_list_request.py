# coding: utf-8

import six

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
        'page_size': 'int',
        'page_num': 'int',
        'key_name': 'str',
        'sort_key': 'str',
        'sort_dir': 'str'
    }

    attribute_map = {
        'app_id': 'app_id',
        'page_size': 'page_size',
        'page_num': 'page_num',
        'key_name': 'key_name',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir'
    }

    def __init__(self, app_id=None, page_size=None, page_num=None, key_name=None, sort_key=None, sort_dir=None):
        r"""ShowAppAccessKeyListRequest

        The model defined in huaweicloud sdk

        :param app_id: 应用ID
        :type app_id: str
        :param page_size: 指定查询返回记录条数，默认值10
        :type page_size: int
        :param page_num: 索引位置，从page_num指定的下一条数据开始查询默认值为0
        :type page_num: int
        :param key_name: 访问密钥名称
        :type key_name: str
        :param sort_key: 排序属性，目前支持以下属性： - **create_time** : 应用的创建时间（默认）
        :type sort_key: str
        :param sort_dir: 排序方向，支持以下值： - **DESC** : 降序（默认） - **ASC** : 升序
        :type sort_dir: str
        """
        
        

        self._app_id = None
        self._page_size = None
        self._page_num = None
        self._key_name = None
        self._sort_key = None
        self._sort_dir = None
        self.discriminator = None

        self.app_id = app_id
        if page_size is not None:
            self.page_size = page_size
        if page_num is not None:
            self.page_num = page_num
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
    def page_size(self):
        r"""Gets the page_size of this ShowAppAccessKeyListRequest.

        指定查询返回记录条数，默认值10

        :return: The page_size of this ShowAppAccessKeyListRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ShowAppAccessKeyListRequest.

        指定查询返回记录条数，默认值10

        :param page_size: The page_size of this ShowAppAccessKeyListRequest.
        :type page_size: int
        """
        self._page_size = page_size

    @property
    def page_num(self):
        r"""Gets the page_num of this ShowAppAccessKeyListRequest.

        索引位置，从page_num指定的下一条数据开始查询默认值为0

        :return: The page_num of this ShowAppAccessKeyListRequest.
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        r"""Sets the page_num of this ShowAppAccessKeyListRequest.

        索引位置，从page_num指定的下一条数据开始查询默认值为0

        :param page_num: The page_num of this ShowAppAccessKeyListRequest.
        :type page_num: int
        """
        self._page_num = page_num

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
        if not isinstance(other, ShowAppAccessKeyListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
