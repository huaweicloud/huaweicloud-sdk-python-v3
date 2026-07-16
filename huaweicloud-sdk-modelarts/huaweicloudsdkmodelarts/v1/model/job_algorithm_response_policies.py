# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobAlgorithmResponsePolicies:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auto_search': 'JobAlgorithmResponsePoliciesAutoSearch'
    }

    attribute_map = {
        'auto_search': 'auto_search'
    }

    def __init__(self, auto_search=None):
        r"""JobAlgorithmResponsePolicies

        The model defined in huaweicloud sdk

        :param auto_search: 
        :type auto_search: :class:`huaweicloudsdkmodelarts.v1.JobAlgorithmResponsePoliciesAutoSearch`
        """
        
        

        self._auto_search = None
        self.discriminator = None

        if auto_search is not None:
            self.auto_search = auto_search

    @property
    def auto_search(self):
        r"""Gets the auto_search of this JobAlgorithmResponsePolicies.

        :return: The auto_search of this JobAlgorithmResponsePolicies.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.JobAlgorithmResponsePoliciesAutoSearch`
        """
        return self._auto_search

    @auto_search.setter
    def auto_search(self, auto_search):
        r"""Sets the auto_search of this JobAlgorithmResponsePolicies.

        :param auto_search: The auto_search of this JobAlgorithmResponsePolicies.
        :type auto_search: :class:`huaweicloudsdkmodelarts.v1.JobAlgorithmResponsePoliciesAutoSearch`
        """
        self._auto_search = auto_search

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, JobAlgorithmResponsePolicies):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
