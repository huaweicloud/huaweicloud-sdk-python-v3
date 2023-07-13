# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodeSpecDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'code': 'str',
        'name': 'str',
        'ram': 'int',
        'vcpus': 'str'
    }

    attribute_map = {
        'code': 'code',
        'name': 'name',
        'ram': 'ram',
        'vcpus': 'vcpus'
    }

    def __init__(self, code=None, name=None, ram=None, vcpus=None):
        """NodeSpecDto

        The model defined in huaweicloud sdk

        :param code: 规格编号
        :type code: str
        :param name: 规格名称
        :type name: str
        :param ram: 内存
        :type ram: int
        :param vcpus: vcpus
        :type vcpus: str
        """
        
        

        self._code = None
        self._name = None
        self._ram = None
        self._vcpus = None
        self.discriminator = None

        if code is not None:
            self.code = code
        if name is not None:
            self.name = name
        if ram is not None:
            self.ram = ram
        if vcpus is not None:
            self.vcpus = vcpus

    @property
    def code(self):
        """Gets the code of this NodeSpecDto.

        规格编号

        :return: The code of this NodeSpecDto.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this NodeSpecDto.

        规格编号

        :param code: The code of this NodeSpecDto.
        :type code: str
        """
        self._code = code

    @property
    def name(self):
        """Gets the name of this NodeSpecDto.

        规格名称

        :return: The name of this NodeSpecDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NodeSpecDto.

        规格名称

        :param name: The name of this NodeSpecDto.
        :type name: str
        """
        self._name = name

    @property
    def ram(self):
        """Gets the ram of this NodeSpecDto.

        内存

        :return: The ram of this NodeSpecDto.
        :rtype: int
        """
        return self._ram

    @ram.setter
    def ram(self, ram):
        """Sets the ram of this NodeSpecDto.

        内存

        :param ram: The ram of this NodeSpecDto.
        :type ram: int
        """
        self._ram = ram

    @property
    def vcpus(self):
        """Gets the vcpus of this NodeSpecDto.

        vcpus

        :return: The vcpus of this NodeSpecDto.
        :rtype: str
        """
        return self._vcpus

    @vcpus.setter
    def vcpus(self, vcpus):
        """Sets the vcpus of this NodeSpecDto.

        vcpus

        :param vcpus: The vcpus of this NodeSpecDto.
        :type vcpus: str
        """
        self._vcpus = vcpus

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
        if not isinstance(other, NodeSpecDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
