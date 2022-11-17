# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSubCustomerCouponsResponse(SdkResponse):

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
        'user_coupons': 'list[IQueryUserCouponsResultV2]'
    }

    attribute_map = {
        'count': 'count',
        'user_coupons': 'user_coupons'
    }

    def __init__(self, count=None, user_coupons=None):
        """ListSubCustomerCouponsResponse

        The model defined in huaweicloud sdk

        :param count: 符合查询条件的总条数。
        :type count: int
        :param user_coupons: 优惠券记录。 具体请参见表2。
        :type user_coupons: list[:class:`huaweicloudsdkbss.v2.IQueryUserCouponsResultV2`]
        """
        
        super(ListSubCustomerCouponsResponse, self).__init__()

        self._count = None
        self._user_coupons = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if user_coupons is not None:
            self.user_coupons = user_coupons

    @property
    def count(self):
        """Gets the count of this ListSubCustomerCouponsResponse.

        符合查询条件的总条数。

        :return: The count of this ListSubCustomerCouponsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListSubCustomerCouponsResponse.

        符合查询条件的总条数。

        :param count: The count of this ListSubCustomerCouponsResponse.
        :type count: int
        """
        self._count = count

    @property
    def user_coupons(self):
        """Gets the user_coupons of this ListSubCustomerCouponsResponse.

        优惠券记录。 具体请参见表2。

        :return: The user_coupons of this ListSubCustomerCouponsResponse.
        :rtype: list[:class:`huaweicloudsdkbss.v2.IQueryUserCouponsResultV2`]
        """
        return self._user_coupons

    @user_coupons.setter
    def user_coupons(self, user_coupons):
        """Sets the user_coupons of this ListSubCustomerCouponsResponse.

        优惠券记录。 具体请参见表2。

        :param user_coupons: The user_coupons of this ListSubCustomerCouponsResponse.
        :type user_coupons: list[:class:`huaweicloudsdkbss.v2.IQueryUserCouponsResultV2`]
        """
        self._user_coupons = user_coupons

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
        if not isinstance(other, ListSubCustomerCouponsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
