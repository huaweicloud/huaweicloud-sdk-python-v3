# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateServerRequestServerCertificate:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'source': 'str'
    }

    attribute_map = {
        'id': 'id',
        'source': 'source'
    }

    def __init__(self, id=None, source=None):
        r"""CreateServerRequestServerCertificate

        The model defined in huaweicloud sdk

        :param id: 服务端证书ID,为CCM服务中的证书ID。服务端证书类型为CCM时，必填
        :type id: str
        :param source: 证书来源
        :type source: str
        """
        
        

        self._id = None
        self._source = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if source is not None:
            self.source = source

    @property
    def id(self):
        r"""Gets the id of this CreateServerRequestServerCertificate.

        服务端证书ID,为CCM服务中的证书ID。服务端证书类型为CCM时，必填

        :return: The id of this CreateServerRequestServerCertificate.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this CreateServerRequestServerCertificate.

        服务端证书ID,为CCM服务中的证书ID。服务端证书类型为CCM时，必填

        :param id: The id of this CreateServerRequestServerCertificate.
        :type id: str
        """
        self._id = id

    @property
    def source(self):
        r"""Gets the source of this CreateServerRequestServerCertificate.

        证书来源

        :return: The source of this CreateServerRequestServerCertificate.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this CreateServerRequestServerCertificate.

        证书来源

        :param source: The source of this CreateServerRequestServerCertificate.
        :type source: str
        """
        self._source = source

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
        if not isinstance(other, CreateServerRequestServerCertificate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
