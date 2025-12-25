# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePreProcessRulesResponseBodyData:

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
        'workspace_id': 'str',
        'mapping_id': 'str',
        'preprocess_rules': 'list[CreatePreProcessRulesResponseBodyDataPreprocessRules]'
    }

    attribute_map = {
        'project_id': 'project_id',
        'workspace_id': 'workspace_id',
        'mapping_id': 'mapping_id',
        'preprocess_rules': 'preprocess_rules'
    }

    def __init__(self, project_id=None, workspace_id=None, mapping_id=None, preprocess_rules=None):
        r"""CreatePreProcessRulesResponseBodyData

        The model defined in huaweicloud sdk

        :param project_id: 映射id
        :type project_id: str
        :param workspace_id: 映射id
        :type workspace_id: str
        :param mapping_id: 映射id
        :type mapping_id: str
        :param preprocess_rules: 预处理规则列表
        :type preprocess_rules: list[:class:`huaweicloudsdksecmaster.v1.CreatePreProcessRulesResponseBodyDataPreprocessRules`]
        """
        
        

        self._project_id = None
        self._workspace_id = None
        self._mapping_id = None
        self._preprocess_rules = None
        self.discriminator = None

        if project_id is not None:
            self.project_id = project_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if mapping_id is not None:
            self.mapping_id = mapping_id
        if preprocess_rules is not None:
            self.preprocess_rules = preprocess_rules

    @property
    def project_id(self):
        r"""Gets the project_id of this CreatePreProcessRulesResponseBodyData.

        映射id

        :return: The project_id of this CreatePreProcessRulesResponseBodyData.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this CreatePreProcessRulesResponseBodyData.

        映射id

        :param project_id: The project_id of this CreatePreProcessRulesResponseBodyData.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this CreatePreProcessRulesResponseBodyData.

        映射id

        :return: The workspace_id of this CreatePreProcessRulesResponseBodyData.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this CreatePreProcessRulesResponseBodyData.

        映射id

        :param workspace_id: The workspace_id of this CreatePreProcessRulesResponseBodyData.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def mapping_id(self):
        r"""Gets the mapping_id of this CreatePreProcessRulesResponseBodyData.

        映射id

        :return: The mapping_id of this CreatePreProcessRulesResponseBodyData.
        :rtype: str
        """
        return self._mapping_id

    @mapping_id.setter
    def mapping_id(self, mapping_id):
        r"""Sets the mapping_id of this CreatePreProcessRulesResponseBodyData.

        映射id

        :param mapping_id: The mapping_id of this CreatePreProcessRulesResponseBodyData.
        :type mapping_id: str
        """
        self._mapping_id = mapping_id

    @property
    def preprocess_rules(self):
        r"""Gets the preprocess_rules of this CreatePreProcessRulesResponseBodyData.

        预处理规则列表

        :return: The preprocess_rules of this CreatePreProcessRulesResponseBodyData.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.CreatePreProcessRulesResponseBodyDataPreprocessRules`]
        """
        return self._preprocess_rules

    @preprocess_rules.setter
    def preprocess_rules(self, preprocess_rules):
        r"""Sets the preprocess_rules of this CreatePreProcessRulesResponseBodyData.

        预处理规则列表

        :param preprocess_rules: The preprocess_rules of this CreatePreProcessRulesResponseBodyData.
        :type preprocess_rules: list[:class:`huaweicloudsdksecmaster.v1.CreatePreProcessRulesResponseBodyDataPreprocessRules`]
        """
        self._preprocess_rules = preprocess_rules

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
        if not isinstance(other, CreatePreProcessRulesResponseBodyData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
