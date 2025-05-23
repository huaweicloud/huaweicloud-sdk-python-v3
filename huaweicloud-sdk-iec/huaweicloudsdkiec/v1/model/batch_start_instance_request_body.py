# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchStartInstanceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'os_start': 'BatchStart'
    }

    attribute_map = {
        'os_start': 'os-start'
    }

    def __init__(self, os_start=None):
        r"""BatchStartInstanceRequestBody

        The model defined in huaweicloud sdk

        :param os_start: 
        :type os_start: :class:`huaweicloudsdkiec.v1.BatchStart`
        """
        
        

        self._os_start = None
        self.discriminator = None

        if os_start is not None:
            self.os_start = os_start

    @property
    def os_start(self):
        r"""Gets the os_start of this BatchStartInstanceRequestBody.

        :return: The os_start of this BatchStartInstanceRequestBody.
        :rtype: :class:`huaweicloudsdkiec.v1.BatchStart`
        """
        return self._os_start

    @os_start.setter
    def os_start(self, os_start):
        r"""Sets the os_start of this BatchStartInstanceRequestBody.

        :param os_start: The os_start of this BatchStartInstanceRequestBody.
        :type os_start: :class:`huaweicloudsdkiec.v1.BatchStart`
        """
        self._os_start = os_start

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
        if not isinstance(other, BatchStartInstanceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
