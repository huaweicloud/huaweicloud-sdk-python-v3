# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListKeystoreResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'list[ListKeystoreResult]',
        'status': 'str'
    }

    attribute_map = {
        'result': 'result',
        'status': 'status'
    }

    def __init__(self, result=None, status=None):
        r"""ListKeystoreResponse

        The model defined in huaweicloud sdk

        :param result: 文件列表
        :type result: list[:class:`huaweicloudsdkcodeartsbuild.v3.ListKeystoreResult`]
        :param status: 返回状态信息
        :type status: str
        """
        
        super(ListKeystoreResponse, self).__init__()

        self._result = None
        self._status = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if status is not None:
            self.status = status

    @property
    def result(self):
        r"""Gets the result of this ListKeystoreResponse.

        文件列表

        :return: The result of this ListKeystoreResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.ListKeystoreResult`]
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ListKeystoreResponse.

        文件列表

        :param result: The result of this ListKeystoreResponse.
        :type result: list[:class:`huaweicloudsdkcodeartsbuild.v3.ListKeystoreResult`]
        """
        self._result = result

    @property
    def status(self):
        r"""Gets the status of this ListKeystoreResponse.

        返回状态信息

        :return: The status of this ListKeystoreResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListKeystoreResponse.

        返回状态信息

        :param status: The status of this ListKeystoreResponse.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ListKeystoreResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
