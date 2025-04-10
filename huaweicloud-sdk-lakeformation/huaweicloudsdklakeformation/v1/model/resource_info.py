# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'catalogs': 'list[CatalogInfo]',
        'uris': 'list[str]',
        'type': 'str'
    }

    attribute_map = {
        'catalogs': 'catalogs',
        'uris': 'uris',
        'type': 'type'
    }

    def __init__(self, catalogs=None, uris=None, type=None):
        r"""ResourceInfo

        The model defined in huaweicloud sdk

        :param catalogs: catalog info
        :type catalogs: list[:class:`huaweicloudsdklakeformation.v1.CatalogInfo`]
        :param uris: uri
        :type uris: list[str]
        :param type: resource type
        :type type: str
        """
        
        

        self._catalogs = None
        self._uris = None
        self._type = None
        self.discriminator = None

        if catalogs is not None:
            self.catalogs = catalogs
        if uris is not None:
            self.uris = uris
        self.type = type

    @property
    def catalogs(self):
        r"""Gets the catalogs of this ResourceInfo.

        catalog info

        :return: The catalogs of this ResourceInfo.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.CatalogInfo`]
        """
        return self._catalogs

    @catalogs.setter
    def catalogs(self, catalogs):
        r"""Sets the catalogs of this ResourceInfo.

        catalog info

        :param catalogs: The catalogs of this ResourceInfo.
        :type catalogs: list[:class:`huaweicloudsdklakeformation.v1.CatalogInfo`]
        """
        self._catalogs = catalogs

    @property
    def uris(self):
        r"""Gets the uris of this ResourceInfo.

        uri

        :return: The uris of this ResourceInfo.
        :rtype: list[str]
        """
        return self._uris

    @uris.setter
    def uris(self, uris):
        r"""Sets the uris of this ResourceInfo.

        uri

        :param uris: The uris of this ResourceInfo.
        :type uris: list[str]
        """
        self._uris = uris

    @property
    def type(self):
        r"""Gets the type of this ResourceInfo.

        resource type

        :return: The type of this ResourceInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ResourceInfo.

        resource type

        :param type: The type of this ResourceInfo.
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
        if not isinstance(other, ResourceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
