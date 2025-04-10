# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFindingsReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'filters': 'list[FindingFilter]',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'filters': 'filters',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, filters=None, limit=None, marker=None):
        r"""ListFindingsReqBody

        The model defined in huaweicloud sdk

        :param filters: 匹配要返回的访问分析结果的筛选器。
        :type filters: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.FindingFilter`]
        :param limit: 单页最大结果数。
        :type limit: int
        :param marker: 页面标记。
        :type marker: str
        """
        
        

        self._filters = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        if filters is not None:
            self.filters = filters
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def filters(self):
        r"""Gets the filters of this ListFindingsReqBody.

        匹配要返回的访问分析结果的筛选器。

        :return: The filters of this ListFindingsReqBody.
        :rtype: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.FindingFilter`]
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        r"""Sets the filters of this ListFindingsReqBody.

        匹配要返回的访问分析结果的筛选器。

        :param filters: The filters of this ListFindingsReqBody.
        :type filters: list[:class:`huaweicloudsdkiamaccessanalyzer.v1.FindingFilter`]
        """
        self._filters = filters

    @property
    def limit(self):
        r"""Gets the limit of this ListFindingsReqBody.

        单页最大结果数。

        :return: The limit of this ListFindingsReqBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListFindingsReqBody.

        单页最大结果数。

        :param limit: The limit of this ListFindingsReqBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListFindingsReqBody.

        页面标记。

        :return: The marker of this ListFindingsReqBody.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListFindingsReqBody.

        页面标记。

        :param marker: The marker of this ListFindingsReqBody.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListFindingsReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
