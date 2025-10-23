# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProtectionCount:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'ungraded': 'int',
        'graded': 'GradedCount'
    }

    attribute_map = {
        'total': 'total',
        'ungraded': 'ungraded',
        'graded': 'graded'
    }

    def __init__(self, total=None, ungraded=None, graded=None):
        r"""ProtectionCount

        The model defined in huaweicloud sdk

        :param total: 总数
        :type total: int
        :param ungraded: 未定级资源总数
        :type ungraded: int
        :param graded: 
        :type graded: :class:`huaweicloudsdkbcc.v1.GradedCount`
        """
        
        

        self._total = None
        self._ungraded = None
        self._graded = None
        self.discriminator = None

        self.total = total
        if ungraded is not None:
            self.ungraded = ungraded
        if graded is not None:
            self.graded = graded

    @property
    def total(self):
        r"""Gets the total of this ProtectionCount.

        总数

        :return: The total of this ProtectionCount.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ProtectionCount.

        总数

        :param total: The total of this ProtectionCount.
        :type total: int
        """
        self._total = total

    @property
    def ungraded(self):
        r"""Gets the ungraded of this ProtectionCount.

        未定级资源总数

        :return: The ungraded of this ProtectionCount.
        :rtype: int
        """
        return self._ungraded

    @ungraded.setter
    def ungraded(self, ungraded):
        r"""Sets the ungraded of this ProtectionCount.

        未定级资源总数

        :param ungraded: The ungraded of this ProtectionCount.
        :type ungraded: int
        """
        self._ungraded = ungraded

    @property
    def graded(self):
        r"""Gets the graded of this ProtectionCount.

        :return: The graded of this ProtectionCount.
        :rtype: :class:`huaweicloudsdkbcc.v1.GradedCount`
        """
        return self._graded

    @graded.setter
    def graded(self, graded):
        r"""Sets the graded of this ProtectionCount.

        :param graded: The graded of this ProtectionCount.
        :type graded: :class:`huaweicloudsdkbcc.v1.GradedCount`
        """
        self._graded = graded

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
        if not isinstance(other, ProtectionCount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
