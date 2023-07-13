# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceListView:

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
        'application_id': 'str',
        'application_name': 'str',
        'component_id': 'str',
        'component_name': 'str',
        'name': 'str',
        'environment_id': 'str',
        'environment_name': 'str',
        'platform_type': 'str',
        'version': 'str',
        'external_accesses': 'list[ExternalAccesses]',
        'artifacts': 'dict(str, object)',
        'creator': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'status_detail': 'InstanceStatusView'
    }

    attribute_map = {
        'id': 'id',
        'application_id': 'application_id',
        'application_name': 'application_name',
        'component_id': 'component_id',
        'component_name': 'component_name',
        'name': 'name',
        'environment_id': 'environment_id',
        'environment_name': 'environment_name',
        'platform_type': 'platform_type',
        'version': 'version',
        'external_accesses': 'external_accesses',
        'artifacts': 'artifacts',
        'creator': 'creator',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'status_detail': 'status_detail'
    }

    def __init__(self, id=None, application_id=None, application_name=None, component_id=None, component_name=None, name=None, environment_id=None, environment_name=None, platform_type=None, version=None, external_accesses=None, artifacts=None, creator=None, create_time=None, update_time=None, status_detail=None):
        """InstanceListView

        The model defined in huaweicloud sdk

        :param id: 应用组件实例ID。
        :type id: str
        :param application_id: 应用ID。
        :type application_id: str
        :param application_name: 应用名称。
        :type application_name: str
        :param component_id: 组件ID。
        :type component_id: str
        :param component_name: 组件名称。
        :type component_name: str
        :param name: 应用组件实例名称。
        :type name: str
        :param environment_id: 应用组件环境ID。
        :type environment_id: str
        :param environment_name: 环境名称。
        :type environment_name: str
        :param platform_type: 运行平台类型。 应用可以在不同的平台上运行，可选用的平台的类型有以下几种：cce、vmapp。 
        :type platform_type: str
        :param version: 应用组件版本号。
        :type version: str
        :param external_accesses: 访问方式。
        :type external_accesses: list[:class:`huaweicloudsdkservicestage.v2.ExternalAccesses`]
        :param artifacts: 组件部署件。key为组件component_name，对于Docker多容器场景，key为容器名称。
        :type artifacts: dict(str, object)
        :param creator: 创建人。
        :type creator: str
        :param create_time: 创建时间。
        :type create_time: int
        :param update_time: 修改时间。
        :type update_time: int
        :param status_detail: 
        :type status_detail: :class:`huaweicloudsdkservicestage.v2.InstanceStatusView`
        """
        
        

        self._id = None
        self._application_id = None
        self._application_name = None
        self._component_id = None
        self._component_name = None
        self._name = None
        self._environment_id = None
        self._environment_name = None
        self._platform_type = None
        self._version = None
        self._external_accesses = None
        self._artifacts = None
        self._creator = None
        self._create_time = None
        self._update_time = None
        self._status_detail = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if application_id is not None:
            self.application_id = application_id
        if application_name is not None:
            self.application_name = application_name
        if component_id is not None:
            self.component_id = component_id
        if component_name is not None:
            self.component_name = component_name
        if name is not None:
            self.name = name
        if environment_id is not None:
            self.environment_id = environment_id
        if environment_name is not None:
            self.environment_name = environment_name
        if platform_type is not None:
            self.platform_type = platform_type
        if version is not None:
            self.version = version
        if external_accesses is not None:
            self.external_accesses = external_accesses
        if artifacts is not None:
            self.artifacts = artifacts
        if creator is not None:
            self.creator = creator
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if status_detail is not None:
            self.status_detail = status_detail

    @property
    def id(self):
        """Gets the id of this InstanceListView.

        应用组件实例ID。

        :return: The id of this InstanceListView.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InstanceListView.

        应用组件实例ID。

        :param id: The id of this InstanceListView.
        :type id: str
        """
        self._id = id

    @property
    def application_id(self):
        """Gets the application_id of this InstanceListView.

        应用ID。

        :return: The application_id of this InstanceListView.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this InstanceListView.

        应用ID。

        :param application_id: The application_id of this InstanceListView.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def application_name(self):
        """Gets the application_name of this InstanceListView.

        应用名称。

        :return: The application_name of this InstanceListView.
        :rtype: str
        """
        return self._application_name

    @application_name.setter
    def application_name(self, application_name):
        """Sets the application_name of this InstanceListView.

        应用名称。

        :param application_name: The application_name of this InstanceListView.
        :type application_name: str
        """
        self._application_name = application_name

    @property
    def component_id(self):
        """Gets the component_id of this InstanceListView.

        组件ID。

        :return: The component_id of this InstanceListView.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        """Sets the component_id of this InstanceListView.

        组件ID。

        :param component_id: The component_id of this InstanceListView.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def component_name(self):
        """Gets the component_name of this InstanceListView.

        组件名称。

        :return: The component_name of this InstanceListView.
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name):
        """Sets the component_name of this InstanceListView.

        组件名称。

        :param component_name: The component_name of this InstanceListView.
        :type component_name: str
        """
        self._component_name = component_name

    @property
    def name(self):
        """Gets the name of this InstanceListView.

        应用组件实例名称。

        :return: The name of this InstanceListView.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InstanceListView.

        应用组件实例名称。

        :param name: The name of this InstanceListView.
        :type name: str
        """
        self._name = name

    @property
    def environment_id(self):
        """Gets the environment_id of this InstanceListView.

        应用组件环境ID。

        :return: The environment_id of this InstanceListView.
        :rtype: str
        """
        return self._environment_id

    @environment_id.setter
    def environment_id(self, environment_id):
        """Sets the environment_id of this InstanceListView.

        应用组件环境ID。

        :param environment_id: The environment_id of this InstanceListView.
        :type environment_id: str
        """
        self._environment_id = environment_id

    @property
    def environment_name(self):
        """Gets the environment_name of this InstanceListView.

        环境名称。

        :return: The environment_name of this InstanceListView.
        :rtype: str
        """
        return self._environment_name

    @environment_name.setter
    def environment_name(self, environment_name):
        """Sets the environment_name of this InstanceListView.

        环境名称。

        :param environment_name: The environment_name of this InstanceListView.
        :type environment_name: str
        """
        self._environment_name = environment_name

    @property
    def platform_type(self):
        """Gets the platform_type of this InstanceListView.

        运行平台类型。 应用可以在不同的平台上运行，可选用的平台的类型有以下几种：cce、vmapp。 

        :return: The platform_type of this InstanceListView.
        :rtype: str
        """
        return self._platform_type

    @platform_type.setter
    def platform_type(self, platform_type):
        """Sets the platform_type of this InstanceListView.

        运行平台类型。 应用可以在不同的平台上运行，可选用的平台的类型有以下几种：cce、vmapp。 

        :param platform_type: The platform_type of this InstanceListView.
        :type platform_type: str
        """
        self._platform_type = platform_type

    @property
    def version(self):
        """Gets the version of this InstanceListView.

        应用组件版本号。

        :return: The version of this InstanceListView.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this InstanceListView.

        应用组件版本号。

        :param version: The version of this InstanceListView.
        :type version: str
        """
        self._version = version

    @property
    def external_accesses(self):
        """Gets the external_accesses of this InstanceListView.

        访问方式。

        :return: The external_accesses of this InstanceListView.
        :rtype: list[:class:`huaweicloudsdkservicestage.v2.ExternalAccesses`]
        """
        return self._external_accesses

    @external_accesses.setter
    def external_accesses(self, external_accesses):
        """Sets the external_accesses of this InstanceListView.

        访问方式。

        :param external_accesses: The external_accesses of this InstanceListView.
        :type external_accesses: list[:class:`huaweicloudsdkservicestage.v2.ExternalAccesses`]
        """
        self._external_accesses = external_accesses

    @property
    def artifacts(self):
        """Gets the artifacts of this InstanceListView.

        组件部署件。key为组件component_name，对于Docker多容器场景，key为容器名称。

        :return: The artifacts of this InstanceListView.
        :rtype: dict(str, object)
        """
        return self._artifacts

    @artifacts.setter
    def artifacts(self, artifacts):
        """Sets the artifacts of this InstanceListView.

        组件部署件。key为组件component_name，对于Docker多容器场景，key为容器名称。

        :param artifacts: The artifacts of this InstanceListView.
        :type artifacts: dict(str, object)
        """
        self._artifacts = artifacts

    @property
    def creator(self):
        """Gets the creator of this InstanceListView.

        创建人。

        :return: The creator of this InstanceListView.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this InstanceListView.

        创建人。

        :param creator: The creator of this InstanceListView.
        :type creator: str
        """
        self._creator = creator

    @property
    def create_time(self):
        """Gets the create_time of this InstanceListView.

        创建时间。

        :return: The create_time of this InstanceListView.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this InstanceListView.

        创建时间。

        :param create_time: The create_time of this InstanceListView.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this InstanceListView.

        修改时间。

        :return: The update_time of this InstanceListView.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this InstanceListView.

        修改时间。

        :param update_time: The update_time of this InstanceListView.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def status_detail(self):
        """Gets the status_detail of this InstanceListView.

        :return: The status_detail of this InstanceListView.
        :rtype: :class:`huaweicloudsdkservicestage.v2.InstanceStatusView`
        """
        return self._status_detail

    @status_detail.setter
    def status_detail(self, status_detail):
        """Sets the status_detail of this InstanceListView.

        :param status_detail: The status_detail of this InstanceListView.
        :type status_detail: :class:`huaweicloudsdkservicestage.v2.InstanceStatusView`
        """
        self._status_detail = status_detail

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
        if not isinstance(other, InstanceListView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
