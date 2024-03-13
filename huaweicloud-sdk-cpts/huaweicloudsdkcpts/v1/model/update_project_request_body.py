# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateProjectRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'name': 'str',
        'description': 'str',
        'variables_no_file': 'list[str]',
        'source': 'int',
        'external_params': 'object'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'variables_no_file': 'variables_no_file',
        'source': 'source',
        'external_params': 'external_params'
    }

    def __init__(self, id=None, name=None, description=None, variables_no_file=None, source=None, external_params=None):
        """UpdateProjectRequestBody

        The model defined in huaweicloud sdk

        :param id: 工程id
        :type id: int
        :param name: 工程名称
        :type name: str
        :param description: 工程描述
        :type description: str
        :param variables_no_file: 导入工程时，缺失的存在于变量文件中的变量
        :type variables_no_file: list[str]
        :param source: 来源（0-PerfTest；2-CloudTest）
        :type source: int
        :param external_params: 扩展参数
        :type external_params: object
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._variables_no_file = None
        self._source = None
        self._external_params = None
        self.discriminator = None

        self.id = id
        self.name = name
        if description is not None:
            self.description = description
        if variables_no_file is not None:
            self.variables_no_file = variables_no_file
        if source is not None:
            self.source = source
        if external_params is not None:
            self.external_params = external_params

    @property
    def id(self):
        """Gets the id of this UpdateProjectRequestBody.

        工程id

        :return: The id of this UpdateProjectRequestBody.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateProjectRequestBody.

        工程id

        :param id: The id of this UpdateProjectRequestBody.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this UpdateProjectRequestBody.

        工程名称

        :return: The name of this UpdateProjectRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateProjectRequestBody.

        工程名称

        :param name: The name of this UpdateProjectRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateProjectRequestBody.

        工程描述

        :return: The description of this UpdateProjectRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateProjectRequestBody.

        工程描述

        :param description: The description of this UpdateProjectRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def variables_no_file(self):
        """Gets the variables_no_file of this UpdateProjectRequestBody.

        导入工程时，缺失的存在于变量文件中的变量

        :return: The variables_no_file of this UpdateProjectRequestBody.
        :rtype: list[str]
        """
        return self._variables_no_file

    @variables_no_file.setter
    def variables_no_file(self, variables_no_file):
        """Sets the variables_no_file of this UpdateProjectRequestBody.

        导入工程时，缺失的存在于变量文件中的变量

        :param variables_no_file: The variables_no_file of this UpdateProjectRequestBody.
        :type variables_no_file: list[str]
        """
        self._variables_no_file = variables_no_file

    @property
    def source(self):
        """Gets the source of this UpdateProjectRequestBody.

        来源（0-PerfTest；2-CloudTest）

        :return: The source of this UpdateProjectRequestBody.
        :rtype: int
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this UpdateProjectRequestBody.

        来源（0-PerfTest；2-CloudTest）

        :param source: The source of this UpdateProjectRequestBody.
        :type source: int
        """
        self._source = source

    @property
    def external_params(self):
        """Gets the external_params of this UpdateProjectRequestBody.

        扩展参数

        :return: The external_params of this UpdateProjectRequestBody.
        :rtype: object
        """
        return self._external_params

    @external_params.setter
    def external_params(self, external_params):
        """Sets the external_params of this UpdateProjectRequestBody.

        扩展参数

        :param external_params: The external_params of this UpdateProjectRequestBody.
        :type external_params: object
        """
        self._external_params = external_params

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
        if not isinstance(other, UpdateProjectRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
