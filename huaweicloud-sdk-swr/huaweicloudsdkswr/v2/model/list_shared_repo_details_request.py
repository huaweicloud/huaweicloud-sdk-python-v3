# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSharedRepoDetailsRequest:

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
        'name': 'str',
        'shared_by': 'str',
        'limit': 'int',
        'marker': 'int',
        'status': 'bool'
    }

    attribute_map = {
        'namespace': 'namespace',
        'name': 'name',
        'shared_by': 'shared_by',
        'limit': 'limit',
        'marker': 'marker',
        'status': 'status'
    }

    def __init__(self, namespace=None, name=None, shared_by=None, limit=None, marker=None, status=None):
        r"""ListSharedRepoDetailsRequest

        The model defined in huaweicloud sdk

        :param namespace: 组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。
        :type namespace: str
        :param name: 镜像仓库名称
        :type name: str
        :param shared_by: self: 我共享的镜像。thirdparty: 他人共享给我的镜像
        :type shared_by: str
        :param limit: 返回条数,默认返回100条记录，最多返回1000条。
        :type limit: int
        :param marker: 分页查询时下一次查询的起始地址。
        :type marker: int
        :param status: 查询他人共享给我的镜像是否已过期 false：共享已过期。true：正常
        :type status: bool
        """
        
        

        self._namespace = None
        self._name = None
        self._shared_by = None
        self._limit = None
        self._marker = None
        self._status = None
        self.discriminator = None

        if namespace is not None:
            self.namespace = namespace
        if name is not None:
            self.name = name
        self.shared_by = shared_by
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if status is not None:
            self.status = status

    @property
    def namespace(self):
        r"""Gets the namespace of this ListSharedRepoDetailsRequest.

        组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。

        :return: The namespace of this ListSharedRepoDetailsRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ListSharedRepoDetailsRequest.

        组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。

        :param namespace: The namespace of this ListSharedRepoDetailsRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def name(self):
        r"""Gets the name of this ListSharedRepoDetailsRequest.

        镜像仓库名称

        :return: The name of this ListSharedRepoDetailsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListSharedRepoDetailsRequest.

        镜像仓库名称

        :param name: The name of this ListSharedRepoDetailsRequest.
        :type name: str
        """
        self._name = name

    @property
    def shared_by(self):
        r"""Gets the shared_by of this ListSharedRepoDetailsRequest.

        self: 我共享的镜像。thirdparty: 他人共享给我的镜像

        :return: The shared_by of this ListSharedRepoDetailsRequest.
        :rtype: str
        """
        return self._shared_by

    @shared_by.setter
    def shared_by(self, shared_by):
        r"""Sets the shared_by of this ListSharedRepoDetailsRequest.

        self: 我共享的镜像。thirdparty: 他人共享给我的镜像

        :param shared_by: The shared_by of this ListSharedRepoDetailsRequest.
        :type shared_by: str
        """
        self._shared_by = shared_by

    @property
    def limit(self):
        r"""Gets the limit of this ListSharedRepoDetailsRequest.

        返回条数,默认返回100条记录，最多返回1000条。

        :return: The limit of this ListSharedRepoDetailsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSharedRepoDetailsRequest.

        返回条数,默认返回100条记录，最多返回1000条。

        :param limit: The limit of this ListSharedRepoDetailsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListSharedRepoDetailsRequest.

        分页查询时下一次查询的起始地址。

        :return: The marker of this ListSharedRepoDetailsRequest.
        :rtype: int
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListSharedRepoDetailsRequest.

        分页查询时下一次查询的起始地址。

        :param marker: The marker of this ListSharedRepoDetailsRequest.
        :type marker: int
        """
        self._marker = marker

    @property
    def status(self):
        r"""Gets the status of this ListSharedRepoDetailsRequest.

        查询他人共享给我的镜像是否已过期 false：共享已过期。true：正常

        :return: The status of this ListSharedRepoDetailsRequest.
        :rtype: bool
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListSharedRepoDetailsRequest.

        查询他人共享给我的镜像是否已过期 false：共享已过期。true：正常

        :param status: The status of this ListSharedRepoDetailsRequest.
        :type status: bool
        """
        self._status = status

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
        if not isinstance(other, ListSharedRepoDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
