# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAllAppResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_num': 'int',
        'result': 'list[AppExecutionInfo]'
    }

    attribute_map = {
        'total_num': 'total_num',
        'result': 'result'
    }

    def __init__(self, total_num=None, result=None):
        """ListAllAppResponse

        The model defined in huaweicloud sdk

        :param total_num: 总数
        :type total_num: int
        :param result: 应用列表数组
        :type result: list[:class:`huaweicloudsdkcodeartsdeploy.v2.AppExecutionInfo`]
        """
        
        super(ListAllAppResponse, self).__init__()

        self._total_num = None
        self._result = None
        self.discriminator = None

        if total_num is not None:
            self.total_num = total_num
        if result is not None:
            self.result = result

    @property
    def total_num(self):
        """Gets the total_num of this ListAllAppResponse.

        总数

        :return: The total_num of this ListAllAppResponse.
        :rtype: int
        """
        return self._total_num

    @total_num.setter
    def total_num(self, total_num):
        """Sets the total_num of this ListAllAppResponse.

        总数

        :param total_num: The total_num of this ListAllAppResponse.
        :type total_num: int
        """
        self._total_num = total_num

    @property
    def result(self):
        """Gets the result of this ListAllAppResponse.

        应用列表数组

        :return: The result of this ListAllAppResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartsdeploy.v2.AppExecutionInfo`]
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ListAllAppResponse.

        应用列表数组

        :param result: The result of this ListAllAppResponse.
        :type result: list[:class:`huaweicloudsdkcodeartsdeploy.v2.AppExecutionInfo`]
        """
        self._result = result

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
        if not isinstance(other, ListAllAppResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
