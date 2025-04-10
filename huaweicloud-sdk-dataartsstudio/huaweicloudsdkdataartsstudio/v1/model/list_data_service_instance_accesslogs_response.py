# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDataServiceInstanceAccesslogsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'number': 'int',
        'records': 'list[InstanceAccesslog]'
    }

    attribute_map = {
        'number': 'number',
        'records': 'records'
    }

    def __init__(self, number=None, records=None):
        r"""ListDataServiceInstanceAccesslogsResponse

        The model defined in huaweicloud sdk

        :param number: 访问日志数量。
        :type number: int
        :param records: 访问日志列表。
        :type records: list[:class:`huaweicloudsdkdataartsstudio.v1.InstanceAccesslog`]
        """
        
        super(ListDataServiceInstanceAccesslogsResponse, self).__init__()

        self._number = None
        self._records = None
        self.discriminator = None

        if number is not None:
            self.number = number
        if records is not None:
            self.records = records

    @property
    def number(self):
        r"""Gets the number of this ListDataServiceInstanceAccesslogsResponse.

        访问日志数量。

        :return: The number of this ListDataServiceInstanceAccesslogsResponse.
        :rtype: int
        """
        return self._number

    @number.setter
    def number(self, number):
        r"""Sets the number of this ListDataServiceInstanceAccesslogsResponse.

        访问日志数量。

        :param number: The number of this ListDataServiceInstanceAccesslogsResponse.
        :type number: int
        """
        self._number = number

    @property
    def records(self):
        r"""Gets the records of this ListDataServiceInstanceAccesslogsResponse.

        访问日志列表。

        :return: The records of this ListDataServiceInstanceAccesslogsResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.InstanceAccesslog`]
        """
        return self._records

    @records.setter
    def records(self, records):
        r"""Sets the records of this ListDataServiceInstanceAccesslogsResponse.

        访问日志列表。

        :param records: The records of this ListDataServiceInstanceAccesslogsResponse.
        :type records: list[:class:`huaweicloudsdkdataartsstudio.v1.InstanceAccesslog`]
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
        if not isinstance(other, ListDataServiceInstanceAccesslogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
