# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LdApiScriptBase:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ds_id': 'str',
        'ds_name': 'str',
        'ds_type': 'str',
        'type': 'str',
        'object_name': 'str',
        'content': 'str',
        'enable_result_paging': 'bool',
        'enable_preparestatement': 'bool'
    }

    attribute_map = {
        'ds_id': 'ds_id',
        'ds_name': 'ds_name',
        'ds_type': 'ds_type',
        'type': 'type',
        'object_name': 'object_name',
        'content': 'content',
        'enable_result_paging': 'enable_result_paging',
        'enable_preparestatement': 'enable_preparestatement'
    }

    def __init__(self, ds_id=None, ds_name=None, ds_type=None, type=None, object_name=None, content=None, enable_result_paging=None, enable_preparestatement=None):
        """LdApiScriptBase

        The model defined in huaweicloud sdk

        :param ds_id: 数据源编号，当api_type &#x3D; data时，必选
        :type ds_id: str
        :param ds_name: 数据源名称
        :type ds_name: str
        :param ds_type: 数据源类型：  - oracle：oracle数据源类型  - mysql：mysql数据源类型  - mongodb：mongodb数据源类型  - redis：redis数据源类型  - postgresql：postgresql/opengauss数据源类型  - hive：hive数据源类型  - mssql：sqlserver数据源类型  - sqlserver：sqlserver数据源类型  - dws：dws数据源类型  - gauss100：gauss100数据源类型  - zenith：zenith数据源类型
        :type ds_type: str
        :param type: 脚本类型 - SQL：sql语句 - SP：存储过程 
        :type type: str
        :param object_name: 返回对象。
        :type object_name: str
        :param content: API脚本内容  请对脚本进行base64编码
        :type content: str
        :param enable_result_paging: 数据脚本是否结果分页，当api_type &#x3D; data时有效
        :type enable_result_paging: bool
        :param enable_preparestatement: 数据脚本是否预编译，当api_type &#x3D; data时有效
        :type enable_preparestatement: bool
        """
        
        

        self._ds_id = None
        self._ds_name = None
        self._ds_type = None
        self._type = None
        self._object_name = None
        self._content = None
        self._enable_result_paging = None
        self._enable_preparestatement = None
        self.discriminator = None

        if ds_id is not None:
            self.ds_id = ds_id
        if ds_name is not None:
            self.ds_name = ds_name
        if ds_type is not None:
            self.ds_type = ds_type
        if type is not None:
            self.type = type
        self.object_name = object_name
        self.content = content
        if enable_result_paging is not None:
            self.enable_result_paging = enable_result_paging
        if enable_preparestatement is not None:
            self.enable_preparestatement = enable_preparestatement

    @property
    def ds_id(self):
        """Gets the ds_id of this LdApiScriptBase.

        数据源编号，当api_type = data时，必选

        :return: The ds_id of this LdApiScriptBase.
        :rtype: str
        """
        return self._ds_id

    @ds_id.setter
    def ds_id(self, ds_id):
        """Sets the ds_id of this LdApiScriptBase.

        数据源编号，当api_type = data时，必选

        :param ds_id: The ds_id of this LdApiScriptBase.
        :type ds_id: str
        """
        self._ds_id = ds_id

    @property
    def ds_name(self):
        """Gets the ds_name of this LdApiScriptBase.

        数据源名称

        :return: The ds_name of this LdApiScriptBase.
        :rtype: str
        """
        return self._ds_name

    @ds_name.setter
    def ds_name(self, ds_name):
        """Sets the ds_name of this LdApiScriptBase.

        数据源名称

        :param ds_name: The ds_name of this LdApiScriptBase.
        :type ds_name: str
        """
        self._ds_name = ds_name

    @property
    def ds_type(self):
        """Gets the ds_type of this LdApiScriptBase.

        数据源类型：  - oracle：oracle数据源类型  - mysql：mysql数据源类型  - mongodb：mongodb数据源类型  - redis：redis数据源类型  - postgresql：postgresql/opengauss数据源类型  - hive：hive数据源类型  - mssql：sqlserver数据源类型  - sqlserver：sqlserver数据源类型  - dws：dws数据源类型  - gauss100：gauss100数据源类型  - zenith：zenith数据源类型

        :return: The ds_type of this LdApiScriptBase.
        :rtype: str
        """
        return self._ds_type

    @ds_type.setter
    def ds_type(self, ds_type):
        """Sets the ds_type of this LdApiScriptBase.

        数据源类型：  - oracle：oracle数据源类型  - mysql：mysql数据源类型  - mongodb：mongodb数据源类型  - redis：redis数据源类型  - postgresql：postgresql/opengauss数据源类型  - hive：hive数据源类型  - mssql：sqlserver数据源类型  - sqlserver：sqlserver数据源类型  - dws：dws数据源类型  - gauss100：gauss100数据源类型  - zenith：zenith数据源类型

        :param ds_type: The ds_type of this LdApiScriptBase.
        :type ds_type: str
        """
        self._ds_type = ds_type

    @property
    def type(self):
        """Gets the type of this LdApiScriptBase.

        脚本类型 - SQL：sql语句 - SP：存储过程 

        :return: The type of this LdApiScriptBase.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LdApiScriptBase.

        脚本类型 - SQL：sql语句 - SP：存储过程 

        :param type: The type of this LdApiScriptBase.
        :type type: str
        """
        self._type = type

    @property
    def object_name(self):
        """Gets the object_name of this LdApiScriptBase.

        返回对象。

        :return: The object_name of this LdApiScriptBase.
        :rtype: str
        """
        return self._object_name

    @object_name.setter
    def object_name(self, object_name):
        """Sets the object_name of this LdApiScriptBase.

        返回对象。

        :param object_name: The object_name of this LdApiScriptBase.
        :type object_name: str
        """
        self._object_name = object_name

    @property
    def content(self):
        """Gets the content of this LdApiScriptBase.

        API脚本内容  请对脚本进行base64编码

        :return: The content of this LdApiScriptBase.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this LdApiScriptBase.

        API脚本内容  请对脚本进行base64编码

        :param content: The content of this LdApiScriptBase.
        :type content: str
        """
        self._content = content

    @property
    def enable_result_paging(self):
        """Gets the enable_result_paging of this LdApiScriptBase.

        数据脚本是否结果分页，当api_type = data时有效

        :return: The enable_result_paging of this LdApiScriptBase.
        :rtype: bool
        """
        return self._enable_result_paging

    @enable_result_paging.setter
    def enable_result_paging(self, enable_result_paging):
        """Sets the enable_result_paging of this LdApiScriptBase.

        数据脚本是否结果分页，当api_type = data时有效

        :param enable_result_paging: The enable_result_paging of this LdApiScriptBase.
        :type enable_result_paging: bool
        """
        self._enable_result_paging = enable_result_paging

    @property
    def enable_preparestatement(self):
        """Gets the enable_preparestatement of this LdApiScriptBase.

        数据脚本是否预编译，当api_type = data时有效

        :return: The enable_preparestatement of this LdApiScriptBase.
        :rtype: bool
        """
        return self._enable_preparestatement

    @enable_preparestatement.setter
    def enable_preparestatement(self, enable_preparestatement):
        """Sets the enable_preparestatement of this LdApiScriptBase.

        数据脚本是否预编译，当api_type = data时有效

        :param enable_preparestatement: The enable_preparestatement of this LdApiScriptBase.
        :type enable_preparestatement: bool
        """
        self._enable_preparestatement = enable_preparestatement

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
        if not isinstance(other, LdApiScriptBase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
