# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNodesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, cluster_id=None, limit=None, marker=None):
        r"""ListNodesRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。
        :type cluster_id: str
        :param limit: **参数解释**： 设置每页显示的数据条数。 **约束限制**： 不涉及 **取值范围**： 1到2000之间（含1和2000）的整数。 **默认取值**： 2000
        :type limit: int
        :param marker: **参数解释**： 通过资源uid进行分页查询,默认为查询第一页数据。marker&#x3D;{{uid}}表示查询该uid后的资源列表的信息(查询结果不包含该uid的资源)。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 无
        :type marker: str
        """
        
        

        self._cluster_id = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        self.cluster_id = cluster_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListNodesRequest.

        集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :return: The cluster_id of this ListNodesRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListNodesRequest.

        集群ID，获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。

        :param cluster_id: The cluster_id of this ListNodesRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def limit(self):
        r"""Gets the limit of this ListNodesRequest.

        **参数解释**： 设置每页显示的数据条数。 **约束限制**： 不涉及 **取值范围**： 1到2000之间（含1和2000）的整数。 **默认取值**： 2000

        :return: The limit of this ListNodesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListNodesRequest.

        **参数解释**： 设置每页显示的数据条数。 **约束限制**： 不涉及 **取值范围**： 1到2000之间（含1和2000）的整数。 **默认取值**： 2000

        :param limit: The limit of this ListNodesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListNodesRequest.

        **参数解释**： 通过资源uid进行分页查询,默认为查询第一页数据。marker={{uid}}表示查询该uid后的资源列表的信息(查询结果不包含该uid的资源)。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 无

        :return: The marker of this ListNodesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListNodesRequest.

        **参数解释**： 通过资源uid进行分页查询,默认为查询第一页数据。marker={{uid}}表示查询该uid后的资源列表的信息(查询结果不包含该uid的资源)。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 无

        :param marker: The marker of this ListNodesRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListNodesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
