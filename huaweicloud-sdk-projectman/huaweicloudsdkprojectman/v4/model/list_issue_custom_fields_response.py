# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListIssueCustomFieldsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'datas': 'list[IssueCustomField]'
    }

    attribute_map = {
        'datas': 'datas'
    }

    def __init__(self, datas=None):
        """ListIssueCustomFieldsResponse

        The model defined in huaweicloud sdk

        :param datas: 自定义字段返回数据
        :type datas: list[:class:`huaweicloudsdkprojectman.v4.IssueCustomField`]
        """
        
        super(ListIssueCustomFieldsResponse, self).__init__()

        self._datas = None
        self.discriminator = None

        if datas is not None:
            self.datas = datas

    @property
    def datas(self):
        """Gets the datas of this ListIssueCustomFieldsResponse.

        自定义字段返回数据

        :return: The datas of this ListIssueCustomFieldsResponse.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.IssueCustomField`]
        """
        return self._datas

    @datas.setter
    def datas(self, datas):
        """Sets the datas of this ListIssueCustomFieldsResponse.

        自定义字段返回数据

        :param datas: The datas of this ListIssueCustomFieldsResponse.
        :type datas: list[:class:`huaweicloudsdkprojectman.v4.IssueCustomField`]
        """
        self._datas = datas

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
        if not isinstance(other, ListIssueCustomFieldsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
