# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PlaybookStatisticDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'unapproved_num': 'int',
        'disabled_num': 'int',
        'enabled_num': 'int'
    }

    attribute_map = {
        'unapproved_num': 'unapproved_num',
        'disabled_num': 'disabled_num',
        'enabled_num': 'enabled_num'
    }

    def __init__(self, unapproved_num=None, disabled_num=None, enabled_num=None):
        r"""PlaybookStatisticDetail

        The model defined in huaweicloud sdk

        :param unapproved_num: 未审核剧本数量
        :type unapproved_num: int
        :param disabled_num: 未启用剧本数量
        :type disabled_num: int
        :param enabled_num: 已启用剧本数量
        :type enabled_num: int
        """
        
        

        self._unapproved_num = None
        self._disabled_num = None
        self._enabled_num = None
        self.discriminator = None

        if unapproved_num is not None:
            self.unapproved_num = unapproved_num
        if disabled_num is not None:
            self.disabled_num = disabled_num
        if enabled_num is not None:
            self.enabled_num = enabled_num

    @property
    def unapproved_num(self):
        r"""Gets the unapproved_num of this PlaybookStatisticDetail.

        未审核剧本数量

        :return: The unapproved_num of this PlaybookStatisticDetail.
        :rtype: int
        """
        return self._unapproved_num

    @unapproved_num.setter
    def unapproved_num(self, unapproved_num):
        r"""Sets the unapproved_num of this PlaybookStatisticDetail.

        未审核剧本数量

        :param unapproved_num: The unapproved_num of this PlaybookStatisticDetail.
        :type unapproved_num: int
        """
        self._unapproved_num = unapproved_num

    @property
    def disabled_num(self):
        r"""Gets the disabled_num of this PlaybookStatisticDetail.

        未启用剧本数量

        :return: The disabled_num of this PlaybookStatisticDetail.
        :rtype: int
        """
        return self._disabled_num

    @disabled_num.setter
    def disabled_num(self, disabled_num):
        r"""Sets the disabled_num of this PlaybookStatisticDetail.

        未启用剧本数量

        :param disabled_num: The disabled_num of this PlaybookStatisticDetail.
        :type disabled_num: int
        """
        self._disabled_num = disabled_num

    @property
    def enabled_num(self):
        r"""Gets the enabled_num of this PlaybookStatisticDetail.

        已启用剧本数量

        :return: The enabled_num of this PlaybookStatisticDetail.
        :rtype: int
        """
        return self._enabled_num

    @enabled_num.setter
    def enabled_num(self, enabled_num):
        r"""Sets the enabled_num of this PlaybookStatisticDetail.

        已启用剧本数量

        :param enabled_num: The enabled_num of this PlaybookStatisticDetail.
        :type enabled_num: int
        """
        self._enabled_num = enabled_num

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
        if not isinstance(other, PlaybookStatisticDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
