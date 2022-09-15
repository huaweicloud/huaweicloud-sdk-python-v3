# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RecyclePolicyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'recycle_policy': 'RecyclePolicy'
    }

    attribute_map = {
        'recycle_policy': 'recycle_policy'
    }

    def __init__(self, recycle_policy=None):
        """RecyclePolicyRequestBody

        The model defined in huaweicloud sdk

        :param recycle_policy: 
        :type recycle_policy: :class:`huaweicloudsdkgaussdbforopengauss.v3.RecyclePolicy`
        """
        
        

        self._recycle_policy = None
        self.discriminator = None

        self.recycle_policy = recycle_policy

    @property
    def recycle_policy(self):
        """Gets the recycle_policy of this RecyclePolicyRequestBody.


        :return: The recycle_policy of this RecyclePolicyRequestBody.
        :rtype: :class:`huaweicloudsdkgaussdbforopengauss.v3.RecyclePolicy`
        """
        return self._recycle_policy

    @recycle_policy.setter
    def recycle_policy(self, recycle_policy):
        """Sets the recycle_policy of this RecyclePolicyRequestBody.


        :param recycle_policy: The recycle_policy of this RecyclePolicyRequestBody.
        :type recycle_policy: :class:`huaweicloudsdkgaussdbforopengauss.v3.RecyclePolicy`
        """
        self._recycle_policy = recycle_policy

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
        if not isinstance(other, RecyclePolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
