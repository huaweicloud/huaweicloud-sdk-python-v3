# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HybridSearchBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'store_name': 'str',
        'collection_name': 'str',
        'output_fields': 'list[str]',
        'top_k': 'int',
        'offset': 'int',
        'sub_search': 'list[SubSearch]',
        'rerank': 'Rerank'
    }

    attribute_map = {
        'store_name': 'store_name',
        'collection_name': 'collection_name',
        'output_fields': 'output_fields',
        'top_k': 'top_k',
        'offset': 'offset',
        'sub_search': 'sub_search',
        'rerank': 'rerank'
    }

    def __init__(self, store_name=None, collection_name=None, output_fields=None, top_k=None, offset=None, sub_search=None, rerank=None):
        r"""HybridSearchBody

        The model defined in huaweicloud sdk

        :param store_name: 知识仓实例名称
        :type store_name: str
        :param collection_name: collection名称
        :type collection_name: str
        :param output_fields: 配置需返回的字段。
        :type output_fields: list[str]
        :param top_k: 返回个数限制
        :type top_k: int
        :param offset: 搜索结果中要跳过的entity数。
        :type offset: int
        :param sub_search: 
        :type sub_search: list[:class:`huaweicloudsdkdwr.v1.SubSearch`]
        :param rerank: 
        :type rerank: :class:`huaweicloudsdkdwr.v1.Rerank`
        """
        
        

        self._store_name = None
        self._collection_name = None
        self._output_fields = None
        self._top_k = None
        self._offset = None
        self._sub_search = None
        self._rerank = None
        self.discriminator = None

        self.store_name = store_name
        self.collection_name = collection_name
        if output_fields is not None:
            self.output_fields = output_fields
        if top_k is not None:
            self.top_k = top_k
        if offset is not None:
            self.offset = offset
        self.sub_search = sub_search
        if rerank is not None:
            self.rerank = rerank

    @property
    def store_name(self):
        r"""Gets the store_name of this HybridSearchBody.

        知识仓实例名称

        :return: The store_name of this HybridSearchBody.
        :rtype: str
        """
        return self._store_name

    @store_name.setter
    def store_name(self, store_name):
        r"""Sets the store_name of this HybridSearchBody.

        知识仓实例名称

        :param store_name: The store_name of this HybridSearchBody.
        :type store_name: str
        """
        self._store_name = store_name

    @property
    def collection_name(self):
        r"""Gets the collection_name of this HybridSearchBody.

        collection名称

        :return: The collection_name of this HybridSearchBody.
        :rtype: str
        """
        return self._collection_name

    @collection_name.setter
    def collection_name(self, collection_name):
        r"""Sets the collection_name of this HybridSearchBody.

        collection名称

        :param collection_name: The collection_name of this HybridSearchBody.
        :type collection_name: str
        """
        self._collection_name = collection_name

    @property
    def output_fields(self):
        r"""Gets the output_fields of this HybridSearchBody.

        配置需返回的字段。

        :return: The output_fields of this HybridSearchBody.
        :rtype: list[str]
        """
        return self._output_fields

    @output_fields.setter
    def output_fields(self, output_fields):
        r"""Sets the output_fields of this HybridSearchBody.

        配置需返回的字段。

        :param output_fields: The output_fields of this HybridSearchBody.
        :type output_fields: list[str]
        """
        self._output_fields = output_fields

    @property
    def top_k(self):
        r"""Gets the top_k of this HybridSearchBody.

        返回个数限制

        :return: The top_k of this HybridSearchBody.
        :rtype: int
        """
        return self._top_k

    @top_k.setter
    def top_k(self, top_k):
        r"""Sets the top_k of this HybridSearchBody.

        返回个数限制

        :param top_k: The top_k of this HybridSearchBody.
        :type top_k: int
        """
        self._top_k = top_k

    @property
    def offset(self):
        r"""Gets the offset of this HybridSearchBody.

        搜索结果中要跳过的entity数。

        :return: The offset of this HybridSearchBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this HybridSearchBody.

        搜索结果中要跳过的entity数。

        :param offset: The offset of this HybridSearchBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def sub_search(self):
        r"""Gets the sub_search of this HybridSearchBody.

        :return: The sub_search of this HybridSearchBody.
        :rtype: list[:class:`huaweicloudsdkdwr.v1.SubSearch`]
        """
        return self._sub_search

    @sub_search.setter
    def sub_search(self, sub_search):
        r"""Sets the sub_search of this HybridSearchBody.

        :param sub_search: The sub_search of this HybridSearchBody.
        :type sub_search: list[:class:`huaweicloudsdkdwr.v1.SubSearch`]
        """
        self._sub_search = sub_search

    @property
    def rerank(self):
        r"""Gets the rerank of this HybridSearchBody.

        :return: The rerank of this HybridSearchBody.
        :rtype: :class:`huaweicloudsdkdwr.v1.Rerank`
        """
        return self._rerank

    @rerank.setter
    def rerank(self, rerank):
        r"""Sets the rerank of this HybridSearchBody.

        :param rerank: The rerank of this HybridSearchBody.
        :type rerank: :class:`huaweicloudsdkdwr.v1.Rerank`
        """
        self._rerank = rerank

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
        if not isinstance(other, HybridSearchBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
