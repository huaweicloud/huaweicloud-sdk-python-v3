# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtensionAllSnake:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'extension_id': 'str',
        'extension_name': 'str',
        'display_name': 'str',
        'flags': 'int',
        'last_updated': 'datetime',
        'published_date': 'datetime',
        'release_date': 'datetime',
        'short_description': 'str',
        'tags': 'list[str]',
        'tag_all_list': 'list[str]',
        'publisher': 'PublisherSnake',
        'arch': 'list[str]',
        'target': 'str',
        'categories': 'list[str]',
        'category_all_list': 'list[str]',
        'publish_manager': 'PublisherSnake',
        'status': 'str',
        'validate_status': 'str',
        'install_count': 'int',
        'average_star': 'float',
        'identifier': 'str',
        'support_os': 'list[str]',
        'support_ide': 'int',
        'support_ide_info': 'str',
        'versions': 'list[ExtensionVersionSnake]',
        'validate_result': 'str',
        'extension_statistics': 'ExtensionStatistics',
        'preview': 'bool',
        'ext_info': 'ExtensionExternalInfo',
        'platform': 'str',
        'check_result': 'CheckResult',
        'gray_version_count': 'int',
        'extension_owner': 'str'
    }

    attribute_map = {
        'extension_id': 'extension_id',
        'extension_name': 'extension_name',
        'display_name': 'display_name',
        'flags': 'flags',
        'last_updated': 'last_updated',
        'published_date': 'published_date',
        'release_date': 'release_date',
        'short_description': 'short_description',
        'tags': 'tags',
        'tag_all_list': 'tag_all_list',
        'publisher': 'publisher',
        'arch': 'arch',
        'target': 'target',
        'categories': 'categories',
        'category_all_list': 'category_all_list',
        'publish_manager': 'publish_manager',
        'status': 'status',
        'validate_status': 'validate_status',
        'install_count': 'install_count',
        'average_star': 'average_star',
        'identifier': 'identifier',
        'support_os': 'support_os',
        'support_ide': 'support_ide',
        'support_ide_info': 'support_ide_info',
        'versions': 'versions',
        'validate_result': 'validate_result',
        'extension_statistics': 'extension_statistics',
        'preview': 'preview',
        'ext_info': 'ext_info',
        'platform': 'platform',
        'check_result': 'check_result',
        'gray_version_count': 'gray_version_count',
        'extension_owner': 'extension_owner'
    }

    def __init__(self, extension_id=None, extension_name=None, display_name=None, flags=None, last_updated=None, published_date=None, release_date=None, short_description=None, tags=None, tag_all_list=None, publisher=None, arch=None, target=None, categories=None, category_all_list=None, publish_manager=None, status=None, validate_status=None, install_count=None, average_star=None, identifier=None, support_os=None, support_ide=None, support_ide_info=None, versions=None, validate_result=None, extension_statistics=None, preview=None, ext_info=None, platform=None, check_result=None, gray_version_count=None, extension_owner=None):
        """ExtensionAllSnake

        The model defined in huaweicloud sdk

        :param extension_id: 插件id
        :type extension_id: str
        :param extension_name: 插件名称
        :type extension_name: str
        :param display_name: 插件显示名称
        :type display_name: str
        :param flags: 插件flag;通过传递flag参数来进行过滤或其他操作。flag的基础数字是2\\4\\8\\16;传递的参数只能是这四个数字加法组合而成的数字 利用它们之间二进制的运算获取的值进行其他操作.比如6&#x3D;0110&#x3D;0010+0100也就是2和4的集合flags
        :type flags: int
        :param last_updated: 更新时间
        :type last_updated: datetime
        :param published_date: 上传时间
        :type published_date: datetime
        :param release_date: 发布时间
        :type release_date: datetime
        :param short_description: 插件描述
        :type short_description: str
        :param tags: 插件标签
        :type tags: list[str]
        :param tag_all_list: 所有标签
        :type tag_all_list: list[str]
        :param publisher: 
        :type publisher: :class:`huaweicloudsdkcloudide.v2.PublisherSnake`
        :param arch: 系统架构
        :type arch: list[str]
        :param target: 安装目标
        :type target: str
        :param categories: 插件分类
        :type categories: list[str]
        :param category_all_list: 全部分类列表
        :type category_all_list: list[str]
        :param publish_manager: 
        :type publish_manager: :class:`huaweicloudsdkcloudide.v2.PublisherSnake`
        :param status: 插件状态  - INIT 上传插件的第一个版本 - NORMAL 插件有审核通过的版本 - OFFLINE 插件下线 - ABANDONED 上传废弃 - GRAYED 灰度插件
        :type status: str
        :param validate_status: 插件审核状态  - NONE 审核结束 - VALIDATING 审核中
        :type validate_status: str
        :param install_count: 下载量
        :type install_count: int
        :param average_star: 平均评星值
        :type average_star: float
        :param identifier: 插件唯一标识内部插件市场保留
        :type identifier: str
        :param support_os: 插件支持的操作系统
        :type support_os: list[str]
        :param support_ide: 插件支持的ide
        :type support_ide: int
        :param support_ide_info: 插件支持的ide名称
        :type support_ide_info: str
        :param versions: 插件版本集合
        :type versions: list[:class:`huaweicloudsdkcloudide.v2.ExtensionVersionSnake`]
        :param validate_result: 插件审核结果
        :type validate_result: str
        :param extension_statistics: 
        :type extension_statistics: :class:`huaweicloudsdkcloudide.v2.ExtensionStatistics`
        :param preview: 是否支持预览
        :type preview: bool
        :param ext_info: 
        :type ext_info: :class:`huaweicloudsdkcloudide.v2.ExtensionExternalInfo`
        :param platform: 安装目标
        :type platform: str
        :param check_result: 
        :type check_result: :class:`huaweicloudsdkcloudide.v2.CheckResult`
        :param gray_version_count: 灰度版本数量
        :type gray_version_count: int
        :param extension_owner: 插件作者
        :type extension_owner: str
        """
        
        

        self._extension_id = None
        self._extension_name = None
        self._display_name = None
        self._flags = None
        self._last_updated = None
        self._published_date = None
        self._release_date = None
        self._short_description = None
        self._tags = None
        self._tag_all_list = None
        self._publisher = None
        self._arch = None
        self._target = None
        self._categories = None
        self._category_all_list = None
        self._publish_manager = None
        self._status = None
        self._validate_status = None
        self._install_count = None
        self._average_star = None
        self._identifier = None
        self._support_os = None
        self._support_ide = None
        self._support_ide_info = None
        self._versions = None
        self._validate_result = None
        self._extension_statistics = None
        self._preview = None
        self._ext_info = None
        self._platform = None
        self._check_result = None
        self._gray_version_count = None
        self._extension_owner = None
        self.discriminator = None

        if extension_id is not None:
            self.extension_id = extension_id
        if extension_name is not None:
            self.extension_name = extension_name
        if display_name is not None:
            self.display_name = display_name
        if flags is not None:
            self.flags = flags
        if last_updated is not None:
            self.last_updated = last_updated
        if published_date is not None:
            self.published_date = published_date
        if release_date is not None:
            self.release_date = release_date
        if short_description is not None:
            self.short_description = short_description
        if tags is not None:
            self.tags = tags
        if tag_all_list is not None:
            self.tag_all_list = tag_all_list
        if publisher is not None:
            self.publisher = publisher
        if arch is not None:
            self.arch = arch
        if target is not None:
            self.target = target
        if categories is not None:
            self.categories = categories
        if category_all_list is not None:
            self.category_all_list = category_all_list
        if publish_manager is not None:
            self.publish_manager = publish_manager
        if status is not None:
            self.status = status
        if validate_status is not None:
            self.validate_status = validate_status
        if install_count is not None:
            self.install_count = install_count
        if average_star is not None:
            self.average_star = average_star
        if identifier is not None:
            self.identifier = identifier
        if support_os is not None:
            self.support_os = support_os
        if support_ide is not None:
            self.support_ide = support_ide
        if support_ide_info is not None:
            self.support_ide_info = support_ide_info
        if versions is not None:
            self.versions = versions
        if validate_result is not None:
            self.validate_result = validate_result
        if extension_statistics is not None:
            self.extension_statistics = extension_statistics
        if preview is not None:
            self.preview = preview
        if ext_info is not None:
            self.ext_info = ext_info
        if platform is not None:
            self.platform = platform
        if check_result is not None:
            self.check_result = check_result
        if gray_version_count is not None:
            self.gray_version_count = gray_version_count
        if extension_owner is not None:
            self.extension_owner = extension_owner

    @property
    def extension_id(self):
        """Gets the extension_id of this ExtensionAllSnake.

        插件id

        :return: The extension_id of this ExtensionAllSnake.
        :rtype: str
        """
        return self._extension_id

    @extension_id.setter
    def extension_id(self, extension_id):
        """Sets the extension_id of this ExtensionAllSnake.

        插件id

        :param extension_id: The extension_id of this ExtensionAllSnake.
        :type extension_id: str
        """
        self._extension_id = extension_id

    @property
    def extension_name(self):
        """Gets the extension_name of this ExtensionAllSnake.

        插件名称

        :return: The extension_name of this ExtensionAllSnake.
        :rtype: str
        """
        return self._extension_name

    @extension_name.setter
    def extension_name(self, extension_name):
        """Sets the extension_name of this ExtensionAllSnake.

        插件名称

        :param extension_name: The extension_name of this ExtensionAllSnake.
        :type extension_name: str
        """
        self._extension_name = extension_name

    @property
    def display_name(self):
        """Gets the display_name of this ExtensionAllSnake.

        插件显示名称

        :return: The display_name of this ExtensionAllSnake.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ExtensionAllSnake.

        插件显示名称

        :param display_name: The display_name of this ExtensionAllSnake.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def flags(self):
        """Gets the flags of this ExtensionAllSnake.

        插件flag;通过传递flag参数来进行过滤或其他操作。flag的基础数字是2\\4\\8\\16;传递的参数只能是这四个数字加法组合而成的数字 利用它们之间二进制的运算获取的值进行其他操作.比如6=0110=0010+0100也就是2和4的集合flags

        :return: The flags of this ExtensionAllSnake.
        :rtype: int
        """
        return self._flags

    @flags.setter
    def flags(self, flags):
        """Sets the flags of this ExtensionAllSnake.

        插件flag;通过传递flag参数来进行过滤或其他操作。flag的基础数字是2\\4\\8\\16;传递的参数只能是这四个数字加法组合而成的数字 利用它们之间二进制的运算获取的值进行其他操作.比如6=0110=0010+0100也就是2和4的集合flags

        :param flags: The flags of this ExtensionAllSnake.
        :type flags: int
        """
        self._flags = flags

    @property
    def last_updated(self):
        """Gets the last_updated of this ExtensionAllSnake.

        更新时间

        :return: The last_updated of this ExtensionAllSnake.
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this ExtensionAllSnake.

        更新时间

        :param last_updated: The last_updated of this ExtensionAllSnake.
        :type last_updated: datetime
        """
        self._last_updated = last_updated

    @property
    def published_date(self):
        """Gets the published_date of this ExtensionAllSnake.

        上传时间

        :return: The published_date of this ExtensionAllSnake.
        :rtype: datetime
        """
        return self._published_date

    @published_date.setter
    def published_date(self, published_date):
        """Sets the published_date of this ExtensionAllSnake.

        上传时间

        :param published_date: The published_date of this ExtensionAllSnake.
        :type published_date: datetime
        """
        self._published_date = published_date

    @property
    def release_date(self):
        """Gets the release_date of this ExtensionAllSnake.

        发布时间

        :return: The release_date of this ExtensionAllSnake.
        :rtype: datetime
        """
        return self._release_date

    @release_date.setter
    def release_date(self, release_date):
        """Sets the release_date of this ExtensionAllSnake.

        发布时间

        :param release_date: The release_date of this ExtensionAllSnake.
        :type release_date: datetime
        """
        self._release_date = release_date

    @property
    def short_description(self):
        """Gets the short_description of this ExtensionAllSnake.

        插件描述

        :return: The short_description of this ExtensionAllSnake.
        :rtype: str
        """
        return self._short_description

    @short_description.setter
    def short_description(self, short_description):
        """Sets the short_description of this ExtensionAllSnake.

        插件描述

        :param short_description: The short_description of this ExtensionAllSnake.
        :type short_description: str
        """
        self._short_description = short_description

    @property
    def tags(self):
        """Gets the tags of this ExtensionAllSnake.

        插件标签

        :return: The tags of this ExtensionAllSnake.
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ExtensionAllSnake.

        插件标签

        :param tags: The tags of this ExtensionAllSnake.
        :type tags: list[str]
        """
        self._tags = tags

    @property
    def tag_all_list(self):
        """Gets the tag_all_list of this ExtensionAllSnake.

        所有标签

        :return: The tag_all_list of this ExtensionAllSnake.
        :rtype: list[str]
        """
        return self._tag_all_list

    @tag_all_list.setter
    def tag_all_list(self, tag_all_list):
        """Sets the tag_all_list of this ExtensionAllSnake.

        所有标签

        :param tag_all_list: The tag_all_list of this ExtensionAllSnake.
        :type tag_all_list: list[str]
        """
        self._tag_all_list = tag_all_list

    @property
    def publisher(self):
        """Gets the publisher of this ExtensionAllSnake.

        :return: The publisher of this ExtensionAllSnake.
        :rtype: :class:`huaweicloudsdkcloudide.v2.PublisherSnake`
        """
        return self._publisher

    @publisher.setter
    def publisher(self, publisher):
        """Sets the publisher of this ExtensionAllSnake.

        :param publisher: The publisher of this ExtensionAllSnake.
        :type publisher: :class:`huaweicloudsdkcloudide.v2.PublisherSnake`
        """
        self._publisher = publisher

    @property
    def arch(self):
        """Gets the arch of this ExtensionAllSnake.

        系统架构

        :return: The arch of this ExtensionAllSnake.
        :rtype: list[str]
        """
        return self._arch

    @arch.setter
    def arch(self, arch):
        """Sets the arch of this ExtensionAllSnake.

        系统架构

        :param arch: The arch of this ExtensionAllSnake.
        :type arch: list[str]
        """
        self._arch = arch

    @property
    def target(self):
        """Gets the target of this ExtensionAllSnake.

        安装目标

        :return: The target of this ExtensionAllSnake.
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this ExtensionAllSnake.

        安装目标

        :param target: The target of this ExtensionAllSnake.
        :type target: str
        """
        self._target = target

    @property
    def categories(self):
        """Gets the categories of this ExtensionAllSnake.

        插件分类

        :return: The categories of this ExtensionAllSnake.
        :rtype: list[str]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        """Sets the categories of this ExtensionAllSnake.

        插件分类

        :param categories: The categories of this ExtensionAllSnake.
        :type categories: list[str]
        """
        self._categories = categories

    @property
    def category_all_list(self):
        """Gets the category_all_list of this ExtensionAllSnake.

        全部分类列表

        :return: The category_all_list of this ExtensionAllSnake.
        :rtype: list[str]
        """
        return self._category_all_list

    @category_all_list.setter
    def category_all_list(self, category_all_list):
        """Sets the category_all_list of this ExtensionAllSnake.

        全部分类列表

        :param category_all_list: The category_all_list of this ExtensionAllSnake.
        :type category_all_list: list[str]
        """
        self._category_all_list = category_all_list

    @property
    def publish_manager(self):
        """Gets the publish_manager of this ExtensionAllSnake.

        :return: The publish_manager of this ExtensionAllSnake.
        :rtype: :class:`huaweicloudsdkcloudide.v2.PublisherSnake`
        """
        return self._publish_manager

    @publish_manager.setter
    def publish_manager(self, publish_manager):
        """Sets the publish_manager of this ExtensionAllSnake.

        :param publish_manager: The publish_manager of this ExtensionAllSnake.
        :type publish_manager: :class:`huaweicloudsdkcloudide.v2.PublisherSnake`
        """
        self._publish_manager = publish_manager

    @property
    def status(self):
        """Gets the status of this ExtensionAllSnake.

        插件状态  - INIT 上传插件的第一个版本 - NORMAL 插件有审核通过的版本 - OFFLINE 插件下线 - ABANDONED 上传废弃 - GRAYED 灰度插件

        :return: The status of this ExtensionAllSnake.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ExtensionAllSnake.

        插件状态  - INIT 上传插件的第一个版本 - NORMAL 插件有审核通过的版本 - OFFLINE 插件下线 - ABANDONED 上传废弃 - GRAYED 灰度插件

        :param status: The status of this ExtensionAllSnake.
        :type status: str
        """
        self._status = status

    @property
    def validate_status(self):
        """Gets the validate_status of this ExtensionAllSnake.

        插件审核状态  - NONE 审核结束 - VALIDATING 审核中

        :return: The validate_status of this ExtensionAllSnake.
        :rtype: str
        """
        return self._validate_status

    @validate_status.setter
    def validate_status(self, validate_status):
        """Sets the validate_status of this ExtensionAllSnake.

        插件审核状态  - NONE 审核结束 - VALIDATING 审核中

        :param validate_status: The validate_status of this ExtensionAllSnake.
        :type validate_status: str
        """
        self._validate_status = validate_status

    @property
    def install_count(self):
        """Gets the install_count of this ExtensionAllSnake.

        下载量

        :return: The install_count of this ExtensionAllSnake.
        :rtype: int
        """
        return self._install_count

    @install_count.setter
    def install_count(self, install_count):
        """Sets the install_count of this ExtensionAllSnake.

        下载量

        :param install_count: The install_count of this ExtensionAllSnake.
        :type install_count: int
        """
        self._install_count = install_count

    @property
    def average_star(self):
        """Gets the average_star of this ExtensionAllSnake.

        平均评星值

        :return: The average_star of this ExtensionAllSnake.
        :rtype: float
        """
        return self._average_star

    @average_star.setter
    def average_star(self, average_star):
        """Sets the average_star of this ExtensionAllSnake.

        平均评星值

        :param average_star: The average_star of this ExtensionAllSnake.
        :type average_star: float
        """
        self._average_star = average_star

    @property
    def identifier(self):
        """Gets the identifier of this ExtensionAllSnake.

        插件唯一标识内部插件市场保留

        :return: The identifier of this ExtensionAllSnake.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this ExtensionAllSnake.

        插件唯一标识内部插件市场保留

        :param identifier: The identifier of this ExtensionAllSnake.
        :type identifier: str
        """
        self._identifier = identifier

    @property
    def support_os(self):
        """Gets the support_os of this ExtensionAllSnake.

        插件支持的操作系统

        :return: The support_os of this ExtensionAllSnake.
        :rtype: list[str]
        """
        return self._support_os

    @support_os.setter
    def support_os(self, support_os):
        """Sets the support_os of this ExtensionAllSnake.

        插件支持的操作系统

        :param support_os: The support_os of this ExtensionAllSnake.
        :type support_os: list[str]
        """
        self._support_os = support_os

    @property
    def support_ide(self):
        """Gets the support_ide of this ExtensionAllSnake.

        插件支持的ide

        :return: The support_ide of this ExtensionAllSnake.
        :rtype: int
        """
        return self._support_ide

    @support_ide.setter
    def support_ide(self, support_ide):
        """Sets the support_ide of this ExtensionAllSnake.

        插件支持的ide

        :param support_ide: The support_ide of this ExtensionAllSnake.
        :type support_ide: int
        """
        self._support_ide = support_ide

    @property
    def support_ide_info(self):
        """Gets the support_ide_info of this ExtensionAllSnake.

        插件支持的ide名称

        :return: The support_ide_info of this ExtensionAllSnake.
        :rtype: str
        """
        return self._support_ide_info

    @support_ide_info.setter
    def support_ide_info(self, support_ide_info):
        """Sets the support_ide_info of this ExtensionAllSnake.

        插件支持的ide名称

        :param support_ide_info: The support_ide_info of this ExtensionAllSnake.
        :type support_ide_info: str
        """
        self._support_ide_info = support_ide_info

    @property
    def versions(self):
        """Gets the versions of this ExtensionAllSnake.

        插件版本集合

        :return: The versions of this ExtensionAllSnake.
        :rtype: list[:class:`huaweicloudsdkcloudide.v2.ExtensionVersionSnake`]
        """
        return self._versions

    @versions.setter
    def versions(self, versions):
        """Sets the versions of this ExtensionAllSnake.

        插件版本集合

        :param versions: The versions of this ExtensionAllSnake.
        :type versions: list[:class:`huaweicloudsdkcloudide.v2.ExtensionVersionSnake`]
        """
        self._versions = versions

    @property
    def validate_result(self):
        """Gets the validate_result of this ExtensionAllSnake.

        插件审核结果

        :return: The validate_result of this ExtensionAllSnake.
        :rtype: str
        """
        return self._validate_result

    @validate_result.setter
    def validate_result(self, validate_result):
        """Sets the validate_result of this ExtensionAllSnake.

        插件审核结果

        :param validate_result: The validate_result of this ExtensionAllSnake.
        :type validate_result: str
        """
        self._validate_result = validate_result

    @property
    def extension_statistics(self):
        """Gets the extension_statistics of this ExtensionAllSnake.

        :return: The extension_statistics of this ExtensionAllSnake.
        :rtype: :class:`huaweicloudsdkcloudide.v2.ExtensionStatistics`
        """
        return self._extension_statistics

    @extension_statistics.setter
    def extension_statistics(self, extension_statistics):
        """Sets the extension_statistics of this ExtensionAllSnake.

        :param extension_statistics: The extension_statistics of this ExtensionAllSnake.
        :type extension_statistics: :class:`huaweicloudsdkcloudide.v2.ExtensionStatistics`
        """
        self._extension_statistics = extension_statistics

    @property
    def preview(self):
        """Gets the preview of this ExtensionAllSnake.

        是否支持预览

        :return: The preview of this ExtensionAllSnake.
        :rtype: bool
        """
        return self._preview

    @preview.setter
    def preview(self, preview):
        """Sets the preview of this ExtensionAllSnake.

        是否支持预览

        :param preview: The preview of this ExtensionAllSnake.
        :type preview: bool
        """
        self._preview = preview

    @property
    def ext_info(self):
        """Gets the ext_info of this ExtensionAllSnake.

        :return: The ext_info of this ExtensionAllSnake.
        :rtype: :class:`huaweicloudsdkcloudide.v2.ExtensionExternalInfo`
        """
        return self._ext_info

    @ext_info.setter
    def ext_info(self, ext_info):
        """Sets the ext_info of this ExtensionAllSnake.

        :param ext_info: The ext_info of this ExtensionAllSnake.
        :type ext_info: :class:`huaweicloudsdkcloudide.v2.ExtensionExternalInfo`
        """
        self._ext_info = ext_info

    @property
    def platform(self):
        """Gets the platform of this ExtensionAllSnake.

        安装目标

        :return: The platform of this ExtensionAllSnake.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this ExtensionAllSnake.

        安装目标

        :param platform: The platform of this ExtensionAllSnake.
        :type platform: str
        """
        self._platform = platform

    @property
    def check_result(self):
        """Gets the check_result of this ExtensionAllSnake.

        :return: The check_result of this ExtensionAllSnake.
        :rtype: :class:`huaweicloudsdkcloudide.v2.CheckResult`
        """
        return self._check_result

    @check_result.setter
    def check_result(self, check_result):
        """Sets the check_result of this ExtensionAllSnake.

        :param check_result: The check_result of this ExtensionAllSnake.
        :type check_result: :class:`huaweicloudsdkcloudide.v2.CheckResult`
        """
        self._check_result = check_result

    @property
    def gray_version_count(self):
        """Gets the gray_version_count of this ExtensionAllSnake.

        灰度版本数量

        :return: The gray_version_count of this ExtensionAllSnake.
        :rtype: int
        """
        return self._gray_version_count

    @gray_version_count.setter
    def gray_version_count(self, gray_version_count):
        """Sets the gray_version_count of this ExtensionAllSnake.

        灰度版本数量

        :param gray_version_count: The gray_version_count of this ExtensionAllSnake.
        :type gray_version_count: int
        """
        self._gray_version_count = gray_version_count

    @property
    def extension_owner(self):
        """Gets the extension_owner of this ExtensionAllSnake.

        插件作者

        :return: The extension_owner of this ExtensionAllSnake.
        :rtype: str
        """
        return self._extension_owner

    @extension_owner.setter
    def extension_owner(self, extension_owner):
        """Sets the extension_owner of this ExtensionAllSnake.

        插件作者

        :param extension_owner: The extension_owner of this ExtensionAllSnake.
        :type extension_owner: str
        """
        self._extension_owner = extension_owner

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
        if not isinstance(other, ExtensionAllSnake):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
