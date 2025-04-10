# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTemplateDetailResponse(SdkResponse):

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
        'title': 'str',
        'description': 'str',
        'region_id': 'str',
        'repostory_id': 'str',
        'code_url': 'str',
        'ssh_url': 'str',
        'project_uuid': 'str',
        'status': 'int',
        'properties': 'list[object]',
        'dependencies': 'list[object]',
        'dependency_type': 'str',
        'deployment': 'object'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'description': 'description',
        'region_id': 'region_id',
        'repostory_id': 'repostory_id',
        'code_url': 'code_url',
        'ssh_url': 'ssh_url',
        'project_uuid': 'project_uuid',
        'status': 'status',
        'properties': 'properties',
        'dependencies': 'dependencies',
        'dependency_type': 'dependency_type',
        'deployment': 'deployment'
    }

    def __init__(self, id=None, title=None, description=None, region_id=None, repostory_id=None, code_url=None, ssh_url=None, project_uuid=None, status=None, properties=None, dependencies=None, dependency_type=None, deployment=None):
        r"""ShowTemplateDetailResponse

        The model defined in huaweicloud sdk

        :param id: 模板的id。
        :type id: str
        :param title: 模板的名称。
        :type title: str
        :param description: 模板的描述信息。
        :type description: str
        :param region_id: 模板关联的region host id。
        :type region_id: str
        :param repostory_id: 模板关联的repo id。
        :type repostory_id: str
        :param code_url: 模板https下载路径。
        :type code_url: str
        :param ssh_url: 模板ssh下载路径。
        :type ssh_url: str
        :param project_uuid: 项目id。
        :type project_uuid: str
        :param status: 模板状态。
        :type status: int
        :param properties: 源数据信息： - key：元数据标识 - defaultValue：用户输入值的默认值 - isShow：前台界面组件是否展示该元数据 - isProjectName：是否使用作为项目名称 - label：前台界面组件展示名称 - type：前台界面组件类型 - helpText：前台界面组件帮助文本 - readOnly：前台界面组件是否可修改 - required：前台界面组件是否展示必填 - regType：该元数据进行正则校验类型；简化模板编码使用 - regPattern：该元数据对应js语法正则表达式 - regTip：该元数据正则校验提示信息 - visibleRule：该元数据可见规则 - isRequired：是否必填 - isReadOnly：是否只读 - options：option对象集合   - displayName：前台界面展示字符串   - value：该选项值 - eventOnchange：联动属性集合   - associatedProperty：被关联Property的key值   - associatedValue：被关联的value - fold：是否折叠 - show：是否展示该Property 
        :type properties: list[object]
        :param dependencies: dependency信息： - id：依赖全局唯一标识 - name：依赖展示名称 - description：依赖展示描述 - recommended：是否推荐使用该依赖 - versionProperty：该依赖版本被关联Property的key值 - versionRange：该依赖版本适用范围 - groupName：分组名称 - items：分组列表 
        :type dependencies: list[object]
        :param dependency_type: dependency类型： - 0：分组 - 1：不分组 - null：无分组信息 
        :type dependency_type: str
        :param deployment: 部署信息： - param：参数对象   - build：构建类型   - runtime：函数运行时   - handler：函数执行入口   - outputFile：构建产物文件路径 - target：部署环境 
        :type deployment: object
        """
        
        super(ShowTemplateDetailResponse, self).__init__()

        self._id = None
        self._title = None
        self._description = None
        self._region_id = None
        self._repostory_id = None
        self._code_url = None
        self._ssh_url = None
        self._project_uuid = None
        self._status = None
        self._properties = None
        self._dependencies = None
        self._dependency_type = None
        self._deployment = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if region_id is not None:
            self.region_id = region_id
        if repostory_id is not None:
            self.repostory_id = repostory_id
        if code_url is not None:
            self.code_url = code_url
        if ssh_url is not None:
            self.ssh_url = ssh_url
        if project_uuid is not None:
            self.project_uuid = project_uuid
        if status is not None:
            self.status = status
        if properties is not None:
            self.properties = properties
        if dependencies is not None:
            self.dependencies = dependencies
        if dependency_type is not None:
            self.dependency_type = dependency_type
        if deployment is not None:
            self.deployment = deployment

    @property
    def id(self):
        r"""Gets the id of this ShowTemplateDetailResponse.

        模板的id。

        :return: The id of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowTemplateDetailResponse.

        模板的id。

        :param id: The id of this ShowTemplateDetailResponse.
        :type id: str
        """
        self._id = id

    @property
    def title(self):
        r"""Gets the title of this ShowTemplateDetailResponse.

        模板的名称。

        :return: The title of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this ShowTemplateDetailResponse.

        模板的名称。

        :param title: The title of this ShowTemplateDetailResponse.
        :type title: str
        """
        self._title = title

    @property
    def description(self):
        r"""Gets the description of this ShowTemplateDetailResponse.

        模板的描述信息。

        :return: The description of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowTemplateDetailResponse.

        模板的描述信息。

        :param description: The description of this ShowTemplateDetailResponse.
        :type description: str
        """
        self._description = description

    @property
    def region_id(self):
        r"""Gets the region_id of this ShowTemplateDetailResponse.

        模板关联的region host id。

        :return: The region_id of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        r"""Sets the region_id of this ShowTemplateDetailResponse.

        模板关联的region host id。

        :param region_id: The region_id of this ShowTemplateDetailResponse.
        :type region_id: str
        """
        self._region_id = region_id

    @property
    def repostory_id(self):
        r"""Gets the repostory_id of this ShowTemplateDetailResponse.

        模板关联的repo id。

        :return: The repostory_id of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._repostory_id

    @repostory_id.setter
    def repostory_id(self, repostory_id):
        r"""Sets the repostory_id of this ShowTemplateDetailResponse.

        模板关联的repo id。

        :param repostory_id: The repostory_id of this ShowTemplateDetailResponse.
        :type repostory_id: str
        """
        self._repostory_id = repostory_id

    @property
    def code_url(self):
        r"""Gets the code_url of this ShowTemplateDetailResponse.

        模板https下载路径。

        :return: The code_url of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._code_url

    @code_url.setter
    def code_url(self, code_url):
        r"""Sets the code_url of this ShowTemplateDetailResponse.

        模板https下载路径。

        :param code_url: The code_url of this ShowTemplateDetailResponse.
        :type code_url: str
        """
        self._code_url = code_url

    @property
    def ssh_url(self):
        r"""Gets the ssh_url of this ShowTemplateDetailResponse.

        模板ssh下载路径。

        :return: The ssh_url of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._ssh_url

    @ssh_url.setter
    def ssh_url(self, ssh_url):
        r"""Sets the ssh_url of this ShowTemplateDetailResponse.

        模板ssh下载路径。

        :param ssh_url: The ssh_url of this ShowTemplateDetailResponse.
        :type ssh_url: str
        """
        self._ssh_url = ssh_url

    @property
    def project_uuid(self):
        r"""Gets the project_uuid of this ShowTemplateDetailResponse.

        项目id。

        :return: The project_uuid of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        r"""Sets the project_uuid of this ShowTemplateDetailResponse.

        项目id。

        :param project_uuid: The project_uuid of this ShowTemplateDetailResponse.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def status(self):
        r"""Gets the status of this ShowTemplateDetailResponse.

        模板状态。

        :return: The status of this ShowTemplateDetailResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowTemplateDetailResponse.

        模板状态。

        :param status: The status of this ShowTemplateDetailResponse.
        :type status: int
        """
        self._status = status

    @property
    def properties(self):
        r"""Gets the properties of this ShowTemplateDetailResponse.

        源数据信息： - key：元数据标识 - defaultValue：用户输入值的默认值 - isShow：前台界面组件是否展示该元数据 - isProjectName：是否使用作为项目名称 - label：前台界面组件展示名称 - type：前台界面组件类型 - helpText：前台界面组件帮助文本 - readOnly：前台界面组件是否可修改 - required：前台界面组件是否展示必填 - regType：该元数据进行正则校验类型；简化模板编码使用 - regPattern：该元数据对应js语法正则表达式 - regTip：该元数据正则校验提示信息 - visibleRule：该元数据可见规则 - isRequired：是否必填 - isReadOnly：是否只读 - options：option对象集合   - displayName：前台界面展示字符串   - value：该选项值 - eventOnchange：联动属性集合   - associatedProperty：被关联Property的key值   - associatedValue：被关联的value - fold：是否折叠 - show：是否展示该Property 

        :return: The properties of this ShowTemplateDetailResponse.
        :rtype: list[object]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        r"""Sets the properties of this ShowTemplateDetailResponse.

        源数据信息： - key：元数据标识 - defaultValue：用户输入值的默认值 - isShow：前台界面组件是否展示该元数据 - isProjectName：是否使用作为项目名称 - label：前台界面组件展示名称 - type：前台界面组件类型 - helpText：前台界面组件帮助文本 - readOnly：前台界面组件是否可修改 - required：前台界面组件是否展示必填 - regType：该元数据进行正则校验类型；简化模板编码使用 - regPattern：该元数据对应js语法正则表达式 - regTip：该元数据正则校验提示信息 - visibleRule：该元数据可见规则 - isRequired：是否必填 - isReadOnly：是否只读 - options：option对象集合   - displayName：前台界面展示字符串   - value：该选项值 - eventOnchange：联动属性集合   - associatedProperty：被关联Property的key值   - associatedValue：被关联的value - fold：是否折叠 - show：是否展示该Property 

        :param properties: The properties of this ShowTemplateDetailResponse.
        :type properties: list[object]
        """
        self._properties = properties

    @property
    def dependencies(self):
        r"""Gets the dependencies of this ShowTemplateDetailResponse.

        dependency信息： - id：依赖全局唯一标识 - name：依赖展示名称 - description：依赖展示描述 - recommended：是否推荐使用该依赖 - versionProperty：该依赖版本被关联Property的key值 - versionRange：该依赖版本适用范围 - groupName：分组名称 - items：分组列表 

        :return: The dependencies of this ShowTemplateDetailResponse.
        :rtype: list[object]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        r"""Sets the dependencies of this ShowTemplateDetailResponse.

        dependency信息： - id：依赖全局唯一标识 - name：依赖展示名称 - description：依赖展示描述 - recommended：是否推荐使用该依赖 - versionProperty：该依赖版本被关联Property的key值 - versionRange：该依赖版本适用范围 - groupName：分组名称 - items：分组列表 

        :param dependencies: The dependencies of this ShowTemplateDetailResponse.
        :type dependencies: list[object]
        """
        self._dependencies = dependencies

    @property
    def dependency_type(self):
        r"""Gets the dependency_type of this ShowTemplateDetailResponse.

        dependency类型： - 0：分组 - 1：不分组 - null：无分组信息 

        :return: The dependency_type of this ShowTemplateDetailResponse.
        :rtype: str
        """
        return self._dependency_type

    @dependency_type.setter
    def dependency_type(self, dependency_type):
        r"""Sets the dependency_type of this ShowTemplateDetailResponse.

        dependency类型： - 0：分组 - 1：不分组 - null：无分组信息 

        :param dependency_type: The dependency_type of this ShowTemplateDetailResponse.
        :type dependency_type: str
        """
        self._dependency_type = dependency_type

    @property
    def deployment(self):
        r"""Gets the deployment of this ShowTemplateDetailResponse.

        部署信息： - param：参数对象   - build：构建类型   - runtime：函数运行时   - handler：函数执行入口   - outputFile：构建产物文件路径 - target：部署环境 

        :return: The deployment of this ShowTemplateDetailResponse.
        :rtype: object
        """
        return self._deployment

    @deployment.setter
    def deployment(self, deployment):
        r"""Sets the deployment of this ShowTemplateDetailResponse.

        部署信息： - param：参数对象   - build：构建类型   - runtime：函数运行时   - handler：函数执行入口   - outputFile：构建产物文件路径 - target：部署环境 

        :param deployment: The deployment of this ShowTemplateDetailResponse.
        :type deployment: object
        """
        self._deployment = deployment

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
        if not isinstance(other, ShowTemplateDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
