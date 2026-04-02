# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobParameters:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'delete_untagged': 'bool',
        'workers': 'int',
        'dry_run': 'bool',
        'purged_blobs': 'int',
        'purged_manifests': 'int',
        'freed_space': 'int'
    }

    attribute_map = {
        'delete_untagged': 'delete_untagged',
        'workers': 'workers',
        'dry_run': 'dry_run',
        'purged_blobs': 'purged_blobs',
        'purged_manifests': 'purged_manifests',
        'freed_space': 'freed_space'
    }

    def __init__(self, delete_untagged=None, workers=None, dry_run=None, purged_blobs=None, purged_manifests=None, freed_space=None):
        r"""JobParameters

        The model defined in huaweicloud sdk

        :param delete_untagged: 是否删除无tag的制品；默认为false，不删除无tag的制品。
        :type delete_untagged: bool
        :param workers: 并行执行制品清理任务的工作者数量，最小值为1，最大值为5。
        :type workers: int
        :param dry_run: 是否模拟执行任务；默认值为false，非模拟运行。
        :type dry_run: bool
        :param purged_blobs: 清理镜像层的个数。
        :type purged_blobs: int
        :param purged_manifests: 清理镜像manifest的个数。
        :type purged_manifests: int
        :param freed_space: 释放的镜像存储空间大小(单位为字节)。
        :type freed_space: int
        """
        
        

        self._delete_untagged = None
        self._workers = None
        self._dry_run = None
        self._purged_blobs = None
        self._purged_manifests = None
        self._freed_space = None
        self.discriminator = None

        if delete_untagged is not None:
            self.delete_untagged = delete_untagged
        self.workers = workers
        if dry_run is not None:
            self.dry_run = dry_run
        if purged_blobs is not None:
            self.purged_blobs = purged_blobs
        if purged_manifests is not None:
            self.purged_manifests = purged_manifests
        if freed_space is not None:
            self.freed_space = freed_space

    @property
    def delete_untagged(self):
        r"""Gets the delete_untagged of this JobParameters.

        是否删除无tag的制品；默认为false，不删除无tag的制品。

        :return: The delete_untagged of this JobParameters.
        :rtype: bool
        """
        return self._delete_untagged

    @delete_untagged.setter
    def delete_untagged(self, delete_untagged):
        r"""Sets the delete_untagged of this JobParameters.

        是否删除无tag的制品；默认为false，不删除无tag的制品。

        :param delete_untagged: The delete_untagged of this JobParameters.
        :type delete_untagged: bool
        """
        self._delete_untagged = delete_untagged

    @property
    def workers(self):
        r"""Gets the workers of this JobParameters.

        并行执行制品清理任务的工作者数量，最小值为1，最大值为5。

        :return: The workers of this JobParameters.
        :rtype: int
        """
        return self._workers

    @workers.setter
    def workers(self, workers):
        r"""Sets the workers of this JobParameters.

        并行执行制品清理任务的工作者数量，最小值为1，最大值为5。

        :param workers: The workers of this JobParameters.
        :type workers: int
        """
        self._workers = workers

    @property
    def dry_run(self):
        r"""Gets the dry_run of this JobParameters.

        是否模拟执行任务；默认值为false，非模拟运行。

        :return: The dry_run of this JobParameters.
        :rtype: bool
        """
        return self._dry_run

    @dry_run.setter
    def dry_run(self, dry_run):
        r"""Sets the dry_run of this JobParameters.

        是否模拟执行任务；默认值为false，非模拟运行。

        :param dry_run: The dry_run of this JobParameters.
        :type dry_run: bool
        """
        self._dry_run = dry_run

    @property
    def purged_blobs(self):
        r"""Gets the purged_blobs of this JobParameters.

        清理镜像层的个数。

        :return: The purged_blobs of this JobParameters.
        :rtype: int
        """
        return self._purged_blobs

    @purged_blobs.setter
    def purged_blobs(self, purged_blobs):
        r"""Sets the purged_blobs of this JobParameters.

        清理镜像层的个数。

        :param purged_blobs: The purged_blobs of this JobParameters.
        :type purged_blobs: int
        """
        self._purged_blobs = purged_blobs

    @property
    def purged_manifests(self):
        r"""Gets the purged_manifests of this JobParameters.

        清理镜像manifest的个数。

        :return: The purged_manifests of this JobParameters.
        :rtype: int
        """
        return self._purged_manifests

    @purged_manifests.setter
    def purged_manifests(self, purged_manifests):
        r"""Sets the purged_manifests of this JobParameters.

        清理镜像manifest的个数。

        :param purged_manifests: The purged_manifests of this JobParameters.
        :type purged_manifests: int
        """
        self._purged_manifests = purged_manifests

    @property
    def freed_space(self):
        r"""Gets the freed_space of this JobParameters.

        释放的镜像存储空间大小(单位为字节)。

        :return: The freed_space of this JobParameters.
        :rtype: int
        """
        return self._freed_space

    @freed_space.setter
    def freed_space(self, freed_space):
        r"""Sets the freed_space of this JobParameters.

        释放的镜像存储空间大小(单位为字节)。

        :param freed_space: The freed_space of this JobParameters.
        :type freed_space: int
        """
        self._freed_space = freed_space

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, JobParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
