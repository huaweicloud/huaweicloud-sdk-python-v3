# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateWorkspaceRequestInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'metastore_id': 'str',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'metastore_id': 'metastore_id',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, name=None, description=None, metastore_id=None, enterprise_project_id=None):
        r"""CreateWorkspaceRequestInput

        The model defined in huaweicloud sdk

        :param name: 工作空间名称。
        :type name: str
        :param description: 描述。用户输入的描述，最长为255个字符。
        :type description: str
        :param metastore_id: Metastore信息，LakeFormation服务的实例Id，即MetaStoreId。
        :type metastore_id: str
        :param enterprise_project_id: 企业项目ID，只有对接了企业项目才可以填写。只能包含字母、数字和中划线，且长度为1到64个字符。默认是0，即default
        :type enterprise_project_id: str
        """
        
        

        self._name = None
        self._description = None
        self._metastore_id = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if metastore_id is not None:
            self.metastore_id = metastore_id
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def name(self):
        r"""Gets the name of this CreateWorkspaceRequestInput.

        工作空间名称。

        :return: The name of this CreateWorkspaceRequestInput.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateWorkspaceRequestInput.

        工作空间名称。

        :param name: The name of this CreateWorkspaceRequestInput.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this CreateWorkspaceRequestInput.

        描述。用户输入的描述，最长为255个字符。

        :return: The description of this CreateWorkspaceRequestInput.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateWorkspaceRequestInput.

        描述。用户输入的描述，最长为255个字符。

        :param description: The description of this CreateWorkspaceRequestInput.
        :type description: str
        """
        self._description = description

    @property
    def metastore_id(self):
        r"""Gets the metastore_id of this CreateWorkspaceRequestInput.

        Metastore信息，LakeFormation服务的实例Id，即MetaStoreId。

        :return: The metastore_id of this CreateWorkspaceRequestInput.
        :rtype: str
        """
        return self._metastore_id

    @metastore_id.setter
    def metastore_id(self, metastore_id):
        r"""Sets the metastore_id of this CreateWorkspaceRequestInput.

        Metastore信息，LakeFormation服务的实例Id，即MetaStoreId。

        :param metastore_id: The metastore_id of this CreateWorkspaceRequestInput.
        :type metastore_id: str
        """
        self._metastore_id = metastore_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateWorkspaceRequestInput.

        企业项目ID，只有对接了企业项目才可以填写。只能包含字母、数字和中划线，且长度为1到64个字符。默认是0，即default

        :return: The enterprise_project_id of this CreateWorkspaceRequestInput.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateWorkspaceRequestInput.

        企业项目ID，只有对接了企业项目才可以填写。只能包含字母、数字和中划线，且长度为1到64个字符。默认是0，即default

        :param enterprise_project_id: The enterprise_project_id of this CreateWorkspaceRequestInput.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, CreateWorkspaceRequestInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
