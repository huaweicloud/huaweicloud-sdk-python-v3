# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDataServiceInstancesOverviewRequest:

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
        'dlm_type': 'str',
        'limit': 'int',
        'offset': 'int',
        'name': 'str',
        'create_user': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'dlm_type': 'Dlm-Type',
        'limit': 'limit',
        'offset': 'offset',
        'name': 'name',
        'create_user': 'create_user'
    }

    def __init__(self, workspace=None, dlm_type=None, limit=None, offset=None, name=None, create_user=None):
        r"""ListDataServiceInstancesOverviewRequest

        The model defined in huaweicloud sdk

        :param workspace: 工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。
        :type workspace: str
        :param dlm_type: 数据服务的版本类型，指定SHARED共享版或EXCLUSIVE专享版。
        :type dlm_type: str
        :param limit: 查询条数限制。
        :type limit: int
        :param offset: 查询起始坐标。
        :type offset: int
        :param name: 集群名称。
        :type name: str
        :param create_user: 创建人名称。
        :type create_user: str
        """
        
        

        self._workspace = None
        self._dlm_type = None
        self._limit = None
        self._offset = None
        self._name = None
        self._create_user = None
        self.discriminator = None

        self.workspace = workspace
        if dlm_type is not None:
            self.dlm_type = dlm_type
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if name is not None:
            self.name = name
        if create_user is not None:
            self.create_user = create_user

    @property
    def workspace(self):
        r"""Gets the workspace of this ListDataServiceInstancesOverviewRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :return: The workspace of this ListDataServiceInstancesOverviewRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ListDataServiceInstancesOverviewRequest.

        工作空间ID，获取方法请参见[实例ID和工作空间ID](dataartsstudio_02_0350.xml)。

        :param workspace: The workspace of this ListDataServiceInstancesOverviewRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def dlm_type(self):
        r"""Gets the dlm_type of this ListDataServiceInstancesOverviewRequest.

        数据服务的版本类型，指定SHARED共享版或EXCLUSIVE专享版。

        :return: The dlm_type of this ListDataServiceInstancesOverviewRequest.
        :rtype: str
        """
        return self._dlm_type

    @dlm_type.setter
    def dlm_type(self, dlm_type):
        r"""Sets the dlm_type of this ListDataServiceInstancesOverviewRequest.

        数据服务的版本类型，指定SHARED共享版或EXCLUSIVE专享版。

        :param dlm_type: The dlm_type of this ListDataServiceInstancesOverviewRequest.
        :type dlm_type: str
        """
        self._dlm_type = dlm_type

    @property
    def limit(self):
        r"""Gets the limit of this ListDataServiceInstancesOverviewRequest.

        查询条数限制。

        :return: The limit of this ListDataServiceInstancesOverviewRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDataServiceInstancesOverviewRequest.

        查询条数限制。

        :param limit: The limit of this ListDataServiceInstancesOverviewRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListDataServiceInstancesOverviewRequest.

        查询起始坐标。

        :return: The offset of this ListDataServiceInstancesOverviewRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListDataServiceInstancesOverviewRequest.

        查询起始坐标。

        :param offset: The offset of this ListDataServiceInstancesOverviewRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def name(self):
        r"""Gets the name of this ListDataServiceInstancesOverviewRequest.

        集群名称。

        :return: The name of this ListDataServiceInstancesOverviewRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListDataServiceInstancesOverviewRequest.

        集群名称。

        :param name: The name of this ListDataServiceInstancesOverviewRequest.
        :type name: str
        """
        self._name = name

    @property
    def create_user(self):
        r"""Gets the create_user of this ListDataServiceInstancesOverviewRequest.

        创建人名称。

        :return: The create_user of this ListDataServiceInstancesOverviewRequest.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this ListDataServiceInstancesOverviewRequest.

        创建人名称。

        :param create_user: The create_user of this ListDataServiceInstancesOverviewRequest.
        :type create_user: str
        """
        self._create_user = create_user

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
        if not isinstance(other, ListDataServiceInstancesOverviewRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
