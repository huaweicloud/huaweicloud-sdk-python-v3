# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowApplyHistoryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'histories': 'list[ApplyHistoryRsp]'
    }

    attribute_map = {
        'histories': 'histories'
    }

    def __init__(self, histories=None):
        """ShowApplyHistoryResponse

        The model defined in huaweicloud sdk

        :param histories: 参数组模板应用历史列表
        :type histories: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ApplyHistoryRsp`]
        """
        
        super(ShowApplyHistoryResponse, self).__init__()

        self._histories = None
        self.discriminator = None

        if histories is not None:
            self.histories = histories

    @property
    def histories(self):
        """Gets the histories of this ShowApplyHistoryResponse.

        参数组模板应用历史列表

        :return: The histories of this ShowApplyHistoryResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ApplyHistoryRsp`]
        """
        return self._histories

    @histories.setter
    def histories(self, histories):
        """Sets the histories of this ShowApplyHistoryResponse.

        参数组模板应用历史列表

        :param histories: The histories of this ShowApplyHistoryResponse.
        :type histories: list[:class:`huaweicloudsdkgaussdbfornosql.v3.ApplyHistoryRsp`]
        """
        self._histories = histories

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
        if not isinstance(other, ShowApplyHistoryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
