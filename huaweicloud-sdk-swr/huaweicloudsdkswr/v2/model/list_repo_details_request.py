# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRepoDetailsRequest:

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
        'category': 'str',
        'limit': 'int',
        'marker': 'int',
        'is_public': 'bool'
    }

    attribute_map = {
        'namespace': 'namespace',
        'name': 'name',
        'category': 'category',
        'limit': 'limit',
        'marker': 'marker',
        'is_public': 'is_public'
    }

    def __init__(self, namespace=None, name=None, category=None, limit=None, marker=None, is_public=None):
        r"""ListRepoDetailsRequest

        The model defined in huaweicloud sdk

        :param namespace: 组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。
        :type namespace: str
        :param name: 镜像仓库名称。
        :type name: str
        :param category: 镜像仓库分类，可设置为app_server, linux, framework_app, database, lang, other, windows, arm。
        :type category: str
        :param limit: 返回条数，默认返回100条记录，最多返回1000条记录。
        :type limit: int
        :param marker: 分页查询下一次查询起始标记，接口的返回值nextMarker为下一次查询的起始标记。
        :type marker: int
        :param is_public: 是否公开私有，true为公开，false为私有。
        :type is_public: bool
        """
        
        

        self._namespace = None
        self._name = None
        self._category = None
        self._limit = None
        self._marker = None
        self._is_public = None
        self.discriminator = None

        if namespace is not None:
            self.namespace = namespace
        if name is not None:
            self.name = name
        if category is not None:
            self.category = category
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if is_public is not None:
            self.is_public = is_public

    @property
    def namespace(self):
        r"""Gets the namespace of this ListRepoDetailsRequest.

        组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。

        :return: The namespace of this ListRepoDetailsRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        r"""Sets the namespace of this ListRepoDetailsRequest.

        组织名称。小写字母开头，后面跟小写字母、数字、小数点、下划线或中划线（其中下划线最多允许连续两个，小数点、下划线、中划线不能直接相连），小写字母或数字结尾，1-64个字符。

        :param namespace: The namespace of this ListRepoDetailsRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def name(self):
        r"""Gets the name of this ListRepoDetailsRequest.

        镜像仓库名称。

        :return: The name of this ListRepoDetailsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListRepoDetailsRequest.

        镜像仓库名称。

        :param name: The name of this ListRepoDetailsRequest.
        :type name: str
        """
        self._name = name

    @property
    def category(self):
        r"""Gets the category of this ListRepoDetailsRequest.

        镜像仓库分类，可设置为app_server, linux, framework_app, database, lang, other, windows, arm。

        :return: The category of this ListRepoDetailsRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ListRepoDetailsRequest.

        镜像仓库分类，可设置为app_server, linux, framework_app, database, lang, other, windows, arm。

        :param category: The category of this ListRepoDetailsRequest.
        :type category: str
        """
        self._category = category

    @property
    def limit(self):
        r"""Gets the limit of this ListRepoDetailsRequest.

        返回条数，默认返回100条记录，最多返回1000条记录。

        :return: The limit of this ListRepoDetailsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListRepoDetailsRequest.

        返回条数，默认返回100条记录，最多返回1000条记录。

        :param limit: The limit of this ListRepoDetailsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListRepoDetailsRequest.

        分页查询下一次查询起始标记，接口的返回值nextMarker为下一次查询的起始标记。

        :return: The marker of this ListRepoDetailsRequest.
        :rtype: int
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListRepoDetailsRequest.

        分页查询下一次查询起始标记，接口的返回值nextMarker为下一次查询的起始标记。

        :param marker: The marker of this ListRepoDetailsRequest.
        :type marker: int
        """
        self._marker = marker

    @property
    def is_public(self):
        r"""Gets the is_public of this ListRepoDetailsRequest.

        是否公开私有，true为公开，false为私有。

        :return: The is_public of this ListRepoDetailsRequest.
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        r"""Sets the is_public of this ListRepoDetailsRequest.

        是否公开私有，true为公开，false为私有。

        :param is_public: The is_public of this ListRepoDetailsRequest.
        :type is_public: bool
        """
        self._is_public = is_public

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
        if not isinstance(other, ListRepoDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
