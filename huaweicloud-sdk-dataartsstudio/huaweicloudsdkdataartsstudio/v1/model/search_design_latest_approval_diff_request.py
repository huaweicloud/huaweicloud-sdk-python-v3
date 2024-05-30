# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchDesignLatestApprovalDiffRequest:

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
        'biz_id': 'str',
        'biz_type': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'x_project_id': 'X-Project-Id',
        'biz_id': 'biz_id',
        'biz_type': 'biz_type'
    }

    def __init__(self, workspace=None, x_project_id=None, biz_id=None, biz_type=None):
        """SearchDesignLatestApprovalDiffRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param x_project_id: 项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。
        :type x_project_id: str
        :param biz_id: 待比较下展的实体ID，填写String类型替代Long类型。
        :type biz_id: str
        :param biz_type: 待删除下展的实体类型。 枚举值：   - ATOMIC_INDEX: 原子指标   - DERIVATIVE_INDEX: 衍生指标   - DIMENSION: 维度   - FACT_LOGIC_TABLE: 事实表   - TABLE_MODEL:关系建模：逻辑实体/物理表   - STANDARD_ELEMENT: 数据标准   - AGGREGATION_LOGIC_TABLE: 汇总表   - CODE_TABLE: 码表   - BIZ_METRIC: 业务指标   - COMPOUND_METRIC: 复合指标 
        :type biz_type: str
        """
        
        

        self._workspace = None
        self._x_project_id = None
        self._biz_id = None
        self._biz_type = None
        self.discriminator = None

        self.workspace = workspace
        if x_project_id is not None:
            self.x_project_id = x_project_id
        self.biz_id = biz_id
        self.biz_type = biz_type

    @property
    def workspace(self):
        """Gets the workspace of this SearchDesignLatestApprovalDiffRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this SearchDesignLatestApprovalDiffRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this SearchDesignLatestApprovalDiffRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this SearchDesignLatestApprovalDiffRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def x_project_id(self):
        """Gets the x_project_id of this SearchDesignLatestApprovalDiffRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :return: The x_project_id of this SearchDesignLatestApprovalDiffRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        """Sets the x_project_id of this SearchDesignLatestApprovalDiffRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :param x_project_id: The x_project_id of this SearchDesignLatestApprovalDiffRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def biz_id(self):
        """Gets the biz_id of this SearchDesignLatestApprovalDiffRequest.

        待比较下展的实体ID，填写String类型替代Long类型。

        :return: The biz_id of this SearchDesignLatestApprovalDiffRequest.
        :rtype: str
        """
        return self._biz_id

    @biz_id.setter
    def biz_id(self, biz_id):
        """Sets the biz_id of this SearchDesignLatestApprovalDiffRequest.

        待比较下展的实体ID，填写String类型替代Long类型。

        :param biz_id: The biz_id of this SearchDesignLatestApprovalDiffRequest.
        :type biz_id: str
        """
        self._biz_id = biz_id

    @property
    def biz_type(self):
        """Gets the biz_type of this SearchDesignLatestApprovalDiffRequest.

        待删除下展的实体类型。 枚举值：   - ATOMIC_INDEX: 原子指标   - DERIVATIVE_INDEX: 衍生指标   - DIMENSION: 维度   - FACT_LOGIC_TABLE: 事实表   - TABLE_MODEL:关系建模：逻辑实体/物理表   - STANDARD_ELEMENT: 数据标准   - AGGREGATION_LOGIC_TABLE: 汇总表   - CODE_TABLE: 码表   - BIZ_METRIC: 业务指标   - COMPOUND_METRIC: 复合指标 

        :return: The biz_type of this SearchDesignLatestApprovalDiffRequest.
        :rtype: str
        """
        return self._biz_type

    @biz_type.setter
    def biz_type(self, biz_type):
        """Sets the biz_type of this SearchDesignLatestApprovalDiffRequest.

        待删除下展的实体类型。 枚举值：   - ATOMIC_INDEX: 原子指标   - DERIVATIVE_INDEX: 衍生指标   - DIMENSION: 维度   - FACT_LOGIC_TABLE: 事实表   - TABLE_MODEL:关系建模：逻辑实体/物理表   - STANDARD_ELEMENT: 数据标准   - AGGREGATION_LOGIC_TABLE: 汇总表   - CODE_TABLE: 码表   - BIZ_METRIC: 业务指标   - COMPOUND_METRIC: 复合指标 

        :param biz_type: The biz_type of this SearchDesignLatestApprovalDiffRequest.
        :type biz_type: str
        """
        self._biz_type = biz_type

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
        if not isinstance(other, SearchDesignLatestApprovalDiffRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
