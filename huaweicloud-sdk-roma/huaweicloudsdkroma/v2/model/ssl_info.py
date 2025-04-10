# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SslInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ssl_id': 'str',
        'ssl_name': 'str',
        'algorithm_type': 'str',
        'type': 'str'
    }

    attribute_map = {
        'ssl_id': 'ssl_id',
        'ssl_name': 'ssl_name',
        'algorithm_type': 'algorithm_type',
        'type': 'type'
    }

    def __init__(self, ssl_id=None, ssl_name=None, algorithm_type=None, type=None):
        r"""SslInfo

        The model defined in huaweicloud sdk

        :param ssl_id: SSL证书编号
        :type ssl_id: str
        :param ssl_name: SSL证书名称
        :type ssl_name: str
        :param algorithm_type: 证书算法类型： - RSA - ECC - SM2  [暂不支持](tag:hws;hws_hk;g42;Site)
        :type algorithm_type: str
        :param type: 证书可见范围： - instance：当前实例 - global：全局
        :type type: str
        """
        
        

        self._ssl_id = None
        self._ssl_name = None
        self._algorithm_type = None
        self._type = None
        self.discriminator = None

        if ssl_id is not None:
            self.ssl_id = ssl_id
        if ssl_name is not None:
            self.ssl_name = ssl_name
        if algorithm_type is not None:
            self.algorithm_type = algorithm_type
        if type is not None:
            self.type = type

    @property
    def ssl_id(self):
        r"""Gets the ssl_id of this SslInfo.

        SSL证书编号

        :return: The ssl_id of this SslInfo.
        :rtype: str
        """
        return self._ssl_id

    @ssl_id.setter
    def ssl_id(self, ssl_id):
        r"""Sets the ssl_id of this SslInfo.

        SSL证书编号

        :param ssl_id: The ssl_id of this SslInfo.
        :type ssl_id: str
        """
        self._ssl_id = ssl_id

    @property
    def ssl_name(self):
        r"""Gets the ssl_name of this SslInfo.

        SSL证书名称

        :return: The ssl_name of this SslInfo.
        :rtype: str
        """
        return self._ssl_name

    @ssl_name.setter
    def ssl_name(self, ssl_name):
        r"""Sets the ssl_name of this SslInfo.

        SSL证书名称

        :param ssl_name: The ssl_name of this SslInfo.
        :type ssl_name: str
        """
        self._ssl_name = ssl_name

    @property
    def algorithm_type(self):
        r"""Gets the algorithm_type of this SslInfo.

        证书算法类型： - RSA - ECC - SM2  [暂不支持](tag:hws;hws_hk;g42;Site)

        :return: The algorithm_type of this SslInfo.
        :rtype: str
        """
        return self._algorithm_type

    @algorithm_type.setter
    def algorithm_type(self, algorithm_type):
        r"""Sets the algorithm_type of this SslInfo.

        证书算法类型： - RSA - ECC - SM2  [暂不支持](tag:hws;hws_hk;g42;Site)

        :param algorithm_type: The algorithm_type of this SslInfo.
        :type algorithm_type: str
        """
        self._algorithm_type = algorithm_type

    @property
    def type(self):
        r"""Gets the type of this SslInfo.

        证书可见范围： - instance：当前实例 - global：全局

        :return: The type of this SslInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SslInfo.

        证书可见范围： - instance：当前实例 - global：全局

        :param type: The type of this SslInfo.
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
        if not isinstance(other, SslInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
