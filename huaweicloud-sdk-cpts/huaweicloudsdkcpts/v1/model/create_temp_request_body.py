# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateTempRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'int',
        'temp_type': 'int',
        'name': 'str',
        'description': 'str',
        'contents': 'list[object]'
    }

    attribute_map = {
        'project_id': 'project_id',
        'temp_type': 'temp_type',
        'name': 'name',
        'description': 'description',
        'contents': 'contents'
    }

    def __init__(self, project_id=None, temp_type=None, name=None, description=None, contents=None):
        r"""CreateTempRequestBody

        The model defined in huaweicloud sdk

        :param project_id: 所属工程id
        :type project_id: int
        :param temp_type: 事务类型
        :type temp_type: int
        :param name: 事务名称
        :type name: str
        :param description: 描述信息
        :type description: str
        :param contents: 事务脚本信息
        :type contents: list[object]
        """
        
        

        self._project_id = None
        self._temp_type = None
        self._name = None
        self._description = None
        self._contents = None
        self.discriminator = None

        self.project_id = project_id
        self.temp_type = temp_type
        self.name = name
        if description is not None:
            self.description = description
        if contents is not None:
            self.contents = contents

    @property
    def project_id(self):
        r"""Gets the project_id of this CreateTempRequestBody.

        所属工程id

        :return: The project_id of this CreateTempRequestBody.
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CreateTempRequestBody.

        所属工程id

        :param project_id: The project_id of this CreateTempRequestBody.
        :type project_id: int
        """
        self._project_id = project_id

    @property
    def temp_type(self):
        r"""Gets the temp_type of this CreateTempRequestBody.

        事务类型

        :return: The temp_type of this CreateTempRequestBody.
        :rtype: int
        """
        return self._temp_type

    @temp_type.setter
    def temp_type(self, temp_type):
        r"""Sets the temp_type of this CreateTempRequestBody.

        事务类型

        :param temp_type: The temp_type of this CreateTempRequestBody.
        :type temp_type: int
        """
        self._temp_type = temp_type

    @property
    def name(self):
        r"""Gets the name of this CreateTempRequestBody.

        事务名称

        :return: The name of this CreateTempRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateTempRequestBody.

        事务名称

        :param name: The name of this CreateTempRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateTempRequestBody.

        描述信息

        :return: The description of this CreateTempRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateTempRequestBody.

        描述信息

        :param description: The description of this CreateTempRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def contents(self):
        r"""Gets the contents of this CreateTempRequestBody.

        事务脚本信息

        :return: The contents of this CreateTempRequestBody.
        :rtype: list[object]
        """
        return self._contents

    @contents.setter
    def contents(self, contents):
        r"""Sets the contents of this CreateTempRequestBody.

        事务脚本信息

        :param contents: The contents of this CreateTempRequestBody.
        :type contents: list[object]
        """
        self._contents = contents

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
        if not isinstance(other, CreateTempRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
