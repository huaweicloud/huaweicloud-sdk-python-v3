# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSyncJobRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'repository': 'str',
        'filter': 'str'
    }

    attribute_map = {
        'namespace': 'namespace',
        'repository': 'repository',
        'filter': 'filter'
    }

    def __init__(self, namespace=None, repository=None, filter=None):
        r"""ShowSyncJobRequest

        The model defined in huaweicloud sdk

        :param namespace: 组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。
        :type namespace: str
        :param repository: 镜像仓库名称
        :type repository: str
        :param filter: 应填写 limit::{limit}|offset::{offset}|order::{order} ,其中{limit}为返回条数,{offset}为起始索引,注意：offset和limit参数需要配套使用，且必选。{order}为排序类型（可选），可设置为desc（降序）、asc（升序）
        :type filter: str
        """
        
        

        self._namespace = None
        self._repository = None
        self._filter = None
        self.discriminator = None

        self.namespace = namespace
        self.repository = repository
        self.filter = filter

    @property
    def namespace(self):
        r"""Gets the namespace of this ShowSyncJobRequest.

        组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。

        :return: The namespace of this ShowSyncJobRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ShowSyncJobRequest.

        组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。

        :param namespace: The namespace of this ShowSyncJobRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def repository(self):
        r"""Gets the repository of this ShowSyncJobRequest.

        镜像仓库名称

        :return: The repository of this ShowSyncJobRequest.
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        r"""Sets the repository of this ShowSyncJobRequest.

        镜像仓库名称

        :param repository: The repository of this ShowSyncJobRequest.
        :type repository: str
        """
        self._repository = repository

    @property
    def filter(self):
        r"""Gets the filter of this ShowSyncJobRequest.

        应填写 limit::{limit}|offset::{offset}|order::{order} ,其中{limit}为返回条数,{offset}为起始索引,注意：offset和limit参数需要配套使用，且必选。{order}为排序类型（可选），可设置为desc（降序）、asc（升序）

        :return: The filter of this ShowSyncJobRequest.
        :rtype: str
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this ShowSyncJobRequest.

        应填写 limit::{limit}|offset::{offset}|order::{order} ,其中{limit}为返回条数,{offset}为起始索引,注意：offset和limit参数需要配套使用，且必选。{order}为排序类型（可选），可设置为desc（降序）、asc（升序）

        :param filter: The filter of this ShowSyncJobRequest.
        :type filter: str
        """
        self._filter = filter

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
        if not isinstance(other, ShowSyncJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
