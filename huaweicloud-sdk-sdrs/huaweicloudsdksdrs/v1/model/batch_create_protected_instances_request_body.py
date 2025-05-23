# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateProtectedInstancesRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protected_instances': 'BatchCreateProtectedInstancesRequestParams'
    }

    attribute_map = {
        'protected_instances': 'protected_instances'
    }

    def __init__(self, protected_instances=None):
        r"""BatchCreateProtectedInstancesRequestBody

        The model defined in huaweicloud sdk

        :param protected_instances: 
        :type protected_instances: :class:`huaweicloudsdksdrs.v1.BatchCreateProtectedInstancesRequestParams`
        """
        
        

        self._protected_instances = None
        self.discriminator = None

        self.protected_instances = protected_instances

    @property
    def protected_instances(self):
        r"""Gets the protected_instances of this BatchCreateProtectedInstancesRequestBody.

        :return: The protected_instances of this BatchCreateProtectedInstancesRequestBody.
        :rtype: :class:`huaweicloudsdksdrs.v1.BatchCreateProtectedInstancesRequestParams`
        """
        return self._protected_instances

    @protected_instances.setter
    def protected_instances(self, protected_instances):
        r"""Sets the protected_instances of this BatchCreateProtectedInstancesRequestBody.

        :param protected_instances: The protected_instances of this BatchCreateProtectedInstancesRequestBody.
        :type protected_instances: :class:`huaweicloudsdksdrs.v1.BatchCreateProtectedInstancesRequestParams`
        """
        self._protected_instances = protected_instances

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
        if not isinstance(other, BatchCreateProtectedInstancesRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
