# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlternateIdentifierDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'external_id': 'ExternalIdDto',
        'unique_attribute': 'UniqueAttributeDto'
    }

    attribute_map = {
        'external_id': 'external_id',
        'unique_attribute': 'unique_attribute'
    }

    def __init__(self, external_id=None, unique_attribute=None):
        r"""AlternateIdentifierDto

        The model defined in huaweicloud sdk

        :param external_id: 
        :type external_id: :class:`huaweicloudsdkidentitycenterstore.v1.ExternalIdDto`
        :param unique_attribute: 
        :type unique_attribute: :class:`huaweicloudsdkidentitycenterstore.v1.UniqueAttributeDto`
        """
        
        

        self._external_id = None
        self._unique_attribute = None
        self.discriminator = None

        if external_id is not None:
            self.external_id = external_id
        if unique_attribute is not None:
            self.unique_attribute = unique_attribute

    @property
    def external_id(self):
        r"""Gets the external_id of this AlternateIdentifierDto.

        :return: The external_id of this AlternateIdentifierDto.
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.ExternalIdDto`
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        r"""Sets the external_id of this AlternateIdentifierDto.

        :param external_id: The external_id of this AlternateIdentifierDto.
        :type external_id: :class:`huaweicloudsdkidentitycenterstore.v1.ExternalIdDto`
        """
        self._external_id = external_id

    @property
    def unique_attribute(self):
        r"""Gets the unique_attribute of this AlternateIdentifierDto.

        :return: The unique_attribute of this AlternateIdentifierDto.
        :rtype: :class:`huaweicloudsdkidentitycenterstore.v1.UniqueAttributeDto`
        """
        return self._unique_attribute

    @unique_attribute.setter
    def unique_attribute(self, unique_attribute):
        r"""Sets the unique_attribute of this AlternateIdentifierDto.

        :param unique_attribute: The unique_attribute of this AlternateIdentifierDto.
        :type unique_attribute: :class:`huaweicloudsdkidentitycenterstore.v1.UniqueAttributeDto`
        """
        self._unique_attribute = unique_attribute

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
        if not isinstance(other, AlternateIdentifierDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
