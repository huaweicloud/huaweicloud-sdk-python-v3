# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchAuthorizeAppResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'records': 'list[RecordForGetAuthApp]'
    }

    attribute_map = {
        'total': 'total',
        'records': 'records'
    }

    def __init__(self, total=None, records=None):
        """SearchAuthorizeAppResponse

        The model defined in huaweicloud sdk

        :param total: 符合条件的APP总数
        :type total: int
        :param records: 本次返回的APP列表
        :type records: list[:class:`huaweicloudsdkdataartsstudio.v1.RecordForGetAuthApp`]
        """
        
        super(SearchAuthorizeAppResponse, self).__init__()

        self._total = None
        self._records = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if records is not None:
            self.records = records

    @property
    def total(self):
        """Gets the total of this SearchAuthorizeAppResponse.

        符合条件的APP总数

        :return: The total of this SearchAuthorizeAppResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this SearchAuthorizeAppResponse.

        符合条件的APP总数

        :param total: The total of this SearchAuthorizeAppResponse.
        :type total: int
        """
        self._total = total

    @property
    def records(self):
        """Gets the records of this SearchAuthorizeAppResponse.

        本次返回的APP列表

        :return: The records of this SearchAuthorizeAppResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.RecordForGetAuthApp`]
        """
        return self._records

    @records.setter
    def records(self, records):
        """Sets the records of this SearchAuthorizeAppResponse.

        本次返回的APP列表

        :param records: The records of this SearchAuthorizeAppResponse.
        :type records: list[:class:`huaweicloudsdkdataartsstudio.v1.RecordForGetAuthApp`]
        """
        self._records = records

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
        if not isinstance(other, SearchAuthorizeAppResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
