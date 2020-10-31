# coding: utf-8

import pprint
import re

import six





class TemplateInfo:


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
        'productshorts': 'list[str]',
        'products': 'list[TemplateProductExt]',
        'topic': 'list[TopicCategory]',
        'creator_id': 'str',
        'creator': 'str',
        'nickname': 'str',
        'score': 'int',
        'label': 'str',
        'store': 'int',
        'store_info': 'str',
        'status': 'int',
        'view_count': 'int',
        'usage_count': 'int',
        'created_at': 'str',
        'updated_at': 'str',
        'published_at': 'str',
        'favorite_state': 'int',
        'tags': 'list[TagInfo]',
        'type': 'int',
        'is_static': 'int',
        'maintainers': 'list[str]',
        'pipeline_template': 'PipelineTemplateInfo',
        'platform_source': 'int',
        'references': 'list[Reference]',
        'properties': 'object',
        'dependencies': 'list[object]',
        'dependency_type': 'str',
        'forum_id': 'int',
        'file_size': 'int',
        'deployment': 'object',
        'update_id': 'str',
        'is_support_cloudide': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'description': 'description',
        'productshorts': 'productshorts',
        'products': 'products',
        'topic': 'topic',
        'creator_id': 'creator_id',
        'creator': 'creator',
        'nickname': 'nickname',
        'score': 'score',
        'label': 'label',
        'store': 'store',
        'store_info': 'store_info',
        'status': 'status',
        'view_count': 'view_count',
        'usage_count': 'usage_count',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'published_at': 'published_at',
        'favorite_state': 'favorite_state',
        'tags': 'tags',
        'type': 'type',
        'is_static': 'is_static',
        'maintainers': 'maintainers',
        'pipeline_template': 'pipeline_template',
        'platform_source': 'platform_source',
        'references': 'references',
        'properties': 'properties',
        'dependencies': 'dependencies',
        'dependency_type': 'dependency_type',
        'forum_id': 'forum_id',
        'file_size': 'file_size',
        'deployment': 'deployment',
        'update_id': 'update_id',
        'is_support_cloudide': 'is_support_cloudide'
    }

    def __init__(self, id=None, title=None, description=None, productshorts=None, products=None, topic=None, creator_id=None, creator=None, nickname=None, score=None, label=None, store=None, store_info=None, status=None, view_count=None, usage_count=None, created_at=None, updated_at=None, published_at=None, favorite_state=None, tags=None, type=None, is_static=None, maintainers=None, pipeline_template=None, platform_source=None, references=None, properties=None, dependencies=None, dependency_type=None, forum_id=None, file_size=None, deployment=None, update_id=None, is_support_cloudide=False):
        """TemplateInfo - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._title = None
        self._description = None
        self._productshorts = None
        self._products = None
        self._topic = None
        self._creator_id = None
        self._creator = None
        self._nickname = None
        self._score = None
        self._label = None
        self._store = None
        self._store_info = None
        self._status = None
        self._view_count = None
        self._usage_count = None
        self._created_at = None
        self._updated_at = None
        self._published_at = None
        self._favorite_state = None
        self._tags = None
        self._type = None
        self._is_static = None
        self._maintainers = None
        self._pipeline_template = None
        self._platform_source = None
        self._references = None
        self._properties = None
        self._dependencies = None
        self._dependency_type = None
        self._forum_id = None
        self._file_size = None
        self._deployment = None
        self._update_id = None
        self._is_support_cloudide = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if productshorts is not None:
            self.productshorts = productshorts
        if products is not None:
            self.products = products
        if topic is not None:
            self.topic = topic
        if creator_id is not None:
            self.creator_id = creator_id
        if creator is not None:
            self.creator = creator
        if nickname is not None:
            self.nickname = nickname
        if score is not None:
            self.score = score
        if label is not None:
            self.label = label
        if store is not None:
            self.store = store
        if store_info is not None:
            self.store_info = store_info
        if status is not None:
            self.status = status
        if view_count is not None:
            self.view_count = view_count
        if usage_count is not None:
            self.usage_count = usage_count
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if published_at is not None:
            self.published_at = published_at
        if favorite_state is not None:
            self.favorite_state = favorite_state
        if tags is not None:
            self.tags = tags
        if type is not None:
            self.type = type
        if is_static is not None:
            self.is_static = is_static
        if maintainers is not None:
            self.maintainers = maintainers
        if pipeline_template is not None:
            self.pipeline_template = pipeline_template
        if platform_source is not None:
            self.platform_source = platform_source
        if references is not None:
            self.references = references
        if properties is not None:
            self.properties = properties
        if dependencies is not None:
            self.dependencies = dependencies
        if dependency_type is not None:
            self.dependency_type = dependency_type
        if forum_id is not None:
            self.forum_id = forum_id
        if file_size is not None:
            self.file_size = file_size
        if deployment is not None:
            self.deployment = deployment
        if update_id is not None:
            self.update_id = update_id
        if is_support_cloudide is not None:
            self.is_support_cloudide = is_support_cloudide

    @property
    def id(self):
        """Gets the id of this TemplateInfo.

        模板id

        :return: The id of this TemplateInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TemplateInfo.

        模板id

        :param id: The id of this TemplateInfo.
        :type: str
        """
        self._id = id

    @property
    def title(self):
        """Gets the title of this TemplateInfo.

        模板名

        :return: The title of this TemplateInfo.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this TemplateInfo.

        模板名

        :param title: The title of this TemplateInfo.
        :type: str
        """
        self._title = title

    @property
    def description(self):
        """Gets the description of this TemplateInfo.

        模板描述

        :return: The description of this TemplateInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TemplateInfo.

        模板描述

        :param description: The description of this TemplateInfo.
        :type: str
        """
        self._description = description

    @property
    def productshorts(self):
        """Gets the productshorts of this TemplateInfo.

        模板关联的所有云服务（产品短名）

        :return: The productshorts of this TemplateInfo.
        :rtype: list[str]
        """
        return self._productshorts

    @productshorts.setter
    def productshorts(self, productshorts):
        """Sets the productshorts of this TemplateInfo.

        模板关联的所有云服务（产品短名）

        :param productshorts: The productshorts of this TemplateInfo.
        :type: list[str]
        """
        self._productshorts = productshorts

    @property
    def products(self):
        """Gets the products of this TemplateInfo.

        模板关联的云产品

        :return: The products of this TemplateInfo.
        :rtype: list[TemplateProductExt]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this TemplateInfo.

        模板关联的云产品

        :param products: The products of this TemplateInfo.
        :type: list[TemplateProductExt]
        """
        self._products = products

    @property
    def topic(self):
        """Gets the topic of this TemplateInfo.

        模板标签

        :return: The topic of this TemplateInfo.
        :rtype: list[TopicCategory]
        """
        return self._topic

    @topic.setter
    def topic(self, topic):
        """Sets the topic of this TemplateInfo.

        模板标签

        :param topic: The topic of this TemplateInfo.
        :type: list[TopicCategory]
        """
        self._topic = topic

    @property
    def creator_id(self):
        """Gets the creator_id of this TemplateInfo.

        模板创建者id

        :return: The creator_id of this TemplateInfo.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this TemplateInfo.

        模板创建者id

        :param creator_id: The creator_id of this TemplateInfo.
        :type: str
        """
        self._creator_id = creator_id

    @property
    def creator(self):
        """Gets the creator of this TemplateInfo.

        模板创建者,有别名返回别名

        :return: The creator of this TemplateInfo.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this TemplateInfo.

        模板创建者,有别名返回别名

        :param creator: The creator of this TemplateInfo.
        :type: str
        """
        self._creator = creator

    @property
    def nickname(self):
        """Gets the nickname of this TemplateInfo.

        模板创建者,有别名返回别名

        :return: The nickname of this TemplateInfo.
        :rtype: str
        """
        return self._nickname

    @nickname.setter
    def nickname(self, nickname):
        """Sets the nickname of this TemplateInfo.

        模板创建者,有别名返回别名

        :param nickname: The nickname of this TemplateInfo.
        :type: str
        """
        self._nickname = nickname

    @property
    def score(self):
        """Gets the score of this TemplateInfo.

        模板评分（点赞数）

        :return: The score of this TemplateInfo.
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this TemplateInfo.

        模板评分（点赞数）

        :param score: The score of this TemplateInfo.
        :type: int
        """
        self._score = score

    @property
    def label(self):
        """Gets the label of this TemplateInfo.

        模板标签（new、hot等）

        :return: The label of this TemplateInfo.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this TemplateInfo.

        模板标签（new、hot等）

        :param label: The label of this TemplateInfo.
        :type: str
        """
        self._label = label

    @property
    def store(self):
        """Gets the store of this TemplateInfo.

        代码存储位置

        :return: The store of this TemplateInfo.
        :rtype: int
        """
        return self._store

    @store.setter
    def store(self, store):
        """Sets the store of this TemplateInfo.

        代码存储位置

        :param store: The store of this TemplateInfo.
        :type: int
        """
        self._store = store

    @property
    def store_info(self):
        """Gets the store_info of this TemplateInfo.

        获取代码模版所需的信息

        :return: The store_info of this TemplateInfo.
        :rtype: str
        """
        return self._store_info

    @store_info.setter
    def store_info(self, store_info):
        """Sets the store_info of this TemplateInfo.

        获取代码模版所需的信息

        :param store_info: The store_info of this TemplateInfo.
        :type: str
        """
        self._store_info = store_info

    @property
    def status(self):
        """Gets the status of this TemplateInfo.

        模板状态（0:审核中 1: 已上架 2: 未上架（已下架）3: 未上架（合规检查不通过）4：未上架（待上架）5：已删除）

        :return: The status of this TemplateInfo.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TemplateInfo.

        模板状态（0:审核中 1: 已上架 2: 未上架（已下架）3: 未上架（合规检查不通过）4：未上架（待上架）5：已删除）

        :param status: The status of this TemplateInfo.
        :type: int
        """
        self._status = status

    @property
    def view_count(self):
        """Gets the view_count of this TemplateInfo.

        访问量

        :return: The view_count of this TemplateInfo.
        :rtype: int
        """
        return self._view_count

    @view_count.setter
    def view_count(self, view_count):
        """Sets the view_count of this TemplateInfo.

        访问量

        :param view_count: The view_count of this TemplateInfo.
        :type: int
        """
        self._view_count = view_count

    @property
    def usage_count(self):
        """Gets the usage_count of this TemplateInfo.

        引用量

        :return: The usage_count of this TemplateInfo.
        :rtype: int
        """
        return self._usage_count

    @usage_count.setter
    def usage_count(self, usage_count):
        """Sets the usage_count of this TemplateInfo.

        引用量

        :param usage_count: The usage_count of this TemplateInfo.
        :type: int
        """
        self._usage_count = usage_count

    @property
    def created_at(self):
        """Gets the created_at of this TemplateInfo.

        创建时间

        :return: The created_at of this TemplateInfo.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this TemplateInfo.

        创建时间

        :param created_at: The created_at of this TemplateInfo.
        :type: str
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this TemplateInfo.

        更新时间

        :return: The updated_at of this TemplateInfo.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this TemplateInfo.

        更新时间

        :param updated_at: The updated_at of this TemplateInfo.
        :type: str
        """
        self._updated_at = updated_at

    @property
    def published_at(self):
        """Gets the published_at of this TemplateInfo.

        模板上架时间

        :return: The published_at of this TemplateInfo.
        :rtype: str
        """
        return self._published_at

    @published_at.setter
    def published_at(self, published_at):
        """Sets the published_at of this TemplateInfo.

        模板上架时间

        :param published_at: The published_at of this TemplateInfo.
        :type: str
        """
        self._published_at = published_at

    @property
    def favorite_state(self):
        """Gets the favorite_state of this TemplateInfo.

        点赞状态(1：点赞，0：未点赞)

        :return: The favorite_state of this TemplateInfo.
        :rtype: int
        """
        return self._favorite_state

    @favorite_state.setter
    def favorite_state(self, favorite_state):
        """Sets the favorite_state of this TemplateInfo.

        点赞状态(1：点赞，0：未点赞)

        :param favorite_state: The favorite_state of this TemplateInfo.
        :type: int
        """
        self._favorite_state = favorite_state

    @property
    def tags(self):
        """Gets the tags of this TemplateInfo.

        模板标签

        :return: The tags of this TemplateInfo.
        :rtype: list[TagInfo]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TemplateInfo.

        模板标签

        :param tags: The tags of this TemplateInfo.
        :type: list[TagInfo]
        """
        self._tags = tags

    @property
    def type(self):
        """Gets the type of this TemplateInfo.

        模板类型（0:doc、1:code、2:pipeline、3:devops四种）

        :return: The type of this TemplateInfo.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TemplateInfo.

        模板类型（0:doc、1:code、2:pipeline、3:devops四种）

        :param type: The type of this TemplateInfo.
        :type: int
        """
        self._type = type

    @property
    def is_static(self):
        """Gets the is_static of this TemplateInfo.

        动、静态代码模板标识（0：动态模板codetemplate，1：静态模板codesample）

        :return: The is_static of this TemplateInfo.
        :rtype: int
        """
        return self._is_static

    @is_static.setter
    def is_static(self, is_static):
        """Sets the is_static of this TemplateInfo.

        动、静态代码模板标识（0：动态模板codetemplate，1：静态模板codesample）

        :param is_static: The is_static of this TemplateInfo.
        :type: int
        """
        self._is_static = is_static

    @property
    def maintainers(self):
        """Gets the maintainers of this TemplateInfo.

        模板相关联的所有维护人账号名称

        :return: The maintainers of this TemplateInfo.
        :rtype: list[str]
        """
        return self._maintainers

    @maintainers.setter
    def maintainers(self, maintainers):
        """Sets the maintainers of this TemplateInfo.

        模板相关联的所有维护人账号名称

        :param maintainers: The maintainers of this TemplateInfo.
        :type: list[str]
        """
        self._maintainers = maintainers

    @property
    def pipeline_template(self):
        """Gets the pipeline_template of this TemplateInfo.


        :return: The pipeline_template of this TemplateInfo.
        :rtype: PipelineTemplateInfo
        """
        return self._pipeline_template

    @pipeline_template.setter
    def pipeline_template(self, pipeline_template):
        """Sets the pipeline_template of this TemplateInfo.


        :param pipeline_template: The pipeline_template of this TemplateInfo.
        :type: PipelineTemplateInfo
        """
        self._pipeline_template = pipeline_template

    @property
    def platform_source(self):
        """Gets the platform_source of this TemplateInfo.

        平台来源（0:codelabs、1:devstar）

        :return: The platform_source of this TemplateInfo.
        :rtype: int
        """
        return self._platform_source

    @platform_source.setter
    def platform_source(self, platform_source):
        """Sets the platform_source of this TemplateInfo.

        平台来源（0:codelabs、1:devstar）

        :param platform_source: The platform_source of this TemplateInfo.
        :type: int
        """
        self._platform_source = platform_source

    @property
    def references(self):
        """Gets the references of this TemplateInfo.

        相关文档，示例，帖子

        :return: The references of this TemplateInfo.
        :rtype: list[Reference]
        """
        return self._references

    @references.setter
    def references(self, references):
        """Sets the references of this TemplateInfo.

        相关文档，示例，帖子

        :param references: The references of this TemplateInfo.
        :type: list[Reference]
        """
        self._references = references

    @property
    def properties(self):
        """Gets the properties of this TemplateInfo.

        模板自定义参数列表

        :return: The properties of this TemplateInfo.
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this TemplateInfo.

        模板自定义参数列表

        :param properties: The properties of this TemplateInfo.
        :type: object
        """
        self._properties = properties

    @property
    def dependencies(self):
        """Gets the dependencies of this TemplateInfo.

        dependency信息

        :return: The dependencies of this TemplateInfo.
        :rtype: list[object]
        """
        return self._dependencies

    @dependencies.setter
    def dependencies(self, dependencies):
        """Sets the dependencies of this TemplateInfo.

        dependency信息

        :param dependencies: The dependencies of this TemplateInfo.
        :type: list[object]
        """
        self._dependencies = dependencies

    @property
    def dependency_type(self):
        """Gets the dependency_type of this TemplateInfo.

        dependency类型

        :return: The dependency_type of this TemplateInfo.
        :rtype: str
        """
        return self._dependency_type

    @dependency_type.setter
    def dependency_type(self, dependency_type):
        """Sets the dependency_type of this TemplateInfo.

        dependency类型

        :param dependency_type: The dependency_type of this TemplateInfo.
        :type: str
        """
        self._dependency_type = dependency_type

    @property
    def forum_id(self):
        """Gets the forum_id of this TemplateInfo.

        关联论坛板块id

        :return: The forum_id of this TemplateInfo.
        :rtype: int
        """
        return self._forum_id

    @forum_id.setter
    def forum_id(self, forum_id):
        """Sets the forum_id of this TemplateInfo.

        关联论坛板块id

        :param forum_id: The forum_id of this TemplateInfo.
        :type: int
        """
        self._forum_id = forum_id

    @property
    def file_size(self):
        """Gets the file_size of this TemplateInfo.

        模板文件解压缩之后的大小(单位:KB)

        :return: The file_size of this TemplateInfo.
        :rtype: int
        """
        return self._file_size

    @file_size.setter
    def file_size(self, file_size):
        """Sets the file_size of this TemplateInfo.

        模板文件解压缩之后的大小(单位:KB)

        :param file_size: The file_size of this TemplateInfo.
        :type: int
        """
        self._file_size = file_size

    @property
    def deployment(self):
        """Gets the deployment of this TemplateInfo.

        部署信息

        :return: The deployment of this TemplateInfo.
        :rtype: object
        """
        return self._deployment

    @deployment.setter
    def deployment(self, deployment):
        """Sets the deployment of this TemplateInfo.

        部署信息

        :param deployment: The deployment of this TemplateInfo.
        :type: object
        """
        self._deployment = deployment

    @property
    def update_id(self):
        """Gets the update_id of this TemplateInfo.

        模板关联更新态Id

        :return: The update_id of this TemplateInfo.
        :rtype: str
        """
        return self._update_id

    @update_id.setter
    def update_id(self, update_id):
        """Sets the update_id of this TemplateInfo.

        模板关联更新态Id

        :param update_id: The update_id of this TemplateInfo.
        :type: str
        """
        self._update_id = update_id

    @property
    def is_support_cloudide(self):
        """Gets the is_support_cloudide of this TemplateInfo.

        是否支持使用CloudIDE运行源码

        :return: The is_support_cloudide of this TemplateInfo.
        :rtype: bool
        """
        return self._is_support_cloudide

    @is_support_cloudide.setter
    def is_support_cloudide(self, is_support_cloudide):
        """Sets the is_support_cloudide of this TemplateInfo.

        是否支持使用CloudIDE运行源码

        :param is_support_cloudide: The is_support_cloudide of this TemplateInfo.
        :type: bool
        """
        self._is_support_cloudide = is_support_cloudide

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TemplateInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
