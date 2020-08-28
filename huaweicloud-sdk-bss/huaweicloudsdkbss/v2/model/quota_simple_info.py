# coding: utf-8

import pprint
import re

import six





class QuotaSimpleInfo:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'quota_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'quota_id': 'quota_id'
    }

    def __init__(self, id=None, quota_id=None):
        """QuotaSimpleInfo - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._quota_id = None
        self.discriminator = None

        self.id = id
        self.quota_id = quota_id

    @property
    def id(self):
        """Gets the id of this QuotaSimpleInfo.

        |参数名称：批量发放成功客户ID。| |参数约束及描述：批量发放成功客户ID。|

        :return: The id of this QuotaSimpleInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QuotaSimpleInfo.

        |参数名称：批量发放成功客户ID。| |参数约束及描述：批量发放成功客户ID。|

        :param id: The id of this QuotaSimpleInfo.
        :type: str
        """
        self._id = id

    @property
    def quota_id(self):
        """Gets the quota_id of this QuotaSimpleInfo.

        |参数名称：发放成功的券ID| |参数约束及描述：发放成功的券ID|

        :return: The quota_id of this QuotaSimpleInfo.
        :rtype: str
        """
        return self._quota_id

    @quota_id.setter
    def quota_id(self, quota_id):
        """Sets the quota_id of this QuotaSimpleInfo.

        |参数名称：发放成功的券ID| |参数约束及描述：发放成功的券ID|

        :param quota_id: The quota_id of this QuotaSimpleInfo.
        :type: str
        """
        self._quota_id = quota_id

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
        if not isinstance(other, QuotaSimpleInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
