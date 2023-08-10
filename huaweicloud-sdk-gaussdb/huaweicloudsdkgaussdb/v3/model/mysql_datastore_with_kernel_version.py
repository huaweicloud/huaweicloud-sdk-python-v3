# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MysqlDatastoreWithKernelVersion:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'version': 'str',
        'kernel_version': 'str'
    }

    attribute_map = {
        'type': 'type',
        'version': 'version',
        'kernel_version': 'kernel_version'
    }

    def __init__(self, type=None, version=None, kernel_version=None):
        """MysqlDatastoreWithKernelVersion

        The model defined in huaweicloud sdk

        :param type: 数据库引擎，现在只支持gaussdb-mysql。
        :type type: str
        :param version: 数据库版本。  数据库支持的详细版本信息，可调用查询数据库引擎的版本接口获取。
        :type version: str
        :param kernel_version: 数据库内核版本
        :type kernel_version: str
        """
        
        

        self._type = None
        self._version = None
        self._kernel_version = None
        self.discriminator = None

        self.type = type
        self.version = version
        self.kernel_version = kernel_version

    @property
    def type(self):
        """Gets the type of this MysqlDatastoreWithKernelVersion.

        数据库引擎，现在只支持gaussdb-mysql。

        :return: The type of this MysqlDatastoreWithKernelVersion.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MysqlDatastoreWithKernelVersion.

        数据库引擎，现在只支持gaussdb-mysql。

        :param type: The type of this MysqlDatastoreWithKernelVersion.
        :type type: str
        """
        self._type = type

    @property
    def version(self):
        """Gets the version of this MysqlDatastoreWithKernelVersion.

        数据库版本。  数据库支持的详细版本信息，可调用查询数据库引擎的版本接口获取。

        :return: The version of this MysqlDatastoreWithKernelVersion.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this MysqlDatastoreWithKernelVersion.

        数据库版本。  数据库支持的详细版本信息，可调用查询数据库引擎的版本接口获取。

        :param version: The version of this MysqlDatastoreWithKernelVersion.
        :type version: str
        """
        self._version = version

    @property
    def kernel_version(self):
        """Gets the kernel_version of this MysqlDatastoreWithKernelVersion.

        数据库内核版本

        :return: The kernel_version of this MysqlDatastoreWithKernelVersion.
        :rtype: str
        """
        return self._kernel_version

    @kernel_version.setter
    def kernel_version(self, kernel_version):
        """Sets the kernel_version of this MysqlDatastoreWithKernelVersion.

        数据库内核版本

        :param kernel_version: The kernel_version of this MysqlDatastoreWithKernelVersion.
        :type kernel_version: str
        """
        self._kernel_version = kernel_version

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
        if not isinstance(other, MysqlDatastoreWithKernelVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
