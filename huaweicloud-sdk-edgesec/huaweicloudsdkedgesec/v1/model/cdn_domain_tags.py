# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CdnDomainTags:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'notes': 'str',
        'constraint': 'str'
    }

    attribute_map = {
        'notes': 'notes',
        'constraint': 'constraint'
    }

    def __init__(self, notes=None, constraint=None):
        """CdnDomainTags

        The model defined in huaweicloud sdk

        :param notes: 约束原因
        :type notes: str
        :param constraint: 约束内容
        :type constraint: str
        """
        
        

        self._notes = None
        self._constraint = None
        self.discriminator = None

        if notes is not None:
            self.notes = notes
        if constraint is not None:
            self.constraint = constraint

    @property
    def notes(self):
        """Gets the notes of this CdnDomainTags.

        约束原因

        :return: The notes of this CdnDomainTags.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        """Sets the notes of this CdnDomainTags.

        约束原因

        :param notes: The notes of this CdnDomainTags.
        :type notes: str
        """
        self._notes = notes

    @property
    def constraint(self):
        """Gets the constraint of this CdnDomainTags.

        约束内容

        :return: The constraint of this CdnDomainTags.
        :rtype: str
        """
        return self._constraint

    @constraint.setter
    def constraint(self, constraint):
        """Sets the constraint of this CdnDomainTags.

        约束内容

        :param constraint: The constraint of this CdnDomainTags.
        :type constraint: str
        """
        self._constraint = constraint

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
        if not isinstance(other, CdnDomainTags):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
