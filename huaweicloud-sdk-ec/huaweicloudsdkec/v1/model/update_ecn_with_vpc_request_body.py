# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEcnWithVpcRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'local_subnet_list': 'list[str]',
        'refresh_remote_subnet_route': 'bool'
    }

    attribute_map = {
        'local_subnet_list': 'local_subnet_list',
        'refresh_remote_subnet_route': 'refresh_remote_subnet_route'
    }

    def __init__(self, local_subnet_list=None, refresh_remote_subnet_route=None):
        r"""UpdateEcnWithVpcRequestBody

        The model defined in huaweicloud sdk

        :param local_subnet_list: 本端子网列表
        :type local_subnet_list: list[str]
        :param refresh_remote_subnet_route: 是否刷新对端子网路由
        :type refresh_remote_subnet_route: bool
        """
        
        

        self._local_subnet_list = None
        self._refresh_remote_subnet_route = None
        self.discriminator = None

        if local_subnet_list is not None:
            self.local_subnet_list = local_subnet_list
        self.refresh_remote_subnet_route = refresh_remote_subnet_route

    @property
    def local_subnet_list(self):
        r"""Gets the local_subnet_list of this UpdateEcnWithVpcRequestBody.

        本端子网列表

        :return: The local_subnet_list of this UpdateEcnWithVpcRequestBody.
        :rtype: list[str]
        """
        return self._local_subnet_list

    @local_subnet_list.setter
    def local_subnet_list(self, local_subnet_list):
        r"""Sets the local_subnet_list of this UpdateEcnWithVpcRequestBody.

        本端子网列表

        :param local_subnet_list: The local_subnet_list of this UpdateEcnWithVpcRequestBody.
        :type local_subnet_list: list[str]
        """
        self._local_subnet_list = local_subnet_list

    @property
    def refresh_remote_subnet_route(self):
        r"""Gets the refresh_remote_subnet_route of this UpdateEcnWithVpcRequestBody.

        是否刷新对端子网路由

        :return: The refresh_remote_subnet_route of this UpdateEcnWithVpcRequestBody.
        :rtype: bool
        """
        return self._refresh_remote_subnet_route

    @refresh_remote_subnet_route.setter
    def refresh_remote_subnet_route(self, refresh_remote_subnet_route):
        r"""Sets the refresh_remote_subnet_route of this UpdateEcnWithVpcRequestBody.

        是否刷新对端子网路由

        :param refresh_remote_subnet_route: The refresh_remote_subnet_route of this UpdateEcnWithVpcRequestBody.
        :type refresh_remote_subnet_route: bool
        """
        self._refresh_remote_subnet_route = refresh_remote_subnet_route

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
        if not isinstance(other, UpdateEcnWithVpcRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
