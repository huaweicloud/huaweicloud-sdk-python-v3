# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTemplateGroupCollectionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'group_collection_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'group_collection_id': 'group_collection_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, group_collection_id=None, offset=None, limit=None):
        """ListTemplateGroupCollectionRequest

        The model defined in huaweicloud sdk

        :param group_collection_id: 模板组集合id 
        :type group_collection_id: str
        :param offset: 偏移量。默认为0。指定group_collection_id时该参数无效。&lt;br/&gt; 
        :type offset: int
        :param limit: 每页记录数。默认为10，范围[1,100]。指定group_collection_id时该参数无效。&lt;br/&gt; 
        :type limit: int
        """
        
        

        self._group_collection_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if group_collection_id is not None:
            self.group_collection_id = group_collection_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def group_collection_id(self):
        """Gets the group_collection_id of this ListTemplateGroupCollectionRequest.

        模板组集合id 

        :return: The group_collection_id of this ListTemplateGroupCollectionRequest.
        :rtype: str
        """
        return self._group_collection_id

    @group_collection_id.setter
    def group_collection_id(self, group_collection_id):
        """Sets the group_collection_id of this ListTemplateGroupCollectionRequest.

        模板组集合id 

        :param group_collection_id: The group_collection_id of this ListTemplateGroupCollectionRequest.
        :type group_collection_id: str
        """
        self._group_collection_id = group_collection_id

    @property
    def offset(self):
        """Gets the offset of this ListTemplateGroupCollectionRequest.

        偏移量。默认为0。指定group_collection_id时该参数无效。<br/> 

        :return: The offset of this ListTemplateGroupCollectionRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListTemplateGroupCollectionRequest.

        偏移量。默认为0。指定group_collection_id时该参数无效。<br/> 

        :param offset: The offset of this ListTemplateGroupCollectionRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListTemplateGroupCollectionRequest.

        每页记录数。默认为10，范围[1,100]。指定group_collection_id时该参数无效。<br/> 

        :return: The limit of this ListTemplateGroupCollectionRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListTemplateGroupCollectionRequest.

        每页记录数。默认为10，范围[1,100]。指定group_collection_id时该参数无效。<br/> 

        :param limit: The limit of this ListTemplateGroupCollectionRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListTemplateGroupCollectionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
