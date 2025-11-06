# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVulRepairCmdsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'select_type': 'str',
        'data_list': 'list[VulOperateInfo]',
        'host_data_list': 'list[HostVulOperateInfo]',
        'is_container': 'bool',
        'cluster_id': 'str'
    }

    attribute_map = {
        'select_type': 'select_type',
        'data_list': 'data_list',
        'host_data_list': 'host_data_list',
        'is_container': 'is_container',
        'cluster_id': 'cluster_id'
    }

    def __init__(self, select_type=None, data_list=None, host_data_list=None, is_container=None, cluster_id=None):
        r"""ListVulRepairCmdsRequestBody

        The model defined in huaweicloud sdk

        :param select_type: **参数解释**: 选择全部漏洞类型,该参数优先级高于data_list和host_data_list **约束限制**: 不涉及 **取值范围**: - all_vul：选择全部漏洞 - all_host：选择全部主机漏洞 - all_vul_container_host：选择所有容器节点 - all_vul_container：选择所有容器  **默认取值**: 不涉及 
        :type select_type: str
        :param data_list: **参数解释**: 漏洞列表 **约束限制**: 不涉及 **取值范围**: 最少1条，最多500条 **默认取值**: 不涉及 
        :type data_list: list[:class:`huaweicloudsdkhss.v5.VulOperateInfo`]
        :param host_data_list: **参数解释**: 主机维度漏洞列表 **约束限制**: 不涉及 **取值范围**: 最少1条，最多500条 **默认取值**: 不涉及 
        :type host_data_list: list[:class:`huaweicloudsdkhss.v5.HostVulOperateInfo`]
        :param is_container: **参数解释**: 是否是容器场景 **约束限制**: 不涉及 **取值范围**: - true：是容器场景 - false：不是容器场景 **默认取值**: false 
        :type is_container: bool
        :param cluster_id: **参数解释**: 集群id **约束限制**: 不涉及 **取值范围**: 字符长度0-256 **默认取值**: 不涉及 
        :type cluster_id: str
        """
        
        

        self._select_type = None
        self._data_list = None
        self._host_data_list = None
        self._is_container = None
        self._cluster_id = None
        self.discriminator = None

        if select_type is not None:
            self.select_type = select_type
        if data_list is not None:
            self.data_list = data_list
        if host_data_list is not None:
            self.host_data_list = host_data_list
        if is_container is not None:
            self.is_container = is_container
        if cluster_id is not None:
            self.cluster_id = cluster_id

    @property
    def select_type(self):
        r"""Gets the select_type of this ListVulRepairCmdsRequestBody.

        **参数解释**: 选择全部漏洞类型,该参数优先级高于data_list和host_data_list **约束限制**: 不涉及 **取值范围**: - all_vul：选择全部漏洞 - all_host：选择全部主机漏洞 - all_vul_container_host：选择所有容器节点 - all_vul_container：选择所有容器  **默认取值**: 不涉及 

        :return: The select_type of this ListVulRepairCmdsRequestBody.
        :rtype: str
        """
        return self._select_type

    @select_type.setter
    def select_type(self, select_type):
        r"""Sets the select_type of this ListVulRepairCmdsRequestBody.

        **参数解释**: 选择全部漏洞类型,该参数优先级高于data_list和host_data_list **约束限制**: 不涉及 **取值范围**: - all_vul：选择全部漏洞 - all_host：选择全部主机漏洞 - all_vul_container_host：选择所有容器节点 - all_vul_container：选择所有容器  **默认取值**: 不涉及 

        :param select_type: The select_type of this ListVulRepairCmdsRequestBody.
        :type select_type: str
        """
        self._select_type = select_type

    @property
    def data_list(self):
        r"""Gets the data_list of this ListVulRepairCmdsRequestBody.

        **参数解释**: 漏洞列表 **约束限制**: 不涉及 **取值范围**: 最少1条，最多500条 **默认取值**: 不涉及 

        :return: The data_list of this ListVulRepairCmdsRequestBody.
        :rtype: list[:class:`huaweicloudsdkhss.v5.VulOperateInfo`]
        """
        return self._data_list

    @data_list.setter
    def data_list(self, data_list):
        r"""Sets the data_list of this ListVulRepairCmdsRequestBody.

        **参数解释**: 漏洞列表 **约束限制**: 不涉及 **取值范围**: 最少1条，最多500条 **默认取值**: 不涉及 

        :param data_list: The data_list of this ListVulRepairCmdsRequestBody.
        :type data_list: list[:class:`huaweicloudsdkhss.v5.VulOperateInfo`]
        """
        self._data_list = data_list

    @property
    def host_data_list(self):
        r"""Gets the host_data_list of this ListVulRepairCmdsRequestBody.

        **参数解释**: 主机维度漏洞列表 **约束限制**: 不涉及 **取值范围**: 最少1条，最多500条 **默认取值**: 不涉及 

        :return: The host_data_list of this ListVulRepairCmdsRequestBody.
        :rtype: list[:class:`huaweicloudsdkhss.v5.HostVulOperateInfo`]
        """
        return self._host_data_list

    @host_data_list.setter
    def host_data_list(self, host_data_list):
        r"""Sets the host_data_list of this ListVulRepairCmdsRequestBody.

        **参数解释**: 主机维度漏洞列表 **约束限制**: 不涉及 **取值范围**: 最少1条，最多500条 **默认取值**: 不涉及 

        :param host_data_list: The host_data_list of this ListVulRepairCmdsRequestBody.
        :type host_data_list: list[:class:`huaweicloudsdkhss.v5.HostVulOperateInfo`]
        """
        self._host_data_list = host_data_list

    @property
    def is_container(self):
        r"""Gets the is_container of this ListVulRepairCmdsRequestBody.

        **参数解释**: 是否是容器场景 **约束限制**: 不涉及 **取值范围**: - true：是容器场景 - false：不是容器场景 **默认取值**: false 

        :return: The is_container of this ListVulRepairCmdsRequestBody.
        :rtype: bool
        """
        return self._is_container

    @is_container.setter
    def is_container(self, is_container):
        r"""Sets the is_container of this ListVulRepairCmdsRequestBody.

        **参数解释**: 是否是容器场景 **约束限制**: 不涉及 **取值范围**: - true：是容器场景 - false：不是容器场景 **默认取值**: false 

        :param is_container: The is_container of this ListVulRepairCmdsRequestBody.
        :type is_container: bool
        """
        self._is_container = is_container

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ListVulRepairCmdsRequestBody.

        **参数解释**: 集群id **约束限制**: 不涉及 **取值范围**: 字符长度0-256 **默认取值**: 不涉及 

        :return: The cluster_id of this ListVulRepairCmdsRequestBody.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ListVulRepairCmdsRequestBody.

        **参数解释**: 集群id **约束限制**: 不涉及 **取值范围**: 字符长度0-256 **默认取值**: 不涉及 

        :param cluster_id: The cluster_id of this ListVulRepairCmdsRequestBody.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

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
        if not isinstance(other, ListVulRepairCmdsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
