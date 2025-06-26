# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceStatisticsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'storage_used': 'int',
        'total_namespace_count': 'int',
        'total_image_count': 'int',
        'namespace_quota': 'int',
        'image_repo_quota': 'int',
        'replica_policy_quota': 'int',
        'retention_policy_quota': 'int',
        'notify_policy_quota': 'int',
        'replica_registry_quota': 'int',
        'sign_policy_quota': 'int',
        'replica_policy_count': 'int',
        'retention_policy_count': 'int',
        'notify_policy_count': 'int',
        'replica_registry_count': 'int',
        'intranet_endpoint_quota': 'int',
        'intranet_endpoint_count': 'int',
        'long_term_quota': 'int',
        'sign_policy_count': 'int'
    }

    attribute_map = {
        'storage_used': 'storage_used',
        'total_namespace_count': 'total_namespace_count',
        'total_image_count': 'total_image_count',
        'namespace_quota': 'namespace_quota',
        'image_repo_quota': 'image_repo_quota',
        'replica_policy_quota': 'replica_policy_quota',
        'retention_policy_quota': 'retention_policy_quota',
        'notify_policy_quota': 'notify_policy_quota',
        'replica_registry_quota': 'replica_registry_quota',
        'sign_policy_quota': 'sign_policy_quota',
        'replica_policy_count': 'replica_policy_count',
        'retention_policy_count': 'retention_policy_count',
        'notify_policy_count': 'notify_policy_count',
        'replica_registry_count': 'replica_registry_count',
        'intranet_endpoint_quota': 'intranet_endpoint_quota',
        'intranet_endpoint_count': 'intranet_endpoint_count',
        'long_term_quota': 'long_term_quota',
        'sign_policy_count': 'sign_policy_count'
    }

    def __init__(self, storage_used=None, total_namespace_count=None, total_image_count=None, namespace_quota=None, image_repo_quota=None, replica_policy_quota=None, retention_policy_quota=None, notify_policy_quota=None, replica_registry_quota=None, sign_policy_quota=None, replica_policy_count=None, retention_policy_count=None, notify_policy_count=None, replica_registry_count=None, intranet_endpoint_quota=None, intranet_endpoint_count=None, long_term_quota=None, sign_policy_count=None):
        r"""ListInstanceStatisticsResponse

        The model defined in huaweicloud sdk

        :param storage_used: 已用存储空间
        :type storage_used: int
        :param total_namespace_count: 命名空间的总数
        :type total_namespace_count: int
        :param total_image_count: 镜像的总数
        :type total_image_count: int
        :param namespace_quota: 命名空间的配额
        :type namespace_quota: int
        :param image_repo_quota: 镜像的配额
        :type image_repo_quota: int
        :param replica_policy_quota: 镜像同步策略的配额
        :type replica_policy_quota: int
        :param retention_policy_quota: 镜像老化策略的配额
        :type retention_policy_quota: int
        :param notify_policy_quota: 触发器策略的配额
        :type notify_policy_quota: int
        :param replica_registry_quota: 镜像同步的目标仓库配额
        :type replica_registry_quota: int
        :param sign_policy_quota: 镜像签名策略的配额
        :type sign_policy_quota: int
        :param replica_policy_count: 镜像同步策略总数
        :type replica_policy_count: int
        :param retention_policy_count: 镜像老化策略的总数
        :type retention_policy_count: int
        :param notify_policy_count: 触发器策略的总数
        :type notify_policy_count: int
        :param replica_registry_count: 镜像同步策略的目标仓库总数
        :type replica_registry_count: int
        :param intranet_endpoint_quota: 内网访问控制的配额
        :type intranet_endpoint_quota: int
        :param intranet_endpoint_count: 内网访问控制的总数
        :type intranet_endpoint_count: int
        :param long_term_quota: 长期登录指令的配额
        :type long_term_quota: int
        :param sign_policy_count: 镜像签名策略的总数
        :type sign_policy_count: int
        """
        
        super(ListInstanceStatisticsResponse, self).__init__()

        self._storage_used = None
        self._total_namespace_count = None
        self._total_image_count = None
        self._namespace_quota = None
        self._image_repo_quota = None
        self._replica_policy_quota = None
        self._retention_policy_quota = None
        self._notify_policy_quota = None
        self._replica_registry_quota = None
        self._sign_policy_quota = None
        self._replica_policy_count = None
        self._retention_policy_count = None
        self._notify_policy_count = None
        self._replica_registry_count = None
        self._intranet_endpoint_quota = None
        self._intranet_endpoint_count = None
        self._long_term_quota = None
        self._sign_policy_count = None
        self.discriminator = None

        if storage_used is not None:
            self.storage_used = storage_used
        if total_namespace_count is not None:
            self.total_namespace_count = total_namespace_count
        if total_image_count is not None:
            self.total_image_count = total_image_count
        if namespace_quota is not None:
            self.namespace_quota = namespace_quota
        if image_repo_quota is not None:
            self.image_repo_quota = image_repo_quota
        if replica_policy_quota is not None:
            self.replica_policy_quota = replica_policy_quota
        if retention_policy_quota is not None:
            self.retention_policy_quota = retention_policy_quota
        if notify_policy_quota is not None:
            self.notify_policy_quota = notify_policy_quota
        if replica_registry_quota is not None:
            self.replica_registry_quota = replica_registry_quota
        if sign_policy_quota is not None:
            self.sign_policy_quota = sign_policy_quota
        if replica_policy_count is not None:
            self.replica_policy_count = replica_policy_count
        if retention_policy_count is not None:
            self.retention_policy_count = retention_policy_count
        if notify_policy_count is not None:
            self.notify_policy_count = notify_policy_count
        if replica_registry_count is not None:
            self.replica_registry_count = replica_registry_count
        if intranet_endpoint_quota is not None:
            self.intranet_endpoint_quota = intranet_endpoint_quota
        if intranet_endpoint_count is not None:
            self.intranet_endpoint_count = intranet_endpoint_count
        if long_term_quota is not None:
            self.long_term_quota = long_term_quota
        if sign_policy_count is not None:
            self.sign_policy_count = sign_policy_count

    @property
    def storage_used(self):
        r"""Gets the storage_used of this ListInstanceStatisticsResponse.

        已用存储空间

        :return: The storage_used of this ListInstanceStatisticsResponse.
        :rtype: int
        """
        return self._storage_used

    @storage_used.setter
    def storage_used(self, storage_used):
        r"""Sets the storage_used of this ListInstanceStatisticsResponse.

        已用存储空间

        :param storage_used: The storage_used of this ListInstanceStatisticsResponse.
        :type storage_used: int
        """
        self._storage_used = storage_used

    @property
    def total_namespace_count(self):
        r"""Gets the total_namespace_count of this ListInstanceStatisticsResponse.

        命名空间的总数

        :return: The total_namespace_count of this ListInstanceStatisticsResponse.
        :rtype: int
        """
        return self._total_namespace_count

    @total_namespace_count.setter
    def total_namespace_count(self, total_namespace_count):
        r"""Sets the total_namespace_count of this ListInstanceStatisticsResponse.

        命名空间的总数

        :param total_namespace_count: The total_namespace_count of this ListInstanceStatisticsResponse.
        :type total_namespace_count: int
        """
        self._total_namespace_count = total_namespace_count

    @property
    def total_image_count(self):
        r"""Gets the total_image_count of this ListInstanceStatisticsResponse.

        镜像的总数

        :return: The total_image_count of this ListInstanceStatisticsResponse.
        :rtype: int
        """
        return self._total_image_count

    @total_image_count.setter
    def total_image_count(self, total_image_count):
        r"""Sets the total_image_count of this ListInstanceStatisticsResponse.

        镜像的总数

        :param total_image_count: The total_image_count of this ListInstanceStatisticsResponse.
        :type total_image_count: int
        """
        self._total_image_count = total_image_count

    @property
    def namespace_quota(self):
        r"""Gets the namespace_quota of this ListInstanceStatisticsResponse.

        命名空间的配额

        :return: The namespace_quota of this ListInstanceStatisticsResponse.
        :rtype: int
        """
        return self._namespace_quota

    @namespace_quota.setter
    def namespace_quota(self, namespace_quota):
        r"""Sets the namespace_quota of this ListInstanceStatisticsResponse.

        命名空间的配额

        :param namespace_quota: The namespace_quota of this ListInstanceStatisticsResponse.
        :type namespace_quota: int
        """
        self._namespace_quota = namespace_quota

    @property
    def image_repo_quota(self):
        r"""Gets the image_repo_quota of this ListInstanceStatisticsResponse.

        镜像的配额

        :return: The image_repo_quota of this ListInstanceStatisticsResponse.
        :rtype: int
        """
        return self._image_repo_quota

    @image_repo_quota.setter
    def image_repo_quota(self, image_repo_quota):
        r"""Sets the image_repo_quota of this ListInstanceStatisticsResponse.

        镜像的配额

        :param image_repo_quota: The image_repo_quota of this ListInstanceStatisticsResponse.
        :type image_repo_quota: int
        """
        self._image_repo_quota = image_repo_quota

    @property
    def replica_policy_quota(self):
        r"""Gets the replica_policy_quota of this ListInstanceStatisticsResponse.

        镜像同步策略的配额

        :return: The replica_policy_quota of this ListInstanceStatisticsResponse.
        :rtype: int
        """
        return self._replica_policy_quota

    @replica_policy_quota.setter
    def replica_policy_quota(self, replica_policy_quota):
        r"""Sets the replica_policy_quota of this ListInstanceStatisticsResponse.

        镜像同步策略的配额

        :param replica_policy_quota: The replica_policy_quota of this ListInstanceStatisticsResponse.
        :type replica_policy_quota: int
        """
        self._replica_policy_quota = replica_policy_quota

    @property
    def retention_policy_quota(self):
        r"""Gets the retention_policy_quota of this ListInstanceStatisticsResponse.

        镜像老化策略的配额

        :return: The retention_policy_quota of this ListInstanceStatisticsResponse.
        :rtype: int
        """
        return self._retention_policy_quota

    @retention_policy_quota.setter
    def retention_policy_quota(self, retention_policy_quota):
        r"""Sets the retention_policy_quota of this ListInstanceStatisticsResponse.

        镜像老化策略的配额

        :param retention_policy_quota: The retention_policy_quota of this ListInstanceStatisticsResponse.
        :type retention_policy_quota: int
        """
        self._retention_policy_quota = retention_policy_quota

    @property
    def notify_policy_quota(self):
        r"""Gets the notify_policy_quota of this ListInstanceStatisticsResponse.

        触发器策略的配额

        :return: The notify_policy_quota of this ListInstanceStatisticsResponse.
        :rtype: int
        """
        return self._notify_policy_quota

    @notify_policy_quota.setter
    def notify_policy_quota(self, notify_policy_quota):
        r"""Sets the notify_policy_quota of this ListInstanceStatisticsResponse.

        触发器策略的配额

        :param notify_policy_quota: The notify_policy_quota of this ListInstanceStatisticsResponse.
        :type notify_policy_quota: int
        """
        self._notify_policy_quota = notify_policy_quota

    @property
    def replica_registry_quota(self):
        r"""Gets the replica_registry_quota of this ListInstanceStatisticsResponse.

        镜像同步的目标仓库配额

        :return: The replica_registry_quota of this ListInstanceStatisticsResponse.
        :rtype: int
        """
        return self._replica_registry_quota

    @replica_registry_quota.setter
    def replica_registry_quota(self, replica_registry_quota):
        r"""Sets the replica_registry_quota of this ListInstanceStatisticsResponse.

        镜像同步的目标仓库配额

        :param replica_registry_quota: The replica_registry_quota of this ListInstanceStatisticsResponse.
        :type replica_registry_quota: int
        """
        self._replica_registry_quota = replica_registry_quota

    @property
    def sign_policy_quota(self):
        r"""Gets the sign_policy_quota of this ListInstanceStatisticsResponse.

        镜像签名策略的配额

        :return: The sign_policy_quota of this ListInstanceStatisticsResponse.
        :rtype: int
        """
        return self._sign_policy_quota

    @sign_policy_quota.setter
    def sign_policy_quota(self, sign_policy_quota):
        r"""Sets the sign_policy_quota of this ListInstanceStatisticsResponse.

        镜像签名策略的配额

        :param sign_policy_quota: The sign_policy_quota of this ListInstanceStatisticsResponse.
        :type sign_policy_quota: int
        """
        self._sign_policy_quota = sign_policy_quota

    @property
    def replica_policy_count(self):
        r"""Gets the replica_policy_count of this ListInstanceStatisticsResponse.

        镜像同步策略总数

        :return: The replica_policy_count of this ListInstanceStatisticsResponse.
        :rtype: int
        """
        return self._replica_policy_count

    @replica_policy_count.setter
    def replica_policy_count(self, replica_policy_count):
        r"""Sets the replica_policy_count of this ListInstanceStatisticsResponse.

        镜像同步策略总数

        :param replica_policy_count: The replica_policy_count of this ListInstanceStatisticsResponse.
        :type replica_policy_count: int
        """
        self._replica_policy_count = replica_policy_count

    @property
    def retention_policy_count(self):
        r"""Gets the retention_policy_count of this ListInstanceStatisticsResponse.

        镜像老化策略的总数

        :return: The retention_policy_count of this ListInstanceStatisticsResponse.
        :rtype: int
        """
        return self._retention_policy_count

    @retention_policy_count.setter
    def retention_policy_count(self, retention_policy_count):
        r"""Sets the retention_policy_count of this ListInstanceStatisticsResponse.

        镜像老化策略的总数

        :param retention_policy_count: The retention_policy_count of this ListInstanceStatisticsResponse.
        :type retention_policy_count: int
        """
        self._retention_policy_count = retention_policy_count

    @property
    def notify_policy_count(self):
        r"""Gets the notify_policy_count of this ListInstanceStatisticsResponse.

        触发器策略的总数

        :return: The notify_policy_count of this ListInstanceStatisticsResponse.
        :rtype: int
        """
        return self._notify_policy_count

    @notify_policy_count.setter
    def notify_policy_count(self, notify_policy_count):
        r"""Sets the notify_policy_count of this ListInstanceStatisticsResponse.

        触发器策略的总数

        :param notify_policy_count: The notify_policy_count of this ListInstanceStatisticsResponse.
        :type notify_policy_count: int
        """
        self._notify_policy_count = notify_policy_count

    @property
    def replica_registry_count(self):
        r"""Gets the replica_registry_count of this ListInstanceStatisticsResponse.

        镜像同步策略的目标仓库总数

        :return: The replica_registry_count of this ListInstanceStatisticsResponse.
        :rtype: int
        """
        return self._replica_registry_count

    @replica_registry_count.setter
    def replica_registry_count(self, replica_registry_count):
        r"""Sets the replica_registry_count of this ListInstanceStatisticsResponse.

        镜像同步策略的目标仓库总数

        :param replica_registry_count: The replica_registry_count of this ListInstanceStatisticsResponse.
        :type replica_registry_count: int
        """
        self._replica_registry_count = replica_registry_count

    @property
    def intranet_endpoint_quota(self):
        r"""Gets the intranet_endpoint_quota of this ListInstanceStatisticsResponse.

        内网访问控制的配额

        :return: The intranet_endpoint_quota of this ListInstanceStatisticsResponse.
        :rtype: int
        """
        return self._intranet_endpoint_quota

    @intranet_endpoint_quota.setter
    def intranet_endpoint_quota(self, intranet_endpoint_quota):
        r"""Sets the intranet_endpoint_quota of this ListInstanceStatisticsResponse.

        内网访问控制的配额

        :param intranet_endpoint_quota: The intranet_endpoint_quota of this ListInstanceStatisticsResponse.
        :type intranet_endpoint_quota: int
        """
        self._intranet_endpoint_quota = intranet_endpoint_quota

    @property
    def intranet_endpoint_count(self):
        r"""Gets the intranet_endpoint_count of this ListInstanceStatisticsResponse.

        内网访问控制的总数

        :return: The intranet_endpoint_count of this ListInstanceStatisticsResponse.
        :rtype: int
        """
        return self._intranet_endpoint_count

    @intranet_endpoint_count.setter
    def intranet_endpoint_count(self, intranet_endpoint_count):
        r"""Sets the intranet_endpoint_count of this ListInstanceStatisticsResponse.

        内网访问控制的总数

        :param intranet_endpoint_count: The intranet_endpoint_count of this ListInstanceStatisticsResponse.
        :type intranet_endpoint_count: int
        """
        self._intranet_endpoint_count = intranet_endpoint_count

    @property
    def long_term_quota(self):
        r"""Gets the long_term_quota of this ListInstanceStatisticsResponse.

        长期登录指令的配额

        :return: The long_term_quota of this ListInstanceStatisticsResponse.
        :rtype: int
        """
        return self._long_term_quota

    @long_term_quota.setter
    def long_term_quota(self, long_term_quota):
        r"""Sets the long_term_quota of this ListInstanceStatisticsResponse.

        长期登录指令的配额

        :param long_term_quota: The long_term_quota of this ListInstanceStatisticsResponse.
        :type long_term_quota: int
        """
        self._long_term_quota = long_term_quota

    @property
    def sign_policy_count(self):
        r"""Gets the sign_policy_count of this ListInstanceStatisticsResponse.

        镜像签名策略的总数

        :return: The sign_policy_count of this ListInstanceStatisticsResponse.
        :rtype: int
        """
        return self._sign_policy_count

    @sign_policy_count.setter
    def sign_policy_count(self, sign_policy_count):
        r"""Sets the sign_policy_count of this ListInstanceStatisticsResponse.

        镜像签名策略的总数

        :param sign_policy_count: The sign_policy_count of this ListInstanceStatisticsResponse.
        :type sign_policy_count: int
        """
        self._sign_policy_count = sign_policy_count

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
        if not isinstance(other, ListInstanceStatisticsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
