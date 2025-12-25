# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateShipperBodyShipperSource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'region': 'str',
        'source_dataspace': 'str',
        'source_dataspace_name': 'str',
        'source_identity_role': 'str',
        'source_table': 'str',
        'source_table_name': 'str',
        'source_pipe': 'str',
        'source_pipe_name': 'str',
        'source_type': 'int',
        'source_workspace': 'str',
        'source_workspace_name': 'str'
    }

    attribute_map = {
        'region': 'region',
        'source_dataspace': 'source_dataspace',
        'source_dataspace_name': 'source_dataspace_name',
        'source_identity_role': 'source_identity_role',
        'source_table': 'source_table',
        'source_table_name': 'source_table_name',
        'source_pipe': 'source_pipe',
        'source_pipe_name': 'source_pipe_name',
        'source_type': 'source_type',
        'source_workspace': 'source_workspace',
        'source_workspace_name': 'source_workspace_name'
    }

    def __init__(self, region=None, source_dataspace=None, source_dataspace_name=None, source_identity_role=None, source_table=None, source_table_name=None, source_pipe=None, source_pipe_name=None, source_type=None, source_workspace=None, source_workspace_name=None):
        r"""CreateShipperBodyShipperSource

        The model defined in huaweicloud sdk

        :param region: 区域信息
        :type region: str
        :param source_dataspace: 源数据空间ID
        :type source_dataspace: str
        :param source_dataspace_name: 源数据空间名称
        :type source_dataspace_name: str
        :param source_identity_role: 源身份角色
        :type source_identity_role: str
        :param source_table: 源表ID
        :type source_table: str
        :param source_table_name: 源表名称
        :type source_table_name: str
        :param source_pipe: 源管道ID
        :type source_pipe: str
        :param source_pipe_name: 源管道名称
        :type source_pipe_name: str
        :param source_type: 源类型
        :type source_type: int
        :param source_workspace: 源工作空间ID
        :type source_workspace: str
        :param source_workspace_name: 源工作空间名称
        :type source_workspace_name: str
        """
        
        

        self._region = None
        self._source_dataspace = None
        self._source_dataspace_name = None
        self._source_identity_role = None
        self._source_table = None
        self._source_table_name = None
        self._source_pipe = None
        self._source_pipe_name = None
        self._source_type = None
        self._source_workspace = None
        self._source_workspace_name = None
        self.discriminator = None

        if region is not None:
            self.region = region
        if source_dataspace is not None:
            self.source_dataspace = source_dataspace
        if source_dataspace_name is not None:
            self.source_dataspace_name = source_dataspace_name
        if source_identity_role is not None:
            self.source_identity_role = source_identity_role
        if source_table is not None:
            self.source_table = source_table
        if source_table_name is not None:
            self.source_table_name = source_table_name
        if source_pipe is not None:
            self.source_pipe = source_pipe
        if source_pipe_name is not None:
            self.source_pipe_name = source_pipe_name
        if source_type is not None:
            self.source_type = source_type
        if source_workspace is not None:
            self.source_workspace = source_workspace
        if source_workspace_name is not None:
            self.source_workspace_name = source_workspace_name

    @property
    def region(self):
        r"""Gets the region of this CreateShipperBodyShipperSource.

        区域信息

        :return: The region of this CreateShipperBodyShipperSource.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this CreateShipperBodyShipperSource.

        区域信息

        :param region: The region of this CreateShipperBodyShipperSource.
        :type region: str
        """
        self._region = region

    @property
    def source_dataspace(self):
        r"""Gets the source_dataspace of this CreateShipperBodyShipperSource.

        源数据空间ID

        :return: The source_dataspace of this CreateShipperBodyShipperSource.
        :rtype: str
        """
        return self._source_dataspace

    @source_dataspace.setter
    def source_dataspace(self, source_dataspace):
        r"""Sets the source_dataspace of this CreateShipperBodyShipperSource.

        源数据空间ID

        :param source_dataspace: The source_dataspace of this CreateShipperBodyShipperSource.
        :type source_dataspace: str
        """
        self._source_dataspace = source_dataspace

    @property
    def source_dataspace_name(self):
        r"""Gets the source_dataspace_name of this CreateShipperBodyShipperSource.

        源数据空间名称

        :return: The source_dataspace_name of this CreateShipperBodyShipperSource.
        :rtype: str
        """
        return self._source_dataspace_name

    @source_dataspace_name.setter
    def source_dataspace_name(self, source_dataspace_name):
        r"""Sets the source_dataspace_name of this CreateShipperBodyShipperSource.

        源数据空间名称

        :param source_dataspace_name: The source_dataspace_name of this CreateShipperBodyShipperSource.
        :type source_dataspace_name: str
        """
        self._source_dataspace_name = source_dataspace_name

    @property
    def source_identity_role(self):
        r"""Gets the source_identity_role of this CreateShipperBodyShipperSource.

        源身份角色

        :return: The source_identity_role of this CreateShipperBodyShipperSource.
        :rtype: str
        """
        return self._source_identity_role

    @source_identity_role.setter
    def source_identity_role(self, source_identity_role):
        r"""Sets the source_identity_role of this CreateShipperBodyShipperSource.

        源身份角色

        :param source_identity_role: The source_identity_role of this CreateShipperBodyShipperSource.
        :type source_identity_role: str
        """
        self._source_identity_role = source_identity_role

    @property
    def source_table(self):
        r"""Gets the source_table of this CreateShipperBodyShipperSource.

        源表ID

        :return: The source_table of this CreateShipperBodyShipperSource.
        :rtype: str
        """
        return self._source_table

    @source_table.setter
    def source_table(self, source_table):
        r"""Sets the source_table of this CreateShipperBodyShipperSource.

        源表ID

        :param source_table: The source_table of this CreateShipperBodyShipperSource.
        :type source_table: str
        """
        self._source_table = source_table

    @property
    def source_table_name(self):
        r"""Gets the source_table_name of this CreateShipperBodyShipperSource.

        源表名称

        :return: The source_table_name of this CreateShipperBodyShipperSource.
        :rtype: str
        """
        return self._source_table_name

    @source_table_name.setter
    def source_table_name(self, source_table_name):
        r"""Sets the source_table_name of this CreateShipperBodyShipperSource.

        源表名称

        :param source_table_name: The source_table_name of this CreateShipperBodyShipperSource.
        :type source_table_name: str
        """
        self._source_table_name = source_table_name

    @property
    def source_pipe(self):
        r"""Gets the source_pipe of this CreateShipperBodyShipperSource.

        源管道ID

        :return: The source_pipe of this CreateShipperBodyShipperSource.
        :rtype: str
        """
        return self._source_pipe

    @source_pipe.setter
    def source_pipe(self, source_pipe):
        r"""Sets the source_pipe of this CreateShipperBodyShipperSource.

        源管道ID

        :param source_pipe: The source_pipe of this CreateShipperBodyShipperSource.
        :type source_pipe: str
        """
        self._source_pipe = source_pipe

    @property
    def source_pipe_name(self):
        r"""Gets the source_pipe_name of this CreateShipperBodyShipperSource.

        源管道名称

        :return: The source_pipe_name of this CreateShipperBodyShipperSource.
        :rtype: str
        """
        return self._source_pipe_name

    @source_pipe_name.setter
    def source_pipe_name(self, source_pipe_name):
        r"""Sets the source_pipe_name of this CreateShipperBodyShipperSource.

        源管道名称

        :param source_pipe_name: The source_pipe_name of this CreateShipperBodyShipperSource.
        :type source_pipe_name: str
        """
        self._source_pipe_name = source_pipe_name

    @property
    def source_type(self):
        r"""Gets the source_type of this CreateShipperBodyShipperSource.

        源类型

        :return: The source_type of this CreateShipperBodyShipperSource.
        :rtype: int
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        r"""Sets the source_type of this CreateShipperBodyShipperSource.

        源类型

        :param source_type: The source_type of this CreateShipperBodyShipperSource.
        :type source_type: int
        """
        self._source_type = source_type

    @property
    def source_workspace(self):
        r"""Gets the source_workspace of this CreateShipperBodyShipperSource.

        源工作空间ID

        :return: The source_workspace of this CreateShipperBodyShipperSource.
        :rtype: str
        """
        return self._source_workspace

    @source_workspace.setter
    def source_workspace(self, source_workspace):
        r"""Sets the source_workspace of this CreateShipperBodyShipperSource.

        源工作空间ID

        :param source_workspace: The source_workspace of this CreateShipperBodyShipperSource.
        :type source_workspace: str
        """
        self._source_workspace = source_workspace

    @property
    def source_workspace_name(self):
        r"""Gets the source_workspace_name of this CreateShipperBodyShipperSource.

        源工作空间名称

        :return: The source_workspace_name of this CreateShipperBodyShipperSource.
        :rtype: str
        """
        return self._source_workspace_name

    @source_workspace_name.setter
    def source_workspace_name(self, source_workspace_name):
        r"""Sets the source_workspace_name of this CreateShipperBodyShipperSource.

        源工作空间名称

        :param source_workspace_name: The source_workspace_name of this CreateShipperBodyShipperSource.
        :type source_workspace_name: str
        """
        self._source_workspace_name = source_workspace_name

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
        if not isinstance(other, CreateShipperBodyShipperSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
