# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListIndirectPartnersResponse(SdkResponse):


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
        'indirect_partners': 'list[IndirectPartnerInfo]'
    }

    attribute_map = {
        'count': 'count',
        'indirect_partners': 'indirect_partners'
    }

    def __init__(self, count=None, indirect_partners=None):
        """ListIndirectPartnersResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._count = None
        self._indirect_partners = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if indirect_partners is not None:
            self.indirect_partners = indirect_partners

    @property
    def count(self):
        """Gets the count of this ListIndirectPartnersResponse.

        |参数名称：符合条件的记录个数，只有成功的时候出现| |参数的约束及描述：符合条件的记录个数，只有成功的时候出现|

        :return: The count of this ListIndirectPartnersResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListIndirectPartnersResponse.

        |参数名称：符合条件的记录个数，只有成功的时候出现| |参数的约束及描述：符合条件的记录个数，只有成功的时候出现|

        :param count: The count of this ListIndirectPartnersResponse.
        :type: int
        """
        self._count = count

    @property
    def indirect_partners(self):
        """Gets the indirect_partners of this ListIndirectPartnersResponse.

        |参数名称：二级渠道邀请记录列表| |参数约束以及描述：二级渠道邀请记录列表|

        :return: The indirect_partners of this ListIndirectPartnersResponse.
        :rtype: list[IndirectPartnerInfo]
        """
        return self._indirect_partners

    @indirect_partners.setter
    def indirect_partners(self, indirect_partners):
        """Sets the indirect_partners of this ListIndirectPartnersResponse.

        |参数名称：二级渠道邀请记录列表| |参数约束以及描述：二级渠道邀请记录列表|

        :param indirect_partners: The indirect_partners of this ListIndirectPartnersResponse.
        :type: list[IndirectPartnerInfo]
        """
        self._indirect_partners = indirect_partners

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListIndirectPartnersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
