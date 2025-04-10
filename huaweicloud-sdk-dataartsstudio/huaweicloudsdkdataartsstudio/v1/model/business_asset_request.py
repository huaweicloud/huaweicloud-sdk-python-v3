# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BusinessAssetRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'search_all_attributes': 'bool',
        'tags': 'object',
        'limit': 'int',
        'offset': 'int',
        'guid': 'str',
        'query': 'str',
        'type': 'str'
    }

    attribute_map = {
        'search_all_attributes': 'search_all_attributes',
        'tags': 'tags',
        'limit': 'limit',
        'offset': 'offset',
        'guid': 'guid',
        'query': 'query',
        'type': 'type'
    }

    def __init__(self, search_all_attributes=None, tags=None, limit=None, offset=None, guid=None, query=None, type=None):
        r"""BusinessAssetRequest

        The model defined in huaweicloud sdk

        :param search_all_attributes: 关键字查询是否匹配所有属性，true为查询所有属性，false为仅查询名称描述
        :type search_all_attributes: bool
        :param tags: 标签信息 Set&lt;String&gt;
        :type tags: object
        :param limit: 查询返回数目
        :type limit: int
        :param offset: 查询偏移量
        :type offset: int
        :param guid: 查询节点的guid
        :type guid: str
        :param query: 查询关键字
        :type query: str
        :param type: 查询类型
        :type type: str
        """
        
        

        self._search_all_attributes = None
        self._tags = None
        self._limit = None
        self._offset = None
        self._guid = None
        self._query = None
        self._type = None
        self.discriminator = None

        self.search_all_attributes = search_all_attributes
        if tags is not None:
            self.tags = tags
        self.limit = limit
        self.offset = offset
        if guid is not None:
            self.guid = guid
        self.query = query
        self.type = type

    @property
    def search_all_attributes(self):
        r"""Gets the search_all_attributes of this BusinessAssetRequest.

        关键字查询是否匹配所有属性，true为查询所有属性，false为仅查询名称描述

        :return: The search_all_attributes of this BusinessAssetRequest.
        :rtype: bool
        """
        return self._search_all_attributes

    @search_all_attributes.setter
    def search_all_attributes(self, search_all_attributes):
        r"""Sets the search_all_attributes of this BusinessAssetRequest.

        关键字查询是否匹配所有属性，true为查询所有属性，false为仅查询名称描述

        :param search_all_attributes: The search_all_attributes of this BusinessAssetRequest.
        :type search_all_attributes: bool
        """
        self._search_all_attributes = search_all_attributes

    @property
    def tags(self):
        r"""Gets the tags of this BusinessAssetRequest.

        标签信息 Set<String>

        :return: The tags of this BusinessAssetRequest.
        :rtype: object
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this BusinessAssetRequest.

        标签信息 Set<String>

        :param tags: The tags of this BusinessAssetRequest.
        :type tags: object
        """
        self._tags = tags

    @property
    def limit(self):
        r"""Gets the limit of this BusinessAssetRequest.

        查询返回数目

        :return: The limit of this BusinessAssetRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this BusinessAssetRequest.

        查询返回数目

        :param limit: The limit of this BusinessAssetRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this BusinessAssetRequest.

        查询偏移量

        :return: The offset of this BusinessAssetRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this BusinessAssetRequest.

        查询偏移量

        :param offset: The offset of this BusinessAssetRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def guid(self):
        r"""Gets the guid of this BusinessAssetRequest.

        查询节点的guid

        :return: The guid of this BusinessAssetRequest.
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        r"""Sets the guid of this BusinessAssetRequest.

        查询节点的guid

        :param guid: The guid of this BusinessAssetRequest.
        :type guid: str
        """
        self._guid = guid

    @property
    def query(self):
        r"""Gets the query of this BusinessAssetRequest.

        查询关键字

        :return: The query of this BusinessAssetRequest.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        r"""Sets the query of this BusinessAssetRequest.

        查询关键字

        :param query: The query of this BusinessAssetRequest.
        :type query: str
        """
        self._query = query

    @property
    def type(self):
        r"""Gets the type of this BusinessAssetRequest.

        查询类型

        :return: The type of this BusinessAssetRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this BusinessAssetRequest.

        查询类型

        :param type: The type of this BusinessAssetRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, BusinessAssetRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
