# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExtensionVersionSnake:

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
        'version': 'str',
        'version_ranking': 'int',
        'status': 'str',
        'version_status': 'str',
        'asset_uri': 'str',
        'last_updated': 'datetime',
        'files': 'list[ExtensionFileSnake]',
        'validate_message': 'str',
        'version_validate_status': 'str',
        'display_name': 'str',
        'description': 'str',
        'min_ide_version': 'str',
        'max_ide_version': 'str',
        'version_date': 'datetime',
        'preview': 'bool',
        'extension_pack': 'str',
        'extension_dependencies': 'str',
        'created_at': 'datetime',
        'support_ide': 'int',
        'repo_url': 'str',
        'help_page': 'str',
        'website': 'str',
        'issue_link': 'str',
        'asset_size': 'int',
        'depends': 'list[str]',
        'property_list': 'list[CloudIDEExtensionVersionProperty]',
        'uploader': 'str',
        'extension_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'version': 'version',
        'version_ranking': 'version_ranking',
        'status': 'status',
        'version_status': 'version_status',
        'asset_uri': 'asset_uri',
        'last_updated': 'last_updated',
        'files': 'files',
        'validate_message': 'validate_message',
        'version_validate_status': 'version_validate_status',
        'display_name': 'display_name',
        'description': 'description',
        'min_ide_version': 'min_ide_version',
        'max_ide_version': 'max_ide_version',
        'version_date': 'version_date',
        'preview': 'preview',
        'extension_pack': 'extension_pack',
        'extension_dependencies': 'extension_dependencies',
        'created_at': 'created_at',
        'support_ide': 'support_ide',
        'repo_url': 'repo_url',
        'help_page': 'help_page',
        'website': 'website',
        'issue_link': 'issue_link',
        'asset_size': 'asset_size',
        'depends': 'depends',
        'property_list': 'property_list',
        'uploader': 'uploader',
        'extension_id': 'extension_id'
    }

    def __init__(self, id=None, version=None, version_ranking=None, status=None, version_status=None, asset_uri=None, last_updated=None, files=None, validate_message=None, version_validate_status=None, display_name=None, description=None, min_ide_version=None, max_ide_version=None, version_date=None, preview=None, extension_pack=None, extension_dependencies=None, created_at=None, support_ide=None, repo_url=None, help_page=None, website=None, issue_link=None, asset_size=None, depends=None, property_list=None, uploader=None, extension_id=None):
        """ExtensionVersionSnake

        The model defined in huaweicloud sdk

        :param id: 插件版本id
        :type id: str
        :param version: 插件版本号
        :type version: str
        :param version_ranking: 版本排序
        :type version_ranking: int
        :param status: 插件版本状态 - INIT 待发布 - VALIDATING 审核中 - REJECTED 审核拒绝 - PUBLISHED 插件上架 - OFFLINE 插件下线 - ABANDONED 废弃 - GRAY_INIT 灰度审核 - GRAYED 灰度发布 - GRAY_REJECTED 灰度拒绝
        :type status: str
        :param version_status: 插件状态 - INIT 待发布 - VALIDATING 审核中 - REJECTED 审核拒绝 - PUBLISHED 插件上架 - OFFLINE 插件下线 - ABANDONED 废弃 - GRAY_INIT 灰度审核 - GRAYED 灰度发布 - GRAY_REJECTED 灰度拒绝
        :type version_status: str
        :param asset_uri: 资源文件url
        :type asset_uri: str
        :param last_updated: 更新时间
        :type last_updated: datetime
        :param files: 插件文件集合
        :type files: list[:class:`huaweicloudsdkcloudide.v2.ExtensionFileSnake`]
        :param validate_message: 插件审核信息
        :type validate_message: str
        :param version_validate_status: 插件审核状态 - NONE 无 - UPLOADING 上传中 - VALIDATING 系统审核 - OFFLINING 用户申请下线 - ONLINING 用户申请上线 - UMS_VALIDATING 发布商审核中
        :type version_validate_status: str
        :param display_name: 插件展示名称
        :type display_name: str
        :param description: 插件描述
        :type description: str
        :param min_ide_version: 插件支持ide版本
        :type min_ide_version: str
        :param max_ide_version: 支持的最大版本
        :type max_ide_version: str
        :param version_date: 发布时间
        :type version_date: datetime
        :param preview: 是否预览
        :type preview: bool
        :param extension_pack: 包含插件列表
        :type extension_pack: str
        :param extension_dependencies: 依赖插件列表
        :type extension_dependencies: str
        :param created_at: 创建时间
        :type created_at: datetime
        :param support_ide: 支持的ide编码
        :type support_ide: int
        :param repo_url: 插件包源码仓
        :type repo_url: str
        :param help_page: 帮助页面
        :type help_page: str
        :param website: 产品首页
        :type website: str
        :param issue_link: 问题链接
        :type issue_link: str
        :param asset_size: 插件大小
        :type asset_size: int
        :param depends: 依赖插件
        :type depends: list[str]
        :param property_list: cloudide插件版本参数
        :type property_list: list[:class:`huaweicloudsdkcloudide.v2.CloudIDEExtensionVersionProperty`]
        :param uploader: 版本发布者
        :type uploader: str
        :param extension_id: 插件id
        :type extension_id: str
        """
        
        

        self._id = None
        self._version = None
        self._version_ranking = None
        self._status = None
        self._version_status = None
        self._asset_uri = None
        self._last_updated = None
        self._files = None
        self._validate_message = None
        self._version_validate_status = None
        self._display_name = None
        self._description = None
        self._min_ide_version = None
        self._max_ide_version = None
        self._version_date = None
        self._preview = None
        self._extension_pack = None
        self._extension_dependencies = None
        self._created_at = None
        self._support_ide = None
        self._repo_url = None
        self._help_page = None
        self._website = None
        self._issue_link = None
        self._asset_size = None
        self._depends = None
        self._property_list = None
        self._uploader = None
        self._extension_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if version is not None:
            self.version = version
        if version_ranking is not None:
            self.version_ranking = version_ranking
        if status is not None:
            self.status = status
        if version_status is not None:
            self.version_status = version_status
        if asset_uri is not None:
            self.asset_uri = asset_uri
        if last_updated is not None:
            self.last_updated = last_updated
        if files is not None:
            self.files = files
        if validate_message is not None:
            self.validate_message = validate_message
        if version_validate_status is not None:
            self.version_validate_status = version_validate_status
        if display_name is not None:
            self.display_name = display_name
        if description is not None:
            self.description = description
        if min_ide_version is not None:
            self.min_ide_version = min_ide_version
        if max_ide_version is not None:
            self.max_ide_version = max_ide_version
        if version_date is not None:
            self.version_date = version_date
        if preview is not None:
            self.preview = preview
        if extension_pack is not None:
            self.extension_pack = extension_pack
        if extension_dependencies is not None:
            self.extension_dependencies = extension_dependencies
        if created_at is not None:
            self.created_at = created_at
        if support_ide is not None:
            self.support_ide = support_ide
        if repo_url is not None:
            self.repo_url = repo_url
        if help_page is not None:
            self.help_page = help_page
        if website is not None:
            self.website = website
        if issue_link is not None:
            self.issue_link = issue_link
        if asset_size is not None:
            self.asset_size = asset_size
        if depends is not None:
            self.depends = depends
        if property_list is not None:
            self.property_list = property_list
        if uploader is not None:
            self.uploader = uploader
        if extension_id is not None:
            self.extension_id = extension_id

    @property
    def id(self):
        """Gets the id of this ExtensionVersionSnake.

        插件版本id

        :return: The id of this ExtensionVersionSnake.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ExtensionVersionSnake.

        插件版本id

        :param id: The id of this ExtensionVersionSnake.
        :type id: str
        """
        self._id = id

    @property
    def version(self):
        """Gets the version of this ExtensionVersionSnake.

        插件版本号

        :return: The version of this ExtensionVersionSnake.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ExtensionVersionSnake.

        插件版本号

        :param version: The version of this ExtensionVersionSnake.
        :type version: str
        """
        self._version = version

    @property
    def version_ranking(self):
        """Gets the version_ranking of this ExtensionVersionSnake.

        版本排序

        :return: The version_ranking of this ExtensionVersionSnake.
        :rtype: int
        """
        return self._version_ranking

    @version_ranking.setter
    def version_ranking(self, version_ranking):
        """Sets the version_ranking of this ExtensionVersionSnake.

        版本排序

        :param version_ranking: The version_ranking of this ExtensionVersionSnake.
        :type version_ranking: int
        """
        self._version_ranking = version_ranking

    @property
    def status(self):
        """Gets the status of this ExtensionVersionSnake.

        插件版本状态 - INIT 待发布 - VALIDATING 审核中 - REJECTED 审核拒绝 - PUBLISHED 插件上架 - OFFLINE 插件下线 - ABANDONED 废弃 - GRAY_INIT 灰度审核 - GRAYED 灰度发布 - GRAY_REJECTED 灰度拒绝

        :return: The status of this ExtensionVersionSnake.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ExtensionVersionSnake.

        插件版本状态 - INIT 待发布 - VALIDATING 审核中 - REJECTED 审核拒绝 - PUBLISHED 插件上架 - OFFLINE 插件下线 - ABANDONED 废弃 - GRAY_INIT 灰度审核 - GRAYED 灰度发布 - GRAY_REJECTED 灰度拒绝

        :param status: The status of this ExtensionVersionSnake.
        :type status: str
        """
        self._status = status

    @property
    def version_status(self):
        """Gets the version_status of this ExtensionVersionSnake.

        插件状态 - INIT 待发布 - VALIDATING 审核中 - REJECTED 审核拒绝 - PUBLISHED 插件上架 - OFFLINE 插件下线 - ABANDONED 废弃 - GRAY_INIT 灰度审核 - GRAYED 灰度发布 - GRAY_REJECTED 灰度拒绝

        :return: The version_status of this ExtensionVersionSnake.
        :rtype: str
        """
        return self._version_status

    @version_status.setter
    def version_status(self, version_status):
        """Sets the version_status of this ExtensionVersionSnake.

        插件状态 - INIT 待发布 - VALIDATING 审核中 - REJECTED 审核拒绝 - PUBLISHED 插件上架 - OFFLINE 插件下线 - ABANDONED 废弃 - GRAY_INIT 灰度审核 - GRAYED 灰度发布 - GRAY_REJECTED 灰度拒绝

        :param version_status: The version_status of this ExtensionVersionSnake.
        :type version_status: str
        """
        self._version_status = version_status

    @property
    def asset_uri(self):
        """Gets the asset_uri of this ExtensionVersionSnake.

        资源文件url

        :return: The asset_uri of this ExtensionVersionSnake.
        :rtype: str
        """
        return self._asset_uri

    @asset_uri.setter
    def asset_uri(self, asset_uri):
        """Sets the asset_uri of this ExtensionVersionSnake.

        资源文件url

        :param asset_uri: The asset_uri of this ExtensionVersionSnake.
        :type asset_uri: str
        """
        self._asset_uri = asset_uri

    @property
    def last_updated(self):
        """Gets the last_updated of this ExtensionVersionSnake.

        更新时间

        :return: The last_updated of this ExtensionVersionSnake.
        :rtype: datetime
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this ExtensionVersionSnake.

        更新时间

        :param last_updated: The last_updated of this ExtensionVersionSnake.
        :type last_updated: datetime
        """
        self._last_updated = last_updated

    @property
    def files(self):
        """Gets the files of this ExtensionVersionSnake.

        插件文件集合

        :return: The files of this ExtensionVersionSnake.
        :rtype: list[:class:`huaweicloudsdkcloudide.v2.ExtensionFileSnake`]
        """
        return self._files

    @files.setter
    def files(self, files):
        """Sets the files of this ExtensionVersionSnake.

        插件文件集合

        :param files: The files of this ExtensionVersionSnake.
        :type files: list[:class:`huaweicloudsdkcloudide.v2.ExtensionFileSnake`]
        """
        self._files = files

    @property
    def validate_message(self):
        """Gets the validate_message of this ExtensionVersionSnake.

        插件审核信息

        :return: The validate_message of this ExtensionVersionSnake.
        :rtype: str
        """
        return self._validate_message

    @validate_message.setter
    def validate_message(self, validate_message):
        """Sets the validate_message of this ExtensionVersionSnake.

        插件审核信息

        :param validate_message: The validate_message of this ExtensionVersionSnake.
        :type validate_message: str
        """
        self._validate_message = validate_message

    @property
    def version_validate_status(self):
        """Gets the version_validate_status of this ExtensionVersionSnake.

        插件审核状态 - NONE 无 - UPLOADING 上传中 - VALIDATING 系统审核 - OFFLINING 用户申请下线 - ONLINING 用户申请上线 - UMS_VALIDATING 发布商审核中

        :return: The version_validate_status of this ExtensionVersionSnake.
        :rtype: str
        """
        return self._version_validate_status

    @version_validate_status.setter
    def version_validate_status(self, version_validate_status):
        """Sets the version_validate_status of this ExtensionVersionSnake.

        插件审核状态 - NONE 无 - UPLOADING 上传中 - VALIDATING 系统审核 - OFFLINING 用户申请下线 - ONLINING 用户申请上线 - UMS_VALIDATING 发布商审核中

        :param version_validate_status: The version_validate_status of this ExtensionVersionSnake.
        :type version_validate_status: str
        """
        self._version_validate_status = version_validate_status

    @property
    def display_name(self):
        """Gets the display_name of this ExtensionVersionSnake.

        插件展示名称

        :return: The display_name of this ExtensionVersionSnake.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ExtensionVersionSnake.

        插件展示名称

        :param display_name: The display_name of this ExtensionVersionSnake.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """Gets the description of this ExtensionVersionSnake.

        插件描述

        :return: The description of this ExtensionVersionSnake.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ExtensionVersionSnake.

        插件描述

        :param description: The description of this ExtensionVersionSnake.
        :type description: str
        """
        self._description = description

    @property
    def min_ide_version(self):
        """Gets the min_ide_version of this ExtensionVersionSnake.

        插件支持ide版本

        :return: The min_ide_version of this ExtensionVersionSnake.
        :rtype: str
        """
        return self._min_ide_version

    @min_ide_version.setter
    def min_ide_version(self, min_ide_version):
        """Sets the min_ide_version of this ExtensionVersionSnake.

        插件支持ide版本

        :param min_ide_version: The min_ide_version of this ExtensionVersionSnake.
        :type min_ide_version: str
        """
        self._min_ide_version = min_ide_version

    @property
    def max_ide_version(self):
        """Gets the max_ide_version of this ExtensionVersionSnake.

        支持的最大版本

        :return: The max_ide_version of this ExtensionVersionSnake.
        :rtype: str
        """
        return self._max_ide_version

    @max_ide_version.setter
    def max_ide_version(self, max_ide_version):
        """Sets the max_ide_version of this ExtensionVersionSnake.

        支持的最大版本

        :param max_ide_version: The max_ide_version of this ExtensionVersionSnake.
        :type max_ide_version: str
        """
        self._max_ide_version = max_ide_version

    @property
    def version_date(self):
        """Gets the version_date of this ExtensionVersionSnake.

        发布时间

        :return: The version_date of this ExtensionVersionSnake.
        :rtype: datetime
        """
        return self._version_date

    @version_date.setter
    def version_date(self, version_date):
        """Sets the version_date of this ExtensionVersionSnake.

        发布时间

        :param version_date: The version_date of this ExtensionVersionSnake.
        :type version_date: datetime
        """
        self._version_date = version_date

    @property
    def preview(self):
        """Gets the preview of this ExtensionVersionSnake.

        是否预览

        :return: The preview of this ExtensionVersionSnake.
        :rtype: bool
        """
        return self._preview

    @preview.setter
    def preview(self, preview):
        """Sets the preview of this ExtensionVersionSnake.

        是否预览

        :param preview: The preview of this ExtensionVersionSnake.
        :type preview: bool
        """
        self._preview = preview

    @property
    def extension_pack(self):
        """Gets the extension_pack of this ExtensionVersionSnake.

        包含插件列表

        :return: The extension_pack of this ExtensionVersionSnake.
        :rtype: str
        """
        return self._extension_pack

    @extension_pack.setter
    def extension_pack(self, extension_pack):
        """Sets the extension_pack of this ExtensionVersionSnake.

        包含插件列表

        :param extension_pack: The extension_pack of this ExtensionVersionSnake.
        :type extension_pack: str
        """
        self._extension_pack = extension_pack

    @property
    def extension_dependencies(self):
        """Gets the extension_dependencies of this ExtensionVersionSnake.

        依赖插件列表

        :return: The extension_dependencies of this ExtensionVersionSnake.
        :rtype: str
        """
        return self._extension_dependencies

    @extension_dependencies.setter
    def extension_dependencies(self, extension_dependencies):
        """Sets the extension_dependencies of this ExtensionVersionSnake.

        依赖插件列表

        :param extension_dependencies: The extension_dependencies of this ExtensionVersionSnake.
        :type extension_dependencies: str
        """
        self._extension_dependencies = extension_dependencies

    @property
    def created_at(self):
        """Gets the created_at of this ExtensionVersionSnake.

        创建时间

        :return: The created_at of this ExtensionVersionSnake.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ExtensionVersionSnake.

        创建时间

        :param created_at: The created_at of this ExtensionVersionSnake.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def support_ide(self):
        """Gets the support_ide of this ExtensionVersionSnake.

        支持的ide编码

        :return: The support_ide of this ExtensionVersionSnake.
        :rtype: int
        """
        return self._support_ide

    @support_ide.setter
    def support_ide(self, support_ide):
        """Sets the support_ide of this ExtensionVersionSnake.

        支持的ide编码

        :param support_ide: The support_ide of this ExtensionVersionSnake.
        :type support_ide: int
        """
        self._support_ide = support_ide

    @property
    def repo_url(self):
        """Gets the repo_url of this ExtensionVersionSnake.

        插件包源码仓

        :return: The repo_url of this ExtensionVersionSnake.
        :rtype: str
        """
        return self._repo_url

    @repo_url.setter
    def repo_url(self, repo_url):
        """Sets the repo_url of this ExtensionVersionSnake.

        插件包源码仓

        :param repo_url: The repo_url of this ExtensionVersionSnake.
        :type repo_url: str
        """
        self._repo_url = repo_url

    @property
    def help_page(self):
        """Gets the help_page of this ExtensionVersionSnake.

        帮助页面

        :return: The help_page of this ExtensionVersionSnake.
        :rtype: str
        """
        return self._help_page

    @help_page.setter
    def help_page(self, help_page):
        """Sets the help_page of this ExtensionVersionSnake.

        帮助页面

        :param help_page: The help_page of this ExtensionVersionSnake.
        :type help_page: str
        """
        self._help_page = help_page

    @property
    def website(self):
        """Gets the website of this ExtensionVersionSnake.

        产品首页

        :return: The website of this ExtensionVersionSnake.
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this ExtensionVersionSnake.

        产品首页

        :param website: The website of this ExtensionVersionSnake.
        :type website: str
        """
        self._website = website

    @property
    def issue_link(self):
        """Gets the issue_link of this ExtensionVersionSnake.

        问题链接

        :return: The issue_link of this ExtensionVersionSnake.
        :rtype: str
        """
        return self._issue_link

    @issue_link.setter
    def issue_link(self, issue_link):
        """Sets the issue_link of this ExtensionVersionSnake.

        问题链接

        :param issue_link: The issue_link of this ExtensionVersionSnake.
        :type issue_link: str
        """
        self._issue_link = issue_link

    @property
    def asset_size(self):
        """Gets the asset_size of this ExtensionVersionSnake.

        插件大小

        :return: The asset_size of this ExtensionVersionSnake.
        :rtype: int
        """
        return self._asset_size

    @asset_size.setter
    def asset_size(self, asset_size):
        """Sets the asset_size of this ExtensionVersionSnake.

        插件大小

        :param asset_size: The asset_size of this ExtensionVersionSnake.
        :type asset_size: int
        """
        self._asset_size = asset_size

    @property
    def depends(self):
        """Gets the depends of this ExtensionVersionSnake.

        依赖插件

        :return: The depends of this ExtensionVersionSnake.
        :rtype: list[str]
        """
        return self._depends

    @depends.setter
    def depends(self, depends):
        """Sets the depends of this ExtensionVersionSnake.

        依赖插件

        :param depends: The depends of this ExtensionVersionSnake.
        :type depends: list[str]
        """
        self._depends = depends

    @property
    def property_list(self):
        """Gets the property_list of this ExtensionVersionSnake.

        cloudide插件版本参数

        :return: The property_list of this ExtensionVersionSnake.
        :rtype: list[:class:`huaweicloudsdkcloudide.v2.CloudIDEExtensionVersionProperty`]
        """
        return self._property_list

    @property_list.setter
    def property_list(self, property_list):
        """Sets the property_list of this ExtensionVersionSnake.

        cloudide插件版本参数

        :param property_list: The property_list of this ExtensionVersionSnake.
        :type property_list: list[:class:`huaweicloudsdkcloudide.v2.CloudIDEExtensionVersionProperty`]
        """
        self._property_list = property_list

    @property
    def uploader(self):
        """Gets the uploader of this ExtensionVersionSnake.

        版本发布者

        :return: The uploader of this ExtensionVersionSnake.
        :rtype: str
        """
        return self._uploader

    @uploader.setter
    def uploader(self, uploader):
        """Sets the uploader of this ExtensionVersionSnake.

        版本发布者

        :param uploader: The uploader of this ExtensionVersionSnake.
        :type uploader: str
        """
        self._uploader = uploader

    @property
    def extension_id(self):
        """Gets the extension_id of this ExtensionVersionSnake.

        插件id

        :return: The extension_id of this ExtensionVersionSnake.
        :rtype: str
        """
        return self._extension_id

    @extension_id.setter
    def extension_id(self, extension_id):
        """Sets the extension_id of this ExtensionVersionSnake.

        插件id

        :param extension_id: The extension_id of this ExtensionVersionSnake.
        :type extension_id: str
        """
        self._extension_id = extension_id

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
        if not isinstance(other, ExtensionVersionSnake):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
