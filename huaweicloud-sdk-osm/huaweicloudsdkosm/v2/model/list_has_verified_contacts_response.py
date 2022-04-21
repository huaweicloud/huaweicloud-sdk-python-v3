# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHasVerifiedContactsResponse(SdkResponse):

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
        'contact_list': 'list[ContactV2]'
    }

    attribute_map = {
        'count': 'count',
        'contact_list': 'contact_list'
    }

    def __init__(self, count=None, contact_list=None):
        """ListHasVerifiedContactsResponse

        The model defined in huaweicloud sdk

        :param count: 总数
        :type count: int
        :param contact_list: 联系方式列表
        :type contact_list: list[:class:`huaweicloudsdkosm.v2.ContactV2`]
        """
        
        super(ListHasVerifiedContactsResponse, self).__init__()

        self._count = None
        self._contact_list = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if contact_list is not None:
            self.contact_list = contact_list

    @property
    def count(self):
        """Gets the count of this ListHasVerifiedContactsResponse.

        总数

        :return: The count of this ListHasVerifiedContactsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListHasVerifiedContactsResponse.

        总数

        :param count: The count of this ListHasVerifiedContactsResponse.
        :type count: int
        """
        self._count = count

    @property
    def contact_list(self):
        """Gets the contact_list of this ListHasVerifiedContactsResponse.

        联系方式列表

        :return: The contact_list of this ListHasVerifiedContactsResponse.
        :rtype: list[:class:`huaweicloudsdkosm.v2.ContactV2`]
        """
        return self._contact_list

    @contact_list.setter
    def contact_list(self, contact_list):
        """Sets the contact_list of this ListHasVerifiedContactsResponse.

        联系方式列表

        :param contact_list: The contact_list of this ListHasVerifiedContactsResponse.
        :type contact_list: list[:class:`huaweicloudsdkosm.v2.ContactV2`]
        """
        self._contact_list = contact_list

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
        if not isinstance(other, ListHasVerifiedContactsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
