# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowComponentDetailResponse(SdkResponse):

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
        'name': 'str',
        'status': 'int',
        'runtime': 'RuntimeType',
        'category': 'ComponentCategory',
        'sub_category': 'ComponentSubCategory',
        'description': 'str',
        'project_id': 'str',
        'application_id': 'str',
        'source': 'SourceObject',
        'build': 'BuildInfo',
        'pipeline_ids': 'list[str]',
        'create_time': 'int',
        'creator': 'str',
        'update_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'runtime': 'runtime',
        'category': 'category',
        'sub_category': 'sub_category',
        'description': 'description',
        'project_id': 'project_id',
        'application_id': 'application_id',
        'source': 'source',
        'build': 'build',
        'pipeline_ids': 'pipeline_ids',
        'create_time': 'create_time',
        'creator': 'creator',
        'update_time': 'update_time'
    }

    def __init__(self, id=None, name=None, status=None, runtime=None, category=None, sub_category=None, description=None, project_id=None, application_id=None, source=None, build=None, pipeline_ids=None, create_time=None, creator=None, update_time=None):
        r"""ShowComponentDetailResponse

        The model defined in huaweicloud sdk

        :param id: 应用组件ID。
        :type id: str
        :param name: 应用组件名称
        :type name: str
        :param status: 取值0或1。  0：表示正常状态。  1：表示正在删除。 
        :type status: int
        :param runtime: 
        :type runtime: :class:`huaweicloudsdkservicestage.v2.RuntimeType`
        :param category: 
        :type category: :class:`huaweicloudsdkservicestage.v2.ComponentCategory`
        :param sub_category: 
        :type sub_category: :class:`huaweicloudsdkservicestage.v2.ComponentSubCategory`
        :param description: 描述。
        :type description: str
        :param project_id: 项目ID。
        :type project_id: str
        :param application_id: 应用ID。
        :type application_id: str
        :param source: 
        :type source: :class:`huaweicloudsdkservicestage.v2.SourceObject`
        :param build: 
        :type build: :class:`huaweicloudsdkservicestage.v2.BuildInfo`
        :param pipeline_ids: 流水线Id列表，最多10个。
        :type pipeline_ids: list[str]
        :param create_time: 创建时间。
        :type create_time: int
        :param creator: 创建者
        :type creator: str
        :param update_time: 修改时间。
        :type update_time: int
        """
        
        super(ShowComponentDetailResponse, self).__init__()

        self._id = None
        self._name = None
        self._status = None
        self._runtime = None
        self._category = None
        self._sub_category = None
        self._description = None
        self._project_id = None
        self._application_id = None
        self._source = None
        self._build = None
        self._pipeline_ids = None
        self._create_time = None
        self._creator = None
        self._update_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if runtime is not None:
            self.runtime = runtime
        if category is not None:
            self.category = category
        if sub_category is not None:
            self.sub_category = sub_category
        if description is not None:
            self.description = description
        if project_id is not None:
            self.project_id = project_id
        if application_id is not None:
            self.application_id = application_id
        if source is not None:
            self.source = source
        if build is not None:
            self.build = build
        if pipeline_ids is not None:
            self.pipeline_ids = pipeline_ids
        if create_time is not None:
            self.create_time = create_time
        if creator is not None:
            self.creator = creator
        if update_time is not None:
            self.update_time = update_time

    @property
    def id(self):
        r"""Gets the id of this ShowComponentDetailResponse.

        应用组件ID。

        :return: The id of this ShowComponentDetailResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowComponentDetailResponse.

        应用组件ID。

        :param id: The id of this ShowComponentDetailResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowComponentDetailResponse.

        应用组件名称

        :return: The name of this ShowComponentDetailResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowComponentDetailResponse.

        应用组件名称

        :param name: The name of this ShowComponentDetailResponse.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ShowComponentDetailResponse.

        取值0或1。  0：表示正常状态。  1：表示正在删除。 

        :return: The status of this ShowComponentDetailResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowComponentDetailResponse.

        取值0或1。  0：表示正常状态。  1：表示正在删除。 

        :param status: The status of this ShowComponentDetailResponse.
        :type status: int
        """
        self._status = status

    @property
    def runtime(self):
        r"""Gets the runtime of this ShowComponentDetailResponse.

        :return: The runtime of this ShowComponentDetailResponse.
        :rtype: :class:`huaweicloudsdkservicestage.v2.RuntimeType`
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        r"""Sets the runtime of this ShowComponentDetailResponse.

        :param runtime: The runtime of this ShowComponentDetailResponse.
        :type runtime: :class:`huaweicloudsdkservicestage.v2.RuntimeType`
        """
        self._runtime = runtime

    @property
    def category(self):
        r"""Gets the category of this ShowComponentDetailResponse.

        :return: The category of this ShowComponentDetailResponse.
        :rtype: :class:`huaweicloudsdkservicestage.v2.ComponentCategory`
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ShowComponentDetailResponse.

        :param category: The category of this ShowComponentDetailResponse.
        :type category: :class:`huaweicloudsdkservicestage.v2.ComponentCategory`
        """
        self._category = category

    @property
    def sub_category(self):
        r"""Gets the sub_category of this ShowComponentDetailResponse.

        :return: The sub_category of this ShowComponentDetailResponse.
        :rtype: :class:`huaweicloudsdkservicestage.v2.ComponentSubCategory`
        """
        return self._sub_category

    @sub_category.setter
    def sub_category(self, sub_category):
        r"""Sets the sub_category of this ShowComponentDetailResponse.

        :param sub_category: The sub_category of this ShowComponentDetailResponse.
        :type sub_category: :class:`huaweicloudsdkservicestage.v2.ComponentSubCategory`
        """
        self._sub_category = sub_category

    @property
    def description(self):
        r"""Gets the description of this ShowComponentDetailResponse.

        描述。

        :return: The description of this ShowComponentDetailResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowComponentDetailResponse.

        描述。

        :param description: The description of this ShowComponentDetailResponse.
        :type description: str
        """
        self._description = description

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowComponentDetailResponse.

        项目ID。

        :return: The project_id of this ShowComponentDetailResponse.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowComponentDetailResponse.

        项目ID。

        :param project_id: The project_id of this ShowComponentDetailResponse.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def application_id(self):
        r"""Gets the application_id of this ShowComponentDetailResponse.

        应用ID。

        :return: The application_id of this ShowComponentDetailResponse.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        r"""Sets the application_id of this ShowComponentDetailResponse.

        应用ID。

        :param application_id: The application_id of this ShowComponentDetailResponse.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def source(self):
        r"""Gets the source of this ShowComponentDetailResponse.

        :return: The source of this ShowComponentDetailResponse.
        :rtype: :class:`huaweicloudsdkservicestage.v2.SourceObject`
        """
        return self._source

    @source.setter
    def source(self, source):
        r"""Sets the source of this ShowComponentDetailResponse.

        :param source: The source of this ShowComponentDetailResponse.
        :type source: :class:`huaweicloudsdkservicestage.v2.SourceObject`
        """
        self._source = source

    @property
    def build(self):
        r"""Gets the build of this ShowComponentDetailResponse.

        :return: The build of this ShowComponentDetailResponse.
        :rtype: :class:`huaweicloudsdkservicestage.v2.BuildInfo`
        """
        return self._build

    @build.setter
    def build(self, build):
        r"""Sets the build of this ShowComponentDetailResponse.

        :param build: The build of this ShowComponentDetailResponse.
        :type build: :class:`huaweicloudsdkservicestage.v2.BuildInfo`
        """
        self._build = build

    @property
    def pipeline_ids(self):
        r"""Gets the pipeline_ids of this ShowComponentDetailResponse.

        流水线Id列表，最多10个。

        :return: The pipeline_ids of this ShowComponentDetailResponse.
        :rtype: list[str]
        """
        return self._pipeline_ids

    @pipeline_ids.setter
    def pipeline_ids(self, pipeline_ids):
        r"""Sets the pipeline_ids of this ShowComponentDetailResponse.

        流水线Id列表，最多10个。

        :param pipeline_ids: The pipeline_ids of this ShowComponentDetailResponse.
        :type pipeline_ids: list[str]
        """
        self._pipeline_ids = pipeline_ids

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowComponentDetailResponse.

        创建时间。

        :return: The create_time of this ShowComponentDetailResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowComponentDetailResponse.

        创建时间。

        :param create_time: The create_time of this ShowComponentDetailResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def creator(self):
        r"""Gets the creator of this ShowComponentDetailResponse.

        创建者

        :return: The creator of this ShowComponentDetailResponse.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this ShowComponentDetailResponse.

        创建者

        :param creator: The creator of this ShowComponentDetailResponse.
        :type creator: str
        """
        self._creator = creator

    @property
    def update_time(self):
        r"""Gets the update_time of this ShowComponentDetailResponse.

        修改时间。

        :return: The update_time of this ShowComponentDetailResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ShowComponentDetailResponse.

        修改时间。

        :param update_time: The update_time of this ShowComponentDetailResponse.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, ShowComponentDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
