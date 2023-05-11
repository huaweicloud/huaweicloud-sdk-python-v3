# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LastAssetPropertyValueRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tags': 'dict(str, object)',
        'property_filter': 'list[PropertyFilter]',
        'property_names': 'list[str]'
    }

    attribute_map = {
        'tags': 'tags',
        'property_filter': 'property_filter',
        'property_names': 'property_names'
    }

    def __init__(self, tags=None, property_filter=None, property_names=None):
        """LastAssetPropertyValueRequest

        The model defined in huaweicloud sdk

        :param tags: 对property按指定tags标签进行过滤查询，填入资产标签属性的属性名与属性值，不可为空，例如 {\&quot;tagPropertyA\&quot;: \&quot;id0001\&quot;}；注意，标签过滤只对打上标签时刻之后的数据生效，打标签之前的数据不能通过标签过滤
        :type tags: dict(str, object)
        :param property_filter: 属性过滤器，最多5个
        :type property_filter: list[:class:`huaweicloudsdkiotanalytics.v1.PropertyFilter`]
        :param property_names: 待查询的资产属性名列表,不携带该字段表示查询全部
        :type property_names: list[str]
        """
        
        

        self._tags = None
        self._property_filter = None
        self._property_names = None
        self.discriminator = None

        if tags is not None:
            self.tags = tags
        if property_filter is not None:
            self.property_filter = property_filter
        if property_names is not None:
            self.property_names = property_names

    @property
    def tags(self):
        """Gets the tags of this LastAssetPropertyValueRequest.

        对property按指定tags标签进行过滤查询，填入资产标签属性的属性名与属性值，不可为空，例如 {\"tagPropertyA\": \"id0001\"}；注意，标签过滤只对打上标签时刻之后的数据生效，打标签之前的数据不能通过标签过滤

        :return: The tags of this LastAssetPropertyValueRequest.
        :rtype: dict(str, object)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this LastAssetPropertyValueRequest.

        对property按指定tags标签进行过滤查询，填入资产标签属性的属性名与属性值，不可为空，例如 {\"tagPropertyA\": \"id0001\"}；注意，标签过滤只对打上标签时刻之后的数据生效，打标签之前的数据不能通过标签过滤

        :param tags: The tags of this LastAssetPropertyValueRequest.
        :type tags: dict(str, object)
        """
        self._tags = tags

    @property
    def property_filter(self):
        """Gets the property_filter of this LastAssetPropertyValueRequest.

        属性过滤器，最多5个

        :return: The property_filter of this LastAssetPropertyValueRequest.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.PropertyFilter`]
        """
        return self._property_filter

    @property_filter.setter
    def property_filter(self, property_filter):
        """Sets the property_filter of this LastAssetPropertyValueRequest.

        属性过滤器，最多5个

        :param property_filter: The property_filter of this LastAssetPropertyValueRequest.
        :type property_filter: list[:class:`huaweicloudsdkiotanalytics.v1.PropertyFilter`]
        """
        self._property_filter = property_filter

    @property
    def property_names(self):
        """Gets the property_names of this LastAssetPropertyValueRequest.

        待查询的资产属性名列表,不携带该字段表示查询全部

        :return: The property_names of this LastAssetPropertyValueRequest.
        :rtype: list[str]
        """
        return self._property_names

    @property_names.setter
    def property_names(self, property_names):
        """Sets the property_names of this LastAssetPropertyValueRequest.

        待查询的资产属性名列表,不携带该字段表示查询全部

        :param property_names: The property_names of this LastAssetPropertyValueRequest.
        :type property_names: list[str]
        """
        self._property_names = property_names

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
        if not isinstance(other, LastAssetPropertyValueRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
