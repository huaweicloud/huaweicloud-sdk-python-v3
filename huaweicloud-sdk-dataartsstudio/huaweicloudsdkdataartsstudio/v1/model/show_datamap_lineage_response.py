# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDatamapLineageResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'float',
        'relationships': 'list[Lineage]',
        'relationship_types': 'object',
        'entities': 'list[Entity]',
        'entity_types': 'object'
    }

    attribute_map = {
        'total': 'total',
        'relationships': 'relationships',
        'relationship_types': 'relationship_types',
        'entities': 'entities',
        'entity_types': 'entity_types'
    }

    def __init__(self, total=None, relationships=None, relationship_types=None, entities=None, entity_types=None):
        """ShowDatamapLineageResponse

        The model defined in huaweicloud sdk

        :param total: 查询命中总条数
        :type total: float
        :param relationships: 关系列表
        :type relationships: list[:class:`huaweicloudsdkdataartsstudio.v1.Lineage`]
        :param relationship_types: 关系类型
        :type relationship_types: object
        :param entities: 资产信息
        :type entities: list[:class:`huaweicloudsdkdataartsstudio.v1.Entity`]
        :param entity_types: 实体类型
        :type entity_types: object
        """
        
        super(ShowDatamapLineageResponse, self).__init__()

        self._total = None
        self._relationships = None
        self._relationship_types = None
        self._entities = None
        self._entity_types = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if relationships is not None:
            self.relationships = relationships
        if relationship_types is not None:
            self.relationship_types = relationship_types
        if entities is not None:
            self.entities = entities
        if entity_types is not None:
            self.entity_types = entity_types

    @property
    def total(self):
        """Gets the total of this ShowDatamapLineageResponse.

        查询命中总条数

        :return: The total of this ShowDatamapLineageResponse.
        :rtype: float
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ShowDatamapLineageResponse.

        查询命中总条数

        :param total: The total of this ShowDatamapLineageResponse.
        :type total: float
        """
        self._total = total

    @property
    def relationships(self):
        """Gets the relationships of this ShowDatamapLineageResponse.

        关系列表

        :return: The relationships of this ShowDatamapLineageResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.Lineage`]
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """Sets the relationships of this ShowDatamapLineageResponse.

        关系列表

        :param relationships: The relationships of this ShowDatamapLineageResponse.
        :type relationships: list[:class:`huaweicloudsdkdataartsstudio.v1.Lineage`]
        """
        self._relationships = relationships

    @property
    def relationship_types(self):
        """Gets the relationship_types of this ShowDatamapLineageResponse.

        关系类型

        :return: The relationship_types of this ShowDatamapLineageResponse.
        :rtype: object
        """
        return self._relationship_types

    @relationship_types.setter
    def relationship_types(self, relationship_types):
        """Sets the relationship_types of this ShowDatamapLineageResponse.

        关系类型

        :param relationship_types: The relationship_types of this ShowDatamapLineageResponse.
        :type relationship_types: object
        """
        self._relationship_types = relationship_types

    @property
    def entities(self):
        """Gets the entities of this ShowDatamapLineageResponse.

        资产信息

        :return: The entities of this ShowDatamapLineageResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.Entity`]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this ShowDatamapLineageResponse.

        资产信息

        :param entities: The entities of this ShowDatamapLineageResponse.
        :type entities: list[:class:`huaweicloudsdkdataartsstudio.v1.Entity`]
        """
        self._entities = entities

    @property
    def entity_types(self):
        """Gets the entity_types of this ShowDatamapLineageResponse.

        实体类型

        :return: The entity_types of this ShowDatamapLineageResponse.
        :rtype: object
        """
        return self._entity_types

    @entity_types.setter
    def entity_types(self, entity_types):
        """Sets the entity_types of this ShowDatamapLineageResponse.

        实体类型

        :param entity_types: The entity_types of this ShowDatamapLineageResponse.
        :type entity_types: object
        """
        self._entity_types = entity_types

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
        if not isinstance(other, ShowDatamapLineageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
