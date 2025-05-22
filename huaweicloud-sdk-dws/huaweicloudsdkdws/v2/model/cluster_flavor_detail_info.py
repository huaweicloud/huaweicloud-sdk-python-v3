# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterFlavorDetailInfo:

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
        'spec_name': 'str',
        'current_node': 'int',
        'min_node': 'int',
        'max_node': 'int',
        'classify': 'str',
        'datastore_version': 'str',
        'attribute': 'list[FlavorAttributeInfo]',
        'volume_node': 'FlavorVolumeNodeInfo'
    }

    attribute_map = {
        'id': 'id',
        'spec_name': 'spec_name',
        'current_node': 'current_node',
        'min_node': 'min_node',
        'max_node': 'max_node',
        'classify': 'classify',
        'datastore_version': 'datastore_version',
        'attribute': 'attribute',
        'volume_node': 'volume_node'
    }

    def __init__(self, id=None, spec_name=None, current_node=None, min_node=None, max_node=None, classify=None, datastore_version=None, attribute=None, volume_node=None):
        r"""ClusterFlavorDetailInfo

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 规格ID。 **取值范围**： 不涉及。
        :type id: str
        :param spec_name: **参数解释**： 规格编码。 **取值范围**： 不涉及。
        :type spec_name: str
        :param current_node: **参数解释**： 当前节点数量。 **取值范围**： 不涉及。
        :type current_node: int
        :param min_node: **参数解释**： 最小节点阈值。 **取值范围**： 不涉及。
        :type min_node: int
        :param max_node: **参数解释**： 最大节点阈值。 **取值范围**： 不涉及。
        :type max_node: int
        :param classify: **参数解释**： 规格类型。 **取值范围**： 不涉及。
        :type classify: str
        :param datastore_version: **参数解释**： 数据仓库版本。 **取值范围**： 不涉及。
        :type datastore_version: str
        :param attribute: **参数解释**： 扩展信息。 **取值范围**： 不涉及。
        :type attribute: list[:class:`huaweicloudsdkdws.v2.FlavorAttributeInfo`]
        :param volume_node: 
        :type volume_node: :class:`huaweicloudsdkdws.v2.FlavorVolumeNodeInfo`
        """
        
        

        self._id = None
        self._spec_name = None
        self._current_node = None
        self._min_node = None
        self._max_node = None
        self._classify = None
        self._datastore_version = None
        self._attribute = None
        self._volume_node = None
        self.discriminator = None

        self.id = id
        self.spec_name = spec_name
        self.current_node = current_node
        self.min_node = min_node
        self.max_node = max_node
        self.classify = classify
        self.datastore_version = datastore_version
        self.attribute = attribute
        self.volume_node = volume_node

    @property
    def id(self):
        r"""Gets the id of this ClusterFlavorDetailInfo.

        **参数解释**： 规格ID。 **取值范围**： 不涉及。

        :return: The id of this ClusterFlavorDetailInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ClusterFlavorDetailInfo.

        **参数解释**： 规格ID。 **取值范围**： 不涉及。

        :param id: The id of this ClusterFlavorDetailInfo.
        :type id: str
        """
        self._id = id

    @property
    def spec_name(self):
        r"""Gets the spec_name of this ClusterFlavorDetailInfo.

        **参数解释**： 规格编码。 **取值范围**： 不涉及。

        :return: The spec_name of this ClusterFlavorDetailInfo.
        :rtype: str
        """
        return self._spec_name

    @spec_name.setter
    def spec_name(self, spec_name):
        r"""Sets the spec_name of this ClusterFlavorDetailInfo.

        **参数解释**： 规格编码。 **取值范围**： 不涉及。

        :param spec_name: The spec_name of this ClusterFlavorDetailInfo.
        :type spec_name: str
        """
        self._spec_name = spec_name

    @property
    def current_node(self):
        r"""Gets the current_node of this ClusterFlavorDetailInfo.

        **参数解释**： 当前节点数量。 **取值范围**： 不涉及。

        :return: The current_node of this ClusterFlavorDetailInfo.
        :rtype: int
        """
        return self._current_node

    @current_node.setter
    def current_node(self, current_node):
        r"""Sets the current_node of this ClusterFlavorDetailInfo.

        **参数解释**： 当前节点数量。 **取值范围**： 不涉及。

        :param current_node: The current_node of this ClusterFlavorDetailInfo.
        :type current_node: int
        """
        self._current_node = current_node

    @property
    def min_node(self):
        r"""Gets the min_node of this ClusterFlavorDetailInfo.

        **参数解释**： 最小节点阈值。 **取值范围**： 不涉及。

        :return: The min_node of this ClusterFlavorDetailInfo.
        :rtype: int
        """
        return self._min_node

    @min_node.setter
    def min_node(self, min_node):
        r"""Sets the min_node of this ClusterFlavorDetailInfo.

        **参数解释**： 最小节点阈值。 **取值范围**： 不涉及。

        :param min_node: The min_node of this ClusterFlavorDetailInfo.
        :type min_node: int
        """
        self._min_node = min_node

    @property
    def max_node(self):
        r"""Gets the max_node of this ClusterFlavorDetailInfo.

        **参数解释**： 最大节点阈值。 **取值范围**： 不涉及。

        :return: The max_node of this ClusterFlavorDetailInfo.
        :rtype: int
        """
        return self._max_node

    @max_node.setter
    def max_node(self, max_node):
        r"""Sets the max_node of this ClusterFlavorDetailInfo.

        **参数解释**： 最大节点阈值。 **取值范围**： 不涉及。

        :param max_node: The max_node of this ClusterFlavorDetailInfo.
        :type max_node: int
        """
        self._max_node = max_node

    @property
    def classify(self):
        r"""Gets the classify of this ClusterFlavorDetailInfo.

        **参数解释**： 规格类型。 **取值范围**： 不涉及。

        :return: The classify of this ClusterFlavorDetailInfo.
        :rtype: str
        """
        return self._classify

    @classify.setter
    def classify(self, classify):
        r"""Sets the classify of this ClusterFlavorDetailInfo.

        **参数解释**： 规格类型。 **取值范围**： 不涉及。

        :param classify: The classify of this ClusterFlavorDetailInfo.
        :type classify: str
        """
        self._classify = classify

    @property
    def datastore_version(self):
        r"""Gets the datastore_version of this ClusterFlavorDetailInfo.

        **参数解释**： 数据仓库版本。 **取值范围**： 不涉及。

        :return: The datastore_version of this ClusterFlavorDetailInfo.
        :rtype: str
        """
        return self._datastore_version

    @datastore_version.setter
    def datastore_version(self, datastore_version):
        r"""Sets the datastore_version of this ClusterFlavorDetailInfo.

        **参数解释**： 数据仓库版本。 **取值范围**： 不涉及。

        :param datastore_version: The datastore_version of this ClusterFlavorDetailInfo.
        :type datastore_version: str
        """
        self._datastore_version = datastore_version

    @property
    def attribute(self):
        r"""Gets the attribute of this ClusterFlavorDetailInfo.

        **参数解释**： 扩展信息。 **取值范围**： 不涉及。

        :return: The attribute of this ClusterFlavorDetailInfo.
        :rtype: list[:class:`huaweicloudsdkdws.v2.FlavorAttributeInfo`]
        """
        return self._attribute

    @attribute.setter
    def attribute(self, attribute):
        r"""Sets the attribute of this ClusterFlavorDetailInfo.

        **参数解释**： 扩展信息。 **取值范围**： 不涉及。

        :param attribute: The attribute of this ClusterFlavorDetailInfo.
        :type attribute: list[:class:`huaweicloudsdkdws.v2.FlavorAttributeInfo`]
        """
        self._attribute = attribute

    @property
    def volume_node(self):
        r"""Gets the volume_node of this ClusterFlavorDetailInfo.

        :return: The volume_node of this ClusterFlavorDetailInfo.
        :rtype: :class:`huaweicloudsdkdws.v2.FlavorVolumeNodeInfo`
        """
        return self._volume_node

    @volume_node.setter
    def volume_node(self, volume_node):
        r"""Sets the volume_node of this ClusterFlavorDetailInfo.

        :param volume_node: The volume_node of this ClusterFlavorDetailInfo.
        :type volume_node: :class:`huaweicloudsdkdws.v2.FlavorVolumeNodeInfo`
        """
        self._volume_node = volume_node

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
        if not isinstance(other, ClusterFlavorDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
