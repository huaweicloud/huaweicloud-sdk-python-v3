# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateNodeByDeviceIdResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'update_nodes': 'NodeUpdateByDevice'
    }

    attribute_map = {
        'update_nodes': 'update_nodes'
    }

    def __init__(self, update_nodes=None):
        """UpdateNodeByDeviceIdResponse

        The model defined in huaweicloud sdk

        :param update_nodes: 
        :type update_nodes: :class:`huaweicloudsdkief.v1.NodeUpdateByDevice`
        """
        
        super(UpdateNodeByDeviceIdResponse, self).__init__()

        self._update_nodes = None
        self.discriminator = None

        if update_nodes is not None:
            self.update_nodes = update_nodes

    @property
    def update_nodes(self):
        """Gets the update_nodes of this UpdateNodeByDeviceIdResponse.


        :return: The update_nodes of this UpdateNodeByDeviceIdResponse.
        :rtype: :class:`huaweicloudsdkief.v1.NodeUpdateByDevice`
        """
        return self._update_nodes

    @update_nodes.setter
    def update_nodes(self, update_nodes):
        """Sets the update_nodes of this UpdateNodeByDeviceIdResponse.


        :param update_nodes: The update_nodes of this UpdateNodeByDeviceIdResponse.
        :type update_nodes: :class:`huaweicloudsdkief.v1.NodeUpdateByDevice`
        """
        self._update_nodes = update_nodes

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
        if not isinstance(other, UpdateNodeByDeviceIdResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
