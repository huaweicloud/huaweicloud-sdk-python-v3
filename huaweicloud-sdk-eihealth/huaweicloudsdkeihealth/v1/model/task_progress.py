# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskProgress:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'overall': 'float'
    }

    attribute_map = {
        'overall': 'overall'
    }

    def __init__(self, overall=None):
        r"""TaskProgress

        The model defined in huaweicloud sdk

        :param overall: 整体进度
        :type overall: float
        """
        
        

        self._overall = None
        self.discriminator = None

        if overall is not None:
            self.overall = overall

    @property
    def overall(self):
        r"""Gets the overall of this TaskProgress.

        整体进度

        :return: The overall of this TaskProgress.
        :rtype: float
        """
        return self._overall

    @overall.setter
    def overall(self, overall):
        r"""Sets the overall of this TaskProgress.

        整体进度

        :param overall: The overall of this TaskProgress.
        :type overall: float
        """
        self._overall = overall

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
        if not isinstance(other, TaskProgress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
