# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SourceObject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'kind': 'SourceKind',
        'spec': 'SourceOrArtifact'
    }

    attribute_map = {
        'kind': 'kind',
        'spec': 'spec'
    }

    def __init__(self, kind=None, spec=None):
        r"""SourceObject

        The model defined in huaweicloud sdk

        :param kind: 
        :type kind: :class:`huaweicloudsdkservicestage.v2.SourceKind`
        :param spec: 
        :type spec: :class:`huaweicloudsdkservicestage.v2.SourceOrArtifact`
        """
        
        

        self._kind = None
        self._spec = None
        self.discriminator = None

        self.kind = kind
        self.spec = spec

    @property
    def kind(self):
        r"""Gets the kind of this SourceObject.

        :return: The kind of this SourceObject.
        :rtype: :class:`huaweicloudsdkservicestage.v2.SourceKind`
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        r"""Sets the kind of this SourceObject.

        :param kind: The kind of this SourceObject.
        :type kind: :class:`huaweicloudsdkservicestage.v2.SourceKind`
        """
        self._kind = kind

    @property
    def spec(self):
        r"""Gets the spec of this SourceObject.

        :return: The spec of this SourceObject.
        :rtype: :class:`huaweicloudsdkservicestage.v2.SourceOrArtifact`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        r"""Sets the spec of this SourceObject.

        :param spec: The spec of this SourceObject.
        :type spec: :class:`huaweicloudsdkservicestage.v2.SourceOrArtifact`
        """
        self._spec = spec

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
        if not isinstance(other, SourceObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
