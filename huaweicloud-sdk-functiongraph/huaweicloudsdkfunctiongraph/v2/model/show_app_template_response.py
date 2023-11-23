# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAppTemplateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'runtime': 'str',
        'category': 'str',
        'params': 'str',
        'image': 'str',
        'deploy_count': 'int',
        'version': 'int',
        'template_guide': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'resources': 'list[AppTemplateResourceDetail]'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'runtime': 'runtime',
        'category': 'category',
        'params': 'params',
        'image': 'image',
        'deploy_count': 'deploy_count',
        'version': 'version',
        'template_guide': 'template_guide',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'resources': 'resources'
    }

    def __init__(self, name=None, description=None, runtime=None, category=None, params=None, image=None, deploy_count=None, version=None, template_guide=None, create_time=None, update_time=None, resources=None):
        """ShowAppTemplateResponse

        The model defined in huaweicloud sdk

        :param name: 模板名称
        :type name: str
        :param description: 模板描述
        :type description: str
        :param runtime: 模板执行运行时
        :type runtime: str
        :param category: 模板使用场景
        :type category: str
        :param params: 模板参数
        :type params: str
        :param image: 模板镜像文件（base64编码）
        :type image: str
        :param deploy_count: 模板部署次数
        :type deploy_count: int
        :param version: 模板版本
        :type version: int
        :param template_guide: 模板指南
        :type template_guide: str
        :param create_time: 模板创建时间
        :type create_time: int
        :param update_time: 模板更新时间
        :type update_time: int
        :param resources: 模板资源
        :type resources: list[:class:`huaweicloudsdkfunctiongraph.v2.AppTemplateResourceDetail`]
        """
        
        super(ShowAppTemplateResponse, self).__init__()

        self._name = None
        self._description = None
        self._runtime = None
        self._category = None
        self._params = None
        self._image = None
        self._deploy_count = None
        self._version = None
        self._template_guide = None
        self._create_time = None
        self._update_time = None
        self._resources = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if runtime is not None:
            self.runtime = runtime
        if category is not None:
            self.category = category
        if params is not None:
            self.params = params
        if image is not None:
            self.image = image
        if deploy_count is not None:
            self.deploy_count = deploy_count
        if version is not None:
            self.version = version
        if template_guide is not None:
            self.template_guide = template_guide
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if resources is not None:
            self.resources = resources

    @property
    def name(self):
        """Gets the name of this ShowAppTemplateResponse.

        模板名称

        :return: The name of this ShowAppTemplateResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowAppTemplateResponse.

        模板名称

        :param name: The name of this ShowAppTemplateResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this ShowAppTemplateResponse.

        模板描述

        :return: The description of this ShowAppTemplateResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowAppTemplateResponse.

        模板描述

        :param description: The description of this ShowAppTemplateResponse.
        :type description: str
        """
        self._description = description

    @property
    def runtime(self):
        """Gets the runtime of this ShowAppTemplateResponse.

        模板执行运行时

        :return: The runtime of this ShowAppTemplateResponse.
        :rtype: str
        """
        return self._runtime

    @runtime.setter
    def runtime(self, runtime):
        """Sets the runtime of this ShowAppTemplateResponse.

        模板执行运行时

        :param runtime: The runtime of this ShowAppTemplateResponse.
        :type runtime: str
        """
        self._runtime = runtime

    @property
    def category(self):
        """Gets the category of this ShowAppTemplateResponse.

        模板使用场景

        :return: The category of this ShowAppTemplateResponse.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ShowAppTemplateResponse.

        模板使用场景

        :param category: The category of this ShowAppTemplateResponse.
        :type category: str
        """
        self._category = category

    @property
    def params(self):
        """Gets the params of this ShowAppTemplateResponse.

        模板参数

        :return: The params of this ShowAppTemplateResponse.
        :rtype: str
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this ShowAppTemplateResponse.

        模板参数

        :param params: The params of this ShowAppTemplateResponse.
        :type params: str
        """
        self._params = params

    @property
    def image(self):
        """Gets the image of this ShowAppTemplateResponse.

        模板镜像文件（base64编码）

        :return: The image of this ShowAppTemplateResponse.
        :rtype: str
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this ShowAppTemplateResponse.

        模板镜像文件（base64编码）

        :param image: The image of this ShowAppTemplateResponse.
        :type image: str
        """
        self._image = image

    @property
    def deploy_count(self):
        """Gets the deploy_count of this ShowAppTemplateResponse.

        模板部署次数

        :return: The deploy_count of this ShowAppTemplateResponse.
        :rtype: int
        """
        return self._deploy_count

    @deploy_count.setter
    def deploy_count(self, deploy_count):
        """Sets the deploy_count of this ShowAppTemplateResponse.

        模板部署次数

        :param deploy_count: The deploy_count of this ShowAppTemplateResponse.
        :type deploy_count: int
        """
        self._deploy_count = deploy_count

    @property
    def version(self):
        """Gets the version of this ShowAppTemplateResponse.

        模板版本

        :return: The version of this ShowAppTemplateResponse.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShowAppTemplateResponse.

        模板版本

        :param version: The version of this ShowAppTemplateResponse.
        :type version: int
        """
        self._version = version

    @property
    def template_guide(self):
        """Gets the template_guide of this ShowAppTemplateResponse.

        模板指南

        :return: The template_guide of this ShowAppTemplateResponse.
        :rtype: str
        """
        return self._template_guide

    @template_guide.setter
    def template_guide(self, template_guide):
        """Sets the template_guide of this ShowAppTemplateResponse.

        模板指南

        :param template_guide: The template_guide of this ShowAppTemplateResponse.
        :type template_guide: str
        """
        self._template_guide = template_guide

    @property
    def create_time(self):
        """Gets the create_time of this ShowAppTemplateResponse.

        模板创建时间

        :return: The create_time of this ShowAppTemplateResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowAppTemplateResponse.

        模板创建时间

        :param create_time: The create_time of this ShowAppTemplateResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ShowAppTemplateResponse.

        模板更新时间

        :return: The update_time of this ShowAppTemplateResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowAppTemplateResponse.

        模板更新时间

        :param update_time: The update_time of this ShowAppTemplateResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def resources(self):
        """Gets the resources of this ShowAppTemplateResponse.

        模板资源

        :return: The resources of this ShowAppTemplateResponse.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.AppTemplateResourceDetail`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this ShowAppTemplateResponse.

        模板资源

        :param resources: The resources of this ShowAppTemplateResponse.
        :type resources: list[:class:`huaweicloudsdkfunctiongraph.v2.AppTemplateResourceDetail`]
        """
        self._resources = resources

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
        if not isinstance(other, ShowAppTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
