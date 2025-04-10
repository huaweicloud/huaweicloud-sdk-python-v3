# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListMetadatas2Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'schema_count': 'int',
        'schema_list': 'list[ListMetadatasRespSchemaList]'
    }

    attribute_map = {
        'schema_count': 'schema_count',
        'schema_list': 'schema_list'
    }

    def __init__(self, schema_count=None, schema_list=None):
        r"""ListMetadatas2Response

        The model defined in huaweicloud sdk

        :param schema_count: 元数据返回个数。请求失败时，字段为空。
        :type schema_count: int
        :param schema_list: 当前projectId下的所有元数据列表。请求失败时，字段为空。
        :type schema_list: list[:class:`huaweicloudsdkges.v2.ListMetadatasRespSchemaList`]
        """
        
        super(ListMetadatas2Response, self).__init__()

        self._schema_count = None
        self._schema_list = None
        self.discriminator = None

        if schema_count is not None:
            self.schema_count = schema_count
        if schema_list is not None:
            self.schema_list = schema_list

    @property
    def schema_count(self):
        r"""Gets the schema_count of this ListMetadatas2Response.

        元数据返回个数。请求失败时，字段为空。

        :return: The schema_count of this ListMetadatas2Response.
        :rtype: int
        """
        return self._schema_count

    @schema_count.setter
    def schema_count(self, schema_count):
        r"""Sets the schema_count of this ListMetadatas2Response.

        元数据返回个数。请求失败时，字段为空。

        :param schema_count: The schema_count of this ListMetadatas2Response.
        :type schema_count: int
        """
        self._schema_count = schema_count

    @property
    def schema_list(self):
        r"""Gets the schema_list of this ListMetadatas2Response.

        当前projectId下的所有元数据列表。请求失败时，字段为空。

        :return: The schema_list of this ListMetadatas2Response.
        :rtype: list[:class:`huaweicloudsdkges.v2.ListMetadatasRespSchemaList`]
        """
        return self._schema_list

    @schema_list.setter
    def schema_list(self, schema_list):
        r"""Sets the schema_list of this ListMetadatas2Response.

        当前projectId下的所有元数据列表。请求失败时，字段为空。

        :param schema_list: The schema_list of this ListMetadatas2Response.
        :type schema_list: list[:class:`huaweicloudsdkges.v2.ListMetadatasRespSchemaList`]
        """
        self._schema_list = schema_list

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
        if not isinstance(other, ListMetadatas2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
