# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCountiesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'counties': 'list[County]'
    }

    attribute_map = {
        'count': 'count',
        'counties': 'counties'
    }

    def __init__(self, count=None, counties=None):
        """ListCountiesResponse

        The model defined in huaweicloud sdk

        :param count: 查询个数，成功的时候返回。
        :type count: int
        :param counties: 区县信息列表，成功的时候返回，具体参见表2。
        :type counties: list[:class:`huaweicloudsdkbss.v2.County`]
        """
        
        super(ListCountiesResponse, self).__init__()

        self._count = None
        self._counties = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if counties is not None:
            self.counties = counties

    @property
    def count(self):
        """Gets the count of this ListCountiesResponse.

        查询个数，成功的时候返回。

        :return: The count of this ListCountiesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListCountiesResponse.

        查询个数，成功的时候返回。

        :param count: The count of this ListCountiesResponse.
        :type count: int
        """
        self._count = count

    @property
    def counties(self):
        """Gets the counties of this ListCountiesResponse.

        区县信息列表，成功的时候返回，具体参见表2。

        :return: The counties of this ListCountiesResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.County`]
        """
        return self._counties

    @counties.setter
    def counties(self, counties):
        """Sets the counties of this ListCountiesResponse.

        区县信息列表，成功的时候返回，具体参见表2。

        :param counties: The counties of this ListCountiesResponse.
        :type counties: list[:class:`huaweicloudsdkbss.v2.County`]
        """
        self._counties = counties

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
        if not isinstance(other, ListCountiesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
