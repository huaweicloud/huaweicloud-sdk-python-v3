# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPlansResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'body': 'list[TestPlanDetail]'
    }

    attribute_map = {
        'body': 'body'
    }

    def __init__(self, body=None):
        r"""ShowPlansResponse

        The model defined in huaweicloud sdk

        :param body: 项目下查询测试计划列表返回结构
        :type body: list[:class:`huaweicloudsdkcloudtest.v1.TestPlanDetail`]
        """
        
        super(ShowPlansResponse, self).__init__()

        self._body = None
        self.discriminator = None

        if body is not None:
            self.body = body

    @property
    def body(self):
        r"""Gets the body of this ShowPlansResponse.

        项目下查询测试计划列表返回结构

        :return: The body of this ShowPlansResponse.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.TestPlanDetail`]
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ShowPlansResponse.

        项目下查询测试计划列表返回结构

        :param body: The body of this ShowPlansResponse.
        :type body: list[:class:`huaweicloudsdkcloudtest.v1.TestPlanDetail`]
        """
        self._body = body

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
        if not isinstance(other, ShowPlansResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
