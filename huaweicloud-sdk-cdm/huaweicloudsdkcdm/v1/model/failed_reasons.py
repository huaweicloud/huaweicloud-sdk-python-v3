# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FailedReasons:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'create_failed': 'FailedReasonsCREATEFAILED'
    }

    attribute_map = {
        'create_failed': 'CREATE_FAILED'
    }

    def __init__(self, create_failed=None):
        """FailedReasons

        The model defined in huaweicloud sdk

        :param create_failed: 
        :type create_failed: :class:`huaweicloudsdkcdm.v1.FailedReasonsCREATEFAILED`
        """
        
        

        self._create_failed = None
        self.discriminator = None

        if create_failed is not None:
            self.create_failed = create_failed

    @property
    def create_failed(self):
        """Gets the create_failed of this FailedReasons.


        :return: The create_failed of this FailedReasons.
        :rtype: :class:`huaweicloudsdkcdm.v1.FailedReasonsCREATEFAILED`
        """
        return self._create_failed

    @create_failed.setter
    def create_failed(self, create_failed):
        """Sets the create_failed of this FailedReasons.


        :param create_failed: The create_failed of this FailedReasons.
        :type create_failed: :class:`huaweicloudsdkcdm.v1.FailedReasonsCREATEFAILED`
        """
        self._create_failed = create_failed

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
        if not isinstance(other, FailedReasons):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
