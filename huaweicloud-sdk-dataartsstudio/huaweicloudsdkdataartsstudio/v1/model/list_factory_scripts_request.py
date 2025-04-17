# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFactoryScriptsRequest:

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
        'limit': 'int',
        'offset': 'int',
        'script_name': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'x_project_id': 'X-Project-Id',
        'limit': 'limit',
        'offset': 'offset',
        'script_name': 'script_name'
    }

    def __init__(self, workspace=None, x_project_id=None, limit=None, offset=None, script_name=None):
        r"""ListFactoryScriptsRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param x_project_id: 项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。
        :type x_project_id: str
        :param limit: 分页返回结果，指定每页最大记录数，范围[1,100]。 默认值：10。
        :type limit: int
        :param offset: 分页的起始页，默认值为0。取值范围大于等于0。
        :type offset: int
        :param script_name: 脚本名称
        :type script_name: str
        """
        
        

        self._workspace = None
        self._x_project_id = None
        self._limit = None
        self._offset = None
        self._script_name = None
        self.discriminator = None

        self.workspace = workspace
        if x_project_id is not None:
            self.x_project_id = x_project_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if script_name is not None:
            self.script_name = script_name

    @property
    def workspace(self):
        r"""Gets the workspace of this ListFactoryScriptsRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this ListFactoryScriptsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ListFactoryScriptsRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this ListFactoryScriptsRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def x_project_id(self):
        r"""Gets the x_project_id of this ListFactoryScriptsRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :return: The x_project_id of this ListFactoryScriptsRequest.
        :rtype: str
        """
        return self._x_project_id

    @x_project_id.setter
    def x_project_id(self, x_project_id):
        r"""Sets the x_project_id of this ListFactoryScriptsRequest.

        项目ID，获取方法请参见[项目ID和账号ID](projectid_accountid.xml)。  多project场景采用AK/SK认证的接口请求，则该字段必选。

        :param x_project_id: The x_project_id of this ListFactoryScriptsRequest.
        :type x_project_id: str
        """
        self._x_project_id = x_project_id

    @property
    def limit(self):
        r"""Gets the limit of this ListFactoryScriptsRequest.

        分页返回结果，指定每页最大记录数，范围[1,100]。 默认值：10。

        :return: The limit of this ListFactoryScriptsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListFactoryScriptsRequest.

        分页返回结果，指定每页最大记录数，范围[1,100]。 默认值：10。

        :param limit: The limit of this ListFactoryScriptsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListFactoryScriptsRequest.

        分页的起始页，默认值为0。取值范围大于等于0。

        :return: The offset of this ListFactoryScriptsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListFactoryScriptsRequest.

        分页的起始页，默认值为0。取值范围大于等于0。

        :param offset: The offset of this ListFactoryScriptsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def script_name(self):
        r"""Gets the script_name of this ListFactoryScriptsRequest.

        脚本名称

        :return: The script_name of this ListFactoryScriptsRequest.
        :rtype: str
        """
        return self._script_name

    @script_name.setter
    def script_name(self, script_name):
        r"""Sets the script_name of this ListFactoryScriptsRequest.

        脚本名称

        :param script_name: The script_name of this ListFactoryScriptsRequest.
        :type script_name: str
        """
        self._script_name = script_name

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
        if not isinstance(other, ListFactoryScriptsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
