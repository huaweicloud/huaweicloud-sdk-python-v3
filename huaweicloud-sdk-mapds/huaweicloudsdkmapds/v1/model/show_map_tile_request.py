# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMapTileRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'z': 'int',
        'x': 'int',
        'y': 'int',
        'authorization': 'str'
    }

    attribute_map = {
        'z': 'z',
        'x': 'x',
        'y': 'y',
        'authorization': 'Authorization'
    }

    def __init__(self, z=None, x=None, y=None, authorization=None):
        r"""ShowMapTileRequest

        The model defined in huaweicloud sdk

        :param z: 缩放级别，取值范围[0~20]。
        :type z: int
        :param x: 缩放网格上的 X 坐标。 值必须在 [0, 2的z次方-1] 范围内。
        :type x: int
        :param y: 缩放网格上的 Y 坐标。 值必须在 [0, 2的z次方-1] 范围内。
        :type y: int
        :param authorization: 签名消息头为：  Authorization: HMAC-SHA256 Clientid&#x3D;xxxx,Expiry&#x3D;xxxx,Signature&#x3D;xxxx  HMAC-SHA256为固定签名算法，Clientid、Expiry、Signature的值从获取获取SAS token请求返回的消息体中获取，要求Clientid，Expiry，Signature同时存在。
        :type authorization: str
        """
        
        

        self._z = None
        self._x = None
        self._y = None
        self._authorization = None
        self.discriminator = None

        self.z = z
        self.x = x
        self.y = y
        self.authorization = authorization

    @property
    def z(self):
        r"""Gets the z of this ShowMapTileRequest.

        缩放级别，取值范围[0~20]。

        :return: The z of this ShowMapTileRequest.
        :rtype: int
        """
        return self._z

    @z.setter
    def z(self, z):
        r"""Sets the z of this ShowMapTileRequest.

        缩放级别，取值范围[0~20]。

        :param z: The z of this ShowMapTileRequest.
        :type z: int
        """
        self._z = z

    @property
    def x(self):
        r"""Gets the x of this ShowMapTileRequest.

        缩放网格上的 X 坐标。 值必须在 [0, 2的z次方-1] 范围内。

        :return: The x of this ShowMapTileRequest.
        :rtype: int
        """
        return self._x

    @x.setter
    def x(self, x):
        r"""Sets the x of this ShowMapTileRequest.

        缩放网格上的 X 坐标。 值必须在 [0, 2的z次方-1] 范围内。

        :param x: The x of this ShowMapTileRequest.
        :type x: int
        """
        self._x = x

    @property
    def y(self):
        r"""Gets the y of this ShowMapTileRequest.

        缩放网格上的 Y 坐标。 值必须在 [0, 2的z次方-1] 范围内。

        :return: The y of this ShowMapTileRequest.
        :rtype: int
        """
        return self._y

    @y.setter
    def y(self, y):
        r"""Sets the y of this ShowMapTileRequest.

        缩放网格上的 Y 坐标。 值必须在 [0, 2的z次方-1] 范围内。

        :param y: The y of this ShowMapTileRequest.
        :type y: int
        """
        self._y = y

    @property
    def authorization(self):
        r"""Gets the authorization of this ShowMapTileRequest.

        签名消息头为：  Authorization: HMAC-SHA256 Clientid=xxxx,Expiry=xxxx,Signature=xxxx  HMAC-SHA256为固定签名算法，Clientid、Expiry、Signature的值从获取获取SAS token请求返回的消息体中获取，要求Clientid，Expiry，Signature同时存在。

        :return: The authorization of this ShowMapTileRequest.
        :rtype: str
        """
        return self._authorization

    @authorization.setter
    def authorization(self, authorization):
        r"""Sets the authorization of this ShowMapTileRequest.

        签名消息头为：  Authorization: HMAC-SHA256 Clientid=xxxx,Expiry=xxxx,Signature=xxxx  HMAC-SHA256为固定签名算法，Clientid、Expiry、Signature的值从获取获取SAS token请求返回的消息体中获取，要求Clientid，Expiry，Signature同时存在。

        :param authorization: The authorization of this ShowMapTileRequest.
        :type authorization: str
        """
        self._authorization = authorization

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
        if not isinstance(other, ShowMapTileRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
