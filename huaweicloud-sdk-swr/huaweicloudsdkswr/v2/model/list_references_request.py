# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListReferencesRequest:

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
        'tag': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'namespace': 'namespace',
        'repository': 'repository',
        'tag': 'tag',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, namespace=None, repository=None, tag=None, limit=None, marker=None):
        r"""ListReferencesRequest

        The model defined in huaweicloud sdk

        :param namespace: 组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。
        :type namespace: str
        :param repository: 镜像仓库名称
        :type repository: str
        :param tag: 签名镜像的版本号
        :type tag: str
        :param limit: 返回条数。如果不传该参数默认返回10条记录，最大支持10条记录
        :type limit: int
        :param marker: 分页查询时的起始标记，接口的返回值next_marker为下一次查询的起始标记
        :type marker: str
        """
        
        

        self._namespace = None
        self._repository = None
        self._tag = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        self.namespace = namespace
        self.repository = repository
        self.tag = tag
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def namespace(self):
        r"""Gets the namespace of this ListReferencesRequest.

        组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。

        :return: The namespace of this ListReferencesRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ListReferencesRequest.

        组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。

        :param namespace: The namespace of this ListReferencesRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def repository(self):
        r"""Gets the repository of this ListReferencesRequest.

        镜像仓库名称

        :return: The repository of this ListReferencesRequest.
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        r"""Sets the repository of this ListReferencesRequest.

        镜像仓库名称

        :param repository: The repository of this ListReferencesRequest.
        :type repository: str
        """
        self._repository = repository

    @property
    def tag(self):
        r"""Gets the tag of this ListReferencesRequest.

        签名镜像的版本号

        :return: The tag of this ListReferencesRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this ListReferencesRequest.

        签名镜像的版本号

        :param tag: The tag of this ListReferencesRequest.
        :type tag: str
        """
        self._tag = tag

    @property
    def limit(self):
        r"""Gets the limit of this ListReferencesRequest.

        返回条数。如果不传该参数默认返回10条记录，最大支持10条记录

        :return: The limit of this ListReferencesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListReferencesRequest.

        返回条数。如果不传该参数默认返回10条记录，最大支持10条记录

        :param limit: The limit of this ListReferencesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListReferencesRequest.

        分页查询时的起始标记，接口的返回值next_marker为下一次查询的起始标记

        :return: The marker of this ListReferencesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListReferencesRequest.

        分页查询时的起始标记，接口的返回值next_marker为下一次查询的起始标记

        :param marker: The marker of this ListReferencesRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListReferencesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
