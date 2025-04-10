# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentOverview:

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
        'name': 'str',
        'project_id': 'str',
        'runtime': 'RuntimeType',
        'category': 'ComponentCategory',
        'sub_category': 'ComponentSubCategory',
        'description': 'str',
        'status': 'int',
        'source': 'SourceObject',
        'build': 'BuildInfo',
        'creator': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'instances': 'list[ComponentInstanceOverView]'
    }

    attribute_map = {
        'id': 'id',
        'application_id': 'application_id',
        'name': 'name',
        'project_id': 'project_id',
        'runtime': 'runtime',
        'category': 'category',
        'sub_category': 'sub_category',
        'description': 'description',
        'status': 'status',
        'source': 'source',
        'build': 'build',
        'creator': 'creator',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'instances': 'instances'
    }

    def __init__(self, id=None, application_id=None, name=None, project_id=None, runtime=None, category=None, sub_category=None, description=None, status=None, source=None, build=None, creator=None, create_time=None, update_time=None, instances=None):
        r"""ComponentOverview

        The model defined in huaweicloud sdk

        :param id: 组件ID。
        :type id: str
        :param application_id: 应用ID。
        :type application_id: str
        :param name: 应用组件名称。
        :type name: str
        :param project_id: 项目ID。
        :type project_id: str
        :param runtime: 
        :type runtime: :class:`huaweicloudsdkservicestage.v2.RuntimeType`
        :param category: 
        :type category: :class:`huaweicloudsdkservicestage.v2.ComponentCategory`
        :param sub_category: 
        :type sub_category: :class:`huaweicloudsdkservicestage.v2.ComponentSubCategory`
        :param description: 组件描述。
        :type description: str
        :param status: 取值0或1。  0：表示正常状态。  1：表示正在删除。 
        :type status: int
        :param source: 
        :type source: :class:`huaweicloudsdkservicestage.v2.SourceObject`
        :param build: 
        :type build: :class:`huaweicloudsdkservicestage.v2.BuildInfo`
        :param creator: 创建人。
        :type creator: str
        :param create_time: 创建时间。
        :type create_time: int
        :param update_time: 修改时间。
        :type update_time: int
        :param instances: 组件部署信息列表。
        :type instances: list[:class:`huaweicloudsdkservicestage.v2.ComponentInstanceOverView`]
        """
        
        

        self._id = None
        self._application_id = None
        self._name = None
        self._project_id = None
        self._runtime = None
        self._category = None
        self._sub_category = None
        self._description = None
        self._status = None
        self._source = None
        self._build = None
        self._creator = None
        self._create_time = None
        self._update_time = None
        self._instances = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if application_id is not None:
            self.application_id = application_id
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if runtime is not None:
            self.runtime = runtime
        if category is not None:
            self.category = category
        if sub_category is not None:
            self.sub_category = sub_category
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if source is not None:
            self.source = source
        if build is not None:
            self.build = build
        if creator is not None:
            self.creator = creator
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if instances is not None:
            self.instances = instances

    @property
    def id(self):
        r"""Gets the id of this ComponentOverview.

        组件ID。

        :return: The id of this ComponentOverview.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ComponentOverview.

        组件ID。

        :param id: The id of this ComponentOverview.
        :type id: str
        """
        self._id = id

    @property
    def application_id(self):
        r"""Gets the application_id of this ComponentOverview.

        应用ID。

        :return: The application_id of this ComponentOverview.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this ComponentOverview.

        应用ID。

        :param application_id: The application_id of this ComponentOverview.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def name(self):
        r"""Gets the name of this ComponentOverview.

        应用组件名称。

        :return: The name of this ComponentOverview.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ComponentOverview.

        应用组件名称。

        :param name: The name of this ComponentOverview.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this ComponentOverview.

        项目ID。

        :return: The project_id of this ComponentOverview.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ComponentOverview.

        项目ID。

        :param project_id: The project_id of this ComponentOverview.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def runtime(self):
        r"""Gets the runtime of this ComponentOverview.

        :return: The runtime of this ComponentOverview.
        :rtype: :class:`huaweicloudsdkservicestage.v2.RuntimeType`
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        r"""Sets the runtime of this ComponentOverview.

        :param runtime: The runtime of this ComponentOverview.
        :type runtime: :class:`huaweicloudsdkservicestage.v2.RuntimeType`
        """
        self._runtime = runtime

    @property
    def category(self):
        r"""Gets the category of this ComponentOverview.

        :return: The category of this ComponentOverview.
        :rtype: :class:`huaweicloudsdkservicestage.v2.ComponentCategory`
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ComponentOverview.

        :param category: The category of this ComponentOverview.
        :type category: :class:`huaweicloudsdkservicestage.v2.ComponentCategory`
        """
        self._category = category

    @property
    def sub_category(self):
        r"""Gets the sub_category of this ComponentOverview.

        :return: The sub_category of this ComponentOverview.
        :rtype: :class:`huaweicloudsdkservicestage.v2.ComponentSubCategory`
        """
        return self._sub_category

    @sub_category.setter
    def sub_category(self, sub_category):
        r"""Sets the sub_category of this ComponentOverview.

        :param sub_category: The sub_category of this ComponentOverview.
        :type sub_category: :class:`huaweicloudsdkservicestage.v2.ComponentSubCategory`
        """
        self._sub_category = sub_category

    @property
    def description(self):
        r"""Gets the description of this ComponentOverview.

        组件描述。

        :return: The description of this ComponentOverview.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ComponentOverview.

        组件描述。

        :param description: The description of this ComponentOverview.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this ComponentOverview.

        取值0或1。  0：表示正常状态。  1：表示正在删除。 

        :return: The status of this ComponentOverview.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ComponentOverview.

        取值0或1。  0：表示正常状态。  1：表示正在删除。 

        :param status: The status of this ComponentOverview.
        :type status: int
        """
        self._status = status

    @property
    def source(self):
        r"""Gets the source of this ComponentOverview.

        :return: The source of this ComponentOverview.
        :rtype: :class:`huaweicloudsdkservicestage.v2.SourceObject`
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this ComponentOverview.

        :param source: The source of this ComponentOverview.
        :type source: :class:`huaweicloudsdkservicestage.v2.SourceObject`
        """
        self._source = source

    @property
    def build(self):
        r"""Gets the build of this ComponentOverview.

        :return: The build of this ComponentOverview.
        :rtype: :class:`huaweicloudsdkservicestage.v2.BuildInfo`
        """
        return self._build

    @build.setter
    def build(self, build):
        r"""Sets the build of this ComponentOverview.

        :param build: The build of this ComponentOverview.
        :type build: :class:`huaweicloudsdkservicestage.v2.BuildInfo`
        """
        self._build = build

    @property
    def creator(self):
        r"""Gets the creator of this ComponentOverview.

        创建人。

        :return: The creator of this ComponentOverview.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ComponentOverview.

        创建人。

        :param creator: The creator of this ComponentOverview.
        :type creator: str
        """
        self._creator = creator

    @property
    def create_time(self):
        r"""Gets the create_time of this ComponentOverview.

        创建时间。

        :return: The create_time of this ComponentOverview.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ComponentOverview.

        创建时间。

        :param create_time: The create_time of this ComponentOverview.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this ComponentOverview.

        修改时间。

        :return: The update_time of this ComponentOverview.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ComponentOverview.

        修改时间。

        :param update_time: The update_time of this ComponentOverview.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def instances(self):
        r"""Gets the instances of this ComponentOverview.

        组件部署信息列表。

        :return: The instances of this ComponentOverview.
        :rtype: list[:class:`huaweicloudsdkservicestage.v2.ComponentInstanceOverView`]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        r"""Sets the instances of this ComponentOverview.

        组件部署信息列表。

        :param instances: The instances of this ComponentOverview.
        :type instances: list[:class:`huaweicloudsdkservicestage.v2.ComponentInstanceOverView`]
        """
        self._instances = instances

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
        if not isinstance(other, ComponentOverview):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
