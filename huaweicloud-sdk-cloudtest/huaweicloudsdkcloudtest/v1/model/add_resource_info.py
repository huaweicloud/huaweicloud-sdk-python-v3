# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddResourceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_uuid': 'str',
        'iterator_uri': 'str',
        'type': 'int',
        'is_all_issues': 'str',
        'all_import': 'bool',
        'feature_uri': 'str',
        'simple_resourceinfo_list': 'list[SimpleResourceInfo]',
        'invert_simple_resourceinfo_list': 'list[SimpleResourceInfo]',
        'add_to_iterator': 'bool'
    }

    attribute_map = {
        'project_uuid': 'project_uuid',
        'iterator_uri': 'iterator_uri',
        'type': 'type',
        'is_all_issues': 'is_all_issues',
        'all_import': 'all_import',
        'feature_uri': 'feature_uri',
        'simple_resourceinfo_list': 'simple_resourceinfo_list',
        'invert_simple_resourceinfo_list': 'invert_simple_resourceinfo_list',
        'add_to_iterator': 'add_to_iterator'
    }

    def __init__(self, project_uuid=None, iterator_uri=None, type=None, is_all_issues=None, all_import=None, feature_uri=None, simple_resourceinfo_list=None, invert_simple_resourceinfo_list=None, add_to_iterator=None):
        """AddResourceInfo

        The model defined in huaweicloud sdk

        :param project_uuid: 项目id
        :type project_uuid: str
        :param iterator_uri: 迭代uri
        :type iterator_uri: str
        :param type: 资源类型, 对应serviceType
        :type type: int
        :param is_all_issues: 是否选择issues
        :type is_all_issues: str
        :param all_import: 是否选择所有用例
        :type all_import: bool
        :param feature_uri: 按照目录引入用例
        :type feature_uri: str
        :param simple_resourceinfo_list: 选择的资源列表, 对应sourceCaseUris
        :type simple_resourceinfo_list: list[:class:`huaweicloudsdkcloudtest.v1.SimpleResourceInfo`]
        :param invert_simple_resourceinfo_list: 反选的资源列表
        :type invert_simple_resourceinfo_list: list[:class:`huaweicloudsdkcloudtest.v1.SimpleResourceInfo`]
        :param add_to_iterator: 是否将需求添加到测试计划（不传或者true添加需求到测试计划，false就不添加）
        :type add_to_iterator: bool
        """
        
        

        self._project_uuid = None
        self._iterator_uri = None
        self._type = None
        self._is_all_issues = None
        self._all_import = None
        self._feature_uri = None
        self._simple_resourceinfo_list = None
        self._invert_simple_resourceinfo_list = None
        self._add_to_iterator = None
        self.discriminator = None

        if project_uuid is not None:
            self.project_uuid = project_uuid
        if iterator_uri is not None:
            self.iterator_uri = iterator_uri
        if type is not None:
            self.type = type
        if is_all_issues is not None:
            self.is_all_issues = is_all_issues
        if all_import is not None:
            self.all_import = all_import
        if feature_uri is not None:
            self.feature_uri = feature_uri
        if simple_resourceinfo_list is not None:
            self.simple_resourceinfo_list = simple_resourceinfo_list
        if invert_simple_resourceinfo_list is not None:
            self.invert_simple_resourceinfo_list = invert_simple_resourceinfo_list
        if add_to_iterator is not None:
            self.add_to_iterator = add_to_iterator

    @property
    def project_uuid(self):
        """Gets the project_uuid of this AddResourceInfo.

        项目id

        :return: The project_uuid of this AddResourceInfo.
        :rtype: str
        """
        return self._project_uuid

    @project_uuid.setter
    def project_uuid(self, project_uuid):
        """Sets the project_uuid of this AddResourceInfo.

        项目id

        :param project_uuid: The project_uuid of this AddResourceInfo.
        :type project_uuid: str
        """
        self._project_uuid = project_uuid

    @property
    def iterator_uri(self):
        """Gets the iterator_uri of this AddResourceInfo.

        迭代uri

        :return: The iterator_uri of this AddResourceInfo.
        :rtype: str
        """
        return self._iterator_uri

    @iterator_uri.setter
    def iterator_uri(self, iterator_uri):
        """Sets the iterator_uri of this AddResourceInfo.

        迭代uri

        :param iterator_uri: The iterator_uri of this AddResourceInfo.
        :type iterator_uri: str
        """
        self._iterator_uri = iterator_uri

    @property
    def type(self):
        """Gets the type of this AddResourceInfo.

        资源类型, 对应serviceType

        :return: The type of this AddResourceInfo.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AddResourceInfo.

        资源类型, 对应serviceType

        :param type: The type of this AddResourceInfo.
        :type type: int
        """
        self._type = type

    @property
    def is_all_issues(self):
        """Gets the is_all_issues of this AddResourceInfo.

        是否选择issues

        :return: The is_all_issues of this AddResourceInfo.
        :rtype: str
        """
        return self._is_all_issues

    @is_all_issues.setter
    def is_all_issues(self, is_all_issues):
        """Sets the is_all_issues of this AddResourceInfo.

        是否选择issues

        :param is_all_issues: The is_all_issues of this AddResourceInfo.
        :type is_all_issues: str
        """
        self._is_all_issues = is_all_issues

    @property
    def all_import(self):
        """Gets the all_import of this AddResourceInfo.

        是否选择所有用例

        :return: The all_import of this AddResourceInfo.
        :rtype: bool
        """
        return self._all_import

    @all_import.setter
    def all_import(self, all_import):
        """Sets the all_import of this AddResourceInfo.

        是否选择所有用例

        :param all_import: The all_import of this AddResourceInfo.
        :type all_import: bool
        """
        self._all_import = all_import

    @property
    def feature_uri(self):
        """Gets the feature_uri of this AddResourceInfo.

        按照目录引入用例

        :return: The feature_uri of this AddResourceInfo.
        :rtype: str
        """
        return self._feature_uri

    @feature_uri.setter
    def feature_uri(self, feature_uri):
        """Sets the feature_uri of this AddResourceInfo.

        按照目录引入用例

        :param feature_uri: The feature_uri of this AddResourceInfo.
        :type feature_uri: str
        """
        self._feature_uri = feature_uri

    @property
    def simple_resourceinfo_list(self):
        """Gets the simple_resourceinfo_list of this AddResourceInfo.

        选择的资源列表, 对应sourceCaseUris

        :return: The simple_resourceinfo_list of this AddResourceInfo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.SimpleResourceInfo`]
        """
        return self._simple_resourceinfo_list

    @simple_resourceinfo_list.setter
    def simple_resourceinfo_list(self, simple_resourceinfo_list):
        """Sets the simple_resourceinfo_list of this AddResourceInfo.

        选择的资源列表, 对应sourceCaseUris

        :param simple_resourceinfo_list: The simple_resourceinfo_list of this AddResourceInfo.
        :type simple_resourceinfo_list: list[:class:`huaweicloudsdkcloudtest.v1.SimpleResourceInfo`]
        """
        self._simple_resourceinfo_list = simple_resourceinfo_list

    @property
    def invert_simple_resourceinfo_list(self):
        """Gets the invert_simple_resourceinfo_list of this AddResourceInfo.

        反选的资源列表

        :return: The invert_simple_resourceinfo_list of this AddResourceInfo.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.SimpleResourceInfo`]
        """
        return self._invert_simple_resourceinfo_list

    @invert_simple_resourceinfo_list.setter
    def invert_simple_resourceinfo_list(self, invert_simple_resourceinfo_list):
        """Sets the invert_simple_resourceinfo_list of this AddResourceInfo.

        反选的资源列表

        :param invert_simple_resourceinfo_list: The invert_simple_resourceinfo_list of this AddResourceInfo.
        :type invert_simple_resourceinfo_list: list[:class:`huaweicloudsdkcloudtest.v1.SimpleResourceInfo`]
        """
        self._invert_simple_resourceinfo_list = invert_simple_resourceinfo_list

    @property
    def add_to_iterator(self):
        """Gets the add_to_iterator of this AddResourceInfo.

        是否将需求添加到测试计划（不传或者true添加需求到测试计划，false就不添加）

        :return: The add_to_iterator of this AddResourceInfo.
        :rtype: bool
        """
        return self._add_to_iterator

    @add_to_iterator.setter
    def add_to_iterator(self, add_to_iterator):
        """Sets the add_to_iterator of this AddResourceInfo.

        是否将需求添加到测试计划（不传或者true添加需求到测试计划，false就不添加）

        :param add_to_iterator: The add_to_iterator of this AddResourceInfo.
        :type add_to_iterator: bool
        """
        self._add_to_iterator = add_to_iterator

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
        if not isinstance(other, AddResourceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
