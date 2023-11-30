# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtLimitPojo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'min_ingress_size': 'int',
        'max_ingress_size': 'int',
        'ratio_95peak': 'int'
    }

    attribute_map = {
        'min_ingress_size': 'min_ingress_size',
        'max_ingress_size': 'max_ingress_size',
        'ratio_95peak': 'ratio_95peak'
    }

    def __init__(self, min_ingress_size=None, max_ingress_size=None, ratio_95peak=None):
        """ExtLimitPojo

        The model defined in huaweicloud sdk

        :param min_ingress_size: - 最小入云限速
        :type min_ingress_size: int
        :param max_ingress_size: - 最大入云限速
        :type max_ingress_size: int
        :param ratio_95peak: 95计费保底率
        :type ratio_95peak: int
        """
        
        

        self._min_ingress_size = None
        self._max_ingress_size = None
        self._ratio_95peak = None
        self.discriminator = None

        if min_ingress_size is not None:
            self.min_ingress_size = min_ingress_size
        if max_ingress_size is not None:
            self.max_ingress_size = max_ingress_size
        if ratio_95peak is not None:
            self.ratio_95peak = ratio_95peak

    @property
    def min_ingress_size(self):
        """Gets the min_ingress_size of this ExtLimitPojo.

        - 最小入云限速

        :return: The min_ingress_size of this ExtLimitPojo.
        :rtype: int
        """
        return self._min_ingress_size

    @min_ingress_size.setter
    def min_ingress_size(self, min_ingress_size):
        """Sets the min_ingress_size of this ExtLimitPojo.

        - 最小入云限速

        :param min_ingress_size: The min_ingress_size of this ExtLimitPojo.
        :type min_ingress_size: int
        """
        self._min_ingress_size = min_ingress_size

    @property
    def max_ingress_size(self):
        """Gets the max_ingress_size of this ExtLimitPojo.

        - 最大入云限速

        :return: The max_ingress_size of this ExtLimitPojo.
        :rtype: int
        """
        return self._max_ingress_size

    @max_ingress_size.setter
    def max_ingress_size(self, max_ingress_size):
        """Sets the max_ingress_size of this ExtLimitPojo.

        - 最大入云限速

        :param max_ingress_size: The max_ingress_size of this ExtLimitPojo.
        :type max_ingress_size: int
        """
        self._max_ingress_size = max_ingress_size

    @property
    def ratio_95peak(self):
        """Gets the ratio_95peak of this ExtLimitPojo.

        95计费保底率

        :return: The ratio_95peak of this ExtLimitPojo.
        :rtype: int
        """
        return self._ratio_95peak

    @ratio_95peak.setter
    def ratio_95peak(self, ratio_95peak):
        """Sets the ratio_95peak of this ExtLimitPojo.

        95计费保底率

        :param ratio_95peak: The ratio_95peak of this ExtLimitPojo.
        :type ratio_95peak: int
        """
        self._ratio_95peak = ratio_95peak

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
        if not isinstance(other, ExtLimitPojo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
