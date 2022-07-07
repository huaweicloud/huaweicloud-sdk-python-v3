# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowVpcepConnectionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'connections': 'list[Connections]',
        'vpcep_update_switch': 'bool',
        'total_count': 'int'
    }

    attribute_map = {
        'connections': 'connections',
        'vpcep_update_switch': 'vpcepUpdateSwitch',
        'total_count': 'total_count'
    }

    def __init__(self, connections=None, vpcep_update_switch=None, total_count=None):
        """ShowVpcepConnectionResponse

        The model defined in huaweicloud sdk

        :param connections: 
        :type connections: list[:class:`huaweicloudsdkcss.v1.Connections`]
        :param vpcep_update_switch: 终端节点更新开关。 - true： 开启终端节点。 - false： 关闭终端节点。
        :type vpcep_update_switch: bool
        :param total_count: 终端节点数量。
        :type total_count: int
        """
        
        super(ShowVpcepConnectionResponse, self).__init__()

        self._connections = None
        self._vpcep_update_switch = None
        self._total_count = None
        self.discriminator = None

        if connections is not None:
            self.connections = connections
        if vpcep_update_switch is not None:
            self.vpcep_update_switch = vpcep_update_switch
        if total_count is not None:
            self.total_count = total_count

    @property
    def connections(self):
        """Gets the connections of this ShowVpcepConnectionResponse.


        :return: The connections of this ShowVpcepConnectionResponse.
        :rtype: list[:class:`huaweicloudsdkcss.v1.Connections`]
        """
        return self._connections

    @connections.setter
    def connections(self, connections):
        """Sets the connections of this ShowVpcepConnectionResponse.


        :param connections: The connections of this ShowVpcepConnectionResponse.
        :type connections: list[:class:`huaweicloudsdkcss.v1.Connections`]
        """
        self._connections = connections

    @property
    def vpcep_update_switch(self):
        """Gets the vpcep_update_switch of this ShowVpcepConnectionResponse.

        终端节点更新开关。 - true： 开启终端节点。 - false： 关闭终端节点。

        :return: The vpcep_update_switch of this ShowVpcepConnectionResponse.
        :rtype: bool
        """
        return self._vpcep_update_switch

    @vpcep_update_switch.setter
    def vpcep_update_switch(self, vpcep_update_switch):
        """Sets the vpcep_update_switch of this ShowVpcepConnectionResponse.

        终端节点更新开关。 - true： 开启终端节点。 - false： 关闭终端节点。

        :param vpcep_update_switch: The vpcep_update_switch of this ShowVpcepConnectionResponse.
        :type vpcep_update_switch: bool
        """
        self._vpcep_update_switch = vpcep_update_switch

    @property
    def total_count(self):
        """Gets the total_count of this ShowVpcepConnectionResponse.

        终端节点数量。

        :return: The total_count of this ShowVpcepConnectionResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ShowVpcepConnectionResponse.

        终端节点数量。

        :param total_count: The total_count of this ShowVpcepConnectionResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ShowVpcepConnectionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
