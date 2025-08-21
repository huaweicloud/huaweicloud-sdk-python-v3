# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateBranchResponse(SdkResponse):

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
        'default': 'bool',
        'can_delete': 'bool',
        'can_read': 'bool',
        'can_download': 'bool',
        'can_push': 'bool',
        'commit': 'CommitDto',
        'merged': 'bool',
        'protected': 'bool',
        'created_at': 'str',
        'creator': 'UserBasicDto',
        'description': 'str',
        'create_source': 'str',
        'create_source_exists': 'bool',
        'latest_pipeline': 'PipelineBasicDto',
        'opened_mr_count': 'int',
        'diverging_commit_counts': 'DivergingCommitCounts'
    }

    attribute_map = {
        'name': 'name',
        'default': 'default',
        'can_delete': 'can_delete',
        'can_read': 'can_read',
        'can_download': 'can_download',
        'can_push': 'can_push',
        'commit': 'commit',
        'merged': 'merged',
        'protected': 'protected',
        'created_at': 'created_at',
        'creator': 'creator',
        'description': 'description',
        'create_source': 'create_source',
        'create_source_exists': 'create_source_exists',
        'latest_pipeline': 'latest_pipeline',
        'opened_mr_count': 'opened_mr_count',
        'diverging_commit_counts': 'diverging_commit_counts'
    }

    def __init__(self, name=None, default=None, can_delete=None, can_read=None, can_download=None, can_push=None, commit=None, merged=None, protected=None, created_at=None, creator=None, description=None, create_source=None, create_source_exists=None, latest_pipeline=None, opened_mr_count=None, diverging_commit_counts=None):
        r"""CreateBranchResponse

        The model defined in huaweicloud sdk

        :param name: 分支名称
        :type name: str
        :param default: 是否为默认分支
        :type default: bool
        :param can_delete: 用户是否为默认分支
        :type can_delete: bool
        :param can_read: 是否为默认分支
        :type can_read: bool
        :param can_download: 是否为默认分支
        :type can_download: bool
        :param can_push: 是否为默认分支
        :type can_push: bool
        :param commit: 
        :type commit: :class:`huaweicloudsdkcodehub.v4.CommitDto`
        :param merged: 所有提交是否合入到默认分支
        :type merged: bool
        :param protected: 是否为保护分支
        :type protected: bool
        :param created_at: 创建时间
        :type created_at: str
        :param creator: 
        :type creator: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        :param description: 分支描述
        :type description: str
        :param create_source: 基于分支
        :type create_source: str
        :param create_source_exists: 基于分支是否存在
        :type create_source_exists: bool
        :param latest_pipeline: 
        :type latest_pipeline: :class:`huaweicloudsdkcodehub.v4.PipelineBasicDto`
        :param opened_mr_count: 该分支正在开启的合并请求个数
        :type opened_mr_count: int
        :param diverging_commit_counts: 
        :type diverging_commit_counts: :class:`huaweicloudsdkcodehub.v4.DivergingCommitCounts`
        """
        
        super(CreateBranchResponse, self).__init__()

        self._name = None
        self._default = None
        self._can_delete = None
        self._can_read = None
        self._can_download = None
        self._can_push = None
        self._commit = None
        self._merged = None
        self._protected = None
        self._created_at = None
        self._creator = None
        self._description = None
        self._create_source = None
        self._create_source_exists = None
        self._latest_pipeline = None
        self._opened_mr_count = None
        self._diverging_commit_counts = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if default is not None:
            self.default = default
        if can_delete is not None:
            self.can_delete = can_delete
        if can_read is not None:
            self.can_read = can_read
        if can_download is not None:
            self.can_download = can_download
        if can_push is not None:
            self.can_push = can_push
        if commit is not None:
            self.commit = commit
        if merged is not None:
            self.merged = merged
        if protected is not None:
            self.protected = protected
        if created_at is not None:
            self.created_at = created_at
        if creator is not None:
            self.creator = creator
        if description is not None:
            self.description = description
        if create_source is not None:
            self.create_source = create_source
        if create_source_exists is not None:
            self.create_source_exists = create_source_exists
        if latest_pipeline is not None:
            self.latest_pipeline = latest_pipeline
        if opened_mr_count is not None:
            self.opened_mr_count = opened_mr_count
        if diverging_commit_counts is not None:
            self.diverging_commit_counts = diverging_commit_counts

    @property
    def name(self):
        r"""Gets the name of this CreateBranchResponse.

        分支名称

        :return: The name of this CreateBranchResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateBranchResponse.

        分支名称

        :param name: The name of this CreateBranchResponse.
        :type name: str
        """
        self._name = name

    @property
    def default(self):
        r"""Gets the default of this CreateBranchResponse.

        是否为默认分支

        :return: The default of this CreateBranchResponse.
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        r"""Sets the default of this CreateBranchResponse.

        是否为默认分支

        :param default: The default of this CreateBranchResponse.
        :type default: bool
        """
        self._default = default

    @property
    def can_delete(self):
        r"""Gets the can_delete of this CreateBranchResponse.

        用户是否为默认分支

        :return: The can_delete of this CreateBranchResponse.
        :rtype: bool
        """
        return self._can_delete

    @can_delete.setter
    def can_delete(self, can_delete):
        r"""Sets the can_delete of this CreateBranchResponse.

        用户是否为默认分支

        :param can_delete: The can_delete of this CreateBranchResponse.
        :type can_delete: bool
        """
        self._can_delete = can_delete

    @property
    def can_read(self):
        r"""Gets the can_read of this CreateBranchResponse.

        是否为默认分支

        :return: The can_read of this CreateBranchResponse.
        :rtype: bool
        """
        return self._can_read

    @can_read.setter
    def can_read(self, can_read):
        r"""Sets the can_read of this CreateBranchResponse.

        是否为默认分支

        :param can_read: The can_read of this CreateBranchResponse.
        :type can_read: bool
        """
        self._can_read = can_read

    @property
    def can_download(self):
        r"""Gets the can_download of this CreateBranchResponse.

        是否为默认分支

        :return: The can_download of this CreateBranchResponse.
        :rtype: bool
        """
        return self._can_download

    @can_download.setter
    def can_download(self, can_download):
        r"""Sets the can_download of this CreateBranchResponse.

        是否为默认分支

        :param can_download: The can_download of this CreateBranchResponse.
        :type can_download: bool
        """
        self._can_download = can_download

    @property
    def can_push(self):
        r"""Gets the can_push of this CreateBranchResponse.

        是否为默认分支

        :return: The can_push of this CreateBranchResponse.
        :rtype: bool
        """
        return self._can_push

    @can_push.setter
    def can_push(self, can_push):
        r"""Sets the can_push of this CreateBranchResponse.

        是否为默认分支

        :param can_push: The can_push of this CreateBranchResponse.
        :type can_push: bool
        """
        self._can_push = can_push

    @property
    def commit(self):
        r"""Gets the commit of this CreateBranchResponse.

        :return: The commit of this CreateBranchResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.CommitDto`
        """
        return self._commit

    @commit.setter
    def commit(self, commit):
        r"""Sets the commit of this CreateBranchResponse.

        :param commit: The commit of this CreateBranchResponse.
        :type commit: :class:`huaweicloudsdkcodehub.v4.CommitDto`
        """
        self._commit = commit

    @property
    def merged(self):
        r"""Gets the merged of this CreateBranchResponse.

        所有提交是否合入到默认分支

        :return: The merged of this CreateBranchResponse.
        :rtype: bool
        """
        return self._merged

    @merged.setter
    def merged(self, merged):
        r"""Sets the merged of this CreateBranchResponse.

        所有提交是否合入到默认分支

        :param merged: The merged of this CreateBranchResponse.
        :type merged: bool
        """
        self._merged = merged

    @property
    def protected(self):
        r"""Gets the protected of this CreateBranchResponse.

        是否为保护分支

        :return: The protected of this CreateBranchResponse.
        :rtype: bool
        """
        return self._protected

    @protected.setter
    def protected(self, protected):
        r"""Sets the protected of this CreateBranchResponse.

        是否为保护分支

        :param protected: The protected of this CreateBranchResponse.
        :type protected: bool
        """
        self._protected = protected

    @property
    def created_at(self):
        r"""Gets the created_at of this CreateBranchResponse.

        创建时间

        :return: The created_at of this CreateBranchResponse.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CreateBranchResponse.

        创建时间

        :param created_at: The created_at of this CreateBranchResponse.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def creator(self):
        r"""Gets the creator of this CreateBranchResponse.

        :return: The creator of this CreateBranchResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this CreateBranchResponse.

        :param creator: The creator of this CreateBranchResponse.
        :type creator: :class:`huaweicloudsdkcodehub.v4.UserBasicDto`
        """
        self._creator = creator

    @property
    def description(self):
        r"""Gets the description of this CreateBranchResponse.

        分支描述

        :return: The description of this CreateBranchResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateBranchResponse.

        分支描述

        :param description: The description of this CreateBranchResponse.
        :type description: str
        """
        self._description = description

    @property
    def create_source(self):
        r"""Gets the create_source of this CreateBranchResponse.

        基于分支

        :return: The create_source of this CreateBranchResponse.
        :rtype: str
        """
        return self._create_source

    @create_source.setter
    def create_source(self, create_source):
        r"""Sets the create_source of this CreateBranchResponse.

        基于分支

        :param create_source: The create_source of this CreateBranchResponse.
        :type create_source: str
        """
        self._create_source = create_source

    @property
    def create_source_exists(self):
        r"""Gets the create_source_exists of this CreateBranchResponse.

        基于分支是否存在

        :return: The create_source_exists of this CreateBranchResponse.
        :rtype: bool
        """
        return self._create_source_exists

    @create_source_exists.setter
    def create_source_exists(self, create_source_exists):
        r"""Sets the create_source_exists of this CreateBranchResponse.

        基于分支是否存在

        :param create_source_exists: The create_source_exists of this CreateBranchResponse.
        :type create_source_exists: bool
        """
        self._create_source_exists = create_source_exists

    @property
    def latest_pipeline(self):
        r"""Gets the latest_pipeline of this CreateBranchResponse.

        :return: The latest_pipeline of this CreateBranchResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.PipelineBasicDto`
        """
        return self._latest_pipeline

    @latest_pipeline.setter
    def latest_pipeline(self, latest_pipeline):
        r"""Sets the latest_pipeline of this CreateBranchResponse.

        :param latest_pipeline: The latest_pipeline of this CreateBranchResponse.
        :type latest_pipeline: :class:`huaweicloudsdkcodehub.v4.PipelineBasicDto`
        """
        self._latest_pipeline = latest_pipeline

    @property
    def opened_mr_count(self):
        r"""Gets the opened_mr_count of this CreateBranchResponse.

        该分支正在开启的合并请求个数

        :return: The opened_mr_count of this CreateBranchResponse.
        :rtype: int
        """
        return self._opened_mr_count

    @opened_mr_count.setter
    def opened_mr_count(self, opened_mr_count):
        r"""Sets the opened_mr_count of this CreateBranchResponse.

        该分支正在开启的合并请求个数

        :param opened_mr_count: The opened_mr_count of this CreateBranchResponse.
        :type opened_mr_count: int
        """
        self._opened_mr_count = opened_mr_count

    @property
    def diverging_commit_counts(self):
        r"""Gets the diverging_commit_counts of this CreateBranchResponse.

        :return: The diverging_commit_counts of this CreateBranchResponse.
        :rtype: :class:`huaweicloudsdkcodehub.v4.DivergingCommitCounts`
        """
        return self._diverging_commit_counts

    @diverging_commit_counts.setter
    def diverging_commit_counts(self, diverging_commit_counts):
        r"""Sets the diverging_commit_counts of this CreateBranchResponse.

        :param diverging_commit_counts: The diverging_commit_counts of this CreateBranchResponse.
        :type diverging_commit_counts: :class:`huaweicloudsdkcodehub.v4.DivergingCommitCounts`
        """
        self._diverging_commit_counts = diverging_commit_counts

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
        if not isinstance(other, CreateBranchResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
