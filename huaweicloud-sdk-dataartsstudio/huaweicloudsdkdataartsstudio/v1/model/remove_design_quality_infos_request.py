# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RemoveDesignQualityInfosRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'x_project_id': 'str',
        'table_id': 'str',
        'table_type': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'x_project_id': 'X-Project-Id',
        'table_id': 'table_id',
        'table_type': 'table_type'
    }

    def __init__(self, workspace=None, x_project_id=None, table_id=None, table_type=None):
        """RemoveDesignQualityInfosRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param x_project_id: 项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。
        :type x_project_id: str
        :param table_id: 表的ID，填写String类型替代Long类型。
        :type table_id: str
        :param table_type: 表类型，默认值是业务表。TABLE_MODEL(业务表(逻辑实体/物理表))、AGGREGATION_LOGIC_TABLE(汇总表)、FACT_LOGIC_TABLE(事实表)、DIMENSION_LOGIC_TABLE(维度表)。 - TABLE_MODEL - AGGREGATION_LOGIC_TABLE - FACT_LOGIC_TABLE - DIMENSION_LOGIC_TABLE
        :type table_type: str
        """
        
        

        self._workspace = None
        self._x_project_id = None
        self._table_id = None
        self._table_type = None
        self.discriminator = None

        self.workspace = workspace
        if x_project_id is not None:
            self.x_project_id = x_project_id
        self.table_id = table_id
        self.table_type = table_type

    @property
    def workspace(self):
        """Gets the workspace of this RemoveDesignQualityInfosRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this RemoveDesignQualityInfosRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this RemoveDesignQualityInfosRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this RemoveDesignQualityInfosRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def x_project_id(self):
        """Gets the x_project_id of this RemoveDesignQualityInfosRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :return: The x_project_id of this RemoveDesignQualityInfosRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        """Sets the x_project_id of this RemoveDesignQualityInfosRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :param x_project_id: The x_project_id of this RemoveDesignQualityInfosRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def table_id(self):
        """Gets the table_id of this RemoveDesignQualityInfosRequest.

        表的ID，填写String类型替代Long类型。

        :return: The table_id of this RemoveDesignQualityInfosRequest.
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        """Sets the table_id of this RemoveDesignQualityInfosRequest.

        表的ID，填写String类型替代Long类型。

        :param table_id: The table_id of this RemoveDesignQualityInfosRequest.
        :type table_id: str
        """
        self._table_id = table_id

    @property
    def table_type(self):
        """Gets the table_type of this RemoveDesignQualityInfosRequest.

        表类型，默认值是业务表。TABLE_MODEL(业务表(逻辑实体/物理表))、AGGREGATION_LOGIC_TABLE(汇总表)、FACT_LOGIC_TABLE(事实表)、DIMENSION_LOGIC_TABLE(维度表)。 - TABLE_MODEL - AGGREGATION_LOGIC_TABLE - FACT_LOGIC_TABLE - DIMENSION_LOGIC_TABLE

        :return: The table_type of this RemoveDesignQualityInfosRequest.
        :rtype: str
        """
        return self._table_type

    @table_type.setter
    def table_type(self, table_type):
        """Sets the table_type of this RemoveDesignQualityInfosRequest.

        表类型，默认值是业务表。TABLE_MODEL(业务表(逻辑实体/物理表))、AGGREGATION_LOGIC_TABLE(汇总表)、FACT_LOGIC_TABLE(事实表)、DIMENSION_LOGIC_TABLE(维度表)。 - TABLE_MODEL - AGGREGATION_LOGIC_TABLE - FACT_LOGIC_TABLE - DIMENSION_LOGIC_TABLE

        :param table_type: The table_type of this RemoveDesignQualityInfosRequest.
        :type table_type: str
        """
        self._table_type = table_type

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
        if not isinstance(other, RemoveDesignQualityInfosRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
