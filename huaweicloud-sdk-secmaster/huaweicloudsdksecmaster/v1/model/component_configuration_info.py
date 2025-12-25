# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentConfigurationInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'configuration_status': 'str',
        'list': 'list[ComponentConfigurationParamVo]',
        'node_id': 'str',
        'node_name': 'str',
        'node_status': 'str',
        'specification': 'str'
    }

    attribute_map = {
        'configuration_status': 'configuration_status',
        'list': 'list',
        'node_id': 'node_id',
        'node_name': 'node_name',
        'node_status': 'node_status',
        'specification': 'specification'
    }

    def __init__(self, configuration_status=None, list=None, node_id=None, node_name=None, node_status=None, specification=None):
        r"""ComponentConfigurationInfo

        The model defined in huaweicloud sdk

        :param configuration_status: 节点配置状态 UN_SAVED 未保存 SAVE_AND_UN_DEPLOY 保存未部署 DEPLOYING正在部署 MOVE_AND_UN_DEPLOY 移除未应用 FAIL_DEPLOY部署失败 DEPLOYED已部署
        :type configuration_status: str
        :param list: 文件参数信息
        :type list: list[:class:`huaweicloudsdksecmaster.v1.ComponentConfigurationParamVo`]
        :param node_id: 节点ID
        :type node_id: str
        :param node_name: 节点名
        :type node_name: str
        :param node_status: 枚举 节点状态 NORMAL正常 ANOMALIES异常 FAULTS 故障 LOST_CONTACT 失联
        :type node_status: str
        :param specification: 节点规格
        :type specification: str
        """
        
        

        self._configuration_status = None
        self._list = None
        self._node_id = None
        self._node_name = None
        self._node_status = None
        self._specification = None
        self.discriminator = None

        if configuration_status is not None:
            self.configuration_status = configuration_status
        if list is not None:
            self.list = list
        self.node_id = node_id
        self.node_name = node_name
        self.node_status = node_status
        self.specification = specification

    @property
    def configuration_status(self):
        r"""Gets the configuration_status of this ComponentConfigurationInfo.

        节点配置状态 UN_SAVED 未保存 SAVE_AND_UN_DEPLOY 保存未部署 DEPLOYING正在部署 MOVE_AND_UN_DEPLOY 移除未应用 FAIL_DEPLOY部署失败 DEPLOYED已部署

        :return: The configuration_status of this ComponentConfigurationInfo.
        :rtype: str
        """
        return self._configuration_status

    @configuration_status.setter
    def configuration_status(self, configuration_status):
        r"""Sets the configuration_status of this ComponentConfigurationInfo.

        节点配置状态 UN_SAVED 未保存 SAVE_AND_UN_DEPLOY 保存未部署 DEPLOYING正在部署 MOVE_AND_UN_DEPLOY 移除未应用 FAIL_DEPLOY部署失败 DEPLOYED已部署

        :param configuration_status: The configuration_status of this ComponentConfigurationInfo.
        :type configuration_status: str
        """
        self._configuration_status = configuration_status

    @property
    def list(self):
        r"""Gets the list of this ComponentConfigurationInfo.

        文件参数信息

        :return: The list of this ComponentConfigurationInfo.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.ComponentConfigurationParamVo`]
        """
        return self._list

    @list.setter
    def list(self, list):
        r"""Sets the list of this ComponentConfigurationInfo.

        文件参数信息

        :param list: The list of this ComponentConfigurationInfo.
        :type list: list[:class:`huaweicloudsdksecmaster.v1.ComponentConfigurationParamVo`]
        """
        self._list = list

    @property
    def node_id(self):
        r"""Gets the node_id of this ComponentConfigurationInfo.

        节点ID

        :return: The node_id of this ComponentConfigurationInfo.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ComponentConfigurationInfo.

        节点ID

        :param node_id: The node_id of this ComponentConfigurationInfo.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def node_name(self):
        r"""Gets the node_name of this ComponentConfigurationInfo.

        节点名

        :return: The node_name of this ComponentConfigurationInfo.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this ComponentConfigurationInfo.

        节点名

        :param node_name: The node_name of this ComponentConfigurationInfo.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def node_status(self):
        r"""Gets the node_status of this ComponentConfigurationInfo.

        枚举 节点状态 NORMAL正常 ANOMALIES异常 FAULTS 故障 LOST_CONTACT 失联

        :return: The node_status of this ComponentConfigurationInfo.
        :rtype: str
        """
        return self._node_status

    @node_status.setter
    def node_status(self, node_status):
        r"""Sets the node_status of this ComponentConfigurationInfo.

        枚举 节点状态 NORMAL正常 ANOMALIES异常 FAULTS 故障 LOST_CONTACT 失联

        :param node_status: The node_status of this ComponentConfigurationInfo.
        :type node_status: str
        """
        self._node_status = node_status

    @property
    def specification(self):
        r"""Gets the specification of this ComponentConfigurationInfo.

        节点规格

        :return: The specification of this ComponentConfigurationInfo.
        :rtype: str
        """
        return self._specification

    @specification.setter
    def specification(self, specification):
        r"""Sets the specification of this ComponentConfigurationInfo.

        节点规格

        :param specification: The specification of this ComponentConfigurationInfo.
        :type specification: str
        """
        self._specification = specification

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
        if not isinstance(other, ComponentConfigurationInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
