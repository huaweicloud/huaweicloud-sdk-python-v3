# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateSwitchoverTestRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'switchover_test_record': 'CreateSwitchoverTest'
    }

    attribute_map = {
        'switchover_test_record': 'switchover_test_record'
    }

    def __init__(self, switchover_test_record=None):
        r"""CreateSwitchoverTestRequestBody

        The model defined in huaweicloud sdk

        :param switchover_test_record: 
        :type switchover_test_record: :class:`huaweicloudsdkdc.v3.CreateSwitchoverTest`
        """
        
        

        self._switchover_test_record = None
        self.discriminator = None

        if switchover_test_record is not None:
            self.switchover_test_record = switchover_test_record

    @property
    def switchover_test_record(self):
        r"""Gets the switchover_test_record of this CreateSwitchoverTestRequestBody.

        :return: The switchover_test_record of this CreateSwitchoverTestRequestBody.
        :rtype: :class:`huaweicloudsdkdc.v3.CreateSwitchoverTest`
        """
        return self._switchover_test_record

    @switchover_test_record.setter
    def switchover_test_record(self, switchover_test_record):
        r"""Sets the switchover_test_record of this CreateSwitchoverTestRequestBody.

        :param switchover_test_record: The switchover_test_record of this CreateSwitchoverTestRequestBody.
        :type switchover_test_record: :class:`huaweicloudsdkdc.v3.CreateSwitchoverTest`
        """
        self._switchover_test_record = switchover_test_record

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
        if not isinstance(other, CreateSwitchoverTestRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
