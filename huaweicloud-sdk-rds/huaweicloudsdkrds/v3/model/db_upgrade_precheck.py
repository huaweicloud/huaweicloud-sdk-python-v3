# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DBUpgradePrecheck:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'int',
        'checks_performed': 'list[DBCheckDetail]'
    }

    attribute_map = {
        'result': 'result',
        'checks_performed': 'checks_performed'
    }

    def __init__(self, result=None, checks_performed=None):
        r"""DBUpgradePrecheck

        The model defined in huaweicloud sdk

        :param result: 检查是否通过，0代表通过，1代表未通过
        :type result: int
        :param checks_performed: 检查项
        :type checks_performed: list[:class:`huaweicloudsdkrds.v3.DBCheckDetail`]
        """
        
        

        self._result = None
        self._checks_performed = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if checks_performed is not None:
            self.checks_performed = checks_performed

    @property
    def result(self):
        r"""Gets the result of this DBUpgradePrecheck.

        检查是否通过，0代表通过，1代表未通过

        :return: The result of this DBUpgradePrecheck.
        :rtype: int
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this DBUpgradePrecheck.

        检查是否通过，0代表通过，1代表未通过

        :param result: The result of this DBUpgradePrecheck.
        :type result: int
        """
        self._result = result

    @property
    def checks_performed(self):
        r"""Gets the checks_performed of this DBUpgradePrecheck.

        检查项

        :return: The checks_performed of this DBUpgradePrecheck.
        :rtype: list[:class:`huaweicloudsdkrds.v3.DBCheckDetail`]
        """
        return self._checks_performed

    @checks_performed.setter
    def checks_performed(self, checks_performed):
        r"""Sets the checks_performed of this DBUpgradePrecheck.

        检查项

        :param checks_performed: The checks_performed of this DBUpgradePrecheck.
        :type checks_performed: list[:class:`huaweicloudsdkrds.v3.DBCheckDetail`]
        """
        self._checks_performed = checks_performed

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
        if not isinstance(other, DBUpgradePrecheck):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
