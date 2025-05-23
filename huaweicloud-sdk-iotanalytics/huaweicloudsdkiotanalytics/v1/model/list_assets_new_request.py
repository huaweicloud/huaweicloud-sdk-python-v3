# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAssetsNewRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'filter': 'str',
        'type': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'filter': 'filter',
        'type': 'type'
    }

    def __init__(self, limit=None, offset=None, filter=None, type=None):
        r"""ListAssetsNewRequest

        The model defined in huaweicloud sdk

        :param limit: 每页记录数
        :type limit: int
        :param offset: 页码
        :type offset: int
        :param filter: 查询过滤器 示例： {\&quot;key\&quot;:\&quot;xxx\&quot;} {\&quot;key1\&quot;:\&quot;xxx\&quot;,\&quot;key2\&quot;:\&quot;xxx\&quot;} {\&quot;key\&quot;:{\&quot;eq|like\&quot;:\&quot;xxx\&quot;}} {\&quot;key\&quot;:{\&quot;in\&quot;:[\&quot;xxx\&quot;,\&quot;xxx\&quot;]}} {\&quot;or\&quot;:{\&quot;key1\&quot;:\&quot;xxx\&quot;,\&quot;key2\&quot;:{\&quot;eq|like\&quot;:\&quot;xxx\&quot;},\&quot;key3\&quot;:{\&quot;in\&quot;:[\&quot;xxx\&quot;,\&quot;xxx\&quot;]}}} {\&quot;and\&quot;:{\&quot;key1\&quot;:\&quot;xxx\&quot;,\&quot;key2\&quot;:{\&quot;eq|like\&quot;:\&quot;xxx\&quot;},\&quot;key3\&quot;:{\&quot;in\&quot;:[\&quot;xxx\&quot;,\&quot;xxx\&quot;]}}} 支持的key： asset_model_id，asset_id，parent，name，display_name，root，state，job_id 注意： job_id只在RELEASE态下生效，只支持contain过滤 {\&quot;job_id\&quot;:{\&quot;contain\&quot;:\&quot;xxx\&quot;}}
        :type filter: str
        :param type: SKETCH：草稿态；RELEASE：发布态
        :type type: str
        """
        
        

        self._limit = None
        self._offset = None
        self._filter = None
        self._type = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if filter is not None:
            self.filter = filter
        self.type = type

    @property
    def limit(self):
        r"""Gets the limit of this ListAssetsNewRequest.

        每页记录数

        :return: The limit of this ListAssetsNewRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAssetsNewRequest.

        每页记录数

        :param limit: The limit of this ListAssetsNewRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListAssetsNewRequest.

        页码

        :return: The offset of this ListAssetsNewRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAssetsNewRequest.

        页码

        :param offset: The offset of this ListAssetsNewRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def filter(self):
        r"""Gets the filter of this ListAssetsNewRequest.

        查询过滤器 示例： {\"key\":\"xxx\"} {\"key1\":\"xxx\",\"key2\":\"xxx\"} {\"key\":{\"eq|like\":\"xxx\"}} {\"key\":{\"in\":[\"xxx\",\"xxx\"]}} {\"or\":{\"key1\":\"xxx\",\"key2\":{\"eq|like\":\"xxx\"},\"key3\":{\"in\":[\"xxx\",\"xxx\"]}}} {\"and\":{\"key1\":\"xxx\",\"key2\":{\"eq|like\":\"xxx\"},\"key3\":{\"in\":[\"xxx\",\"xxx\"]}}} 支持的key： asset_model_id，asset_id，parent，name，display_name，root，state，job_id 注意： job_id只在RELEASE态下生效，只支持contain过滤 {\"job_id\":{\"contain\":\"xxx\"}}

        :return: The filter of this ListAssetsNewRequest.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this ListAssetsNewRequest.

        查询过滤器 示例： {\"key\":\"xxx\"} {\"key1\":\"xxx\",\"key2\":\"xxx\"} {\"key\":{\"eq|like\":\"xxx\"}} {\"key\":{\"in\":[\"xxx\",\"xxx\"]}} {\"or\":{\"key1\":\"xxx\",\"key2\":{\"eq|like\":\"xxx\"},\"key3\":{\"in\":[\"xxx\",\"xxx\"]}}} {\"and\":{\"key1\":\"xxx\",\"key2\":{\"eq|like\":\"xxx\"},\"key3\":{\"in\":[\"xxx\",\"xxx\"]}}} 支持的key： asset_model_id，asset_id，parent，name，display_name，root，state，job_id 注意： job_id只在RELEASE态下生效，只支持contain过滤 {\"job_id\":{\"contain\":\"xxx\"}}

        :param filter: The filter of this ListAssetsNewRequest.
        :type filter: str
        """
        self._filter = filter

    @property
    def type(self):
        r"""Gets the type of this ListAssetsNewRequest.

        SKETCH：草稿态；RELEASE：发布态

        :return: The type of this ListAssetsNewRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListAssetsNewRequest.

        SKETCH：草稿态；RELEASE：发布态

        :param type: The type of this ListAssetsNewRequest.
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
        if not isinstance(other, ListAssetsNewRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
