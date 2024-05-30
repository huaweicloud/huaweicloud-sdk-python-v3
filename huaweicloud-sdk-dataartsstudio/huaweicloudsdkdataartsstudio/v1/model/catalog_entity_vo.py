# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CatalogEntityVO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type_name': 'str',
        'attributes': 'CatalogAttributeVO'
    }

    attribute_map = {
        'type_name': 'typeName',
        'attributes': 'attributes'
    }

    def __init__(self, type_name=None, attributes=None):
        """CatalogEntityVO

        The model defined in huaweicloud sdk

        :param type_name: 类型名称，填写“BusinessCatalog”即可（业务分层）。
        :type type_name: str
        :param attributes: 
        :type attributes: :class:`huaweicloudsdkdataartsstudio.v1.CatalogAttributeVO`
        """
        
        

        self._type_name = None
        self._attributes = None
        self.discriminator = None

        if type_name is not None:
            self.type_name = type_name
        self.attributes = attributes

    @property
    def type_name(self):
        """Gets the type_name of this CatalogEntityVO.

        类型名称，填写“BusinessCatalog”即可（业务分层）。

        :return: The type_name of this CatalogEntityVO.
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        """Sets the type_name of this CatalogEntityVO.

        类型名称，填写“BusinessCatalog”即可（业务分层）。

        :param type_name: The type_name of this CatalogEntityVO.
        :type type_name: str
        """
        self._type_name = type_name

    @property
    def attributes(self):
        """Gets the attributes of this CatalogEntityVO.

        :return: The attributes of this CatalogEntityVO.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.CatalogAttributeVO`
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this CatalogEntityVO.

        :param attributes: The attributes of this CatalogEntityVO.
        :type attributes: :class:`huaweicloudsdkdataartsstudio.v1.CatalogAttributeVO`
        """
        self._attributes = attributes

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
        if not isinstance(other, CatalogEntityVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
