# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublicIpInfoResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'address': 'str',
        'status': 'str',
        'instance_id': 'str',
        'instance_name': 'str',
        'bandwidth_size': 'str'
    }

    attribute_map = {
        'id': 'id',
        'address': 'address',
        'status': 'status',
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'bandwidth_size': 'bandwidth_size'
    }

    def __init__(self, id=None, address=None, status=None, instance_id=None, instance_name=None, bandwidth_size=None):
        r"""PublicIpInfoResponse

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 公网IP的ID。 **取值范围**： 不涉及。
        :type id: str
        :param address: **参数解释**： 公网IP。 **取值范围**： 合法的公网IPV4地址。
        :type address: str
        :param status: **参数解释**： 公网IP状态。 **取值范围**： 不涉及。
        :type status: str
        :param instance_id: **参数解释**： 绑定的DWS集群的节点ID。 **取值范围**： 不涉及。
        :type instance_id: str
        :param instance_name: **参数解释**： 绑定的DWS集群的节点名称。 **取值范围**： 不涉及。
        :type instance_name: str
        :param bandwidth_size: **参数解释**： 公网IP带宽信息。 **取值范围**： 不涉及。
        :type bandwidth_size: str
        """
        
        

        self._id = None
        self._address = None
        self._status = None
        self._instance_id = None
        self._instance_name = None
        self._bandwidth_size = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if address is not None:
            self.address = address
        if status is not None:
            self.status = status
        if instance_id is not None:
            self.instance_id = instance_id
        if instance_name is not None:
            self.instance_name = instance_name
        if bandwidth_size is not None:
            self.bandwidth_size = bandwidth_size

    @property
    def id(self):
        r"""Gets the id of this PublicIpInfoResponse.

        **参数解释**： 公网IP的ID。 **取值范围**： 不涉及。

        :return: The id of this PublicIpInfoResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PublicIpInfoResponse.

        **参数解释**： 公网IP的ID。 **取值范围**： 不涉及。

        :param id: The id of this PublicIpInfoResponse.
        :type id: str
        """
        self._id = id

    @property
    def address(self):
        r"""Gets the address of this PublicIpInfoResponse.

        **参数解释**： 公网IP。 **取值范围**： 合法的公网IPV4地址。

        :return: The address of this PublicIpInfoResponse.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this PublicIpInfoResponse.

        **参数解释**： 公网IP。 **取值范围**： 合法的公网IPV4地址。

        :param address: The address of this PublicIpInfoResponse.
        :type address: str
        """
        self._address = address

    @property
    def status(self):
        r"""Gets the status of this PublicIpInfoResponse.

        **参数解释**： 公网IP状态。 **取值范围**： 不涉及。

        :return: The status of this PublicIpInfoResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this PublicIpInfoResponse.

        **参数解释**： 公网IP状态。 **取值范围**： 不涉及。

        :param status: The status of this PublicIpInfoResponse.
        :type status: str
        """
        self._status = status

    @property
    def instance_id(self):
        r"""Gets the instance_id of this PublicIpInfoResponse.

        **参数解释**： 绑定的DWS集群的节点ID。 **取值范围**： 不涉及。

        :return: The instance_id of this PublicIpInfoResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this PublicIpInfoResponse.

        **参数解释**： 绑定的DWS集群的节点ID。 **取值范围**： 不涉及。

        :param instance_id: The instance_id of this PublicIpInfoResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this PublicIpInfoResponse.

        **参数解释**： 绑定的DWS集群的节点名称。 **取值范围**： 不涉及。

        :return: The instance_name of this PublicIpInfoResponse.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this PublicIpInfoResponse.

        **参数解释**： 绑定的DWS集群的节点名称。 **取值范围**： 不涉及。

        :param instance_name: The instance_name of this PublicIpInfoResponse.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def bandwidth_size(self):
        r"""Gets the bandwidth_size of this PublicIpInfoResponse.

        **参数解释**： 公网IP带宽信息。 **取值范围**： 不涉及。

        :return: The bandwidth_size of this PublicIpInfoResponse.
        :rtype: str
        """
        return self._bandwidth_size

    @bandwidth_size.setter
    def bandwidth_size(self, bandwidth_size):
        r"""Sets the bandwidth_size of this PublicIpInfoResponse.

        **参数解释**： 公网IP带宽信息。 **取值范围**： 不涉及。

        :param bandwidth_size: The bandwidth_size of this PublicIpInfoResponse.
        :type bandwidth_size: str
        """
        self._bandwidth_size = bandwidth_size

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
        if not isinstance(other, PublicIpInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
