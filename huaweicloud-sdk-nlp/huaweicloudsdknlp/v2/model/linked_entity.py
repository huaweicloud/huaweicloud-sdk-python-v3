# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LinkedEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mention': 'str',
        'offset': 'int',
        'entity_title': 'str'
    }

    attribute_map = {
        'mention': 'mention',
        'offset': 'offset',
        'entity_title': 'entity_title'
    }

    def __init__(self, mention=None, offset=None, entity_title=None):
        r"""LinkedEntity

        The model defined in huaweicloud sdk

        :param mention: 实体指称
        :type mention: str
        :param offset: 偏移量
        :type offset: int
        :param entity_title: 实体名称
        :type entity_title: str
        """
        
        

        self._mention = None
        self._offset = None
        self._entity_title = None
        self.discriminator = None

        self.mention = mention
        self.offset = offset
        self.entity_title = entity_title

    @property
    def mention(self):
        r"""Gets the mention of this LinkedEntity.

        实体指称

        :return: The mention of this LinkedEntity.
        :rtype: str
        """
        return self._mention

    @mention.setter
    def mention(self, mention):
        r"""Sets the mention of this LinkedEntity.

        实体指称

        :param mention: The mention of this LinkedEntity.
        :type mention: str
        """
        self._mention = mention

    @property
    def offset(self):
        r"""Gets the offset of this LinkedEntity.

        偏移量

        :return: The offset of this LinkedEntity.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this LinkedEntity.

        偏移量

        :param offset: The offset of this LinkedEntity.
        :type offset: int
        """
        self._offset = offset

    @property
    def entity_title(self):
        r"""Gets the entity_title of this LinkedEntity.

        实体名称

        :return: The entity_title of this LinkedEntity.
        :rtype: str
        """
        return self._entity_title

    @entity_title.setter
    def entity_title(self, entity_title):
        r"""Sets the entity_title of this LinkedEntity.

        实体名称

        :param entity_title: The entity_title of this LinkedEntity.
        :type entity_title: str
        """
        self._entity_title = entity_title

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
        if not isinstance(other, LinkedEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
