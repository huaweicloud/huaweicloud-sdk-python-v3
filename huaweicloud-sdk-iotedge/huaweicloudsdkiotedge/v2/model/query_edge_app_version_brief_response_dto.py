# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryEdgeAppVersionBriefResponseDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'edge_app_id': 'str',
        'version': 'str',
        'sdk_version': 'str',
        'description': 'str',
        'deploy_type': 'str',
        'deploy_multi_instance': 'bool',
        'create_time': 'str',
        'update_time': 'str',
        'state': 'str',
        'arch': 'list[str]',
        'publish_time': 'str',
        'off_shelf_time': 'str'
    }

    attribute_map = {
        'edge_app_id': 'edge_app_id',
        'version': 'version',
        'sdk_version': 'sdk_version',
        'description': 'description',
        'deploy_type': 'deploy_type',
        'deploy_multi_instance': 'deploy_multi_instance',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'state': 'state',
        'arch': 'arch',
        'publish_time': 'publish_time',
        'off_shelf_time': 'off_shelf_time'
    }

    def __init__(self, edge_app_id=None, version=None, sdk_version=None, description=None, deploy_type=None, deploy_multi_instance=None, create_time=None, update_time=None, state=None, arch=None, publish_time=None, off_shelf_time=None):
        """QueryEdgeAppVersionBriefResponseDTO

        The model defined in huaweicloud sdk

        :param edge_app_id: 应用ID
        :type edge_app_id: str
        :param version: 应用名称
        :type version: str
        :param sdk_version: 应用集成的边缘升得快版本
        :type sdk_version: str
        :param description: 应用描述
        :type description: str
        :param deploy_type: 部署类型docker|process
        :type deploy_type: str
        :param deploy_multi_instance: 是否允许部署多实例
        :type deploy_multi_instance: bool
        :param create_time: 创建时间
        :type create_time: str
        :param update_time: 最后一次修改时间
        :type update_time: str
        :param state: 应用版本状态
        :type state: str
        :param arch: 架构
        :type arch: list[str]
        :param publish_time: 发布时间
        :type publish_time: str
        :param off_shelf_time: 下线时间
        :type off_shelf_time: str
        """
        
        

        self._edge_app_id = None
        self._version = None
        self._sdk_version = None
        self._description = None
        self._deploy_type = None
        self._deploy_multi_instance = None
        self._create_time = None
        self._update_time = None
        self._state = None
        self._arch = None
        self._publish_time = None
        self._off_shelf_time = None
        self.discriminator = None

        if edge_app_id is not None:
            self.edge_app_id = edge_app_id
        if version is not None:
            self.version = version
        if sdk_version is not None:
            self.sdk_version = sdk_version
        if description is not None:
            self.description = description
        if deploy_type is not None:
            self.deploy_type = deploy_type
        if deploy_multi_instance is not None:
            self.deploy_multi_instance = deploy_multi_instance
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if state is not None:
            self.state = state
        if arch is not None:
            self.arch = arch
        if publish_time is not None:
            self.publish_time = publish_time
        if off_shelf_time is not None:
            self.off_shelf_time = off_shelf_time

    @property
    def edge_app_id(self):
        """Gets the edge_app_id of this QueryEdgeAppVersionBriefResponseDTO.

        应用ID

        :return: The edge_app_id of this QueryEdgeAppVersionBriefResponseDTO.
        :rtype: str
        """
        return self._edge_app_id

    @edge_app_id.setter
    def edge_app_id(self, edge_app_id):
        """Sets the edge_app_id of this QueryEdgeAppVersionBriefResponseDTO.

        应用ID

        :param edge_app_id: The edge_app_id of this QueryEdgeAppVersionBriefResponseDTO.
        :type edge_app_id: str
        """
        self._edge_app_id = edge_app_id

    @property
    def version(self):
        """Gets the version of this QueryEdgeAppVersionBriefResponseDTO.

        应用名称

        :return: The version of this QueryEdgeAppVersionBriefResponseDTO.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this QueryEdgeAppVersionBriefResponseDTO.

        应用名称

        :param version: The version of this QueryEdgeAppVersionBriefResponseDTO.
        :type version: str
        """
        self._version = version

    @property
    def sdk_version(self):
        """Gets the sdk_version of this QueryEdgeAppVersionBriefResponseDTO.

        应用集成的边缘升得快版本

        :return: The sdk_version of this QueryEdgeAppVersionBriefResponseDTO.
        :rtype: str
        """
        return self._sdk_version

    @sdk_version.setter
    def sdk_version(self, sdk_version):
        """Sets the sdk_version of this QueryEdgeAppVersionBriefResponseDTO.

        应用集成的边缘升得快版本

        :param sdk_version: The sdk_version of this QueryEdgeAppVersionBriefResponseDTO.
        :type sdk_version: str
        """
        self._sdk_version = sdk_version

    @property
    def description(self):
        """Gets the description of this QueryEdgeAppVersionBriefResponseDTO.

        应用描述

        :return: The description of this QueryEdgeAppVersionBriefResponseDTO.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this QueryEdgeAppVersionBriefResponseDTO.

        应用描述

        :param description: The description of this QueryEdgeAppVersionBriefResponseDTO.
        :type description: str
        """
        self._description = description

    @property
    def deploy_type(self):
        """Gets the deploy_type of this QueryEdgeAppVersionBriefResponseDTO.

        部署类型docker|process

        :return: The deploy_type of this QueryEdgeAppVersionBriefResponseDTO.
        :rtype: str
        """
        return self._deploy_type

    @deploy_type.setter
    def deploy_type(self, deploy_type):
        """Sets the deploy_type of this QueryEdgeAppVersionBriefResponseDTO.

        部署类型docker|process

        :param deploy_type: The deploy_type of this QueryEdgeAppVersionBriefResponseDTO.
        :type deploy_type: str
        """
        self._deploy_type = deploy_type

    @property
    def deploy_multi_instance(self):
        """Gets the deploy_multi_instance of this QueryEdgeAppVersionBriefResponseDTO.

        是否允许部署多实例

        :return: The deploy_multi_instance of this QueryEdgeAppVersionBriefResponseDTO.
        :rtype: bool
        """
        return self._deploy_multi_instance

    @deploy_multi_instance.setter
    def deploy_multi_instance(self, deploy_multi_instance):
        """Sets the deploy_multi_instance of this QueryEdgeAppVersionBriefResponseDTO.

        是否允许部署多实例

        :param deploy_multi_instance: The deploy_multi_instance of this QueryEdgeAppVersionBriefResponseDTO.
        :type deploy_multi_instance: bool
        """
        self._deploy_multi_instance = deploy_multi_instance

    @property
    def create_time(self):
        """Gets the create_time of this QueryEdgeAppVersionBriefResponseDTO.

        创建时间

        :return: The create_time of this QueryEdgeAppVersionBriefResponseDTO.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this QueryEdgeAppVersionBriefResponseDTO.

        创建时间

        :param create_time: The create_time of this QueryEdgeAppVersionBriefResponseDTO.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this QueryEdgeAppVersionBriefResponseDTO.

        最后一次修改时间

        :return: The update_time of this QueryEdgeAppVersionBriefResponseDTO.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this QueryEdgeAppVersionBriefResponseDTO.

        最后一次修改时间

        :param update_time: The update_time of this QueryEdgeAppVersionBriefResponseDTO.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def state(self):
        """Gets the state of this QueryEdgeAppVersionBriefResponseDTO.

        应用版本状态

        :return: The state of this QueryEdgeAppVersionBriefResponseDTO.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this QueryEdgeAppVersionBriefResponseDTO.

        应用版本状态

        :param state: The state of this QueryEdgeAppVersionBriefResponseDTO.
        :type state: str
        """
        self._state = state

    @property
    def arch(self):
        """Gets the arch of this QueryEdgeAppVersionBriefResponseDTO.

        架构

        :return: The arch of this QueryEdgeAppVersionBriefResponseDTO.
        :rtype: list[str]
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this QueryEdgeAppVersionBriefResponseDTO.

        架构

        :param arch: The arch of this QueryEdgeAppVersionBriefResponseDTO.
        :type arch: list[str]
        """
        self._arch = arch

    @property
    def publish_time(self):
        """Gets the publish_time of this QueryEdgeAppVersionBriefResponseDTO.

        发布时间

        :return: The publish_time of this QueryEdgeAppVersionBriefResponseDTO.
        :rtype: str
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        """Sets the publish_time of this QueryEdgeAppVersionBriefResponseDTO.

        发布时间

        :param publish_time: The publish_time of this QueryEdgeAppVersionBriefResponseDTO.
        :type publish_time: str
        """
        self._publish_time = publish_time

    @property
    def off_shelf_time(self):
        """Gets the off_shelf_time of this QueryEdgeAppVersionBriefResponseDTO.

        下线时间

        :return: The off_shelf_time of this QueryEdgeAppVersionBriefResponseDTO.
        :rtype: str
        """
        return self._off_shelf_time

    @off_shelf_time.setter
    def off_shelf_time(self, off_shelf_time):
        """Sets the off_shelf_time of this QueryEdgeAppVersionBriefResponseDTO.

        下线时间

        :param off_shelf_time: The off_shelf_time of this QueryEdgeAppVersionBriefResponseDTO.
        :type off_shelf_time: str
        """
        self._off_shelf_time = off_shelf_time

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
        if not isinstance(other, QueryEdgeAppVersionBriefResponseDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
