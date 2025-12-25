# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigurationDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config_status': 'str',
        'list': 'list[FileConfiguration]',
        'node_id': 'str',
        'node_name': 'str',
        'specification': 'str'
    }

    attribute_map = {
        'config_status': 'config_status',
        'list': 'list',
        'node_id': 'node_id',
        'node_name': 'node_name',
        'specification': 'specification'
    }

    def __init__(self, config_status=None, list=None, node_id=None, node_name=None, specification=None):
        r"""ConfigurationDetail

        The model defined in huaweicloud sdk

        :param config_status: **参数解释**: 节点部署状态 - UN_SAVED 待保存 - SAVE_AND_UN_APPLY 待应用 - MOVE_AND_UN_APPLY 待移除 - APPLYING 应用中 - FAIL_APPLY 应用失败 - APPLIED 应用完成  **约束限制** 不涉及 **取值范围**: - UN_SAVED - SAVE_AND_UN_APPLY - MOVE_AND_UN_APPLY - APPLYING - FAIL_APPLY - APPLIED  **默认值** 不涉及
        :type config_status: str
        :param list: 文件配置列表
        :type list: list[:class:`huaweicloudsdksecmaster.v1.FileConfiguration`]
        :param node_id: 节点ID
        :type node_id: str
        :param node_name: 节点名称
        :type node_name: str
        :param specification: 规范
        :type specification: str
        """
        
        

        self._config_status = None
        self._list = None
        self._node_id = None
        self._node_name = None
        self._specification = None
        self.discriminator = None

        if config_status is not None:
            self.config_status = config_status
        self.list = list
        if node_id is not None:
            self.node_id = node_id
        if node_name is not None:
            self.node_name = node_name
        if specification is not None:
            self.specification = specification

    @property
    def config_status(self):
        r"""Gets the config_status of this ConfigurationDetail.

        **参数解释**: 节点部署状态 - UN_SAVED 待保存 - SAVE_AND_UN_APPLY 待应用 - MOVE_AND_UN_APPLY 待移除 - APPLYING 应用中 - FAIL_APPLY 应用失败 - APPLIED 应用完成  **约束限制** 不涉及 **取值范围**: - UN_SAVED - SAVE_AND_UN_APPLY - MOVE_AND_UN_APPLY - APPLYING - FAIL_APPLY - APPLIED  **默认值** 不涉及

        :return: The config_status of this ConfigurationDetail.
        :rtype: str
        """
        return self._config_status

    @config_status.setter
    def config_status(self, config_status):
        r"""Sets the config_status of this ConfigurationDetail.

        **参数解释**: 节点部署状态 - UN_SAVED 待保存 - SAVE_AND_UN_APPLY 待应用 - MOVE_AND_UN_APPLY 待移除 - APPLYING 应用中 - FAIL_APPLY 应用失败 - APPLIED 应用完成  **约束限制** 不涉及 **取值范围**: - UN_SAVED - SAVE_AND_UN_APPLY - MOVE_AND_UN_APPLY - APPLYING - FAIL_APPLY - APPLIED  **默认值** 不涉及

        :param config_status: The config_status of this ConfigurationDetail.
        :type config_status: str
        """
        self._config_status = config_status

    @property
    def list(self):
        r"""Gets the list of this ConfigurationDetail.

        文件配置列表

        :return: The list of this ConfigurationDetail.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.FileConfiguration`]
        """
        return self._list

    @list.setter
    def list(self, list):
        r"""Sets the list of this ConfigurationDetail.

        文件配置列表

        :param list: The list of this ConfigurationDetail.
        :type list: list[:class:`huaweicloudsdksecmaster.v1.FileConfiguration`]
        """
        self._list = list

    @property
    def node_id(self):
        r"""Gets the node_id of this ConfigurationDetail.

        节点ID

        :return: The node_id of this ConfigurationDetail.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ConfigurationDetail.

        节点ID

        :param node_id: The node_id of this ConfigurationDetail.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def node_name(self):
        r"""Gets the node_name of this ConfigurationDetail.

        节点名称

        :return: The node_name of this ConfigurationDetail.
        :rtype: str
        """
        return self._node_name

    @node_name.setter
    def node_name(self, node_name):
        r"""Sets the node_name of this ConfigurationDetail.

        节点名称

        :param node_name: The node_name of this ConfigurationDetail.
        :type node_name: str
        """
        self._node_name = node_name

    @property
    def specification(self):
        r"""Gets the specification of this ConfigurationDetail.

        规范

        :return: The specification of this ConfigurationDetail.
        :rtype: str
        """
        return self._specification

    @specification.setter
    def specification(self, specification):
        r"""Sets the specification of this ConfigurationDetail.

        规范

        :param specification: The specification of this ConfigurationDetail.
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
        if not isinstance(other, ConfigurationDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
