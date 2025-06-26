# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListQueriesData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'queries': 'list[ListQueriesDto]',
        'status': 'ListQueriesStatus'
    }

    attribute_map = {
        'queries': 'queries',
        'status': 'status'
    }

    def __init__(self, queries=None, status=None):
        r"""ListQueriesData

        The model defined in huaweicloud sdk

        :param queries: **参数解释**： 查询数据列表。 **取值范围**： 不涉及。
        :type queries: list[:class:`huaweicloudsdkdws.v2.ListQueriesDto`]
        :param status: 
        :type status: :class:`huaweicloudsdkdws.v2.ListQueriesStatus`
        """
        
        

        self._queries = None
        self._status = None
        self.discriminator = None

        if queries is not None:
            self.queries = queries
        if status is not None:
            self.status = status

    @property
    def queries(self):
        r"""Gets the queries of this ListQueriesData.

        **参数解释**： 查询数据列表。 **取值范围**： 不涉及。

        :return: The queries of this ListQueriesData.
        :rtype: list[:class:`huaweicloudsdkdws.v2.ListQueriesDto`]
        """
        return self._queries

    @queries.setter
    def queries(self, queries):
        r"""Sets the queries of this ListQueriesData.

        **参数解释**： 查询数据列表。 **取值范围**： 不涉及。

        :param queries: The queries of this ListQueriesData.
        :type queries: list[:class:`huaweicloudsdkdws.v2.ListQueriesDto`]
        """
        self._queries = queries

    @property
    def status(self):
        r"""Gets the status of this ListQueriesData.

        :return: The status of this ListQueriesData.
        :rtype: :class:`huaweicloudsdkdws.v2.ListQueriesStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListQueriesData.

        :param status: The status of this ListQueriesData.
        :type status: :class:`huaweicloudsdkdws.v2.ListQueriesStatus`
        """
        self._status = status

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
        if not isinstance(other, ListQueriesData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
