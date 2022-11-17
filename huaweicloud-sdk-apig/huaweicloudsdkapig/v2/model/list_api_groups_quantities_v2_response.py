# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListApiGroupsQuantitiesV2Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offsell_nums': 'int',
        'onsell_nums': 'int'
    }

    attribute_map = {
        'offsell_nums': 'offsell_nums',
        'onsell_nums': 'onsell_nums'
    }

    def __init__(self, offsell_nums=None, onsell_nums=None):
        """ListApiGroupsQuantitiesV2Response

        The model defined in huaweicloud sdk

        :param offsell_nums: 未上架的API分组个数  暂不支持
        :type offsell_nums: int
        :param onsell_nums: 已上架的API分组个数
        :type onsell_nums: int
        """
        
        super(ListApiGroupsQuantitiesV2Response, self).__init__()

        self._offsell_nums = None
        self._onsell_nums = None
        self.discriminator = None

        if offsell_nums is not None:
            self.offsell_nums = offsell_nums
        if onsell_nums is not None:
            self.onsell_nums = onsell_nums

    @property
    def offsell_nums(self):
        """Gets the offsell_nums of this ListApiGroupsQuantitiesV2Response.

        未上架的API分组个数  暂不支持

        :return: The offsell_nums of this ListApiGroupsQuantitiesV2Response.
        :rtype: int
        """
        return self._offsell_nums

    @offsell_nums.setter
    def offsell_nums(self, offsell_nums):
        """Sets the offsell_nums of this ListApiGroupsQuantitiesV2Response.

        未上架的API分组个数  暂不支持

        :param offsell_nums: The offsell_nums of this ListApiGroupsQuantitiesV2Response.
        :type offsell_nums: int
        """
        self._offsell_nums = offsell_nums

    @property
    def onsell_nums(self):
        """Gets the onsell_nums of this ListApiGroupsQuantitiesV2Response.

        已上架的API分组个数

        :return: The onsell_nums of this ListApiGroupsQuantitiesV2Response.
        :rtype: int
        """
        return self._onsell_nums

    @onsell_nums.setter
    def onsell_nums(self, onsell_nums):
        """Sets the onsell_nums of this ListApiGroupsQuantitiesV2Response.

        已上架的API分组个数

        :param onsell_nums: The onsell_nums of this ListApiGroupsQuantitiesV2Response.
        :type onsell_nums: int
        """
        self._onsell_nums = onsell_nums

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
        if not isinstance(other, ListApiGroupsQuantitiesV2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
