# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValueInTwin:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'excepted': 'Excepted',
        'optional': 'bool',
        'metadata': 'Metadata'
    }

    attribute_map = {
        'excepted': 'excepted',
        'optional': 'optional',
        'metadata': 'metadata'
    }

    def __init__(self, excepted=None, optional=None, metadata=None):
        """ValueInTwin

        The model defined in huaweicloud sdk

        :param excepted: 
        :type excepted: :class:`huaweicloudsdkief.v1.Excepted`
        :param optional: 动态属性的实际信息
        :type optional: bool
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkief.v1.Metadata`
        """
        
        

        self._excepted = None
        self._optional = None
        self._metadata = None
        self.discriminator = None

        if excepted is not None:
            self.excepted = excepted
        if optional is not None:
            self.optional = optional
        if metadata is not None:
            self.metadata = metadata

    @property
    def excepted(self):
        """Gets the excepted of this ValueInTwin.

        :return: The excepted of this ValueInTwin.
        :rtype: :class:`huaweicloudsdkief.v1.Excepted`
        """
        return self._excepted

    @excepted.setter
    def excepted(self, excepted):
        """Sets the excepted of this ValueInTwin.

        :param excepted: The excepted of this ValueInTwin.
        :type excepted: :class:`huaweicloudsdkief.v1.Excepted`
        """
        self._excepted = excepted

    @property
    def optional(self):
        """Gets the optional of this ValueInTwin.

        动态属性的实际信息

        :return: The optional of this ValueInTwin.
        :rtype: bool
        """
        return self._optional

    @optional.setter
    def optional(self, optional):
        """Sets the optional of this ValueInTwin.

        动态属性的实际信息

        :param optional: The optional of this ValueInTwin.
        :type optional: bool
        """
        self._optional = optional

    @property
    def metadata(self):
        """Gets the metadata of this ValueInTwin.

        :return: The metadata of this ValueInTwin.
        :rtype: :class:`huaweicloudsdkief.v1.Metadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this ValueInTwin.

        :param metadata: The metadata of this ValueInTwin.
        :type metadata: :class:`huaweicloudsdkief.v1.Metadata`
        """
        self._metadata = metadata

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
        if not isinstance(other, ValueInTwin):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
