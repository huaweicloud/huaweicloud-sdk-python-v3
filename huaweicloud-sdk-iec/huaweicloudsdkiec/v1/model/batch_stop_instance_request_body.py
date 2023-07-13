# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchStopInstanceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'os_stop': 'BatchStop'
    }

    attribute_map = {
        'os_stop': 'os-stop'
    }

    def __init__(self, os_stop=None):
        """BatchStopInstanceRequestBody

        The model defined in huaweicloud sdk

        :param os_stop: 
        :type os_stop: :class:`huaweicloudsdkiec.v1.BatchStop`
        """
        
        

        self._os_stop = None
        self.discriminator = None

        if os_stop is not None:
            self.os_stop = os_stop

    @property
    def os_stop(self):
        """Gets the os_stop of this BatchStopInstanceRequestBody.

        :return: The os_stop of this BatchStopInstanceRequestBody.
        :rtype: :class:`huaweicloudsdkiec.v1.BatchStop`
        """
        return self._os_stop

    @os_stop.setter
    def os_stop(self, os_stop):
        """Sets the os_stop of this BatchStopInstanceRequestBody.

        :param os_stop: The os_stop of this BatchStopInstanceRequestBody.
        :type os_stop: :class:`huaweicloudsdkiec.v1.BatchStop`
        """
        self._os_stop = os_stop

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
        if not isinstance(other, BatchStopInstanceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
