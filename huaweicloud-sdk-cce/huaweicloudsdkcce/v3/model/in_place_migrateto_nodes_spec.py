# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InPlaceMigratetoNodesSpec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'nodes': 'list[InplaceMigrateNodeItem]',
        'data_disk_clean_up_option': 'DataDiskCleanUpOption',
        'extend_param': 'InPlaceMigrateNodeExtendParam'
    }

    attribute_map = {
        'nodes': 'nodes',
        'data_disk_clean_up_option': 'dataDiskCleanUpOption',
        'extend_param': 'extendParam'
    }

    def __init__(self, nodes=None, data_disk_clean_up_option=None, extend_param=None):
        r"""InPlaceMigratetoNodesSpec

        The model defined in huaweicloud sdk

        :param nodes: **参数解释**： 腾挪节点列表 **约束限制**： 不涉及 
        :type nodes: list[:class:`huaweicloudsdkcce.v3.InplaceMigrateNodeItem`]
        :param data_disk_clean_up_option: 
        :type data_disk_clean_up_option: :class:`huaweicloudsdkcce.v3.DataDiskCleanUpOption`
        :param extend_param: 
        :type extend_param: :class:`huaweicloudsdkcce.v3.InPlaceMigrateNodeExtendParam`
        """
        
        

        self._nodes = None
        self._data_disk_clean_up_option = None
        self._extend_param = None
        self.discriminator = None

        self.nodes = nodes
        if data_disk_clean_up_option is not None:
            self.data_disk_clean_up_option = data_disk_clean_up_option
        if extend_param is not None:
            self.extend_param = extend_param

    @property
    def nodes(self):
        r"""Gets the nodes of this InPlaceMigratetoNodesSpec.

        **参数解释**： 腾挪节点列表 **约束限制**： 不涉及 

        :return: The nodes of this InPlaceMigratetoNodesSpec.
        :rtype: list[:class:`huaweicloudsdkcce.v3.InplaceMigrateNodeItem`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        r"""Sets the nodes of this InPlaceMigratetoNodesSpec.

        **参数解释**： 腾挪节点列表 **约束限制**： 不涉及 

        :param nodes: The nodes of this InPlaceMigratetoNodesSpec.
        :type nodes: list[:class:`huaweicloudsdkcce.v3.InplaceMigrateNodeItem`]
        """
        self._nodes = nodes

    @property
    def data_disk_clean_up_option(self):
        r"""Gets the data_disk_clean_up_option of this InPlaceMigratetoNodesSpec.

        :return: The data_disk_clean_up_option of this InPlaceMigratetoNodesSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.DataDiskCleanUpOption`
        """
        return self._data_disk_clean_up_option

    @data_disk_clean_up_option.setter
    def data_disk_clean_up_option(self, data_disk_clean_up_option):
        r"""Sets the data_disk_clean_up_option of this InPlaceMigratetoNodesSpec.

        :param data_disk_clean_up_option: The data_disk_clean_up_option of this InPlaceMigratetoNodesSpec.
        :type data_disk_clean_up_option: :class:`huaweicloudsdkcce.v3.DataDiskCleanUpOption`
        """
        self._data_disk_clean_up_option = data_disk_clean_up_option

    @property
    def extend_param(self):
        r"""Gets the extend_param of this InPlaceMigratetoNodesSpec.

        :return: The extend_param of this InPlaceMigratetoNodesSpec.
        :rtype: :class:`huaweicloudsdkcce.v3.InPlaceMigrateNodeExtendParam`
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        r"""Sets the extend_param of this InPlaceMigratetoNodesSpec.

        :param extend_param: The extend_param of this InPlaceMigratetoNodesSpec.
        :type extend_param: :class:`huaweicloudsdkcce.v3.InPlaceMigrateNodeExtendParam`
        """
        self._extend_param = extend_param

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
        if not isinstance(other, InPlaceMigratetoNodesSpec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
