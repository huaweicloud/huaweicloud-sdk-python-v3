# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteHostGroupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'list[GetHostGroupInfo]',
        'total': 'int'
    }

    attribute_map = {
        'result': 'result',
        'total': 'total'
    }

    def __init__(self, result=None, total=None):
        """DeleteHostGroupResponse

        The model defined in huaweicloud sdk

        :param result: 主机组详细信息
        :type result: list[:class:`huaweicloudsdklts.v2.GetHostGroupInfo`]
        :param total: 删除主机组数量
        :type total: int
        """
        
        super(DeleteHostGroupResponse, self).__init__()

        self._result = None
        self._total = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if total is not None:
            self.total = total

    @property
    def result(self):
        """Gets the result of this DeleteHostGroupResponse.

        主机组详细信息

        :return: The result of this DeleteHostGroupResponse.
        :rtype: list[:class:`huaweicloudsdklts.v2.GetHostGroupInfo`]
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this DeleteHostGroupResponse.

        主机组详细信息

        :param result: The result of this DeleteHostGroupResponse.
        :type result: list[:class:`huaweicloudsdklts.v2.GetHostGroupInfo`]
        """
        self._result = result

    @property
    def total(self):
        """Gets the total of this DeleteHostGroupResponse.

        删除主机组数量

        :return: The total of this DeleteHostGroupResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this DeleteHostGroupResponse.

        删除主机组数量

        :param total: The total of this DeleteHostGroupResponse.
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
        if not isinstance(other, DeleteHostGroupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
