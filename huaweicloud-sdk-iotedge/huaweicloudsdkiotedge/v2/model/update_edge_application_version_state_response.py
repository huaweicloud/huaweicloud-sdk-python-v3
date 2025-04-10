# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEdgeApplicationVersionStateResponse(SdkResponse):

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
        'name': 'str',
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
        'name': 'name',
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

    def __init__(self, edge_app_id=None, name=None, version=None, sdk_version=None, description=None, deploy_type=None, deploy_multi_instance=None, create_time=None, update_time=None, state=None, arch=None, publish_time=None, off_shelf_time=None):
        r"""UpdateEdgeApplicationVersionStateResponse

        The model defined in huaweicloud sdk

        :param edge_app_id: 应用ID
        :type edge_app_id: str
        :param name: 应用名称
        :type name: str
        :param version: 应用名称
        :type version: str
        :param sdk_version: 应用集成的边缘SDK版本
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
        
        super(UpdateEdgeApplicationVersionStateResponse, self).__init__()

        self._edge_app_id = None
        self._name = None
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
        if name is not None:
            self.name = name
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
        r"""Gets the edge_app_id of this UpdateEdgeApplicationVersionStateResponse.

        应用ID

        :return: The edge_app_id of this UpdateEdgeApplicationVersionStateResponse.
        :rtype: str
        """
        return self._edge_app_id

    @edge_app_id.setter
    def edge_app_id(self, edge_app_id):
        r"""Sets the edge_app_id of this UpdateEdgeApplicationVersionStateResponse.

        应用ID

        :param edge_app_id: The edge_app_id of this UpdateEdgeApplicationVersionStateResponse.
        :type edge_app_id: str
        """
        self._edge_app_id = edge_app_id

    @property
    def name(self):
        r"""Gets the name of this UpdateEdgeApplicationVersionStateResponse.

        应用名称

        :return: The name of this UpdateEdgeApplicationVersionStateResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateEdgeApplicationVersionStateResponse.

        应用名称

        :param name: The name of this UpdateEdgeApplicationVersionStateResponse.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        r"""Gets the version of this UpdateEdgeApplicationVersionStateResponse.

        应用名称

        :return: The version of this UpdateEdgeApplicationVersionStateResponse.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this UpdateEdgeApplicationVersionStateResponse.

        应用名称

        :param version: The version of this UpdateEdgeApplicationVersionStateResponse.
        :type version: str
        """
        self._version = version

    @property
    def sdk_version(self):
        r"""Gets the sdk_version of this UpdateEdgeApplicationVersionStateResponse.

        应用集成的边缘SDK版本

        :return: The sdk_version of this UpdateEdgeApplicationVersionStateResponse.
        :rtype: str
        """
        return self._sdk_version

    @sdk_version.setter
    def sdk_version(self, sdk_version):
        r"""Sets the sdk_version of this UpdateEdgeApplicationVersionStateResponse.

        应用集成的边缘SDK版本

        :param sdk_version: The sdk_version of this UpdateEdgeApplicationVersionStateResponse.
        :type sdk_version: str
        """
        self._sdk_version = sdk_version

    @property
    def description(self):
        r"""Gets the description of this UpdateEdgeApplicationVersionStateResponse.

        应用描述

        :return: The description of this UpdateEdgeApplicationVersionStateResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateEdgeApplicationVersionStateResponse.

        应用描述

        :param description: The description of this UpdateEdgeApplicationVersionStateResponse.
        :type description: str
        """
        self._description = description

    @property
    def deploy_type(self):
        r"""Gets the deploy_type of this UpdateEdgeApplicationVersionStateResponse.

        部署类型docker|process

        :return: The deploy_type of this UpdateEdgeApplicationVersionStateResponse.
        :rtype: str
        """
        return self._deploy_type

    @deploy_type.setter
    def deploy_type(self, deploy_type):
        r"""Sets the deploy_type of this UpdateEdgeApplicationVersionStateResponse.

        部署类型docker|process

        :param deploy_type: The deploy_type of this UpdateEdgeApplicationVersionStateResponse.
        :type deploy_type: str
        """
        self._deploy_type = deploy_type

    @property
    def deploy_multi_instance(self):
        r"""Gets the deploy_multi_instance of this UpdateEdgeApplicationVersionStateResponse.

        是否允许部署多实例

        :return: The deploy_multi_instance of this UpdateEdgeApplicationVersionStateResponse.
        :rtype: bool
        """
        return self._deploy_multi_instance

    @deploy_multi_instance.setter
    def deploy_multi_instance(self, deploy_multi_instance):
        r"""Sets the deploy_multi_instance of this UpdateEdgeApplicationVersionStateResponse.

        是否允许部署多实例

        :param deploy_multi_instance: The deploy_multi_instance of this UpdateEdgeApplicationVersionStateResponse.
        :type deploy_multi_instance: bool
        """
        self._deploy_multi_instance = deploy_multi_instance

    @property
    def create_time(self):
        r"""Gets the create_time of this UpdateEdgeApplicationVersionStateResponse.

        创建时间

        :return: The create_time of this UpdateEdgeApplicationVersionStateResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this UpdateEdgeApplicationVersionStateResponse.

        创建时间

        :param create_time: The create_time of this UpdateEdgeApplicationVersionStateResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this UpdateEdgeApplicationVersionStateResponse.

        最后一次修改时间

        :return: The update_time of this UpdateEdgeApplicationVersionStateResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this UpdateEdgeApplicationVersionStateResponse.

        最后一次修改时间

        :param update_time: The update_time of this UpdateEdgeApplicationVersionStateResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def state(self):
        r"""Gets the state of this UpdateEdgeApplicationVersionStateResponse.

        应用版本状态

        :return: The state of this UpdateEdgeApplicationVersionStateResponse.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this UpdateEdgeApplicationVersionStateResponse.

        应用版本状态

        :param state: The state of this UpdateEdgeApplicationVersionStateResponse.
        :type state: str
        """
        self._state = state

    @property
    def arch(self):
        r"""Gets the arch of this UpdateEdgeApplicationVersionStateResponse.

        架构

        :return: The arch of this UpdateEdgeApplicationVersionStateResponse.
        :rtype: list[str]
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        r"""Sets the arch of this UpdateEdgeApplicationVersionStateResponse.

        架构

        :param arch: The arch of this UpdateEdgeApplicationVersionStateResponse.
        :type arch: list[str]
        """
        self._arch = arch

    @property
    def publish_time(self):
        r"""Gets the publish_time of this UpdateEdgeApplicationVersionStateResponse.

        发布时间

        :return: The publish_time of this UpdateEdgeApplicationVersionStateResponse.
        :rtype: str
        """
        return self._publish_time

    @publish_time.setter
    def publish_time(self, publish_time):
        r"""Sets the publish_time of this UpdateEdgeApplicationVersionStateResponse.

        发布时间

        :param publish_time: The publish_time of this UpdateEdgeApplicationVersionStateResponse.
        :type publish_time: str
        """
        self._publish_time = publish_time

    @property
    def off_shelf_time(self):
        r"""Gets the off_shelf_time of this UpdateEdgeApplicationVersionStateResponse.

        下线时间

        :return: The off_shelf_time of this UpdateEdgeApplicationVersionStateResponse.
        :rtype: str
        """
        return self._off_shelf_time

    @off_shelf_time.setter
    def off_shelf_time(self, off_shelf_time):
        r"""Sets the off_shelf_time of this UpdateEdgeApplicationVersionStateResponse.

        下线时间

        :param off_shelf_time: The off_shelf_time of this UpdateEdgeApplicationVersionStateResponse.
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
        if not isinstance(other, UpdateEdgeApplicationVersionStateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
