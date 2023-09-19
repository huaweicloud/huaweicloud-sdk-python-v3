# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCloudPhonesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'phones': 'list[Phone]',
        'request_id': 'str',
        'count': 'int'
    }

    attribute_map = {
        'phones': 'phones',
        'request_id': 'request_id',
        'count': 'count'
    }

    def __init__(self, phones=None, request_id=None, count=None):
        """ListCloudPhonesResponse

        The model defined in huaweicloud sdk

        :param phones: 云手机信息。
        :type phones: list[:class:`huaweicloudsdkcph.v1.Phone`]
        :param request_id: 请求的唯一标识ID。
        :type request_id: str
        :param count: 实例总数。
        :type count: int
        """
        
        super(ListCloudPhonesResponse, self).__init__()

        self._phones = None
        self._request_id = None
        self._count = None
        self.discriminator = None

        if phones is not None:
            self.phones = phones
        if request_id is not None:
            self.request_id = request_id
        if count is not None:
            self.count = count

    @property
    def phones(self):
        """Gets the phones of this ListCloudPhonesResponse.

        云手机信息。

        :return: The phones of this ListCloudPhonesResponse.
        :rtype: list[:class:`huaweicloudsdkcph.v1.Phone`]
        """
        return self._phones

    @phones.setter
    def phones(self, phones):
        """Sets the phones of this ListCloudPhonesResponse.

        云手机信息。

        :param phones: The phones of this ListCloudPhonesResponse.
        :type phones: list[:class:`huaweicloudsdkcph.v1.Phone`]
        """
        self._phones = phones

    @property
    def request_id(self):
        """Gets the request_id of this ListCloudPhonesResponse.

        请求的唯一标识ID。

        :return: The request_id of this ListCloudPhonesResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ListCloudPhonesResponse.

        请求的唯一标识ID。

        :param request_id: The request_id of this ListCloudPhonesResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def count(self):
        """Gets the count of this ListCloudPhonesResponse.

        实例总数。

        :return: The count of this ListCloudPhonesResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListCloudPhonesResponse.

        实例总数。

        :param count: The count of this ListCloudPhonesResponse.
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
        if not isinstance(other, ListCloudPhonesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
