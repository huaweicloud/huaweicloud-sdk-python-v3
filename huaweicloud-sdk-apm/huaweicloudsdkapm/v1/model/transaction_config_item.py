# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TransactionConfigItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'business_id': 'int',
        'env_id': 'int',
        'method': 'str',
        'env_name': 'str',
        'region': 'str',
        'type': 'str',
        'app_name': 'str',
        'url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'business_id': 'business_id',
        'env_id': 'env_id',
        'method': 'method',
        'env_name': 'env_name',
        'region': 'region',
        'type': 'type',
        'app_name': 'app_name',
        'url': 'url'
    }

    def __init__(self, id=None, business_id=None, env_id=None, method=None, env_name=None, region=None, type=None, app_name=None, url=None):
        """TransactionConfigItem

        The model defined in huaweicloud sdk

        :param id: 配置id。
        :type id: int
        :param business_id: 应用id。
        :type business_id: int
        :param env_id: 环境id。
        :type env_id: int
        :param method: 请求方式。
        :type method: str
        :param env_name: 环境名称。
        :type env_name: str
        :param region: region显示英文名称。
        :type region: str
        :param type: 类型。
        :type type: str
        :param app_name: 应用名称。
        :type app_name: str
        :param url: url地址。
        :type url: str
        """
        
        

        self._id = None
        self._business_id = None
        self._env_id = None
        self._method = None
        self._env_name = None
        self._region = None
        self._type = None
        self._app_name = None
        self._url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if business_id is not None:
            self.business_id = business_id
        if env_id is not None:
            self.env_id = env_id
        if method is not None:
            self.method = method
        if env_name is not None:
            self.env_name = env_name
        if region is not None:
            self.region = region
        if type is not None:
            self.type = type
        if app_name is not None:
            self.app_name = app_name
        if url is not None:
            self.url = url

    @property
    def id(self):
        """Gets the id of this TransactionConfigItem.

        配置id。

        :return: The id of this TransactionConfigItem.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TransactionConfigItem.

        配置id。

        :param id: The id of this TransactionConfigItem.
        :type id: int
        """
        self._id = id

    @property
    def business_id(self):
        """Gets the business_id of this TransactionConfigItem.

        应用id。

        :return: The business_id of this TransactionConfigItem.
        :rtype: int
        """
        return self._business_id

    @business_id.setter
    def business_id(self, business_id):
        """Sets the business_id of this TransactionConfigItem.

        应用id。

        :param business_id: The business_id of this TransactionConfigItem.
        :type business_id: int
        """
        self._business_id = business_id

    @property
    def env_id(self):
        """Gets the env_id of this TransactionConfigItem.

        环境id。

        :return: The env_id of this TransactionConfigItem.
        :rtype: int
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this TransactionConfigItem.

        环境id。

        :param env_id: The env_id of this TransactionConfigItem.
        :type env_id: int
        """
        self._env_id = env_id

    @property
    def method(self):
        """Gets the method of this TransactionConfigItem.

        请求方式。

        :return: The method of this TransactionConfigItem.
        :rtype: str
        """
        return self._method

    @method.setter
    def method(self, method):
        """Sets the method of this TransactionConfigItem.

        请求方式。

        :param method: The method of this TransactionConfigItem.
        :type method: str
        """
        self._method = method

    @property
    def env_name(self):
        """Gets the env_name of this TransactionConfigItem.

        环境名称。

        :return: The env_name of this TransactionConfigItem.
        :rtype: str
        """
        return self._env_name

    @env_name.setter
    def env_name(self, env_name):
        """Sets the env_name of this TransactionConfigItem.

        环境名称。

        :param env_name: The env_name of this TransactionConfigItem.
        :type env_name: str
        """
        self._env_name = env_name

    @property
    def region(self):
        """Gets the region of this TransactionConfigItem.

        region显示英文名称。

        :return: The region of this TransactionConfigItem.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this TransactionConfigItem.

        region显示英文名称。

        :param region: The region of this TransactionConfigItem.
        :type region: str
        """
        self._region = region

    @property
    def type(self):
        """Gets the type of this TransactionConfigItem.

        类型。

        :return: The type of this TransactionConfigItem.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TransactionConfigItem.

        类型。

        :param type: The type of this TransactionConfigItem.
        :type type: str
        """
        self._type = type

    @property
    def app_name(self):
        """Gets the app_name of this TransactionConfigItem.

        应用名称。

        :return: The app_name of this TransactionConfigItem.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this TransactionConfigItem.

        应用名称。

        :param app_name: The app_name of this TransactionConfigItem.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def url(self):
        """Gets the url of this TransactionConfigItem.

        url地址。

        :return: The url of this TransactionConfigItem.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this TransactionConfigItem.

        url地址。

        :param url: The url of this TransactionConfigItem.
        :type url: str
        """
        self._url = url

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
        if not isinstance(other, TransactionConfigItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
