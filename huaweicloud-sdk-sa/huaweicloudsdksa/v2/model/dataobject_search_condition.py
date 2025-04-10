# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DataobjectSearchCondition:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'conditions': 'list[ConditonInfo]',
        'logics': 'list[str]'
    }

    attribute_map = {
        'conditions': 'conditions',
        'logics': 'logics'
    }

    def __init__(self, conditions=None, logics=None):
        r"""DataobjectSearchCondition

        The model defined in huaweicloud sdk

        :param conditions: conditions
        :type conditions: list[:class:`huaweicloudsdksa.v2.ConditonInfo`]
        :param logics: conditions
        :type logics: list[str]
        """
        
        

        self._conditions = None
        self._logics = None
        self.discriminator = None

        if conditions is not None:
            self.conditions = conditions
        if logics is not None:
            self.logics = logics

    @property
    def conditions(self):
        r"""Gets the conditions of this DataobjectSearchCondition.

        conditions

        :return: The conditions of this DataobjectSearchCondition.
        :rtype: list[:class:`huaweicloudsdksa.v2.ConditonInfo`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this DataobjectSearchCondition.

        conditions

        :param conditions: The conditions of this DataobjectSearchCondition.
        :type conditions: list[:class:`huaweicloudsdksa.v2.ConditonInfo`]
        """
        self._conditions = conditions

    @property
    def logics(self):
        r"""Gets the logics of this DataobjectSearchCondition.

        conditions

        :return: The logics of this DataobjectSearchCondition.
        :rtype: list[str]
        """
        return self._logics

    @logics.setter
    def logics(self, logics):
        r"""Sets the logics of this DataobjectSearchCondition.

        conditions

        :param logics: The logics of this DataobjectSearchCondition.
        :type logics: list[str]
        """
        self._logics = logics

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
        if not isinstance(other, DataobjectSearchCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
