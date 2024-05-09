# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDatabaseReq2:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'css_id': 'str',
        'file': 'DatabaseFile',
        'columns': 'list[str]',
        'shareable': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'css_id': 'css_id',
        'file': 'file',
        'columns': 'columns',
        'shareable': 'shareable'
    }

    def __init__(self, name=None, description=None, css_id=None, file=None, columns=None, shareable=None):
        """CreateDatabaseReq2

        The model defined in huaweicloud sdk

        :param name: 数据库名称，长度为5-32个字符，首位需以小写英文字母开头，仅可以使用小写字母、数字、下划线“_”和中划线“-”
        :type name: str
        :param description: 数据库描述
        :type description: str
        :param css_id: css集群id
        :type css_id: str
        :param file: 
        :type file: :class:`huaweicloudsdkeihealth.v1.DatabaseFile`
        :param columns: 数据文件列名
        :type columns: list[str]
        :param shareable: 是否打开组织共享
        :type shareable: bool
        """
        
        

        self._name = None
        self._description = None
        self._css_id = None
        self._file = None
        self._columns = None
        self._shareable = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.css_id = css_id
        self.file = file
        self.columns = columns
        if shareable is not None:
            self.shareable = shareable

    @property
    def name(self):
        """Gets the name of this CreateDatabaseReq2.

        数据库名称，长度为5-32个字符，首位需以小写英文字母开头，仅可以使用小写字母、数字、下划线“_”和中划线“-”

        :return: The name of this CreateDatabaseReq2.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateDatabaseReq2.

        数据库名称，长度为5-32个字符，首位需以小写英文字母开头，仅可以使用小写字母、数字、下划线“_”和中划线“-”

        :param name: The name of this CreateDatabaseReq2.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateDatabaseReq2.

        数据库描述

        :return: The description of this CreateDatabaseReq2.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateDatabaseReq2.

        数据库描述

        :param description: The description of this CreateDatabaseReq2.
        :type description: str
        """
        self._description = description

    @property
    def css_id(self):
        """Gets the css_id of this CreateDatabaseReq2.

        css集群id

        :return: The css_id of this CreateDatabaseReq2.
        :rtype: str
        """
        return self._css_id

    @css_id.setter
    def css_id(self, css_id):
        """Sets the css_id of this CreateDatabaseReq2.

        css集群id

        :param css_id: The css_id of this CreateDatabaseReq2.
        :type css_id: str
        """
        self._css_id = css_id

    @property
    def file(self):
        """Gets the file of this CreateDatabaseReq2.

        :return: The file of this CreateDatabaseReq2.
        :rtype: :class:`huaweicloudsdkeihealth.v1.DatabaseFile`
        """
        return self._file

    @file.setter
    def file(self, file):
        """Sets the file of this CreateDatabaseReq2.

        :param file: The file of this CreateDatabaseReq2.
        :type file: :class:`huaweicloudsdkeihealth.v1.DatabaseFile`
        """
        self._file = file

    @property
    def columns(self):
        """Gets the columns of this CreateDatabaseReq2.

        数据文件列名

        :return: The columns of this CreateDatabaseReq2.
        :rtype: list[str]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this CreateDatabaseReq2.

        数据文件列名

        :param columns: The columns of this CreateDatabaseReq2.
        :type columns: list[str]
        """
        self._columns = columns

    @property
    def shareable(self):
        """Gets the shareable of this CreateDatabaseReq2.

        是否打开组织共享

        :return: The shareable of this CreateDatabaseReq2.
        :rtype: bool
        """
        return self._shareable

    @shareable.setter
    def shareable(self, shareable):
        """Sets the shareable of this CreateDatabaseReq2.

        是否打开组织共享

        :param shareable: The shareable of this CreateDatabaseReq2.
        :type shareable: bool
        """
        self._shareable = shareable

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
        if not isinstance(other, CreateDatabaseReq2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
