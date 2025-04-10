# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LockPortRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pub_id': 'str',
        'port': 'str',
        'province': 'str',
        'sign': 'list[str]',
        'ext_port_id': 'str'
    }

    attribute_map = {
        'pub_id': 'pub_id',
        'port': 'port',
        'province': 'province',
        'sign': 'sign',
        'ext_port_id': 'ext_port_id'
    }

    def __init__(self, pub_id=None, port=None, province=None, sign=None, ext_port_id=None):
        r"""LockPortRequestBody

        The model defined in huaweicloud sdk

        :param pub_id: 服务号ID。
        :type pub_id: str
        :param port: 通道号。 - port_type&#x3D;5时，长度必须为5 - port_type&#x3D;1或3，长度在21位内 
        :type port: str
        :param province: 绑定的地区，不允许传入重叠地区。地区取值见《地区名称列表》。
        :type province: str
        :param sign: 绑定签名，必须是该端口号签名的子集。单个签名长度为2-18。
        :type sign: list[str]
        :param ext_port_id: 关联通道号ID，取通道号列表返回的ID。
        :type ext_port_id: str
        """
        
        

        self._pub_id = None
        self._port = None
        self._province = None
        self._sign = None
        self._ext_port_id = None
        self.discriminator = None

        self.pub_id = pub_id
        self.port = port
        self.province = province
        self.sign = sign
        self.ext_port_id = ext_port_id

    @property
    def pub_id(self):
        r"""Gets the pub_id of this LockPortRequestBody.

        服务号ID。

        :return: The pub_id of this LockPortRequestBody.
        :rtype: str
        """
        return self._pub_id

    @pub_id.setter
    def pub_id(self, pub_id):
        r"""Sets the pub_id of this LockPortRequestBody.

        服务号ID。

        :param pub_id: The pub_id of this LockPortRequestBody.
        :type pub_id: str
        """
        self._pub_id = pub_id

    @property
    def port(self):
        r"""Gets the port of this LockPortRequestBody.

        通道号。 - port_type=5时，长度必须为5 - port_type=1或3，长度在21位内 

        :return: The port of this LockPortRequestBody.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        r"""Sets the port of this LockPortRequestBody.

        通道号。 - port_type=5时，长度必须为5 - port_type=1或3，长度在21位内 

        :param port: The port of this LockPortRequestBody.
        :type port: str
        """
        self._port = port

    @property
    def province(self):
        r"""Gets the province of this LockPortRequestBody.

        绑定的地区，不允许传入重叠地区。地区取值见《地区名称列表》。

        :return: The province of this LockPortRequestBody.
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        r"""Sets the province of this LockPortRequestBody.

        绑定的地区，不允许传入重叠地区。地区取值见《地区名称列表》。

        :param province: The province of this LockPortRequestBody.
        :type province: str
        """
        self._province = province

    @property
    def sign(self):
        r"""Gets the sign of this LockPortRequestBody.

        绑定签名，必须是该端口号签名的子集。单个签名长度为2-18。

        :return: The sign of this LockPortRequestBody.
        :rtype: list[str]
        """
        return self._sign

    @sign.setter
    def sign(self, sign):
        r"""Sets the sign of this LockPortRequestBody.

        绑定签名，必须是该端口号签名的子集。单个签名长度为2-18。

        :param sign: The sign of this LockPortRequestBody.
        :type sign: list[str]
        """
        self._sign = sign

    @property
    def ext_port_id(self):
        r"""Gets the ext_port_id of this LockPortRequestBody.

        关联通道号ID，取通道号列表返回的ID。

        :return: The ext_port_id of this LockPortRequestBody.
        :rtype: str
        """
        return self._ext_port_id

    @ext_port_id.setter
    def ext_port_id(self, ext_port_id):
        r"""Sets the ext_port_id of this LockPortRequestBody.

        关联通道号ID，取通道号列表返回的ID。

        :param ext_port_id: The ext_port_id of this LockPortRequestBody.
        :type ext_port_id: str
        """
        self._ext_port_id = ext_port_id

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
        if not isinstance(other, LockPortRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
