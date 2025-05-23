# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateMetadataReqGesMetadataLabels:

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
        'properties': 'list[dict(str, str)]'
    }

    attribute_map = {
        'name': 'name',
        'properties': 'properties'
    }

    def __init__(self, name=None, properties=None):
        r"""CreateMetadataReqGesMetadataLabels

        The model defined in huaweicloud sdk

        :param name: label名称
        :type name: str
        :param properties: label属性map
        :type properties: list[dict(str, str)]
        """
        
        

        self._name = None
        self._properties = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if properties is not None:
            self.properties = properties

    @property
    def name(self):
        r"""Gets the name of this CreateMetadataReqGesMetadataLabels.

        label名称

        :return: The name of this CreateMetadataReqGesMetadataLabels.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateMetadataReqGesMetadataLabels.

        label名称

        :param name: The name of this CreateMetadataReqGesMetadataLabels.
        :type name: str
        """
        self._name = name

    @property
    def properties(self):
        r"""Gets the properties of this CreateMetadataReqGesMetadataLabels.

        label属性map

        :return: The properties of this CreateMetadataReqGesMetadataLabels.
        :rtype: list[dict(str, str)]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this CreateMetadataReqGesMetadataLabels.

        label属性map

        :param properties: The properties of this CreateMetadataReqGesMetadataLabels.
        :type properties: list[dict(str, str)]
        """
        self._properties = properties

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
        if not isinstance(other, CreateMetadataReqGesMetadataLabels):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
