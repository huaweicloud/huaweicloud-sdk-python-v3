# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListLiveDataApiV2Request:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'app_id': 'str',
        'app_name': 'str',
        'name': 'str',
        'status': 'str',
        'path': 'str',
        'precise_search': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'app_id': 'app_id',
        'app_name': 'app_name',
        'name': 'name',
        'status': 'status',
        'path': 'path',
        'precise_search': 'precise_search'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, app_id=None, app_name=None, name=None, status=None, path=None, precise_search=None):
        """ListLiveDataApiV2Request

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param offset: 偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0
        :type offset: int
        :param limit: 每页显示的条目数量
        :type limit: int
        :param app_id: 后端API归属的集成应用编号
        :type app_id: str
        :param app_name: 后端API归属的集成应用名称
        :type app_name: str
        :param name: 后端API名称
        :type name: str
        :param status: 后端API状态，支持1，3，4，分别表示待开发，开发中和已部署状态
        :type status: str
        :param path: 后端API请求路径
        :type path: str
        :param precise_search: 指定需要精确匹配查找的参数名称，多个参数需要支持精确匹配时参数之间使用“,”隔开。  当前支持name，path，status。
        :type precise_search: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._app_id = None
        self._app_name = None
        self._name = None
        self._status = None
        self._path = None
        self._precise_search = None
        self.discriminator = None

        self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if app_id is not None:
            self.app_id = app_id
        if app_name is not None:
            self.app_name = app_name
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if path is not None:
            self.path = path
        if precise_search is not None:
            self.precise_search = precise_search

    @property
    def instance_id(self):
        """Gets the instance_id of this ListLiveDataApiV2Request.

        实例ID

        :return: The instance_id of this ListLiveDataApiV2Request.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListLiveDataApiV2Request.

        实例ID

        :param instance_id: The instance_id of this ListLiveDataApiV2Request.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        """Gets the offset of this ListLiveDataApiV2Request.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :return: The offset of this ListLiveDataApiV2Request.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListLiveDataApiV2Request.

        偏移量，表示从此偏移量开始查询，偏移量小于0时，自动转换为0

        :param offset: The offset of this ListLiveDataApiV2Request.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListLiveDataApiV2Request.

        每页显示的条目数量

        :return: The limit of this ListLiveDataApiV2Request.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListLiveDataApiV2Request.

        每页显示的条目数量

        :param limit: The limit of this ListLiveDataApiV2Request.
        :type limit: int
        """
        self._limit = limit

    @property
    def app_id(self):
        """Gets the app_id of this ListLiveDataApiV2Request.

        后端API归属的集成应用编号

        :return: The app_id of this ListLiveDataApiV2Request.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ListLiveDataApiV2Request.

        后端API归属的集成应用编号

        :param app_id: The app_id of this ListLiveDataApiV2Request.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_name(self):
        """Gets the app_name of this ListLiveDataApiV2Request.

        后端API归属的集成应用名称

        :return: The app_name of this ListLiveDataApiV2Request.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this ListLiveDataApiV2Request.

        后端API归属的集成应用名称

        :param app_name: The app_name of this ListLiveDataApiV2Request.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def name(self):
        """Gets the name of this ListLiveDataApiV2Request.

        后端API名称

        :return: The name of this ListLiveDataApiV2Request.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListLiveDataApiV2Request.

        后端API名称

        :param name: The name of this ListLiveDataApiV2Request.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this ListLiveDataApiV2Request.

        后端API状态，支持1，3，4，分别表示待开发，开发中和已部署状态

        :return: The status of this ListLiveDataApiV2Request.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListLiveDataApiV2Request.

        后端API状态，支持1，3，4，分别表示待开发，开发中和已部署状态

        :param status: The status of this ListLiveDataApiV2Request.
        :type status: str
        """
        self._status = status

    @property
    def path(self):
        """Gets the path of this ListLiveDataApiV2Request.

        后端API请求路径

        :return: The path of this ListLiveDataApiV2Request.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ListLiveDataApiV2Request.

        后端API请求路径

        :param path: The path of this ListLiveDataApiV2Request.
        :type path: str
        """
        self._path = path

    @property
    def precise_search(self):
        """Gets the precise_search of this ListLiveDataApiV2Request.

        指定需要精确匹配查找的参数名称，多个参数需要支持精确匹配时参数之间使用“,”隔开。  当前支持name，path，status。

        :return: The precise_search of this ListLiveDataApiV2Request.
        :rtype: str
        """
        return self._precise_search

    @precise_search.setter
    def precise_search(self, precise_search):
        """Sets the precise_search of this ListLiveDataApiV2Request.

        指定需要精确匹配查找的参数名称，多个参数需要支持精确匹配时参数之间使用“,”隔开。  当前支持name，path，status。

        :param precise_search: The precise_search of this ListLiveDataApiV2Request.
        :type precise_search: str
        """
        self._precise_search = precise_search

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
        if not isinstance(other, ListLiveDataApiV2Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
