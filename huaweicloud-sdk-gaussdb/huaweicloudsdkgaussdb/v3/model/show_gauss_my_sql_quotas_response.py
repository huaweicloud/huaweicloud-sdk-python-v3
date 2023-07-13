# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGaussMySqlQuotasResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'quota_list': 'list[Quota]',
        'total_count': 'int'
    }

    attribute_map = {
        'quota_list': 'quota_list',
        'total_count': 'total_count'
    }

    def __init__(self, quota_list=None, total_count=None):
        """ShowGaussMySqlQuotasResponse

        The model defined in huaweicloud sdk

        :param quota_list: 资源列表对象。
        :type quota_list: list[:class:`huaweicloudsdkgaussdb.v3.Quota`]
        :param total_count: 配额记录的条数。
        :type total_count: int
        """
        
        super(ShowGaussMySqlQuotasResponse, self).__init__()

        self._quota_list = None
        self._total_count = None
        self.discriminator = None

        if quota_list is not None:
            self.quota_list = quota_list
        if total_count is not None:
            self.total_count = total_count

    @property
    def quota_list(self):
        """Gets the quota_list of this ShowGaussMySqlQuotasResponse.

        资源列表对象。

        :return: The quota_list of this ShowGaussMySqlQuotasResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.Quota`]
        """
        return self._quota_list

    @quota_list.setter
    def quota_list(self, quota_list):
        """Sets the quota_list of this ShowGaussMySqlQuotasResponse.

        资源列表对象。

        :param quota_list: The quota_list of this ShowGaussMySqlQuotasResponse.
        :type quota_list: list[:class:`huaweicloudsdkgaussdb.v3.Quota`]
        """
        self._quota_list = quota_list

    @property
    def total_count(self):
        """Gets the total_count of this ShowGaussMySqlQuotasResponse.

        配额记录的条数。

        :return: The total_count of this ShowGaussMySqlQuotasResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ShowGaussMySqlQuotasResponse.

        配额记录的条数。

        :param total_count: The total_count of this ShowGaussMySqlQuotasResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ShowGaussMySqlQuotasResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
