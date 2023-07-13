# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowUnrelatedTableResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attributes': 'AttributeSearchResult',
        'classification': 'str',
        'count': 'int',
        'entities': 'list[AtlasEntityHeader]',
        'full_text_result': 'list[AtlasFullTextResult]',
        'query_text': 'str',
        'query_type': 'str',
        'referred_entities': 'object',
        'scroll_id': 'str',
        'search_parameters': 'object',
        'type': 'str'
    }

    attribute_map = {
        'attributes': 'attributes',
        'classification': 'classification',
        'count': 'count',
        'entities': 'entities',
        'full_text_result': 'full_text_result',
        'query_text': 'query_text',
        'query_type': 'query_type',
        'referred_entities': 'referred_entities',
        'scroll_id': 'scroll_id',
        'search_parameters': 'search_parameters',
        'type': 'type'
    }

    def __init__(self, attributes=None, classification=None, count=None, entities=None, full_text_result=None, query_text=None, query_type=None, referred_entities=None, scroll_id=None, search_parameters=None, type=None):
        """ShowUnrelatedTableResponse

        The model defined in huaweicloud sdk

        :param attributes: 
        :type attributes: :class:`huaweicloudsdkdataartsstudio.v1.AttributeSearchResult`
        :param classification: 分类
        :type classification: str
        :param count: 结果总量
        :type count: int
        :param entities: 资产信息
        :type entities: list[:class:`huaweicloudsdkdataartsstudio.v1.AtlasEntityHeader`]
        :param full_text_result: 
        :type full_text_result: list[:class:`huaweicloudsdkdataartsstudio.v1.AtlasFullTextResult`]
        :param query_text: 查询内容
        :type query_text: str
        :param query_type: 查询类型，取值范围DSL,FULL_TEXT,GREMLIN,BASIC,ATTRIBUTE,RELATIONSHIP,ADVANCED
        :type query_type: str
        :param referred_entities: Map&lt;String, AtlasEntityHeader&gt;
        :type referred_entities: object
        :param scroll_id: 滚动条id
        :type scroll_id: str
        :param search_parameters: 参数
        :type search_parameters: object
        :param type: 类型
        :type type: str
        """
        
        super(ShowUnrelatedTableResponse, self).__init__()

        self._attributes = None
        self._classification = None
        self._count = None
        self._entities = None
        self._full_text_result = None
        self._query_text = None
        self._query_type = None
        self._referred_entities = None
        self._scroll_id = None
        self._search_parameters = None
        self._type = None
        self.discriminator = None

        if attributes is not None:
            self.attributes = attributes
        if classification is not None:
            self.classification = classification
        if count is not None:
            self.count = count
        if entities is not None:
            self.entities = entities
        if full_text_result is not None:
            self.full_text_result = full_text_result
        if query_text is not None:
            self.query_text = query_text
        if query_type is not None:
            self.query_type = query_type
        if referred_entities is not None:
            self.referred_entities = referred_entities
        if scroll_id is not None:
            self.scroll_id = scroll_id
        if search_parameters is not None:
            self.search_parameters = search_parameters
        if type is not None:
            self.type = type

    @property
    def attributes(self):
        """Gets the attributes of this ShowUnrelatedTableResponse.

        :return: The attributes of this ShowUnrelatedTableResponse.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.AttributeSearchResult`
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this ShowUnrelatedTableResponse.

        :param attributes: The attributes of this ShowUnrelatedTableResponse.
        :type attributes: :class:`huaweicloudsdkdataartsstudio.v1.AttributeSearchResult`
        """
        self._attributes = attributes

    @property
    def classification(self):
        """Gets the classification of this ShowUnrelatedTableResponse.

        分类

        :return: The classification of this ShowUnrelatedTableResponse.
        :rtype: str
        """
        return self._classification

    @classification.setter
    def classification(self, classification):
        """Sets the classification of this ShowUnrelatedTableResponse.

        分类

        :param classification: The classification of this ShowUnrelatedTableResponse.
        :type classification: str
        """
        self._classification = classification

    @property
    def count(self):
        """Gets the count of this ShowUnrelatedTableResponse.

        结果总量

        :return: The count of this ShowUnrelatedTableResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ShowUnrelatedTableResponse.

        结果总量

        :param count: The count of this ShowUnrelatedTableResponse.
        :type count: int
        """
        self._count = count

    @property
    def entities(self):
        """Gets the entities of this ShowUnrelatedTableResponse.

        资产信息

        :return: The entities of this ShowUnrelatedTableResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.AtlasEntityHeader`]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this ShowUnrelatedTableResponse.

        资产信息

        :param entities: The entities of this ShowUnrelatedTableResponse.
        :type entities: list[:class:`huaweicloudsdkdataartsstudio.v1.AtlasEntityHeader`]
        """
        self._entities = entities

    @property
    def full_text_result(self):
        """Gets the full_text_result of this ShowUnrelatedTableResponse.

        :return: The full_text_result of this ShowUnrelatedTableResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.AtlasFullTextResult`]
        """
        return self._full_text_result

    @full_text_result.setter
    def full_text_result(self, full_text_result):
        """Sets the full_text_result of this ShowUnrelatedTableResponse.

        :param full_text_result: The full_text_result of this ShowUnrelatedTableResponse.
        :type full_text_result: list[:class:`huaweicloudsdkdataartsstudio.v1.AtlasFullTextResult`]
        """
        self._full_text_result = full_text_result

    @property
    def query_text(self):
        """Gets the query_text of this ShowUnrelatedTableResponse.

        查询内容

        :return: The query_text of this ShowUnrelatedTableResponse.
        :rtype: str
        """
        return self._query_text

    @query_text.setter
    def query_text(self, query_text):
        """Sets the query_text of this ShowUnrelatedTableResponse.

        查询内容

        :param query_text: The query_text of this ShowUnrelatedTableResponse.
        :type query_text: str
        """
        self._query_text = query_text

    @property
    def query_type(self):
        """Gets the query_type of this ShowUnrelatedTableResponse.

        查询类型，取值范围DSL,FULL_TEXT,GREMLIN,BASIC,ATTRIBUTE,RELATIONSHIP,ADVANCED

        :return: The query_type of this ShowUnrelatedTableResponse.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        """Sets the query_type of this ShowUnrelatedTableResponse.

        查询类型，取值范围DSL,FULL_TEXT,GREMLIN,BASIC,ATTRIBUTE,RELATIONSHIP,ADVANCED

        :param query_type: The query_type of this ShowUnrelatedTableResponse.
        :type query_type: str
        """
        self._query_type = query_type

    @property
    def referred_entities(self):
        """Gets the referred_entities of this ShowUnrelatedTableResponse.

        Map<String, AtlasEntityHeader>

        :return: The referred_entities of this ShowUnrelatedTableResponse.
        :rtype: object
        """
        return self._referred_entities

    @referred_entities.setter
    def referred_entities(self, referred_entities):
        """Sets the referred_entities of this ShowUnrelatedTableResponse.

        Map<String, AtlasEntityHeader>

        :param referred_entities: The referred_entities of this ShowUnrelatedTableResponse.
        :type referred_entities: object
        """
        self._referred_entities = referred_entities

    @property
    def scroll_id(self):
        """Gets the scroll_id of this ShowUnrelatedTableResponse.

        滚动条id

        :return: The scroll_id of this ShowUnrelatedTableResponse.
        :rtype: str
        """
        return self._scroll_id

    @scroll_id.setter
    def scroll_id(self, scroll_id):
        """Sets the scroll_id of this ShowUnrelatedTableResponse.

        滚动条id

        :param scroll_id: The scroll_id of this ShowUnrelatedTableResponse.
        :type scroll_id: str
        """
        self._scroll_id = scroll_id

    @property
    def search_parameters(self):
        """Gets the search_parameters of this ShowUnrelatedTableResponse.

        参数

        :return: The search_parameters of this ShowUnrelatedTableResponse.
        :rtype: object
        """
        return self._search_parameters

    @search_parameters.setter
    def search_parameters(self, search_parameters):
        """Sets the search_parameters of this ShowUnrelatedTableResponse.

        参数

        :param search_parameters: The search_parameters of this ShowUnrelatedTableResponse.
        :type search_parameters: object
        """
        self._search_parameters = search_parameters

    @property
    def type(self):
        """Gets the type of this ShowUnrelatedTableResponse.

        类型

        :return: The type of this ShowUnrelatedTableResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowUnrelatedTableResponse.

        类型

        :param type: The type of this ShowUnrelatedTableResponse.
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
        if not isinstance(other, ShowUnrelatedTableResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
