# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCloudPhoneSingleServerRequestBodyPublicIp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ids': 'list[str]',
        'type': 'str',
        'count': 'int',
        'band_width': 'CreateCloudPhoneSingleServerRequestBodyPublicIpBandWidth'
    }

    attribute_map = {
        'ids': 'ids',
        'type': 'type',
        'count': 'count',
        'band_width': 'band_width'
    }

    def __init__(self, ids=None, type=None, count=None, band_width=None):
        r"""CreateCloudPhoneSingleServerRequestBodyPublicIp

        The model defined in huaweicloud sdk

        :param ids: 指定已有的EIP进行云手机裸服务器创建，当前只支持传入一个已有的EIP ID。指定EIP后public_ip结构体中count字段和type字段不生效。
        :type ids: list[str]
        :param type: 弹性公网IP的类型。 例如： 5_telcom：电信 5_union：联通 5_bgp：全动态BGP 5_sbgp：静态BGP
        :type type: str
        :param count: Eip数量。默认为0。取值范围为【0,1】
        :type count: int
        :param band_width: 
        :type band_width: :class:`huaweicloudsdkcph.v1.CreateCloudPhoneSingleServerRequestBodyPublicIpBandWidth`
        """
        
        

        self._ids = None
        self._type = None
        self._count = None
        self._band_width = None
        self.discriminator = None

        if ids is not None:
            self.ids = ids
        if type is not None:
            self.type = type
        if count is not None:
            self.count = count
        self.band_width = band_width

    @property
    def ids(self):
        r"""Gets the ids of this CreateCloudPhoneSingleServerRequestBodyPublicIp.

        指定已有的EIP进行云手机裸服务器创建，当前只支持传入一个已有的EIP ID。指定EIP后public_ip结构体中count字段和type字段不生效。

        :return: The ids of this CreateCloudPhoneSingleServerRequestBodyPublicIp.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this CreateCloudPhoneSingleServerRequestBodyPublicIp.

        指定已有的EIP进行云手机裸服务器创建，当前只支持传入一个已有的EIP ID。指定EIP后public_ip结构体中count字段和type字段不生效。

        :param ids: The ids of this CreateCloudPhoneSingleServerRequestBodyPublicIp.
        :type ids: list[str]
        """
        self._ids = ids

    @property
    def type(self):
        r"""Gets the type of this CreateCloudPhoneSingleServerRequestBodyPublicIp.

        弹性公网IP的类型。 例如： 5_telcom：电信 5_union：联通 5_bgp：全动态BGP 5_sbgp：静态BGP

        :return: The type of this CreateCloudPhoneSingleServerRequestBodyPublicIp.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CreateCloudPhoneSingleServerRequestBodyPublicIp.

        弹性公网IP的类型。 例如： 5_telcom：电信 5_union：联通 5_bgp：全动态BGP 5_sbgp：静态BGP

        :param type: The type of this CreateCloudPhoneSingleServerRequestBodyPublicIp.
        :type type: str
        """
        self._type = type

    @property
    def count(self):
        r"""Gets the count of this CreateCloudPhoneSingleServerRequestBodyPublicIp.

        Eip数量。默认为0。取值范围为【0,1】

        :return: The count of this CreateCloudPhoneSingleServerRequestBodyPublicIp.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this CreateCloudPhoneSingleServerRequestBodyPublicIp.

        Eip数量。默认为0。取值范围为【0,1】

        :param count: The count of this CreateCloudPhoneSingleServerRequestBodyPublicIp.
        :type count: int
        """
        self._count = count

    @property
    def band_width(self):
        r"""Gets the band_width of this CreateCloudPhoneSingleServerRequestBodyPublicIp.

        :return: The band_width of this CreateCloudPhoneSingleServerRequestBodyPublicIp.
        :rtype: :class:`huaweicloudsdkcph.v1.CreateCloudPhoneSingleServerRequestBodyPublicIpBandWidth`
        """
        return self._band_width

    @band_width.setter
    def band_width(self, band_width):
        r"""Sets the band_width of this CreateCloudPhoneSingleServerRequestBodyPublicIp.

        :param band_width: The band_width of this CreateCloudPhoneSingleServerRequestBodyPublicIp.
        :type band_width: :class:`huaweicloudsdkcph.v1.CreateCloudPhoneSingleServerRequestBodyPublicIpBandWidth`
        """
        self._band_width = band_width

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
        if not isinstance(other, CreateCloudPhoneSingleServerRequestBodyPublicIp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
