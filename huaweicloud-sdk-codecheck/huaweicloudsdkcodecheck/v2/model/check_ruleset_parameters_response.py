# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckRulesetParametersResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data': 'list[TaskCheckParamters]',
        'total': 'int'
    }

    attribute_map = {
        'data': 'data',
        'total': 'total'
    }

    def __init__(self, data=None, total=None):
        """CheckRulesetParametersResponse

        The model defined in huaweicloud sdk

        :param data: 历史记录数据
        :type data: list[:class:`huaweicloudsdkcodecheck.v2.TaskCheckParamters`]
        :param total: 总数
        :type total: int
        """
        
        super(CheckRulesetParametersResponse, self).__init__()

        self._data = None
        self._total = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if total is not None:
            self.total = total

    @property
    def data(self):
        """Gets the data of this CheckRulesetParametersResponse.

        历史记录数据

        :return: The data of this CheckRulesetParametersResponse.
        :rtype: list[:class:`huaweicloudsdkcodecheck.v2.TaskCheckParamters`]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this CheckRulesetParametersResponse.

        历史记录数据

        :param data: The data of this CheckRulesetParametersResponse.
        :type data: list[:class:`huaweicloudsdkcodecheck.v2.TaskCheckParamters`]
        """
        self._data = data

    @property
    def total(self):
        """Gets the total of this CheckRulesetParametersResponse.

        总数

        :return: The total of this CheckRulesetParametersResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this CheckRulesetParametersResponse.

        总数

        :param total: The total of this CheckRulesetParametersResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, CheckRulesetParametersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
