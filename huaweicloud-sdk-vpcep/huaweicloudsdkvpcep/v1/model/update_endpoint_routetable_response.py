# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEndpointRoutetableResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'routetables': 'list[str]',
        'error': 'list[RoutetableInfoError]'
    }

    attribute_map = {
        'routetables': 'routetables',
        'error': 'error'
    }

    def __init__(self, routetables=None, error=None):
        """UpdateEndpointRoutetableResponse

        The model defined in huaweicloud sdk

        :param routetables: 路由表ID列表。 若未指定，返回默认VPC下路由表ID。 更新Gateway类型终端节点服务的终端节点时，显示此参数。
        :type routetables: list[str]
        :param error: 当修改终端节点子网路由表失败时，返回错误提示信息
        :type error: list[:class:`huaweicloudsdkvpcep.v1.RoutetableInfoError`]
        """
        
        super(UpdateEndpointRoutetableResponse, self).__init__()

        self._routetables = None
        self._error = None
        self.discriminator = None

        if routetables is not None:
            self.routetables = routetables
        if error is not None:
            self.error = error

    @property
    def routetables(self):
        """Gets the routetables of this UpdateEndpointRoutetableResponse.

        路由表ID列表。 若未指定，返回默认VPC下路由表ID。 更新Gateway类型终端节点服务的终端节点时，显示此参数。

        :return: The routetables of this UpdateEndpointRoutetableResponse.
        :rtype: list[str]
        """
        return self._routetables

    @routetables.setter
    def routetables(self, routetables):
        """Sets the routetables of this UpdateEndpointRoutetableResponse.

        路由表ID列表。 若未指定，返回默认VPC下路由表ID。 更新Gateway类型终端节点服务的终端节点时，显示此参数。

        :param routetables: The routetables of this UpdateEndpointRoutetableResponse.
        :type routetables: list[str]
        """
        self._routetables = routetables

    @property
    def error(self):
        """Gets the error of this UpdateEndpointRoutetableResponse.

        当修改终端节点子网路由表失败时，返回错误提示信息

        :return: The error of this UpdateEndpointRoutetableResponse.
        :rtype: list[:class:`huaweicloudsdkvpcep.v1.RoutetableInfoError`]
        """
        return self._error

    @error.setter
    def error(self, error):
        """Sets the error of this UpdateEndpointRoutetableResponse.

        当修改终端节点子网路由表失败时，返回错误提示信息

        :param error: The error of this UpdateEndpointRoutetableResponse.
        :type error: list[:class:`huaweicloudsdkvpcep.v1.RoutetableInfoError`]
        """
        self._error = error

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
        if not isinstance(other, UpdateEndpointRoutetableResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
