# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RelationConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'relations': 'dict(str, list[Relation])'
    }

    attribute_map = {
        'relations': 'relations'
    }

    def __init__(self, relations=None):
        r"""RelationConfig

        The model defined in huaweicloud sdk

        :param relations: key为工作项类型，value为该类型的所有关联关系
        :type relations: dict(str, list[Relation])
        """
        
        

        self._relations = None
        self.discriminator = None

        if relations is not None:
            self.relations = relations

    @property
    def relations(self):
        r"""Gets the relations of this RelationConfig.

        key为工作项类型，value为该类型的所有关联关系

        :return: The relations of this RelationConfig.
        :rtype: dict(str, list[Relation])
        """
        return self._relations

    @relations.setter
    def relations(self, relations):
        r"""Sets the relations of this RelationConfig.

        key为工作项类型，value为该类型的所有关联关系

        :param relations: The relations of this RelationConfig.
        :type relations: dict(str, list[Relation])
        """
        self._relations = relations

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RelationConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
