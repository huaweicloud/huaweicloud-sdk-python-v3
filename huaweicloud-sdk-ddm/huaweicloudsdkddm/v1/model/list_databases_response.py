# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDatabasesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'databases': 'list[GetDatabaseInfo]',
        'total': 'int'
    }

    attribute_map = {
        'databases': 'databases',
        'total': 'total'
    }

    def __init__(self, databases=None, total=None):
        r"""ListDatabasesResponse

        The model defined in huaweicloud sdk

        :param databases: 逻辑库相关信息的集合
        :type databases: list[:class:`huaweicloudsdkddm.v1.GetDatabaseInfo`]
        :param total: 总条数
        :type total: int
        """
        
        super(ListDatabasesResponse, self).__init__()

        self._databases = None
        self._total = None
        self.discriminator = None

        if databases is not None:
            self.databases = databases
        if total is not None:
            self.total = total

    @property
    def databases(self):
        r"""Gets the databases of this ListDatabasesResponse.

        逻辑库相关信息的集合

        :return: The databases of this ListDatabasesResponse.
        :rtype: list[:class:`huaweicloudsdkddm.v1.GetDatabaseInfo`]
        """
        return self._databases

    @databases.setter
    def databases(self, databases):
        r"""Sets the databases of this ListDatabasesResponse.

        逻辑库相关信息的集合

        :param databases: The databases of this ListDatabasesResponse.
        :type databases: list[:class:`huaweicloudsdkddm.v1.GetDatabaseInfo`]
        """
        self._databases = databases

    @property
    def total(self):
        r"""Gets the total of this ListDatabasesResponse.

        总条数

        :return: The total of this ListDatabasesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListDatabasesResponse.

        总条数

        :param total: The total of this ListDatabasesResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListDatabasesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
