# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateCgwRequestBodyContent:

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
        'id_type': 'str',
        'id_value': 'str',
        'bgp_asn': 'int',
        'ca_certificate': 'CaCertificateRequest',
        'tags': 'list[VpnResourceTag]'
    }

    attribute_map = {
        'name': 'name',
        'id_type': 'id_type',
        'id_value': 'id_value',
        'bgp_asn': 'bgp_asn',
        'ca_certificate': 'ca_certificate',
        'tags': 'tags'
    }

    def __init__(self, name=None, id_type=None, id_value=None, bgp_asn=None, ca_certificate=None, tags=None):
        r"""CreateCgwRequestBodyContent

        The model defined in huaweicloud sdk

        :param name: 网关名称
        :type name: str
        :param id_type: 对端网关标识类型
        :type id_type: str
        :param id_value: 对端网关标识值
        :type id_value: str
        :param bgp_asn: 网关的bgp asn号
        :type bgp_asn: int
        :param ca_certificate: 
        :type ca_certificate: :class:`huaweicloudsdkvpn.v5.CaCertificateRequest`
        :param tags: 标签
        :type tags: list[:class:`huaweicloudsdkvpn.v5.VpnResourceTag`]
        """
        
        

        self._name = None
        self._id_type = None
        self._id_value = None
        self._bgp_asn = None
        self._ca_certificate = None
        self._tags = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id_type is not None:
            self.id_type = id_type
        self.id_value = id_value
        if bgp_asn is not None:
            self.bgp_asn = bgp_asn
        if ca_certificate is not None:
            self.ca_certificate = ca_certificate
        if tags is not None:
            self.tags = tags

    @property
    def name(self):
        r"""Gets the name of this CreateCgwRequestBodyContent.

        网关名称

        :return: The name of this CreateCgwRequestBodyContent.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateCgwRequestBodyContent.

        网关名称

        :param name: The name of this CreateCgwRequestBodyContent.
        :type name: str
        """
        self._name = name

    @property
    def id_type(self):
        r"""Gets the id_type of this CreateCgwRequestBodyContent.

        对端网关标识类型

        :return: The id_type of this CreateCgwRequestBodyContent.
        :rtype: str
        """
        return self._id_type

    @id_type.setter
    def id_type(self, id_type):
        r"""Sets the id_type of this CreateCgwRequestBodyContent.

        对端网关标识类型

        :param id_type: The id_type of this CreateCgwRequestBodyContent.
        :type id_type: str
        """
        self._id_type = id_type

    @property
    def id_value(self):
        r"""Gets the id_value of this CreateCgwRequestBodyContent.

        对端网关标识值

        :return: The id_value of this CreateCgwRequestBodyContent.
        :rtype: str
        """
        return self._id_value

    @id_value.setter
    def id_value(self, id_value):
        r"""Sets the id_value of this CreateCgwRequestBodyContent.

        对端网关标识值

        :param id_value: The id_value of this CreateCgwRequestBodyContent.
        :type id_value: str
        """
        self._id_value = id_value

    @property
    def bgp_asn(self):
        r"""Gets the bgp_asn of this CreateCgwRequestBodyContent.

        网关的bgp asn号

        :return: The bgp_asn of this CreateCgwRequestBodyContent.
        :rtype: int
        """
        return self._bgp_asn

    @bgp_asn.setter
    def bgp_asn(self, bgp_asn):
        r"""Sets the bgp_asn of this CreateCgwRequestBodyContent.

        网关的bgp asn号

        :param bgp_asn: The bgp_asn of this CreateCgwRequestBodyContent.
        :type bgp_asn: int
        """
        self._bgp_asn = bgp_asn

    @property
    def ca_certificate(self):
        r"""Gets the ca_certificate of this CreateCgwRequestBodyContent.

        :return: The ca_certificate of this CreateCgwRequestBodyContent.
        :rtype: :class:`huaweicloudsdkvpn.v5.CaCertificateRequest`
        """
        return self._ca_certificate

    @ca_certificate.setter
    def ca_certificate(self, ca_certificate):
        r"""Sets the ca_certificate of this CreateCgwRequestBodyContent.

        :param ca_certificate: The ca_certificate of this CreateCgwRequestBodyContent.
        :type ca_certificate: :class:`huaweicloudsdkvpn.v5.CaCertificateRequest`
        """
        self._ca_certificate = ca_certificate

    @property
    def tags(self):
        r"""Gets the tags of this CreateCgwRequestBodyContent.

        标签

        :return: The tags of this CreateCgwRequestBodyContent.
        :rtype: list[:class:`huaweicloudsdkvpn.v5.VpnResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateCgwRequestBodyContent.

        标签

        :param tags: The tags of this CreateCgwRequestBodyContent.
        :type tags: list[:class:`huaweicloudsdkvpn.v5.VpnResourceTag`]
        """
        self._tags = tags

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
        if not isinstance(other, CreateCgwRequestBodyContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
