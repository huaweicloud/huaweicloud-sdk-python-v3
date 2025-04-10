# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValueInTwinResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'excepted': 'ExceptedActual',
        'actual': 'ExceptedActual',
        'metadata': 'Metadata',
        'optional': 'bool'
    }

    attribute_map = {
        'excepted': 'excepted',
        'actual': 'actual',
        'metadata': 'metadata',
        'optional': 'optional'
    }

    def __init__(self, excepted=None, actual=None, metadata=None, optional=None):
        r"""ValueInTwinResponse

        The model defined in huaweicloud sdk

        :param excepted: 
        :type excepted: :class:`huaweicloudsdkief.v1.ExceptedActual`
        :param actual: 
        :type actual: :class:`huaweicloudsdkief.v1.ExceptedActual`
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkief.v1.Metadata`
        :param optional: 标识属性是否可选，默认为true，继承模板的属性默认为false
        :type optional: bool
        """
        
        

        self._excepted = None
        self._actual = None
        self._metadata = None
        self._optional = None
        self.discriminator = None

        if excepted is not None:
            self.excepted = excepted
        if actual is not None:
            self.actual = actual
        if metadata is not None:
            self.metadata = metadata
        if optional is not None:
            self.optional = optional

    @property
    def excepted(self):
        r"""Gets the excepted of this ValueInTwinResponse.

        :return: The excepted of this ValueInTwinResponse.
        :rtype: :class:`huaweicloudsdkief.v1.ExceptedActual`
        """
        return self._excepted

    @excepted.setter
    def excepted(self, excepted):
        r"""Sets the excepted of this ValueInTwinResponse.

        :param excepted: The excepted of this ValueInTwinResponse.
        :type excepted: :class:`huaweicloudsdkief.v1.ExceptedActual`
        """
        self._excepted = excepted

    @property
    def actual(self):
        r"""Gets the actual of this ValueInTwinResponse.

        :return: The actual of this ValueInTwinResponse.
        :rtype: :class:`huaweicloudsdkief.v1.ExceptedActual`
        """
        return self._actual

    @actual.setter
    def actual(self, actual):
        r"""Sets the actual of this ValueInTwinResponse.

        :param actual: The actual of this ValueInTwinResponse.
        :type actual: :class:`huaweicloudsdkief.v1.ExceptedActual`
        """
        self._actual = actual

    @property
    def metadata(self):
        r"""Gets the metadata of this ValueInTwinResponse.

        :return: The metadata of this ValueInTwinResponse.
        :rtype: :class:`huaweicloudsdkief.v1.Metadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        r"""Sets the metadata of this ValueInTwinResponse.

        :param metadata: The metadata of this ValueInTwinResponse.
        :type metadata: :class:`huaweicloudsdkief.v1.Metadata`
        """
        self._metadata = metadata

    @property
    def optional(self):
        r"""Gets the optional of this ValueInTwinResponse.

        标识属性是否可选，默认为true，继承模板的属性默认为false

        :return: The optional of this ValueInTwinResponse.
        :rtype: bool
        """
        return self._optional

    @optional.setter
    def optional(self, optional):
        r"""Sets the optional of this ValueInTwinResponse.

        标识属性是否可选，默认为true，继承模板的属性默认为false

        :param optional: The optional of this ValueInTwinResponse.
        :type optional: bool
        """
        self._optional = optional

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
        if not isinstance(other, ValueInTwinResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
