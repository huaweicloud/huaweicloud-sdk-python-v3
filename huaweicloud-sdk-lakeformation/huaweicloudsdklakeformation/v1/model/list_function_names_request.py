# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFunctionNamesRequest:

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
        'catalog_name': 'str',
        'database_name': 'str',
        'function_pattern': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'catalog_name': 'catalog_name',
        'database_name': 'database_name',
        'function_pattern': 'function_pattern'
    }

    def __init__(self, instance_id=None, catalog_name=None, database_name=None, function_pattern=None):
        r"""ListFunctionNamesRequest

        The model defined in huaweicloud sdk

        :param instance_id: LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。
        :type instance_id: str
        :param catalog_name: catalog名称。只能包含字母、数字和下划线，且长度为1~256个字符。
        :type catalog_name: str
        :param database_name: 数据库名称。只能包含中文、字母、数字和下划线，且长度为1~128个字符。
        :type database_name: str
        :param function_pattern: 函数名称通配符。只能包含字母、数字和_|*.特殊字符，且最大长度为256个字符。
        :type function_pattern: str
        """
        
        

        self._instance_id = None
        self._catalog_name = None
        self._database_name = None
        self._function_pattern = None
        self.discriminator = None

        self.instance_id = instance_id
        self.catalog_name = catalog_name
        self.database_name = database_name
        if function_pattern is not None:
            self.function_pattern = function_pattern

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListFunctionNamesRequest.

        LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。

        :return: The instance_id of this ListFunctionNamesRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListFunctionNamesRequest.

        LakeFormation实例ID。创建实例时自动生成。例如：2180518f-42b8-4947-b20b-adfc53981a25。

        :param instance_id: The instance_id of this ListFunctionNamesRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def catalog_name(self):
        r"""Gets the catalog_name of this ListFunctionNamesRequest.

        catalog名称。只能包含字母、数字和下划线，且长度为1~256个字符。

        :return: The catalog_name of this ListFunctionNamesRequest.
        :rtype: str
        """
        return self._catalog_name

    @catalog_name.setter
    def catalog_name(self, catalog_name):
        r"""Sets the catalog_name of this ListFunctionNamesRequest.

        catalog名称。只能包含字母、数字和下划线，且长度为1~256个字符。

        :param catalog_name: The catalog_name of this ListFunctionNamesRequest.
        :type catalog_name: str
        """
        self._catalog_name = catalog_name

    @property
    def database_name(self):
        r"""Gets the database_name of this ListFunctionNamesRequest.

        数据库名称。只能包含中文、字母、数字和下划线，且长度为1~128个字符。

        :return: The database_name of this ListFunctionNamesRequest.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        r"""Sets the database_name of this ListFunctionNamesRequest.

        数据库名称。只能包含中文、字母、数字和下划线，且长度为1~128个字符。

        :param database_name: The database_name of this ListFunctionNamesRequest.
        :type database_name: str
        """
        self._database_name = database_name

    @property
    def function_pattern(self):
        r"""Gets the function_pattern of this ListFunctionNamesRequest.

        函数名称通配符。只能包含字母、数字和_|*.特殊字符，且最大长度为256个字符。

        :return: The function_pattern of this ListFunctionNamesRequest.
        :rtype: str
        """
        return self._function_pattern

    @function_pattern.setter
    def function_pattern(self, function_pattern):
        r"""Sets the function_pattern of this ListFunctionNamesRequest.

        函数名称通配符。只能包含字母、数字和_|*.特殊字符，且最大长度为256个字符。

        :param function_pattern: The function_pattern of this ListFunctionNamesRequest.
        :type function_pattern: str
        """
        self._function_pattern = function_pattern

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
        if not isinstance(other, ListFunctionNamesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
