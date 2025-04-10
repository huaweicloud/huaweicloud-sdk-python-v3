# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLineageResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'base_entity_guid': 'str',
        'guid_entity_map': 'object',
        'relations': 'list[LineageRelation]',
        'referred_entities': 'object'
    }

    attribute_map = {
        'base_entity_guid': 'base_entity_guid',
        'guid_entity_map': 'guid_entity_map',
        'relations': 'relations',
        'referred_entities': 'referred_entities'
    }

    def __init__(self, base_entity_guid=None, guid_entity_map=None, relations=None, referred_entities=None):
        r"""ShowLineageResponse

        The model defined in huaweicloud sdk

        :param base_entity_guid: 当前资产的guid
        :type base_entity_guid: str
        :param guid_entity_map: 实体集合Map(String, OpenEntityHeader)
        :type guid_entity_map: object
        :param relations: 血缘关系
        :type relations: list[:class:`huaweicloudsdkdataartsstudio.v1.LineageRelation`]
        :param referred_entities: 相关实体集合Map(String, OpenEntity)
        :type referred_entities: object
        """
        
        super(ShowLineageResponse, self).__init__()

        self._base_entity_guid = None
        self._guid_entity_map = None
        self._relations = None
        self._referred_entities = None
        self.discriminator = None

        if base_entity_guid is not None:
            self.base_entity_guid = base_entity_guid
        if guid_entity_map is not None:
            self.guid_entity_map = guid_entity_map
        if relations is not None:
            self.relations = relations
        if referred_entities is not None:
            self.referred_entities = referred_entities

    @property
    def base_entity_guid(self):
        r"""Gets the base_entity_guid of this ShowLineageResponse.

        当前资产的guid

        :return: The base_entity_guid of this ShowLineageResponse.
        :rtype: str
        """
        return self._base_entity_guid

    @base_entity_guid.setter
    def base_entity_guid(self, base_entity_guid):
        r"""Sets the base_entity_guid of this ShowLineageResponse.

        当前资产的guid

        :param base_entity_guid: The base_entity_guid of this ShowLineageResponse.
        :type base_entity_guid: str
        """
        self._base_entity_guid = base_entity_guid

    @property
    def guid_entity_map(self):
        r"""Gets the guid_entity_map of this ShowLineageResponse.

        实体集合Map(String, OpenEntityHeader)

        :return: The guid_entity_map of this ShowLineageResponse.
        :rtype: object
        """
        return self._guid_entity_map

    @guid_entity_map.setter
    def guid_entity_map(self, guid_entity_map):
        r"""Sets the guid_entity_map of this ShowLineageResponse.

        实体集合Map(String, OpenEntityHeader)

        :param guid_entity_map: The guid_entity_map of this ShowLineageResponse.
        :type guid_entity_map: object
        """
        self._guid_entity_map = guid_entity_map

    @property
    def relations(self):
        r"""Gets the relations of this ShowLineageResponse.

        血缘关系

        :return: The relations of this ShowLineageResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.LineageRelation`]
        """
        return self._relations

    @relations.setter
    def relations(self, relations):
        r"""Sets the relations of this ShowLineageResponse.

        血缘关系

        :param relations: The relations of this ShowLineageResponse.
        :type relations: list[:class:`huaweicloudsdkdataartsstudio.v1.LineageRelation`]
        """
        self._relations = relations

    @property
    def referred_entities(self):
        r"""Gets the referred_entities of this ShowLineageResponse.

        相关实体集合Map(String, OpenEntity)

        :return: The referred_entities of this ShowLineageResponse.
        :rtype: object
        """
        return self._referred_entities

    @referred_entities.setter
    def referred_entities(self, referred_entities):
        r"""Sets the referred_entities of this ShowLineageResponse.

        相关实体集合Map(String, OpenEntity)

        :param referred_entities: The referred_entities of this ShowLineageResponse.
        :type referred_entities: object
        """
        self._referred_entities = referred_entities

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
        if not isinstance(other, ShowLineageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
