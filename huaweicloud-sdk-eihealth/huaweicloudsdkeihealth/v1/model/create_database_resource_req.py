# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDatabaseResourceReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'spec_code': 'str',
        'disk_space': 'int',
        'disk_encrypt': 'bool'
    }

    attribute_map = {
        'spec_code': 'spec_code',
        'disk_space': 'disk_space',
        'disk_encrypt': 'disk_encrypt'
    }

    def __init__(self, spec_code=None, disk_space=None, disk_encrypt=None):
        """CreateDatabaseResourceReq

        The model defined in huaweicloud sdk

        :param spec_code: 规格编码
        :type spec_code: str
        :param disk_space: 磁盘存储空间，该字段暂不生效
        :type disk_space: int
        :param disk_encrypt: 磁盘是否加密
        :type disk_encrypt: bool
        """
        
        

        self._spec_code = None
        self._disk_space = None
        self._disk_encrypt = None
        self.discriminator = None

        self.spec_code = spec_code
        if disk_space is not None:
            self.disk_space = disk_space
        self.disk_encrypt = disk_encrypt

    @property
    def spec_code(self):
        """Gets the spec_code of this CreateDatabaseResourceReq.

        规格编码

        :return: The spec_code of this CreateDatabaseResourceReq.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this CreateDatabaseResourceReq.

        规格编码

        :param spec_code: The spec_code of this CreateDatabaseResourceReq.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def disk_space(self):
        """Gets the disk_space of this CreateDatabaseResourceReq.

        磁盘存储空间，该字段暂不生效

        :return: The disk_space of this CreateDatabaseResourceReq.
        :rtype: int
        """
        return self._disk_space

    @disk_space.setter
    def disk_space(self, disk_space):
        """Sets the disk_space of this CreateDatabaseResourceReq.

        磁盘存储空间，该字段暂不生效

        :param disk_space: The disk_space of this CreateDatabaseResourceReq.
        :type disk_space: int
        """
        self._disk_space = disk_space

    @property
    def disk_encrypt(self):
        """Gets the disk_encrypt of this CreateDatabaseResourceReq.

        磁盘是否加密

        :return: The disk_encrypt of this CreateDatabaseResourceReq.
        :rtype: bool
        """
        return self._disk_encrypt

    @disk_encrypt.setter
    def disk_encrypt(self, disk_encrypt):
        """Sets the disk_encrypt of this CreateDatabaseResourceReq.

        磁盘是否加密

        :param disk_encrypt: The disk_encrypt of this CreateDatabaseResourceReq.
        :type disk_encrypt: bool
        """
        self._disk_encrypt = disk_encrypt

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
        if not isinstance(other, CreateDatabaseResourceReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
