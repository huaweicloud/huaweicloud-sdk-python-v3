# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlgorithmMetadata:

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
        'workspace_id': 'str',
        'ai_project': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'workspace_id': 'workspace_id',
        'ai_project': 'ai_project'
    }

    def __init__(self, id=None, name=None, description=None, workspace_id=None, ai_project=None):
        r"""AlgorithmMetadata

        The model defined in huaweicloud sdk

        :param id: 算法uuid，创建算法时无需填写。
        :type id: int
        :param name: 算法名称。限制为1-64位只含数字、字母、下划线和中划线的名称。
        :type name: str
        :param description: 对算法的描述，默认为“NULL”，字符串的长度限制为[0, 256]。
        :type description: str
        :param workspace_id: 指定算法所处的工作空间，默认值为“0”。“0” 为默认的工作空间。
        :type workspace_id: str
        :param ai_project: 指定算法所属的ai项目，默认值为\&quot;default-ai-project\&quot;。ai项目已下线，无需关注。
        :type ai_project: str
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._workspace_id = None
        self._ai_project = None
        self.discriminator = None

        if id is not None:
            self.id = id
        self.name = name
        if description is not None:
            self.description = description
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if ai_project is not None:
            self.ai_project = ai_project

    @property
    def id(self):
        r"""Gets the id of this AlgorithmMetadata.

        算法uuid，创建算法时无需填写。

        :return: The id of this AlgorithmMetadata.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AlgorithmMetadata.

        算法uuid，创建算法时无需填写。

        :param id: The id of this AlgorithmMetadata.
        :type id: int
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this AlgorithmMetadata.

        算法名称。限制为1-64位只含数字、字母、下划线和中划线的名称。

        :return: The name of this AlgorithmMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AlgorithmMetadata.

        算法名称。限制为1-64位只含数字、字母、下划线和中划线的名称。

        :param name: The name of this AlgorithmMetadata.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this AlgorithmMetadata.

        对算法的描述，默认为“NULL”，字符串的长度限制为[0, 256]。

        :return: The description of this AlgorithmMetadata.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AlgorithmMetadata.

        对算法的描述，默认为“NULL”，字符串的长度限制为[0, 256]。

        :param description: The description of this AlgorithmMetadata.
        :type description: str
        """
        self._description = description

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this AlgorithmMetadata.

        指定算法所处的工作空间，默认值为“0”。“0” 为默认的工作空间。

        :return: The workspace_id of this AlgorithmMetadata.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this AlgorithmMetadata.

        指定算法所处的工作空间，默认值为“0”。“0” 为默认的工作空间。

        :param workspace_id: The workspace_id of this AlgorithmMetadata.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def ai_project(self):
        r"""Gets the ai_project of this AlgorithmMetadata.

        指定算法所属的ai项目，默认值为\"default-ai-project\"。ai项目已下线，无需关注。

        :return: The ai_project of this AlgorithmMetadata.
        :rtype: str
        """
        return self._ai_project

    @ai_project.setter
    def ai_project(self, ai_project):
        r"""Sets the ai_project of this AlgorithmMetadata.

        指定算法所属的ai项目，默认值为\"default-ai-project\"。ai项目已下线，无需关注。

        :param ai_project: The ai_project of this AlgorithmMetadata.
        :type ai_project: str
        """
        self._ai_project = ai_project

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
        if not isinstance(other, AlgorithmMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
