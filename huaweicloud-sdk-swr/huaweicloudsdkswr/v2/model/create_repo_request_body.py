# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateRepoRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'repository': 'str',
        'is_public': 'bool',
        'category': 'str',
        'description': 'str'
    }

    attribute_map = {
        'repository': 'repository',
        'is_public': 'is_public',
        'category': 'category',
        'description': 'description'
    }

    def __init__(self, repository=None, is_public=None, category=None, description=None):
        r"""CreateRepoRequestBody

        The model defined in huaweicloud sdk

        :param repository: 镜像仓库名称。小写字母或数字开头，后面跟小写字母、数字、小数点、斜杠、下划线或中划线（其中下划线最多允许连续两个，小数点、斜杠、下划线、中划线不能直接相连），小写字母或数字结尾，1-128个字符。
        :type repository: str
        :param is_public: 是否为公共仓库，可选值为true或false。
        :type is_public: bool
        :param category: 仓库类型，可设置为app_server, linux, framework_app, database, lang, other, windows, arm。
        :type category: str
        :param description: 镜像仓库的描述信息。
        :type description: str
        """
        
        

        self._repository = None
        self._is_public = None
        self._category = None
        self._description = None
        self.discriminator = None

        self.repository = repository
        self.is_public = is_public
        if category is not None:
            self.category = category
        if description is not None:
            self.description = description

    @property
    def repository(self):
        r"""Gets the repository of this CreateRepoRequestBody.

        镜像仓库名称。小写字母或数字开头，后面跟小写字母、数字、小数点、斜杠、下划线或中划线（其中下划线最多允许连续两个，小数点、斜杠、下划线、中划线不能直接相连），小写字母或数字结尾，1-128个字符。

        :return: The repository of this CreateRepoRequestBody.
        :rtype: str
        """
        return self._repository

    @repository.setter
    def repository(self, repository):
        r"""Sets the repository of this CreateRepoRequestBody.

        镜像仓库名称。小写字母或数字开头，后面跟小写字母、数字、小数点、斜杠、下划线或中划线（其中下划线最多允许连续两个，小数点、斜杠、下划线、中划线不能直接相连），小写字母或数字结尾，1-128个字符。

        :param repository: The repository of this CreateRepoRequestBody.
        :type repository: str
        """
        self._repository = repository

    @property
    def is_public(self):
        r"""Gets the is_public of this CreateRepoRequestBody.

        是否为公共仓库，可选值为true或false。

        :return: The is_public of this CreateRepoRequestBody.
        :rtype: bool
        """
        return self._is_public

    @is_public.setter
    def is_public(self, is_public):
        r"""Sets the is_public of this CreateRepoRequestBody.

        是否为公共仓库，可选值为true或false。

        :param is_public: The is_public of this CreateRepoRequestBody.
        :type is_public: bool
        """
        self._is_public = is_public

    @property
    def category(self):
        r"""Gets the category of this CreateRepoRequestBody.

        仓库类型，可设置为app_server, linux, framework_app, database, lang, other, windows, arm。

        :return: The category of this CreateRepoRequestBody.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this CreateRepoRequestBody.

        仓库类型，可设置为app_server, linux, framework_app, database, lang, other, windows, arm。

        :param category: The category of this CreateRepoRequestBody.
        :type category: str
        """
        self._category = category

    @property
    def description(self):
        r"""Gets the description of this CreateRepoRequestBody.

        镜像仓库的描述信息。

        :return: The description of this CreateRepoRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateRepoRequestBody.

        镜像仓库的描述信息。

        :param description: The description of this CreateRepoRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, CreateRepoRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
