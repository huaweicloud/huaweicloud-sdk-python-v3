# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RelatedObjectViewDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'object_id': 'str',
        'related_list': 'list[BasicObjectQueryViewDTO]',
        'related_entity_list': 'list[BasicObjectQueryViewDTO]'
    }

    attribute_map = {
        'object_id': 'objectId',
        'related_list': 'relatedList',
        'related_entity_list': 'relatedEntityList'
    }

    def __init__(self, object_id=None, related_list=None, related_entity_list=None):
        r"""RelatedObjectViewDTO

        The model defined in huaweicloud sdk

        :param object_id: **参数解释：**  数据实例ID。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 
        :type object_id: str
        :param related_list: **参数解释：**  关联的数据传输对象列表。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type related_list: list[:class:`huaweicloudsdkidmeclassicapi.v1.BasicObjectQueryViewDTO`]
        :param related_entity_list: **参数解释：**  关联的数据实体列表。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type related_entity_list: list[:class:`huaweicloudsdkidmeclassicapi.v1.BasicObjectQueryViewDTO`]
        """
        
        

        self._object_id = None
        self._related_list = None
        self._related_entity_list = None
        self.discriminator = None

        if object_id is not None:
            self.object_id = object_id
        if related_list is not None:
            self.related_list = related_list
        if related_entity_list is not None:
            self.related_entity_list = related_entity_list

    @property
    def object_id(self):
        r"""Gets the object_id of this RelatedObjectViewDTO.

        **参数解释：**  数据实例ID。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 

        :return: The object_id of this RelatedObjectViewDTO.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this RelatedObjectViewDTO.

        **参数解释：**  数据实例ID。  **取值范围：**  -9223372036854775808到9223372036854775807的整数。  **默认取值：**  不涉及。 

        :param object_id: The object_id of this RelatedObjectViewDTO.
        :type object_id: str
        """
        self._object_id = object_id

    @property
    def related_list(self):
        r"""Gets the related_list of this RelatedObjectViewDTO.

        **参数解释：**  关联的数据传输对象列表。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The related_list of this RelatedObjectViewDTO.
        :rtype: list[:class:`huaweicloudsdkidmeclassicapi.v1.BasicObjectQueryViewDTO`]
        """
        return self._related_list

    @related_list.setter
    def related_list(self, related_list):
        r"""Sets the related_list of this RelatedObjectViewDTO.

        **参数解释：**  关联的数据传输对象列表。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param related_list: The related_list of this RelatedObjectViewDTO.
        :type related_list: list[:class:`huaweicloudsdkidmeclassicapi.v1.BasicObjectQueryViewDTO`]
        """
        self._related_list = related_list

    @property
    def related_entity_list(self):
        r"""Gets the related_entity_list of this RelatedObjectViewDTO.

        **参数解释：**  关联的数据实体列表。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The related_entity_list of this RelatedObjectViewDTO.
        :rtype: list[:class:`huaweicloudsdkidmeclassicapi.v1.BasicObjectQueryViewDTO`]
        """
        return self._related_entity_list

    @related_entity_list.setter
    def related_entity_list(self, related_entity_list):
        r"""Sets the related_entity_list of this RelatedObjectViewDTO.

        **参数解释：**  关联的数据实体列表。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param related_entity_list: The related_entity_list of this RelatedObjectViewDTO.
        :type related_entity_list: list[:class:`huaweicloudsdkidmeclassicapi.v1.BasicObjectQueryViewDTO`]
        """
        self._related_entity_list = related_entity_list

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
        if not isinstance(other, RelatedObjectViewDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
