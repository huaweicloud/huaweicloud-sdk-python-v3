# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRuleErrorsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'errors': 'list[Error]'
    }

    attribute_map = {
        'count': 'count',
        'errors': 'errors'
    }

    def __init__(self, count=None, errors=None):
        """ListRuleErrorsResponse

        The model defined in huaweicloud sdk

        :param count: 满足条件的错误个数
        :type count: int
        :param errors: 错误列表
        :type errors: list[:class:`huaweicloudsdkief.v1.Error`]
        """
        
        super(ListRuleErrorsResponse, self).__init__()

        self._count = None
        self._errors = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if errors is not None:
            self.errors = errors

    @property
    def count(self):
        """Gets the count of this ListRuleErrorsResponse.

        满足条件的错误个数

        :return: The count of this ListRuleErrorsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListRuleErrorsResponse.

        满足条件的错误个数

        :param count: The count of this ListRuleErrorsResponse.
        :type count: int
        """
        self._count = count

    @property
    def errors(self):
        """Gets the errors of this ListRuleErrorsResponse.

        错误列表

        :return: The errors of this ListRuleErrorsResponse.
        :rtype: list[:class:`huaweicloudsdkief.v1.Error`]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        """Sets the errors of this ListRuleErrorsResponse.

        错误列表

        :param errors: The errors of this ListRuleErrorsResponse.
        :type errors: list[:class:`huaweicloudsdkief.v1.Error`]
        """
        self._errors = errors

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
        if not isinstance(other, ListRuleErrorsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
