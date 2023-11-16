# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPipelinesPagePipelines:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pipeline_id': 'str',
        'name': 'str',
        'project_id': 'str',
        'project_name': 'str',
        'component_id': 'str',
        'is_publish': 'bool',
        'is_collect': 'bool',
        'manifest_version': 'str',
        'create_time': 'int',
        'latest_run': 'ListPipelinesPageLatestRun',
        'convert_sign': 'int'
    }

    attribute_map = {
        'pipeline_id': 'pipeline_id',
        'name': 'name',
        'project_id': 'project_id',
        'project_name': 'project_name',
        'component_id': 'component_id',
        'is_publish': 'is_publish',
        'is_collect': 'is_collect',
        'manifest_version': 'manifest_version',
        'create_time': 'create_time',
        'latest_run': 'latest_run',
        'convert_sign': 'convert_sign'
    }

    def __init__(self, pipeline_id=None, name=None, project_id=None, project_name=None, component_id=None, is_publish=None, is_collect=None, manifest_version=None, create_time=None, latest_run=None, convert_sign=None):
        """ListPipelinesPagePipelines

        The model defined in huaweicloud sdk

        :param pipeline_id: 流水线ID
        :type pipeline_id: str
        :param name: 流水线名称
        :type name: str
        :param project_id: 项目ID
        :type project_id: str
        :param project_name: 项目名称
        :type project_name: str
        :param component_id: 组件ID
        :type component_id: str
        :param is_publish: 是否为变更流水线
        :type is_publish: bool
        :param is_collect: 是否收藏此流水线
        :type is_collect: bool
        :param manifest_version: 流水线版本
        :type manifest_version: str
        :param create_time: 创建时间
        :type create_time: int
        :param latest_run: 
        :type latest_run: :class:`huaweicloudsdkcodeartspipeline.v2.ListPipelinesPageLatestRun`
        :param convert_sign: 旧版转新版标识
        :type convert_sign: int
        """
        
        

        self._pipeline_id = None
        self._name = None
        self._project_id = None
        self._project_name = None
        self._component_id = None
        self._is_publish = None
        self._is_collect = None
        self._manifest_version = None
        self._create_time = None
        self._latest_run = None
        self._convert_sign = None
        self.discriminator = None

        if pipeline_id is not None:
            self.pipeline_id = pipeline_id
        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if component_id is not None:
            self.component_id = component_id
        if is_publish is not None:
            self.is_publish = is_publish
        if is_collect is not None:
            self.is_collect = is_collect
        if manifest_version is not None:
            self.manifest_version = manifest_version
        if create_time is not None:
            self.create_time = create_time
        if latest_run is not None:
            self.latest_run = latest_run
        if convert_sign is not None:
            self.convert_sign = convert_sign

    @property
    def pipeline_id(self):
        """Gets the pipeline_id of this ListPipelinesPagePipelines.

        流水线ID

        :return: The pipeline_id of this ListPipelinesPagePipelines.
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        """Sets the pipeline_id of this ListPipelinesPagePipelines.

        流水线ID

        :param pipeline_id: The pipeline_id of this ListPipelinesPagePipelines.
        :type pipeline_id: str
        """
        self._pipeline_id = pipeline_id

    @property
    def name(self):
        """Gets the name of this ListPipelinesPagePipelines.

        流水线名称

        :return: The name of this ListPipelinesPagePipelines.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListPipelinesPagePipelines.

        流水线名称

        :param name: The name of this ListPipelinesPagePipelines.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        """Gets the project_id of this ListPipelinesPagePipelines.

        项目ID

        :return: The project_id of this ListPipelinesPagePipelines.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this ListPipelinesPagePipelines.

        项目ID

        :param project_id: The project_id of this ListPipelinesPagePipelines.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def project_name(self):
        """Gets the project_name of this ListPipelinesPagePipelines.

        项目名称

        :return: The project_name of this ListPipelinesPagePipelines.
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this ListPipelinesPagePipelines.

        项目名称

        :param project_name: The project_name of this ListPipelinesPagePipelines.
        :type project_name: str
        """
        self._project_name = project_name

    @property
    def component_id(self):
        """Gets the component_id of this ListPipelinesPagePipelines.

        组件ID

        :return: The component_id of this ListPipelinesPagePipelines.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        """Sets the component_id of this ListPipelinesPagePipelines.

        组件ID

        :param component_id: The component_id of this ListPipelinesPagePipelines.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def is_publish(self):
        """Gets the is_publish of this ListPipelinesPagePipelines.

        是否为变更流水线

        :return: The is_publish of this ListPipelinesPagePipelines.
        :rtype: bool
        """
        return self._is_publish

    @is_publish.setter
    def is_publish(self, is_publish):
        """Sets the is_publish of this ListPipelinesPagePipelines.

        是否为变更流水线

        :param is_publish: The is_publish of this ListPipelinesPagePipelines.
        :type is_publish: bool
        """
        self._is_publish = is_publish

    @property
    def is_collect(self):
        """Gets the is_collect of this ListPipelinesPagePipelines.

        是否收藏此流水线

        :return: The is_collect of this ListPipelinesPagePipelines.
        :rtype: bool
        """
        return self._is_collect

    @is_collect.setter
    def is_collect(self, is_collect):
        """Sets the is_collect of this ListPipelinesPagePipelines.

        是否收藏此流水线

        :param is_collect: The is_collect of this ListPipelinesPagePipelines.
        :type is_collect: bool
        """
        self._is_collect = is_collect

    @property
    def manifest_version(self):
        """Gets the manifest_version of this ListPipelinesPagePipelines.

        流水线版本

        :return: The manifest_version of this ListPipelinesPagePipelines.
        :rtype: str
        """
        return self._manifest_version

    @manifest_version.setter
    def manifest_version(self, manifest_version):
        """Sets the manifest_version of this ListPipelinesPagePipelines.

        流水线版本

        :param manifest_version: The manifest_version of this ListPipelinesPagePipelines.
        :type manifest_version: str
        """
        self._manifest_version = manifest_version

    @property
    def create_time(self):
        """Gets the create_time of this ListPipelinesPagePipelines.

        创建时间

        :return: The create_time of this ListPipelinesPagePipelines.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ListPipelinesPagePipelines.

        创建时间

        :param create_time: The create_time of this ListPipelinesPagePipelines.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def latest_run(self):
        """Gets the latest_run of this ListPipelinesPagePipelines.

        :return: The latest_run of this ListPipelinesPagePipelines.
        :rtype: :class:`huaweicloudsdkcodeartspipeline.v2.ListPipelinesPageLatestRun`
        """
        return self._latest_run

    @latest_run.setter
    def latest_run(self, latest_run):
        """Sets the latest_run of this ListPipelinesPagePipelines.

        :param latest_run: The latest_run of this ListPipelinesPagePipelines.
        :type latest_run: :class:`huaweicloudsdkcodeartspipeline.v2.ListPipelinesPageLatestRun`
        """
        self._latest_run = latest_run

    @property
    def convert_sign(self):
        """Gets the convert_sign of this ListPipelinesPagePipelines.

        旧版转新版标识

        :return: The convert_sign of this ListPipelinesPagePipelines.
        :rtype: int
        """
        return self._convert_sign

    @convert_sign.setter
    def convert_sign(self, convert_sign):
        """Sets the convert_sign of this ListPipelinesPagePipelines.

        旧版转新版标识

        :param convert_sign: The convert_sign of this ListPipelinesPagePipelines.
        :type convert_sign: int
        """
        self._convert_sign = convert_sign

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
        if not isinstance(other, ListPipelinesPagePipelines):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
