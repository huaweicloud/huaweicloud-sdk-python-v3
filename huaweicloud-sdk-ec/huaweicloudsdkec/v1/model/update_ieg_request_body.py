# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateIegRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'high_availability': 'str'
    }

    attribute_map = {
        'name': 'name',
        'high_availability': 'high_availability'
    }

    def __init__(self, name=None, high_availability=None):
        r"""UpdateIegRequestBody

        The model defined in huaweicloud sdk

        :param name: 智能企业网关名字
        :type name: str
        :param high_availability: 高可用性
        :type high_availability: str
        """
        
        

        self._name = None
        self._high_availability = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if high_availability is not None:
            self.high_availability = high_availability

    @property
    def name(self):
        r"""Gets the name of this UpdateIegRequestBody.

        智能企业网关名字

        :return: The name of this UpdateIegRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateIegRequestBody.

        智能企业网关名字

        :param name: The name of this UpdateIegRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def high_availability(self):
        r"""Gets the high_availability of this UpdateIegRequestBody.

        高可用性

        :return: The high_availability of this UpdateIegRequestBody.
        :rtype: str
        """
        return self._high_availability

    @high_availability.setter
    def high_availability(self, high_availability):
        r"""Sets the high_availability of this UpdateIegRequestBody.

        高可用性

        :param high_availability: The high_availability of this UpdateIegRequestBody.
        :type high_availability: str
        """
        self._high_availability = high_availability

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
        if not isinstance(other, UpdateIegRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
