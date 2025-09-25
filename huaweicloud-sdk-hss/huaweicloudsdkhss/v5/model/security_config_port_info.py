# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SecurityConfigPortInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'port': 'int',
        'type': 'str',
        'status': 'str',
        'port_status': 'int',
        'port_desc': 'str'
    }

    attribute_map = {
        'port': 'port',
        'type': 'type',
        'status': 'status',
        'port_status': 'port_status',
        'port_desc': 'port_desc'
    }

    def __init__(self, port=None, type=None, status=None, port_status=None, port_desc=None):
        r"""SecurityConfigPortInfo

        The model defined in huaweicloud sdk

        :param port: **参数解释**： 端口号 **取值范围**： 0-65535 
        :type port: int
        :param type: **参数解释**： 类型 **取值范围**： 不涉及 
        :type type: str
        :param status: **参数解释**： 端口危险程度 **取值范围**： - normal：正常端口 - danger：危险端口 - unknow：未知端口 
        :type status: str
        :param port_status: **参数解释**： 端口状态 **取值范围**： - 0：未处理 - 1：已忽略 - 2：无需处理 
        :type port_status: int
        :param port_desc: **参数解释**： 端口描述 **取值范围**： 不涉及 
        :type port_desc: str
        """
        
        

        self._port = None
        self._type = None
        self._status = None
        self._port_status = None
        self._port_desc = None
        self.discriminator = None

        if port is not None:
            self.port = port
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if port_status is not None:
            self.port_status = port_status
        if port_desc is not None:
            self.port_desc = port_desc

    @property
    def port(self):
        r"""Gets the port of this SecurityConfigPortInfo.

        **参数解释**： 端口号 **取值范围**： 0-65535 

        :return: The port of this SecurityConfigPortInfo.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this SecurityConfigPortInfo.

        **参数解释**： 端口号 **取值范围**： 0-65535 

        :param port: The port of this SecurityConfigPortInfo.
        :type port: int
        """
        self._port = port

    @property
    def type(self):
        r"""Gets the type of this SecurityConfigPortInfo.

        **参数解释**： 类型 **取值范围**： 不涉及 

        :return: The type of this SecurityConfigPortInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SecurityConfigPortInfo.

        **参数解释**： 类型 **取值范围**： 不涉及 

        :param type: The type of this SecurityConfigPortInfo.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this SecurityConfigPortInfo.

        **参数解释**： 端口危险程度 **取值范围**： - normal：正常端口 - danger：危险端口 - unknow：未知端口 

        :return: The status of this SecurityConfigPortInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SecurityConfigPortInfo.

        **参数解释**： 端口危险程度 **取值范围**： - normal：正常端口 - danger：危险端口 - unknow：未知端口 

        :param status: The status of this SecurityConfigPortInfo.
        :type status: str
        """
        self._status = status

    @property
    def port_status(self):
        r"""Gets the port_status of this SecurityConfigPortInfo.

        **参数解释**： 端口状态 **取值范围**： - 0：未处理 - 1：已忽略 - 2：无需处理 

        :return: The port_status of this SecurityConfigPortInfo.
        :rtype: int
        """
        return self._port_status

    @port_status.setter
    def port_status(self, port_status):
        r"""Sets the port_status of this SecurityConfigPortInfo.

        **参数解释**： 端口状态 **取值范围**： - 0：未处理 - 1：已忽略 - 2：无需处理 

        :param port_status: The port_status of this SecurityConfigPortInfo.
        :type port_status: int
        """
        self._port_status = port_status

    @property
    def port_desc(self):
        r"""Gets the port_desc of this SecurityConfigPortInfo.

        **参数解释**： 端口描述 **取值范围**： 不涉及 

        :return: The port_desc of this SecurityConfigPortInfo.
        :rtype: str
        """
        return self._port_desc

    @port_desc.setter
    def port_desc(self, port_desc):
        r"""Sets the port_desc of this SecurityConfigPortInfo.

        **参数解释**： 端口描述 **取值范围**： 不涉及 

        :param port_desc: The port_desc of this SecurityConfigPortInfo.
        :type port_desc: str
        """
        self._port_desc = port_desc

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
        if not isinstance(other, SecurityConfigPortInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
