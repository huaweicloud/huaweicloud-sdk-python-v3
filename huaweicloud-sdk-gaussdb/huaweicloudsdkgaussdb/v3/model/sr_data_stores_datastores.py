# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SrDataStoresDatastores:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'kernel_version': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'kernel_version': 'kernel_version'
    }

    def __init__(self, id=None, name=None, kernel_version=None):
        r"""SrDataStoresDatastores

        The model defined in huaweicloud sdk

        :param id: 数据库版本ID，该字段不会有重复。
        :type id: str
        :param name: 数据库版本号，只返回两位数的大版本号。
        :type name: str
        :param kernel_version: 数据库内核版本号，返回完整的四位版本号。
        :type kernel_version: str
        """
        
        

        self._id = None
        self._name = None
        self._kernel_version = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if kernel_version is not None:
            self.kernel_version = kernel_version

    @property
    def id(self):
        r"""Gets the id of this SrDataStoresDatastores.

        数据库版本ID，该字段不会有重复。

        :return: The id of this SrDataStoresDatastores.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SrDataStoresDatastores.

        数据库版本ID，该字段不会有重复。

        :param id: The id of this SrDataStoresDatastores.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this SrDataStoresDatastores.

        数据库版本号，只返回两位数的大版本号。

        :return: The name of this SrDataStoresDatastores.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SrDataStoresDatastores.

        数据库版本号，只返回两位数的大版本号。

        :param name: The name of this SrDataStoresDatastores.
        :type name: str
        """
        self._name = name

    @property
    def kernel_version(self):
        r"""Gets the kernel_version of this SrDataStoresDatastores.

        数据库内核版本号，返回完整的四位版本号。

        :return: The kernel_version of this SrDataStoresDatastores.
        :rtype: str
        """
        return self._kernel_version

    @kernel_version.setter
    def kernel_version(self, kernel_version):
        r"""Sets the kernel_version of this SrDataStoresDatastores.

        数据库内核版本号，返回完整的四位版本号。

        :param kernel_version: The kernel_version of this SrDataStoresDatastores.
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
        if not isinstance(other, SrDataStoresDatastores):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
