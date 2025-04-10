# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AvailableZone:

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
        'id': 'str',
        'code': 'str',
        'port': 'str',
        'local_name': 'LocalName',
        'specs': 'dict(str, bool)'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'code': 'code',
        'port': 'port',
        'local_name': 'local_name',
        'specs': 'specs'
    }

    def __init__(self, name=None, id=None, code=None, port=None, local_name=None, specs=None):
        r"""AvailableZone

        The model defined in huaweicloud sdk

        :param name: 可用区名称。
        :type name: str
        :param id: 实例创建失败错误信息
        :type id: str
        :param code: 可用区编码。
        :type code: str
        :param port: 可用区端口号。
        :type port: str
        :param local_name: 
        :type local_name: :class:`huaweicloudsdkapig.v2.LocalName`
        :param specs: 可用区支持的实例规格。
        :type specs: dict(str, bool)
        """
        
        

        self._name = None
        self._id = None
        self._code = None
        self._port = None
        self._local_name = None
        self._specs = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if code is not None:
            self.code = code
        if port is not None:
            self.port = port
        if local_name is not None:
            self.local_name = local_name
        if specs is not None:
            self.specs = specs

    @property
    def name(self):
        r"""Gets the name of this AvailableZone.

        可用区名称。

        :return: The name of this AvailableZone.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AvailableZone.

        可用区名称。

        :param name: The name of this AvailableZone.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this AvailableZone.

        实例创建失败错误信息

        :return: The id of this AvailableZone.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AvailableZone.

        实例创建失败错误信息

        :param id: The id of this AvailableZone.
        :type id: str
        """
        self._id = id

    @property
    def code(self):
        r"""Gets the code of this AvailableZone.

        可用区编码。

        :return: The code of this AvailableZone.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        r"""Sets the code of this AvailableZone.

        可用区编码。

        :param code: The code of this AvailableZone.
        :type code: str
        """
        self._code = code

    @property
    def port(self):
        r"""Gets the port of this AvailableZone.

        可用区端口号。

        :return: The port of this AvailableZone.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this AvailableZone.

        可用区端口号。

        :param port: The port of this AvailableZone.
        :type port: str
        """
        self._port = port

    @property
    def local_name(self):
        r"""Gets the local_name of this AvailableZone.

        :return: The local_name of this AvailableZone.
        :rtype: :class:`huaweicloudsdkapig.v2.LocalName`
        """
        return self._local_name

    @local_name.setter
    def local_name(self, local_name):
        r"""Sets the local_name of this AvailableZone.

        :param local_name: The local_name of this AvailableZone.
        :type local_name: :class:`huaweicloudsdkapig.v2.LocalName`
        """
        self._local_name = local_name

    @property
    def specs(self):
        r"""Gets the specs of this AvailableZone.

        可用区支持的实例规格。

        :return: The specs of this AvailableZone.
        :rtype: dict(str, bool)
        """
        return self._specs

    @specs.setter
    def specs(self, specs):
        r"""Sets the specs of this AvailableZone.

        可用区支持的实例规格。

        :param specs: The specs of this AvailableZone.
        :type specs: dict(str, bool)
        """
        self._specs = specs

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
        if not isinstance(other, AvailableZone):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
