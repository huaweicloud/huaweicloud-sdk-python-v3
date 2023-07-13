# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteTerminalsBindingDesktopsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result_list': 'list[DeleteTerminalsBindingDesktopsResult]'
    }

    attribute_map = {
        'result_list': 'result_list'
    }

    def __init__(self, result_list=None):
        """DeleteTerminalsBindingDesktopsResponse

        The model defined in huaweicloud sdk

        :param result_list: 需删除的策略ID列表
        :type result_list: list[:class:`huaweicloudsdkworkspace.v2.DeleteTerminalsBindingDesktopsResult`]
        """
        
        super(DeleteTerminalsBindingDesktopsResponse, self).__init__()

        self._result_list = None
        self.discriminator = None

        if result_list is not None:
            self.result_list = result_list

    @property
    def result_list(self):
        """Gets the result_list of this DeleteTerminalsBindingDesktopsResponse.

        需删除的策略ID列表

        :return: The result_list of this DeleteTerminalsBindingDesktopsResponse.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.DeleteTerminalsBindingDesktopsResult`]
        """
        return self._result_list

    @result_list.setter
    def result_list(self, result_list):
        """Sets the result_list of this DeleteTerminalsBindingDesktopsResponse.

        需删除的策略ID列表

        :param result_list: The result_list of this DeleteTerminalsBindingDesktopsResponse.
        :type result_list: list[:class:`huaweicloudsdkworkspace.v2.DeleteTerminalsBindingDesktopsResult`]
        """
        self._result_list = result_list

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
        if not isinstance(other, DeleteTerminalsBindingDesktopsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
