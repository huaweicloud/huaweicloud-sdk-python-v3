# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodePublicIP:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ids': 'list[str]',
        'count': 'int',
        'eip': 'NodeEIPSpec'
    }

    attribute_map = {
        'ids': 'ids',
        'count': 'count',
        'eip': 'eip'
    }

    def __init__(self, ids=None, count=None, eip=None):
        r"""NodePublicIP

        The model defined in huaweicloud sdk

        :param ids: **参数解释**： 已有的弹性IP的ID列表。数量不得大于待创建节点数 &gt; 若已配置ids参数，则无需配置count和eip参数 **约束限制**： 该参数仅给节点使用
        :type ids: list[str]
        :param count: **参数解释**： 要动态创建的弹性IP个数。 &gt; count参数与eip参数必须同时配置。 **约束限制**： 该参数仅给节点使用
        :type count: int
        :param eip: 
        :type eip: :class:`huaweicloudsdkcce.v3.NodeEIPSpec`
        """
        
        

        self._ids = None
        self._count = None
        self._eip = None
        self.discriminator = None

        if ids is not None:
            self.ids = ids
        if count is not None:
            self.count = count
        if eip is not None:
            self.eip = eip

    @property
    def ids(self):
        r"""Gets the ids of this NodePublicIP.

        **参数解释**： 已有的弹性IP的ID列表。数量不得大于待创建节点数 > 若已配置ids参数，则无需配置count和eip参数 **约束限制**： 该参数仅给节点使用

        :return: The ids of this NodePublicIP.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this NodePublicIP.

        **参数解释**： 已有的弹性IP的ID列表。数量不得大于待创建节点数 > 若已配置ids参数，则无需配置count和eip参数 **约束限制**： 该参数仅给节点使用

        :param ids: The ids of this NodePublicIP.
        :type ids: list[str]
        """
        self._ids = ids

    @property
    def count(self):
        r"""Gets the count of this NodePublicIP.

        **参数解释**： 要动态创建的弹性IP个数。 > count参数与eip参数必须同时配置。 **约束限制**： 该参数仅给节点使用

        :return: The count of this NodePublicIP.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this NodePublicIP.

        **参数解释**： 要动态创建的弹性IP个数。 > count参数与eip参数必须同时配置。 **约束限制**： 该参数仅给节点使用

        :param count: The count of this NodePublicIP.
        :type count: int
        """
        self._count = count

    @property
    def eip(self):
        r"""Gets the eip of this NodePublicIP.

        :return: The eip of this NodePublicIP.
        :rtype: :class:`huaweicloudsdkcce.v3.NodeEIPSpec`
        """
        return self._eip

    @eip.setter
    def eip(self, eip):
        r"""Sets the eip of this NodePublicIP.

        :param eip: The eip of this NodePublicIP.
        :type eip: :class:`huaweicloudsdkcce.v3.NodeEIPSpec`
        """
        self._eip = eip

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NodePublicIP):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
