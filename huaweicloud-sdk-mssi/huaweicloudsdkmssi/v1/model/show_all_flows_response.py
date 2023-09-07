# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAllFlowsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'str',
        'flow_metas': 'list[FlowMeta]'
    }

    attribute_map = {
        'count': 'count',
        'flow_metas': 'flow_metas'
    }

    def __init__(self, count=None, flow_metas=None):
        """ShowAllFlowsResponse

        The model defined in huaweicloud sdk

        :param count: 流的数量
        :type count: str
        :param flow_metas: 流列表
        :type flow_metas: list[:class:`huaweicloudsdkmssi.v1.FlowMeta`]
        """
        
        super(ShowAllFlowsResponse, self).__init__()

        self._count = None
        self._flow_metas = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if flow_metas is not None:
            self.flow_metas = flow_metas

    @property
    def count(self):
        """Gets the count of this ShowAllFlowsResponse.

        流的数量

        :return: The count of this ShowAllFlowsResponse.
        :rtype: str
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ShowAllFlowsResponse.

        流的数量

        :param count: The count of this ShowAllFlowsResponse.
        :type count: str
        """
        self._count = count

    @property
    def flow_metas(self):
        """Gets the flow_metas of this ShowAllFlowsResponse.

        流列表

        :return: The flow_metas of this ShowAllFlowsResponse.
        :rtype: list[:class:`huaweicloudsdkmssi.v1.FlowMeta`]
        """
        return self._flow_metas

    @flow_metas.setter
    def flow_metas(self, flow_metas):
        """Sets the flow_metas of this ShowAllFlowsResponse.

        流列表

        :param flow_metas: The flow_metas of this ShowAllFlowsResponse.
        :type flow_metas: list[:class:`huaweicloudsdkmssi.v1.FlowMeta`]
        """
        self._flow_metas = flow_metas

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
        if not isinstance(other, ShowAllFlowsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
