# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSchemasResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'schemas': 'list[SchemaInfo]',
        'count': 'int'
    }

    attribute_map = {
        'schemas': 'schemas',
        'count': 'count'
    }

    def __init__(self, schemas=None, count=None):
        r"""ListSchemasResponse

        The model defined in huaweicloud sdk

        :param schemas: **参数解释**： 集群模式空间信息列表。 **取值范围**： 不涉及。
        :type schemas: list[:class:`huaweicloudsdkdws.v2.SchemaInfo`]
        :param count: **参数解释**： 总数量。 **取值范围**： 不涉及。
        :type count: int
        """
        
        super(ListSchemasResponse, self).__init__()

        self._schemas = None
        self._count = None
        self.discriminator = None

        if schemas is not None:
            self.schemas = schemas
        if count is not None:
            self.count = count

    @property
    def schemas(self):
        r"""Gets the schemas of this ListSchemasResponse.

        **参数解释**： 集群模式空间信息列表。 **取值范围**： 不涉及。

        :return: The schemas of this ListSchemasResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.SchemaInfo`]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        r"""Sets the schemas of this ListSchemasResponse.

        **参数解释**： 集群模式空间信息列表。 **取值范围**： 不涉及。

        :param schemas: The schemas of this ListSchemasResponse.
        :type schemas: list[:class:`huaweicloudsdkdws.v2.SchemaInfo`]
        """
        self._schemas = schemas

    @property
    def count(self):
        r"""Gets the count of this ListSchemasResponse.

        **参数解释**： 总数量。 **取值范围**： 不涉及。

        :return: The count of this ListSchemasResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListSchemasResponse.

        **参数解释**： 总数量。 **取值范围**： 不涉及。

        :param count: The count of this ListSchemasResponse.
        :type count: int
        """
        self._count = count

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
        if not isinstance(other, ListSchemasResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
