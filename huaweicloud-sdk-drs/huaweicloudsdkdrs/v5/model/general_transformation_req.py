# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GeneralTransformationReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'filter_object_list': 'list[DataFilterObjectInfo]',
        'source_filter_condition': 'str'
    }

    attribute_map = {
        'filter_object_list': 'filter_object_list',
        'source_filter_condition': 'source_filter_condition'
    }

    def __init__(self, filter_object_list=None, source_filter_condition=None):
        r"""GeneralTransformationReq

        The model defined in huaweicloud sdk

        :param filter_object_list: 数据过滤对象列表。包含需要校验的具体数据库对象（库/Schema/表）信息，在简单条件过滤场景下为必填项。列表中的每个元素代表一个待过滤的数据库对象。适用条件：简单过滤条件场景下必填。
        :type filter_object_list: list[:class:`huaweicloudsdkdrs.v5.DataFilterObjectInfo`]
        :param source_filter_condition: 源端数据库的过滤条件SQL语句。用于定义源库数据过滤规则，支持SQL子查询等高级过滤表达式。当数据过滤涉及子查询场景时，需要通过此字段配置查询条件。
        :type source_filter_condition: str
        """
        
        

        self._filter_object_list = None
        self._source_filter_condition = None
        self.discriminator = None

        if filter_object_list is not None:
            self.filter_object_list = filter_object_list
        if source_filter_condition is not None:
            self.source_filter_condition = source_filter_condition

    @property
    def filter_object_list(self):
        r"""Gets the filter_object_list of this GeneralTransformationReq.

        数据过滤对象列表。包含需要校验的具体数据库对象（库/Schema/表）信息，在简单条件过滤场景下为必填项。列表中的每个元素代表一个待过滤的数据库对象。适用条件：简单过滤条件场景下必填。

        :return: The filter_object_list of this GeneralTransformationReq.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.DataFilterObjectInfo`]
        """
        return self._filter_object_list

    @filter_object_list.setter
    def filter_object_list(self, filter_object_list):
        r"""Sets the filter_object_list of this GeneralTransformationReq.

        数据过滤对象列表。包含需要校验的具体数据库对象（库/Schema/表）信息，在简单条件过滤场景下为必填项。列表中的每个元素代表一个待过滤的数据库对象。适用条件：简单过滤条件场景下必填。

        :param filter_object_list: The filter_object_list of this GeneralTransformationReq.
        :type filter_object_list: list[:class:`huaweicloudsdkdrs.v5.DataFilterObjectInfo`]
        """
        self._filter_object_list = filter_object_list

    @property
    def source_filter_condition(self):
        r"""Gets the source_filter_condition of this GeneralTransformationReq.

        源端数据库的过滤条件SQL语句。用于定义源库数据过滤规则，支持SQL子查询等高级过滤表达式。当数据过滤涉及子查询场景时，需要通过此字段配置查询条件。

        :return: The source_filter_condition of this GeneralTransformationReq.
        :rtype: str
        """
        return self._source_filter_condition

    @source_filter_condition.setter
    def source_filter_condition(self, source_filter_condition):
        r"""Sets the source_filter_condition of this GeneralTransformationReq.

        源端数据库的过滤条件SQL语句。用于定义源库数据过滤规则，支持SQL子查询等高级过滤表达式。当数据过滤涉及子查询场景时，需要通过此字段配置查询条件。

        :param source_filter_condition: The source_filter_condition of this GeneralTransformationReq.
        :type source_filter_condition: str
        """
        self._source_filter_condition = source_filter_condition

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GeneralTransformationReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
