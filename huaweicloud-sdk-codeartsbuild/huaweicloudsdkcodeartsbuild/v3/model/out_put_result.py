# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OutPutResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'name': 'str',
        'version': 'str',
        'package_type': 'str',
        'uri': 'str',
        'type': 'str',
        'daily_build_number': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'name': 'name',
        'version': 'version',
        'package_type': 'package_type',
        'uri': 'uri',
        'type': 'type',
        'daily_build_number': 'daily_build_number'
    }

    def __init__(self, project_id=None, name=None, version=None, package_type=None, uri=None, type=None, daily_build_number=None):
        r"""OutPutResult

        The model defined in huaweicloud sdk

        :param project_id: 构建任务所在项目的ID
        :type project_id: str
        :param name: 产物名称
        :type name: str
        :param version: 产物版本
        :type version: str
        :param package_type: 产物类型
        :type package_type: str
        :param uri: 产物路径
        :type uri: str
        :param type: 类型
        :type type: str
        :param daily_build_number: 构建编号，每日从1开始
        :type daily_build_number: str
        """
        
        

        self._project_id = None
        self._name = None
        self._version = None
        self._package_type = None
        self._uri = None
        self._type = None
        self._daily_build_number = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if name is not None:
            self.name = name
        if version is not None:
            self.version = version
        if package_type is not None:
            self.package_type = package_type
        if uri is not None:
            self.uri = uri
        if type is not None:
            self.type = type
        if daily_build_number is not None:
            self.daily_build_number = daily_build_number

    @property
    def project_id(self):
        r"""Gets the project_id of this OutPutResult.

        构建任务所在项目的ID

        :return: The project_id of this OutPutResult.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this OutPutResult.

        构建任务所在项目的ID

        :param project_id: The project_id of this OutPutResult.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def name(self):
        r"""Gets the name of this OutPutResult.

        产物名称

        :return: The name of this OutPutResult.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this OutPutResult.

        产物名称

        :param name: The name of this OutPutResult.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        r"""Gets the version of this OutPutResult.

        产物版本

        :return: The version of this OutPutResult.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this OutPutResult.

        产物版本

        :param version: The version of this OutPutResult.
        :type version: str
        """
        self._version = version

    @property
    def package_type(self):
        r"""Gets the package_type of this OutPutResult.

        产物类型

        :return: The package_type of this OutPutResult.
        :rtype: str
        """
        return self._package_type

    @package_type.setter
    def package_type(self, package_type):
        r"""Sets the package_type of this OutPutResult.

        产物类型

        :param package_type: The package_type of this OutPutResult.
        :type package_type: str
        """
        self._package_type = package_type

    @property
    def uri(self):
        r"""Gets the uri of this OutPutResult.

        产物路径

        :return: The uri of this OutPutResult.
        :rtype: str
        """
        return self._uri

    @uri.setter
    def uri(self, uri):
        r"""Sets the uri of this OutPutResult.

        产物路径

        :param uri: The uri of this OutPutResult.
        :type uri: str
        """
        self._uri = uri

    @property
    def type(self):
        r"""Gets the type of this OutPutResult.

        类型

        :return: The type of this OutPutResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this OutPutResult.

        类型

        :param type: The type of this OutPutResult.
        :type type: str
        """
        self._type = type

    @property
    def daily_build_number(self):
        r"""Gets the daily_build_number of this OutPutResult.

        构建编号，每日从1开始

        :return: The daily_build_number of this OutPutResult.
        :rtype: str
        """
        return self._daily_build_number

    @daily_build_number.setter
    def daily_build_number(self, daily_build_number):
        r"""Sets the daily_build_number of this OutPutResult.

        构建编号，每日从1开始

        :param daily_build_number: The daily_build_number of this OutPutResult.
        :type daily_build_number: str
        """
        self._daily_build_number = daily_build_number

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
        if not isinstance(other, OutPutResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
