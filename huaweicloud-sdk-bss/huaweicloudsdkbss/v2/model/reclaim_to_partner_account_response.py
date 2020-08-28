# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ReclaimToPartnerAccountResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'trans_id': 'str'
    }

    attribute_map = {
        'trans_id': 'trans_id'
    }

    def __init__(self, trans_id=None):
        """ReclaimToPartnerAccountResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._trans_id = None
        self.discriminator = None

        if trans_id is not None:
            self.trans_id = trans_id

    @property
    def trans_id(self):
        """Gets the trans_id of this ReclaimToPartnerAccountResponse.

        |参数名称：事务流水ID，只有成功响应才会返回。| |参数约束及描述：事务流水ID，只有成功响应才会返回。|

        :return: The trans_id of this ReclaimToPartnerAccountResponse.
        :rtype: str
        """
        return self._trans_id

    @trans_id.setter
    def trans_id(self, trans_id):
        """Sets the trans_id of this ReclaimToPartnerAccountResponse.

        |参数名称：事务流水ID，只有成功响应才会返回。| |参数约束及描述：事务流水ID，只有成功响应才会返回。|

        :param trans_id: The trans_id of this ReclaimToPartnerAccountResponse.
        :type: str
        """
        self._trans_id = trans_id

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
        if not isinstance(other, ReclaimToPartnerAccountResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
