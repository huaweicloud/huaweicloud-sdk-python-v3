# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BridgeResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'bridge_id': 'str',
        'bridge_name': 'str',
        'status': 'str'
    }

    attribute_map = {
        'bridge_id': 'bridge_id',
        'bridge_name': 'bridge_name',
        'status': 'status'
    }

    def __init__(self, bridge_id=None, bridge_name=None, status=None):
        r"""BridgeResponse

        The model defined in huaweicloud sdk

        :param bridge_id: 网桥ID
        :type bridge_id: str
        :param bridge_name: 网桥名称。
        :type bridge_name: str
        :param status: 网桥状态。 - ONLINE：网桥在线。 - OFFLINE：网桥离线。 
        :type status: str
        """
        
        

        self._bridge_id = None
        self._bridge_name = None
        self._status = None
        self.discriminator = None

        if bridge_id is not None:
            self.bridge_id = bridge_id
        if bridge_name is not None:
            self.bridge_name = bridge_name
        if status is not None:
            self.status = status

    @property
    def bridge_id(self):
        r"""Gets the bridge_id of this BridgeResponse.

        网桥ID

        :return: The bridge_id of this BridgeResponse.
        :rtype: str
        """
        return self._bridge_id

    @bridge_id.setter
    def bridge_id(self, bridge_id):
        r"""Sets the bridge_id of this BridgeResponse.

        网桥ID

        :param bridge_id: The bridge_id of this BridgeResponse.
        :type bridge_id: str
        """
        self._bridge_id = bridge_id

    @property
    def bridge_name(self):
        r"""Gets the bridge_name of this BridgeResponse.

        网桥名称。

        :return: The bridge_name of this BridgeResponse.
        :rtype: str
        """
        return self._bridge_name

    @bridge_name.setter
    def bridge_name(self, bridge_name):
        r"""Sets the bridge_name of this BridgeResponse.

        网桥名称。

        :param bridge_name: The bridge_name of this BridgeResponse.
        :type bridge_name: str
        """
        self._bridge_name = bridge_name

    @property
    def status(self):
        r"""Gets the status of this BridgeResponse.

        网桥状态。 - ONLINE：网桥在线。 - OFFLINE：网桥离线。 

        :return: The status of this BridgeResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this BridgeResponse.

        网桥状态。 - ONLINE：网桥在线。 - OFFLINE：网桥离线。 

        :param status: The status of this BridgeResponse.
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
        if not isinstance(other, BridgeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
