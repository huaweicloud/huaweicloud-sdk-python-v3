# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteAccessConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'list[AccessConfigInfo]',
        'total': 'int'
    }

    attribute_map = {
        'result': 'result',
        'total': 'total'
    }

    def __init__(self, result=None, total=None):
        r"""DeleteAccessConfigResponse

        The model defined in huaweicloud sdk

        :param result: 日志接入列表
        :type result: list[:class:`huaweicloudsdklts.v2.AccessConfigInfo`]
        :param total: 日志接入总数
        :type total: int
        """
        
        super(DeleteAccessConfigResponse, self).__init__()

        self._result = None
        self._total = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if total is not None:
            self.total = total

    @property
    def result(self):
        r"""Gets the result of this DeleteAccessConfigResponse.

        日志接入列表

        :return: The result of this DeleteAccessConfigResponse.
        :rtype: list[:class:`huaweicloudsdklts.v2.AccessConfigInfo`]
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this DeleteAccessConfigResponse.

        日志接入列表

        :param result: The result of this DeleteAccessConfigResponse.
        :type result: list[:class:`huaweicloudsdklts.v2.AccessConfigInfo`]
        """
        self._result = result

    @property
    def total(self):
        r"""Gets the total of this DeleteAccessConfigResponse.

        日志接入总数

        :return: The total of this DeleteAccessConfigResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this DeleteAccessConfigResponse.

        日志接入总数

        :param total: The total of this DeleteAccessConfigResponse.
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
        if not isinstance(other, DeleteAccessConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
