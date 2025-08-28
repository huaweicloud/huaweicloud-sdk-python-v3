# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchUpdatePoliciesPriorityRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'l7policies': 'list[BatchUpdatePriorityRequestBody]'
    }

    attribute_map = {
        'l7policies': 'l7policies'
    }

    def __init__(self, l7policies=None):
        r"""BatchUpdatePoliciesPriorityRequestBody

        The model defined in huaweicloud sdk

        :param l7policies: 
        :type l7policies: list[:class:`huaweicloudsdkelb.v3.BatchUpdatePriorityRequestBody`]
        """
        
        

        self._l7policies = None
        self.discriminator = None

        if l7policies is not None:
            self.l7policies = l7policies

    @property
    def l7policies(self):
        r"""Gets the l7policies of this BatchUpdatePoliciesPriorityRequestBody.

        :return: The l7policies of this BatchUpdatePoliciesPriorityRequestBody.
        :rtype: list[:class:`huaweicloudsdkelb.v3.BatchUpdatePriorityRequestBody`]
        """
        return self._l7policies

    @l7policies.setter
    def l7policies(self, l7policies):
        r"""Sets the l7policies of this BatchUpdatePoliciesPriorityRequestBody.

        :param l7policies: The l7policies of this BatchUpdatePoliciesPriorityRequestBody.
        :type l7policies: list[:class:`huaweicloudsdkelb.v3.BatchUpdatePriorityRequestBody`]
        """
        self._l7policies = l7policies

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
        if not isinstance(other, BatchUpdatePoliciesPriorityRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
