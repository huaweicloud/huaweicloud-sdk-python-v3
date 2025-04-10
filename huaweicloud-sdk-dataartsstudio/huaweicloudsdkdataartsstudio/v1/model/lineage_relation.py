# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LineageRelation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'from_entity_id': 'str',
        'relationship_id': 'str',
        'to_entity_id': 'str'
    }

    attribute_map = {
        'from_entity_id': 'from_entity_id',
        'relationship_id': 'relationship_id',
        'to_entity_id': 'to_entity_id'
    }

    def __init__(self, from_entity_id=None, relationship_id=None, to_entity_id=None):
        r"""LineageRelation

        The model defined in huaweicloud sdk

        :param from_entity_id: 血缘来源
        :type from_entity_id: str
        :param relationship_id: 关系id
        :type relationship_id: str
        :param to_entity_id: 血缘流向
        :type to_entity_id: str
        """
        
        

        self._from_entity_id = None
        self._relationship_id = None
        self._to_entity_id = None
        self.discriminator = None

        if from_entity_id is not None:
            self.from_entity_id = from_entity_id
        if relationship_id is not None:
            self.relationship_id = relationship_id
        if to_entity_id is not None:
            self.to_entity_id = to_entity_id

    @property
    def from_entity_id(self):
        r"""Gets the from_entity_id of this LineageRelation.

        血缘来源

        :return: The from_entity_id of this LineageRelation.
        :rtype: str
        """
        return self._from_entity_id

    @from_entity_id.setter
    def from_entity_id(self, from_entity_id):
        r"""Sets the from_entity_id of this LineageRelation.

        血缘来源

        :param from_entity_id: The from_entity_id of this LineageRelation.
        :type from_entity_id: str
        """
        self._from_entity_id = from_entity_id

    @property
    def relationship_id(self):
        r"""Gets the relationship_id of this LineageRelation.

        关系id

        :return: The relationship_id of this LineageRelation.
        :rtype: str
        """
        return self._relationship_id

    @relationship_id.setter
    def relationship_id(self, relationship_id):
        r"""Sets the relationship_id of this LineageRelation.

        关系id

        :param relationship_id: The relationship_id of this LineageRelation.
        :type relationship_id: str
        """
        self._relationship_id = relationship_id

    @property
    def to_entity_id(self):
        r"""Gets the to_entity_id of this LineageRelation.

        血缘流向

        :return: The to_entity_id of this LineageRelation.
        :rtype: str
        """
        return self._to_entity_id

    @to_entity_id.setter
    def to_entity_id(self, to_entity_id):
        r"""Sets the to_entity_id of this LineageRelation.

        血缘流向

        :param to_entity_id: The to_entity_id of this LineageRelation.
        :type to_entity_id: str
        """
        self._to_entity_id = to_entity_id

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
        if not isinstance(other, LineageRelation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
