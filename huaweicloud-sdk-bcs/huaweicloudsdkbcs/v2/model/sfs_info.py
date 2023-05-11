# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SfsInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pvc_name': 'str',
        'name': 'str',
        'addr': 'str',
        'type': 'str'
    }

    attribute_map = {
        'pvc_name': 'pvc_name',
        'name': 'name',
        'addr': 'addr',
        'type': 'type'
    }

    def __init__(self, pvc_name=None, name=None, addr=None, type=None):
        """SfsInfo

        The model defined in huaweicloud sdk

        :param pvc_name: BCS服务下的SFS文件系统名称
        :type pvc_name: str
        :param name: BCS服务网络存储名称
        :type name: str
        :param addr: BCS服务网络存储地址
        :type addr: str
        :param type: BCS服务网络存储类型
        :type type: str
        """
        
        

        self._pvc_name = None
        self._name = None
        self._addr = None
        self._type = None
        self.discriminator = None

        if pvc_name is not None:
            self.pvc_name = pvc_name
        if name is not None:
            self.name = name
        if addr is not None:
            self.addr = addr
        if type is not None:
            self.type = type

    @property
    def pvc_name(self):
        """Gets the pvc_name of this SfsInfo.

        BCS服务下的SFS文件系统名称

        :return: The pvc_name of this SfsInfo.
        :rtype: str
        """
        return self._pvc_name

    @pvc_name.setter
    def pvc_name(self, pvc_name):
        """Sets the pvc_name of this SfsInfo.

        BCS服务下的SFS文件系统名称

        :param pvc_name: The pvc_name of this SfsInfo.
        :type pvc_name: str
        """
        self._pvc_name = pvc_name

    @property
    def name(self):
        """Gets the name of this SfsInfo.

        BCS服务网络存储名称

        :return: The name of this SfsInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SfsInfo.

        BCS服务网络存储名称

        :param name: The name of this SfsInfo.
        :type name: str
        """
        self._name = name

    @property
    def addr(self):
        """Gets the addr of this SfsInfo.

        BCS服务网络存储地址

        :return: The addr of this SfsInfo.
        :rtype: str
        """
        return self._addr

    @addr.setter
    def addr(self, addr):
        """Sets the addr of this SfsInfo.

        BCS服务网络存储地址

        :param addr: The addr of this SfsInfo.
        :type addr: str
        """
        self._addr = addr

    @property
    def type(self):
        """Gets the type of this SfsInfo.

        BCS服务网络存储类型

        :return: The type of this SfsInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SfsInfo.

        BCS服务网络存储类型

        :param type: The type of this SfsInfo.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, SfsInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
