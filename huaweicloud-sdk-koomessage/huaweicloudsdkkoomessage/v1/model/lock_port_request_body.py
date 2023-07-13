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
        """LockPortRequestBody

        The model defined in huaweicloud sdk

        :param pub_id: 服务号ID。
        :type pub_id: str
        :param port: 通道号。 - port_type&#x3D;5时，长度必须为5 - port_type&#x3D;1或3，长度在21位内 
        :type port: str
        :param province: 通道号绑定/解绑的province字段取值范围如下： 全国、河北省、山西省、辽宁省、吉林省、黑龙江省、江苏省、浙江省、安徽省、福建省、江西省、山东省、河南省、湖北省、湖南省、广东省、海南省、四川省、贵州省、云南省、陕西省、甘肃省、青海省、台湾省、内蒙古自治区、广西壮族自治区、西藏自治区、宁夏回族自治区、新疆维吾尔自治区、北京市、天津市、上海市、重庆市、香港特别行政区、澳门特别行政区。
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
        """Gets the pub_id of this LockPortRequestBody.

        服务号ID。

        :return: The pub_id of this LockPortRequestBody.
        :rtype: str
        """
        return self._pub_id

    @pub_id.setter
    def pub_id(self, pub_id):
        """Sets the pub_id of this LockPortRequestBody.

        服务号ID。

        :param pub_id: The pub_id of this LockPortRequestBody.
        :type pub_id: str
        """
        self._pub_id = pub_id

    @property
    def port(self):
        """Gets the port of this LockPortRequestBody.

        通道号。 - port_type=5时，长度必须为5 - port_type=1或3，长度在21位内 

        :return: The port of this LockPortRequestBody.
        :rtype: str
        """
        return self._port

    @port.setter
    def port(self, port):
        """Sets the port of this LockPortRequestBody.

        通道号。 - port_type=5时，长度必须为5 - port_type=1或3，长度在21位内 

        :param port: The port of this LockPortRequestBody.
        :type port: str
        """
        self._port = port

    @property
    def province(self):
        """Gets the province of this LockPortRequestBody.

        通道号绑定/解绑的province字段取值范围如下： 全国、河北省、山西省、辽宁省、吉林省、黑龙江省、江苏省、浙江省、安徽省、福建省、江西省、山东省、河南省、湖北省、湖南省、广东省、海南省、四川省、贵州省、云南省、陕西省、甘肃省、青海省、台湾省、内蒙古自治区、广西壮族自治区、西藏自治区、宁夏回族自治区、新疆维吾尔自治区、北京市、天津市、上海市、重庆市、香港特别行政区、澳门特别行政区。

        :return: The province of this LockPortRequestBody.
        :rtype: str
        """
        return self._province

    @province.setter
    def province(self, province):
        """Sets the province of this LockPortRequestBody.

        通道号绑定/解绑的province字段取值范围如下： 全国、河北省、山西省、辽宁省、吉林省、黑龙江省、江苏省、浙江省、安徽省、福建省、江西省、山东省、河南省、湖北省、湖南省、广东省、海南省、四川省、贵州省、云南省、陕西省、甘肃省、青海省、台湾省、内蒙古自治区、广西壮族自治区、西藏自治区、宁夏回族自治区、新疆维吾尔自治区、北京市、天津市、上海市、重庆市、香港特别行政区、澳门特别行政区。

        :param province: The province of this LockPortRequestBody.
        :type province: str
        """
        self._province = province

    @property
    def sign(self):
        """Gets the sign of this LockPortRequestBody.

        绑定签名，必须是该端口号签名的子集。单个签名长度为2-18。

        :return: The sign of this LockPortRequestBody.
        :rtype: list[str]
        """
        return self._sign

    @sign.setter
    def sign(self, sign):
        """Sets the sign of this LockPortRequestBody.

        绑定签名，必须是该端口号签名的子集。单个签名长度为2-18。

        :param sign: The sign of this LockPortRequestBody.
        :type sign: list[str]
        """
        self._sign = sign

    @property
    def ext_port_id(self):
        """Gets the ext_port_id of this LockPortRequestBody.

        关联通道号ID，取通道号列表返回的ID。

        :return: The ext_port_id of this LockPortRequestBody.
        :rtype: str
        """
        return self._ext_port_id

    @ext_port_id.setter
    def ext_port_id(self, ext_port_id):
        """Sets the ext_port_id of this LockPortRequestBody.

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
