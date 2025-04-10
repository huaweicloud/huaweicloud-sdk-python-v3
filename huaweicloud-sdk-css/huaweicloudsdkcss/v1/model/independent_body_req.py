# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class IndependentBodyReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'flavor_ref': 'str',
        'node_size': 'int',
        'volume_type': 'str'
    }

    attribute_map = {
        'flavor_ref': 'flavor_ref',
        'node_size': 'node_size',
        'volume_type': 'volume_type'
    }

    def __init__(self, flavor_ref=None, node_size=None, volume_type=None):
        r"""IndependentBodyReq

        The model defined in huaweicloud sdk

        :param flavor_ref: 规格id，该参数通过[获取实例规格列表](ListFlavors.xml)接口获取，根据集群版本选择所需要的规格id
        :type flavor_ref: str
        :param node_size: 要独立节点个数。 - 如果路径参数type取值为“ess-master”即新增独立master节点，节点个数必须为大于等于三且小于等于10的奇数。 - 如果路径参数type取值为“ess-client”即新增独立client节点，节点个数要求大于等于1小于等于32。
        :type node_size: int
        :param volume_type: 节点存储类型：取值为ULTRAHIGH，COMMON，HIGH。
        :type volume_type: str
        """
        
        

        self._flavor_ref = None
        self._node_size = None
        self._volume_type = None
        self.discriminator = None

        self.flavor_ref = flavor_ref
        self.node_size = node_size
        self.volume_type = volume_type

    @property
    def flavor_ref(self):
        r"""Gets the flavor_ref of this IndependentBodyReq.

        规格id，该参数通过[获取实例规格列表](ListFlavors.xml)接口获取，根据集群版本选择所需要的规格id

        :return: The flavor_ref of this IndependentBodyReq.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        r"""Sets the flavor_ref of this IndependentBodyReq.

        规格id，该参数通过[获取实例规格列表](ListFlavors.xml)接口获取，根据集群版本选择所需要的规格id

        :param flavor_ref: The flavor_ref of this IndependentBodyReq.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def node_size(self):
        r"""Gets the node_size of this IndependentBodyReq.

        要独立节点个数。 - 如果路径参数type取值为“ess-master”即新增独立master节点，节点个数必须为大于等于三且小于等于10的奇数。 - 如果路径参数type取值为“ess-client”即新增独立client节点，节点个数要求大于等于1小于等于32。

        :return: The node_size of this IndependentBodyReq.
        :rtype: int
        """
        return self._node_size

    @node_size.setter
    def node_size(self, node_size):
        r"""Sets the node_size of this IndependentBodyReq.

        要独立节点个数。 - 如果路径参数type取值为“ess-master”即新增独立master节点，节点个数必须为大于等于三且小于等于10的奇数。 - 如果路径参数type取值为“ess-client”即新增独立client节点，节点个数要求大于等于1小于等于32。

        :param node_size: The node_size of this IndependentBodyReq.
        :type node_size: int
        """
        self._node_size = node_size

    @property
    def volume_type(self):
        r"""Gets the volume_type of this IndependentBodyReq.

        节点存储类型：取值为ULTRAHIGH，COMMON，HIGH。

        :return: The volume_type of this IndependentBodyReq.
        :rtype: str
        """
        return self._volume_type

    @volume_type.setter
    def volume_type(self, volume_type):
        r"""Sets the volume_type of this IndependentBodyReq.

        节点存储类型：取值为ULTRAHIGH，COMMON，HIGH。

        :param volume_type: The volume_type of this IndependentBodyReq.
        :type volume_type: str
        """
        self._volume_type = volume_type

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
        if not isinstance(other, IndependentBodyReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
