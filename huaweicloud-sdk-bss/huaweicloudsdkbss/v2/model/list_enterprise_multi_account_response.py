# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListEnterpriseMultiAccountResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'amount_infos': 'list[RetrieveAmountInfoV2]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'amount_infos': 'amount_infos'
    }

    def __init__(self, total_count=None, amount_infos=None):
        """ListEnterpriseMultiAccountResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._total_count = None
        self._amount_infos = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if amount_infos is not None:
            self.amount_infos = amount_infos

    @property
    def total_count(self):
        """Gets the total_count of this ListEnterpriseMultiAccountResponse.

        |参数名称：记录条数。| |参数的约束及描述：记录条数。|

        :return: The total_count of this ListEnterpriseMultiAccountResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListEnterpriseMultiAccountResponse.

        |参数名称：记录条数。| |参数的约束及描述：记录条数。|

        :param total_count: The total_count of this ListEnterpriseMultiAccountResponse.
        :type: int
        """
        self._total_count = total_count

    @property
    def amount_infos(self):
        """Gets the amount_infos of this ListEnterpriseMultiAccountResponse.

        |参数名称：可回收余额信息，如果是余额账户，只会有一条记录。具体请参见AmountInfo。| |参数约束以及描述：可回收余额信息，如果是余额账户，只会有一条记录。具体请参见AmountInfo。|

        :return: The amount_infos of this ListEnterpriseMultiAccountResponse.
        :rtype: list[RetrieveAmountInfoV2]
        """
        return self._amount_infos

    @amount_infos.setter
    def amount_infos(self, amount_infos):
        """Sets the amount_infos of this ListEnterpriseMultiAccountResponse.

        |参数名称：可回收余额信息，如果是余额账户，只会有一条记录。具体请参见AmountInfo。| |参数约束以及描述：可回收余额信息，如果是余额账户，只会有一条记录。具体请参见AmountInfo。|

        :param amount_infos: The amount_infos of this ListEnterpriseMultiAccountResponse.
        :type: list[RetrieveAmountInfoV2]
        """
        self._amount_infos = amount_infos

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
        if not isinstance(other, ListEnterpriseMultiAccountResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
