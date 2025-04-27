# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VpcsData:

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
        'inbound_endpoint_count': 'int',
        'outbound_endpoint_count': 'int'
    }

    attribute_map = {
        'id': 'id',
        'inbound_endpoint_count': 'inbound_endpoint_count',
        'outbound_endpoint_count': 'outbound_endpoint_count'
    }

    def __init__(self, id=None, inbound_endpoint_count=None, outbound_endpoint_count=None):
        r"""VpcsData

        The model defined in huaweicloud sdk

        :param id: VPC的ID，UUID形式的一个资源标识。
        :type id: str
        :param inbound_endpoint_count: VPC下入站终端节点的数量。
        :type inbound_endpoint_count: int
        :param outbound_endpoint_count: VPC下出站终端节点的数量。
        :type outbound_endpoint_count: int
        """
        
        

        self._id = None
        self._inbound_endpoint_count = None
        self._outbound_endpoint_count = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if inbound_endpoint_count is not None:
            self.inbound_endpoint_count = inbound_endpoint_count
        if outbound_endpoint_count is not None:
            self.outbound_endpoint_count = outbound_endpoint_count

    @property
    def id(self):
        r"""Gets the id of this VpcsData.

        VPC的ID，UUID形式的一个资源标识。

        :return: The id of this VpcsData.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this VpcsData.

        VPC的ID，UUID形式的一个资源标识。

        :param id: The id of this VpcsData.
        :type id: str
        """
        self._id = id

    @property
    def inbound_endpoint_count(self):
        r"""Gets the inbound_endpoint_count of this VpcsData.

        VPC下入站终端节点的数量。

        :return: The inbound_endpoint_count of this VpcsData.
        :rtype: int
        """
        return self._inbound_endpoint_count

    @inbound_endpoint_count.setter
    def inbound_endpoint_count(self, inbound_endpoint_count):
        r"""Sets the inbound_endpoint_count of this VpcsData.

        VPC下入站终端节点的数量。

        :param inbound_endpoint_count: The inbound_endpoint_count of this VpcsData.
        :type inbound_endpoint_count: int
        """
        self._inbound_endpoint_count = inbound_endpoint_count

    @property
    def outbound_endpoint_count(self):
        r"""Gets the outbound_endpoint_count of this VpcsData.

        VPC下出站终端节点的数量。

        :return: The outbound_endpoint_count of this VpcsData.
        :rtype: int
        """
        return self._outbound_endpoint_count

    @outbound_endpoint_count.setter
    def outbound_endpoint_count(self, outbound_endpoint_count):
        r"""Sets the outbound_endpoint_count of this VpcsData.

        VPC下出站终端节点的数量。

        :param outbound_endpoint_count: The outbound_endpoint_count of this VpcsData.
        :type outbound_endpoint_count: int
        """
        self._outbound_endpoint_count = outbound_endpoint_count

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
        if not isinstance(other, VpcsData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
