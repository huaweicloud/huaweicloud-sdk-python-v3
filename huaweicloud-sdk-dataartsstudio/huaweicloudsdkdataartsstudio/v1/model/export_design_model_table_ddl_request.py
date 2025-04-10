# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportDesignModelTableDdlRequest:

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
        'model_id': 'str',
        'tb_names': 'list[str]',
        'with_db': 'bool'
    }

    attribute_map = {
        'workspace': 'workspace',
        'x_project_id': 'X-Project-Id',
        'model_id': 'model_id',
        'tb_names': 'tb_names',
        'with_db': 'with_db'
    }

    def __init__(self, workspace=None, x_project_id=None, model_id=None, tb_names=None, with_db=None):
        r"""ExportDesignModelTableDdlRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param x_project_id: 项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。
        :type x_project_id: str
        :param model_id: 所属关系建模的模型ID，ID字符串。
        :type model_id: str
        :param tb_names: 待导出的表名。
        :type tb_names: list[str]
        :param with_db: 导出的DDL包不包括数据库名。
        :type with_db: bool
        """
        
        

        self._workspace = None
        self._x_project_id = None
        self._model_id = None
        self._tb_names = None
        self._with_db = None
        self.discriminator = None

        self.workspace = workspace
        if x_project_id is not None:
            self.x_project_id = x_project_id
        self.model_id = model_id
        if tb_names is not None:
            self.tb_names = tb_names
        if with_db is not None:
            self.with_db = with_db

    @property
    def workspace(self):
        r"""Gets the workspace of this ExportDesignModelTableDdlRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this ExportDesignModelTableDdlRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ExportDesignModelTableDdlRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this ExportDesignModelTableDdlRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def x_project_id(self):
        r"""Gets the x_project_id of this ExportDesignModelTableDdlRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :return: The x_project_id of this ExportDesignModelTableDdlRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        r"""Sets the x_project_id of this ExportDesignModelTableDdlRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :param x_project_id: The x_project_id of this ExportDesignModelTableDdlRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def model_id(self):
        r"""Gets the model_id of this ExportDesignModelTableDdlRequest.

        所属关系建模的模型ID，ID字符串。

        :return: The model_id of this ExportDesignModelTableDdlRequest.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        r"""Sets the model_id of this ExportDesignModelTableDdlRequest.

        所属关系建模的模型ID，ID字符串。

        :param model_id: The model_id of this ExportDesignModelTableDdlRequest.
        :type model_id: str
        """
        self._model_id = model_id

    @property
    def tb_names(self):
        r"""Gets the tb_names of this ExportDesignModelTableDdlRequest.

        待导出的表名。

        :return: The tb_names of this ExportDesignModelTableDdlRequest.
        :rtype: list[str]
        """
        return self._tb_names

    @tb_names.setter
    def tb_names(self, tb_names):
        r"""Sets the tb_names of this ExportDesignModelTableDdlRequest.

        待导出的表名。

        :param tb_names: The tb_names of this ExportDesignModelTableDdlRequest.
        :type tb_names: list[str]
        """
        self._tb_names = tb_names

    @property
    def with_db(self):
        r"""Gets the with_db of this ExportDesignModelTableDdlRequest.

        导出的DDL包不包括数据库名。

        :return: The with_db of this ExportDesignModelTableDdlRequest.
        :rtype: bool
        """
        return self._with_db

    @with_db.setter
    def with_db(self, with_db):
        r"""Sets the with_db of this ExportDesignModelTableDdlRequest.

        导出的DDL包不包括数据库名。

        :param with_db: The with_db of this ExportDesignModelTableDdlRequest.
        :type with_db: bool
        """
        self._with_db = with_db

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
        if not isinstance(other, ExportDesignModelTableDdlRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
