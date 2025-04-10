# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AttachStatistics:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attached_num': 'int',
        'unattached_num': 'int',
        'attaching_num': 'int',
        'attach_error_num': 'int'
    }

    attribute_map = {
        'attached_num': 'attached_num',
        'unattached_num': 'unattached_num',
        'attaching_num': 'attaching_num',
        'attach_error_num': 'attach_error_num'
    }

    def __init__(self, attached_num=None, unattached_num=None, attaching_num=None, attach_error_num=None):
        r"""AttachStatistics

        The model defined in huaweicloud sdk

        :param attached_num: 已分配个数。
        :type attached_num: int
        :param unattached_num: 未分配个数。
        :type unattached_num: int
        :param attaching_num: 分配中个数。
        :type attaching_num: int
        :param attach_error_num: 分配失败的个数。
        :type attach_error_num: int
        """
        
        

        self._attached_num = None
        self._unattached_num = None
        self._attaching_num = None
        self._attach_error_num = None
        self.discriminator = None

        if attached_num is not None:
            self.attached_num = attached_num
        if unattached_num is not None:
            self.unattached_num = unattached_num
        if attaching_num is not None:
            self.attaching_num = attaching_num
        if attach_error_num is not None:
            self.attach_error_num = attach_error_num

    @property
    def attached_num(self):
        r"""Gets the attached_num of this AttachStatistics.

        已分配个数。

        :return: The attached_num of this AttachStatistics.
        :rtype: int
        """
        return self._attached_num

    @attached_num.setter
    def attached_num(self, attached_num):
        r"""Sets the attached_num of this AttachStatistics.

        已分配个数。

        :param attached_num: The attached_num of this AttachStatistics.
        :type attached_num: int
        """
        self._attached_num = attached_num

    @property
    def unattached_num(self):
        r"""Gets the unattached_num of this AttachStatistics.

        未分配个数。

        :return: The unattached_num of this AttachStatistics.
        :rtype: int
        """
        return self._unattached_num

    @unattached_num.setter
    def unattached_num(self, unattached_num):
        r"""Sets the unattached_num of this AttachStatistics.

        未分配个数。

        :param unattached_num: The unattached_num of this AttachStatistics.
        :type unattached_num: int
        """
        self._unattached_num = unattached_num

    @property
    def attaching_num(self):
        r"""Gets the attaching_num of this AttachStatistics.

        分配中个数。

        :return: The attaching_num of this AttachStatistics.
        :rtype: int
        """
        return self._attaching_num

    @attaching_num.setter
    def attaching_num(self, attaching_num):
        r"""Sets the attaching_num of this AttachStatistics.

        分配中个数。

        :param attaching_num: The attaching_num of this AttachStatistics.
        :type attaching_num: int
        """
        self._attaching_num = attaching_num

    @property
    def attach_error_num(self):
        r"""Gets the attach_error_num of this AttachStatistics.

        分配失败的个数。

        :return: The attach_error_num of this AttachStatistics.
        :rtype: int
        """
        return self._attach_error_num

    @attach_error_num.setter
    def attach_error_num(self, attach_error_num):
        r"""Sets the attach_error_num of this AttachStatistics.

        分配失败的个数。

        :param attach_error_num: The attach_error_num of this AttachStatistics.
        :type attach_error_num: int
        """
        self._attach_error_num = attach_error_num

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
        if not isinstance(other, AttachStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
