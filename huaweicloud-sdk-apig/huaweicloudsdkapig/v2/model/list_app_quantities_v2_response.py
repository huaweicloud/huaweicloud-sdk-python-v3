# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAppQuantitiesV2Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'authed_nums': 'int',
        'unauthed_nums': 'int'
    }

    attribute_map = {
        'authed_nums': 'authed_nums',
        'unauthed_nums': 'unauthed_nums'
    }

    def __init__(self, authed_nums=None, unauthed_nums=None):
        """ListAppQuantitiesV2Response

        The model defined in huaweicloud sdk

        :param authed_nums: 已进行API访问授权的APP个数
        :type authed_nums: int
        :param unauthed_nums: 未进行API访问授权的APP个数
        :type unauthed_nums: int
        """
        
        super(ListAppQuantitiesV2Response, self).__init__()

        self._authed_nums = None
        self._unauthed_nums = None
        self.discriminator = None

        if authed_nums is not None:
            self.authed_nums = authed_nums
        if unauthed_nums is not None:
            self.unauthed_nums = unauthed_nums

    @property
    def authed_nums(self):
        """Gets the authed_nums of this ListAppQuantitiesV2Response.

        已进行API访问授权的APP个数

        :return: The authed_nums of this ListAppQuantitiesV2Response.
        :rtype: int
        """
        return self._authed_nums

    @authed_nums.setter
    def authed_nums(self, authed_nums):
        """Sets the authed_nums of this ListAppQuantitiesV2Response.

        已进行API访问授权的APP个数

        :param authed_nums: The authed_nums of this ListAppQuantitiesV2Response.
        :type authed_nums: int
        """
        self._authed_nums = authed_nums

    @property
    def unauthed_nums(self):
        """Gets the unauthed_nums of this ListAppQuantitiesV2Response.

        未进行API访问授权的APP个数

        :return: The unauthed_nums of this ListAppQuantitiesV2Response.
        :rtype: int
        """
        return self._unauthed_nums

    @unauthed_nums.setter
    def unauthed_nums(self, unauthed_nums):
        """Sets the unauthed_nums of this ListAppQuantitiesV2Response.

        未进行API访问授权的APP个数

        :param unauthed_nums: The unauthed_nums of this ListAppQuantitiesV2Response.
        :type unauthed_nums: int
        """
        self._unauthed_nums = unauthed_nums

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
        if not isinstance(other, ListAppQuantitiesV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
