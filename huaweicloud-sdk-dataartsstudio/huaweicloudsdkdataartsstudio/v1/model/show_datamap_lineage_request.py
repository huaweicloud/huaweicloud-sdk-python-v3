# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDatamapLineageRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance': 'str',
        'guid': 'str',
        'direction': 'str',
        'relationship_types': 'list[str]',
        'relationship_type_categories': 'list[str]',
        'related_entity_types': 'list[str]',
        'extend_process_data_flow': 'bool',
        'include_parent_entity': 'bool'
    }

    attribute_map = {
        'instance': 'instance',
        'guid': 'guid',
        'direction': 'direction',
        'relationship_types': 'relationship_types',
        'relationship_type_categories': 'relationship_type_categories',
        'related_entity_types': 'related_entity_types',
        'extend_process_data_flow': 'extend_process_data_flow',
        'include_parent_entity': 'include_parent_entity'
    }

    def __init__(self, instance=None, guid=None, direction=None, relationship_types=None, relationship_type_categories=None, related_entity_types=None, extend_process_data_flow=None, include_parent_entity=None):
        r"""ShowDatamapLineageRequest

        The model defined in huaweicloud sdk

        :param instance: 实例id
        :type instance: str
        :param guid: 资产guid
        :type guid: str
        :param direction: 血缘查询方向，默认值:BOTH。枚举值[IN OUT BOTH]
        :type direction: str
        :param relationship_types: 关联关系类型列表，默认空
        :type relationship_types: list[str]
        :param relationship_type_categories: 关联关系类型类别，默认空。血缘查询使用DATA_FLOW
        :type relationship_type_categories: list[str]
        :param related_entity_types: 关联实体类型，默认空
        :type related_entity_types: list[str]
        :param extend_process_data_flow: 是否扩展数据，默认false
        :type extend_process_data_flow: bool
        :param include_parent_entity: 是否包含父类实体，默认false
        :type include_parent_entity: bool
        """
        
        

        self._instance = None
        self._guid = None
        self._direction = None
        self._relationship_types = None
        self._relationship_type_categories = None
        self._related_entity_types = None
        self._extend_process_data_flow = None
        self._include_parent_entity = None
        self.discriminator = None

        self.instance = instance
        self.guid = guid
        if direction is not None:
            self.direction = direction
        if relationship_types is not None:
            self.relationship_types = relationship_types
        if relationship_type_categories is not None:
            self.relationship_type_categories = relationship_type_categories
        if related_entity_types is not None:
            self.related_entity_types = related_entity_types
        if extend_process_data_flow is not None:
            self.extend_process_data_flow = extend_process_data_flow
        if include_parent_entity is not None:
            self.include_parent_entity = include_parent_entity

    @property
    def instance(self):
        r"""Gets the instance of this ShowDatamapLineageRequest.

        实例id

        :return: The instance of this ShowDatamapLineageRequest.
        :rtype: str
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        r"""Sets the instance of this ShowDatamapLineageRequest.

        实例id

        :param instance: The instance of this ShowDatamapLineageRequest.
        :type instance: str
        """
        self._instance = instance

    @property
    def guid(self):
        r"""Gets the guid of this ShowDatamapLineageRequest.

        资产guid

        :return: The guid of this ShowDatamapLineageRequest.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        r"""Sets the guid of this ShowDatamapLineageRequest.

        资产guid

        :param guid: The guid of this ShowDatamapLineageRequest.
        :type guid: str
        """
        self._guid = guid

    @property
    def direction(self):
        r"""Gets the direction of this ShowDatamapLineageRequest.

        血缘查询方向，默认值:BOTH。枚举值[IN OUT BOTH]

        :return: The direction of this ShowDatamapLineageRequest.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        r"""Sets the direction of this ShowDatamapLineageRequest.

        血缘查询方向，默认值:BOTH。枚举值[IN OUT BOTH]

        :param direction: The direction of this ShowDatamapLineageRequest.
        :type direction: str
        """
        self._direction = direction

    @property
    def relationship_types(self):
        r"""Gets the relationship_types of this ShowDatamapLineageRequest.

        关联关系类型列表，默认空

        :return: The relationship_types of this ShowDatamapLineageRequest.
        :rtype: list[str]
        """
        return self._relationship_types

    @relationship_types.setter
    def relationship_types(self, relationship_types):
        r"""Sets the relationship_types of this ShowDatamapLineageRequest.

        关联关系类型列表，默认空

        :param relationship_types: The relationship_types of this ShowDatamapLineageRequest.
        :type relationship_types: list[str]
        """
        self._relationship_types = relationship_types

    @property
    def relationship_type_categories(self):
        r"""Gets the relationship_type_categories of this ShowDatamapLineageRequest.

        关联关系类型类别，默认空。血缘查询使用DATA_FLOW

        :return: The relationship_type_categories of this ShowDatamapLineageRequest.
        :rtype: list[str]
        """
        return self._relationship_type_categories

    @relationship_type_categories.setter
    def relationship_type_categories(self, relationship_type_categories):
        r"""Sets the relationship_type_categories of this ShowDatamapLineageRequest.

        关联关系类型类别，默认空。血缘查询使用DATA_FLOW

        :param relationship_type_categories: The relationship_type_categories of this ShowDatamapLineageRequest.
        :type relationship_type_categories: list[str]
        """
        self._relationship_type_categories = relationship_type_categories

    @property
    def related_entity_types(self):
        r"""Gets the related_entity_types of this ShowDatamapLineageRequest.

        关联实体类型，默认空

        :return: The related_entity_types of this ShowDatamapLineageRequest.
        :rtype: list[str]
        """
        return self._related_entity_types

    @related_entity_types.setter
    def related_entity_types(self, related_entity_types):
        r"""Sets the related_entity_types of this ShowDatamapLineageRequest.

        关联实体类型，默认空

        :param related_entity_types: The related_entity_types of this ShowDatamapLineageRequest.
        :type related_entity_types: list[str]
        """
        self._related_entity_types = related_entity_types

    @property
    def extend_process_data_flow(self):
        r"""Gets the extend_process_data_flow of this ShowDatamapLineageRequest.

        是否扩展数据，默认false

        :return: The extend_process_data_flow of this ShowDatamapLineageRequest.
        :rtype: bool
        """
        return self._extend_process_data_flow

    @extend_process_data_flow.setter
    def extend_process_data_flow(self, extend_process_data_flow):
        r"""Sets the extend_process_data_flow of this ShowDatamapLineageRequest.

        是否扩展数据，默认false

        :param extend_process_data_flow: The extend_process_data_flow of this ShowDatamapLineageRequest.
        :type extend_process_data_flow: bool
        """
        self._extend_process_data_flow = extend_process_data_flow

    @property
    def include_parent_entity(self):
        r"""Gets the include_parent_entity of this ShowDatamapLineageRequest.

        是否包含父类实体，默认false

        :return: The include_parent_entity of this ShowDatamapLineageRequest.
        :rtype: bool
        """
        return self._include_parent_entity

    @include_parent_entity.setter
    def include_parent_entity(self, include_parent_entity):
        r"""Sets the include_parent_entity of this ShowDatamapLineageRequest.

        是否包含父类实体，默认false

        :param include_parent_entity: The include_parent_entity of this ShowDatamapLineageRequest.
        :type include_parent_entity: bool
        """
        self._include_parent_entity = include_parent_entity

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
        if not isinstance(other, ShowDatamapLineageRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
