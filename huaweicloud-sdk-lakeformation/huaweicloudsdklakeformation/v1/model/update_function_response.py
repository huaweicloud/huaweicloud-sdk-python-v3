# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateFunctionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'catalog_name': 'str',
        'database_name': 'str',
        'function_name': 'str',
        'function_type': 'str',
        'owner': 'str',
        'owner_type': 'str',
        'class_name': 'str',
        'create_time': 'datetime',
        'resource_uris': 'list[FunctionResourceUri]'
    }

    attribute_map = {
        'catalog_name': 'catalog_name',
        'database_name': 'database_name',
        'function_name': 'function_name',
        'function_type': 'function_type',
        'owner': 'owner',
        'owner_type': 'owner_type',
        'class_name': 'class_name',
        'create_time': 'create_time',
        'resource_uris': 'resource_uris'
    }

    def __init__(self, catalog_name=None, database_name=None, function_name=None, function_type=None, owner=None, owner_type=None, class_name=None, create_time=None, resource_uris=None):
        """UpdateFunctionResponse

        The model defined in huaweicloud sdk

        :param catalog_name: catalog名字
        :type catalog_name: str
        :param database_name: 数据库名字
        :type database_name: str
        :param function_name: 函数名
        :type function_name: str
        :param function_type: 函数类型
        :type function_type: str
        :param owner: 函数所有者
        :type owner: str
        :param owner_type: 所有者类型
        :type owner_type: str
        :param class_name: 函数类名
        :type class_name: str
        :param create_time: 创建时间格式为yyyy-mm-ddThh:mm:sss
        :type create_time: datetime
        :param resource_uris: 函数地址信息
        :type resource_uris: list[:class:`huaweicloudsdklakeformation.v1.FunctionResourceUri`]
        """
        
        super(UpdateFunctionResponse, self).__init__()

        self._catalog_name = None
        self._database_name = None
        self._function_name = None
        self._function_type = None
        self._owner = None
        self._owner_type = None
        self._class_name = None
        self._create_time = None
        self._resource_uris = None
        self.discriminator = None

        if catalog_name is not None:
            self.catalog_name = catalog_name
        if database_name is not None:
            self.database_name = database_name
        if function_name is not None:
            self.function_name = function_name
        if function_type is not None:
            self.function_type = function_type
        if owner is not None:
            self.owner = owner
        if owner_type is not None:
            self.owner_type = owner_type
        if class_name is not None:
            self.class_name = class_name
        if create_time is not None:
            self.create_time = create_time
        if resource_uris is not None:
            self.resource_uris = resource_uris

    @property
    def catalog_name(self):
        """Gets the catalog_name of this UpdateFunctionResponse.

        catalog名字

        :return: The catalog_name of this UpdateFunctionResponse.
        :rtype: str
        """
        return self._catalog_name

    @catalog_name.setter
    def catalog_name(self, catalog_name):
        """Sets the catalog_name of this UpdateFunctionResponse.

        catalog名字

        :param catalog_name: The catalog_name of this UpdateFunctionResponse.
        :type catalog_name: str
        """
        self._catalog_name = catalog_name

    @property
    def database_name(self):
        """Gets the database_name of this UpdateFunctionResponse.

        数据库名字

        :return: The database_name of this UpdateFunctionResponse.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """Sets the database_name of this UpdateFunctionResponse.

        数据库名字

        :param database_name: The database_name of this UpdateFunctionResponse.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def function_name(self):
        """Gets the function_name of this UpdateFunctionResponse.

        函数名

        :return: The function_name of this UpdateFunctionResponse.
        :rtype: str
        """
        return self._function_name

    @function_name.setter
    def function_name(self, function_name):
        """Sets the function_name of this UpdateFunctionResponse.

        函数名

        :param function_name: The function_name of this UpdateFunctionResponse.
        :type function_name: str
        """
        self._function_name = function_name

    @property
    def function_type(self):
        """Gets the function_type of this UpdateFunctionResponse.

        函数类型

        :return: The function_type of this UpdateFunctionResponse.
        :rtype: str
        """
        return self._function_type

    @function_type.setter
    def function_type(self, function_type):
        """Sets the function_type of this UpdateFunctionResponse.

        函数类型

        :param function_type: The function_type of this UpdateFunctionResponse.
        :type function_type: str
        """
        self._function_type = function_type

    @property
    def owner(self):
        """Gets the owner of this UpdateFunctionResponse.

        函数所有者

        :return: The owner of this UpdateFunctionResponse.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this UpdateFunctionResponse.

        函数所有者

        :param owner: The owner of this UpdateFunctionResponse.
        :type owner: str
        """
        self._owner = owner

    @property
    def owner_type(self):
        """Gets the owner_type of this UpdateFunctionResponse.

        所有者类型

        :return: The owner_type of this UpdateFunctionResponse.
        :rtype: str
        """
        return self._owner_type

    @owner_type.setter
    def owner_type(self, owner_type):
        """Sets the owner_type of this UpdateFunctionResponse.

        所有者类型

        :param owner_type: The owner_type of this UpdateFunctionResponse.
        :type owner_type: str
        """
        self._owner_type = owner_type

    @property
    def class_name(self):
        """Gets the class_name of this UpdateFunctionResponse.

        函数类名

        :return: The class_name of this UpdateFunctionResponse.
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """Sets the class_name of this UpdateFunctionResponse.

        函数类名

        :param class_name: The class_name of this UpdateFunctionResponse.
        :type class_name: str
        """
        self._class_name = class_name

    @property
    def create_time(self):
        """Gets the create_time of this UpdateFunctionResponse.

        创建时间格式为yyyy-mm-ddThh:mm:sss

        :return: The create_time of this UpdateFunctionResponse.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this UpdateFunctionResponse.

        创建时间格式为yyyy-mm-ddThh:mm:sss

        :param create_time: The create_time of this UpdateFunctionResponse.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def resource_uris(self):
        """Gets the resource_uris of this UpdateFunctionResponse.

        函数地址信息

        :return: The resource_uris of this UpdateFunctionResponse.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.FunctionResourceUri`]
        """
        return self._resource_uris

    @resource_uris.setter
    def resource_uris(self, resource_uris):
        """Sets the resource_uris of this UpdateFunctionResponse.

        函数地址信息

        :param resource_uris: The resource_uris of this UpdateFunctionResponse.
        :type resource_uris: list[:class:`huaweicloudsdklakeformation.v1.FunctionResourceUri`]
        """
        self._resource_uris = resource_uris

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
        if not isinstance(other, UpdateFunctionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
