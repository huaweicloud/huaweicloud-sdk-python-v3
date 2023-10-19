# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDataSetsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'float',
        'entities': 'list[Entity]',
        'facets': 'object',
        'metrics': 'object',
        'referred_entities': 'object'
    }

    attribute_map = {
        'count': 'count',
        'entities': 'entities',
        'facets': 'facets',
        'metrics': 'metrics',
        'referred_entities': 'referred_entities'
    }

    def __init__(self, count=None, entities=None, facets=None, metrics=None, referred_entities=None):
        """ShowDataSetsResponse

        The model defined in huaweicloud sdk

        :param count: 查询结果总量
        :type count: float
        :param entities: 资产实体列表
        :type entities: list[:class:`huaweicloudsdkdataartsstudio.v1.Entity`]
        :param facets: 资产分类facets维度信息列表，数据结构List&lt;Map&lt;String, List&lt;Aggregation&gt;&gt;&gt; 取值为count
        :type facets: object
        :param metrics: 资产分类metrics维度信息列表，数据结构List&lt;Map&lt;String, List&lt;Aggregation&gt;&gt;&gt;  取值为aggregation
        :type metrics: object
        :param referred_entities: 关联资产，数据类型Map&lt;String, Entity&gt;
        :type referred_entities: object
        """
        
        super(ShowDataSetsResponse, self).__init__()

        self._count = None
        self._entities = None
        self._facets = None
        self._metrics = None
        self._referred_entities = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if entities is not None:
            self.entities = entities
        if facets is not None:
            self.facets = facets
        if metrics is not None:
            self.metrics = metrics
        if referred_entities is not None:
            self.referred_entities = referred_entities

    @property
    def count(self):
        """Gets the count of this ShowDataSetsResponse.

        查询结果总量

        :return: The count of this ShowDataSetsResponse.
        :rtype: float
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ShowDataSetsResponse.

        查询结果总量

        :param count: The count of this ShowDataSetsResponse.
        :type count: float
        """
        self._count = count

    @property
    def entities(self):
        """Gets the entities of this ShowDataSetsResponse.

        资产实体列表

        :return: The entities of this ShowDataSetsResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.Entity`]
        """
        return self._entities

    @entities.setter
    def entities(self, entities):
        """Sets the entities of this ShowDataSetsResponse.

        资产实体列表

        :param entities: The entities of this ShowDataSetsResponse.
        :type entities: list[:class:`huaweicloudsdkdataartsstudio.v1.Entity`]
        """
        self._entities = entities

    @property
    def facets(self):
        """Gets the facets of this ShowDataSetsResponse.

        资产分类facets维度信息列表，数据结构List<Map<String, List<Aggregation>>> 取值为count

        :return: The facets of this ShowDataSetsResponse.
        :rtype: object
        """
        return self._facets

    @facets.setter
    def facets(self, facets):
        """Sets the facets of this ShowDataSetsResponse.

        资产分类facets维度信息列表，数据结构List<Map<String, List<Aggregation>>> 取值为count

        :param facets: The facets of this ShowDataSetsResponse.
        :type facets: object
        """
        self._facets = facets

    @property
    def metrics(self):
        """Gets the metrics of this ShowDataSetsResponse.

        资产分类metrics维度信息列表，数据结构List<Map<String, List<Aggregation>>>  取值为aggregation

        :return: The metrics of this ShowDataSetsResponse.
        :rtype: object
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        """Sets the metrics of this ShowDataSetsResponse.

        资产分类metrics维度信息列表，数据结构List<Map<String, List<Aggregation>>>  取值为aggregation

        :param metrics: The metrics of this ShowDataSetsResponse.
        :type metrics: object
        """
        self._metrics = metrics

    @property
    def referred_entities(self):
        """Gets the referred_entities of this ShowDataSetsResponse.

        关联资产，数据类型Map<String, Entity>

        :return: The referred_entities of this ShowDataSetsResponse.
        :rtype: object
        """
        return self._referred_entities

    @referred_entities.setter
    def referred_entities(self, referred_entities):
        """Sets the referred_entities of this ShowDataSetsResponse.

        关联资产，数据类型Map<String, Entity>

        :param referred_entities: The referred_entities of this ShowDataSetsResponse.
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
        if not isinstance(other, ShowDataSetsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
