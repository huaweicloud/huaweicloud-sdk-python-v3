# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteTemplateGroupCollectionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_collection_id': 'str'
    }

    attribute_map = {
        'group_collection_id': 'group_collection_id'
    }

    def __init__(self, group_collection_id=None):
        """DeleteTemplateGroupCollectionRequest

        The model defined in huaweicloud sdk

        :param group_collection_id: 模板组集合id 
        :type group_collection_id: str
        """
        
        

        self._group_collection_id = None
        self.discriminator = None

        self.group_collection_id = group_collection_id

    @property
    def group_collection_id(self):
        """Gets the group_collection_id of this DeleteTemplateGroupCollectionRequest.

        模板组集合id 

        :return: The group_collection_id of this DeleteTemplateGroupCollectionRequest.
        :rtype: str
        """
        return self._group_collection_id

    @group_collection_id.setter
    def group_collection_id(self, group_collection_id):
        """Sets the group_collection_id of this DeleteTemplateGroupCollectionRequest.

        模板组集合id 

        :param group_collection_id: The group_collection_id of this DeleteTemplateGroupCollectionRequest.
        :type group_collection_id: str
        """
        self._group_collection_id = group_collection_id

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
        if not isinstance(other, DeleteTemplateGroupCollectionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
