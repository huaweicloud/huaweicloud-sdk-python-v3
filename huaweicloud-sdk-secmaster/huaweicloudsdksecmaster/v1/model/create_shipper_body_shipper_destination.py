# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateShipperBodyShipperDestination:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_param': 'str',
        'destination_dataspace': 'str',
        'destination_dataspace_name': 'str',
        'destination_identity_role': 'str',
        'destination_table': 'str',
        'destination_table_name': 'str',
        'destination_pipe': 'str',
        'destination_pipe_name': 'str',
        'destination_region': 'str',
        'destination_shipper_type': 'int',
        'destination_workspace': 'str',
        'destination_workspace_name': 'str'
    }

    attribute_map = {
        'data_param': 'data_param',
        'destination_dataspace': 'destination_dataspace',
        'destination_dataspace_name': 'destination_dataspace_name',
        'destination_identity_role': 'destination_identity_role',
        'destination_table': 'destination_table',
        'destination_table_name': 'destination_table_name',
        'destination_pipe': 'destination_pipe',
        'destination_pipe_name': 'destination_pipe_name',
        'destination_region': 'destination_region',
        'destination_shipper_type': 'destination_shipper_type',
        'destination_workspace': 'destination_workspace',
        'destination_workspace_name': 'destination_workspace_name'
    }

    def __init__(self, data_param=None, destination_dataspace=None, destination_dataspace_name=None, destination_identity_role=None, destination_table=None, destination_table_name=None, destination_pipe=None, destination_pipe_name=None, destination_region=None, destination_shipper_type=None, destination_workspace=None, destination_workspace_name=None):
        r"""CreateShipperBodyShipperDestination

        The model defined in huaweicloud sdk

        :param data_param: 数据参数
        :type data_param: str
        :param destination_dataspace: 目标数据空间ID
        :type destination_dataspace: str
        :param destination_dataspace_name: 目标数据空间名称
        :type destination_dataspace_name: str
        :param destination_identity_role: 目标身份角色
        :type destination_identity_role: str
        :param destination_table: 目标表ID
        :type destination_table: str
        :param destination_table_name: 目标表名称
        :type destination_table_name: str
        :param destination_pipe: 目标管道ID
        :type destination_pipe: str
        :param destination_pipe_name: 目标管道名称
        :type destination_pipe_name: str
        :param destination_region: 目标区域信息
        :type destination_region: str
        :param destination_shipper_type: 目标投递类型
        :type destination_shipper_type: int
        :param destination_workspace: 目标工作空间ID
        :type destination_workspace: str
        :param destination_workspace_name: 目标工作空间名称
        :type destination_workspace_name: str
        """
        
        

        self._data_param = None
        self._destination_dataspace = None
        self._destination_dataspace_name = None
        self._destination_identity_role = None
        self._destination_table = None
        self._destination_table_name = None
        self._destination_pipe = None
        self._destination_pipe_name = None
        self._destination_region = None
        self._destination_shipper_type = None
        self._destination_workspace = None
        self._destination_workspace_name = None
        self.discriminator = None

        if data_param is not None:
            self.data_param = data_param
        if destination_dataspace is not None:
            self.destination_dataspace = destination_dataspace
        if destination_dataspace_name is not None:
            self.destination_dataspace_name = destination_dataspace_name
        if destination_identity_role is not None:
            self.destination_identity_role = destination_identity_role
        if destination_table is not None:
            self.destination_table = destination_table
        if destination_table_name is not None:
            self.destination_table_name = destination_table_name
        if destination_pipe is not None:
            self.destination_pipe = destination_pipe
        if destination_pipe_name is not None:
            self.destination_pipe_name = destination_pipe_name
        if destination_region is not None:
            self.destination_region = destination_region
        if destination_shipper_type is not None:
            self.destination_shipper_type = destination_shipper_type
        if destination_workspace is not None:
            self.destination_workspace = destination_workspace
        if destination_workspace_name is not None:
            self.destination_workspace_name = destination_workspace_name

    @property
    def data_param(self):
        r"""Gets the data_param of this CreateShipperBodyShipperDestination.

        数据参数

        :return: The data_param of this CreateShipperBodyShipperDestination.
        :rtype: str
        """
        return self._data_param

    @data_param.setter
    def data_param(self, data_param):
        r"""Sets the data_param of this CreateShipperBodyShipperDestination.

        数据参数

        :param data_param: The data_param of this CreateShipperBodyShipperDestination.
        :type data_param: str
        """
        self._data_param = data_param

    @property
    def destination_dataspace(self):
        r"""Gets the destination_dataspace of this CreateShipperBodyShipperDestination.

        目标数据空间ID

        :return: The destination_dataspace of this CreateShipperBodyShipperDestination.
        :rtype: str
        """
        return self._destination_dataspace

    @destination_dataspace.setter
    def destination_dataspace(self, destination_dataspace):
        r"""Sets the destination_dataspace of this CreateShipperBodyShipperDestination.

        目标数据空间ID

        :param destination_dataspace: The destination_dataspace of this CreateShipperBodyShipperDestination.
        :type destination_dataspace: str
        """
        self._destination_dataspace = destination_dataspace

    @property
    def destination_dataspace_name(self):
        r"""Gets the destination_dataspace_name of this CreateShipperBodyShipperDestination.

        目标数据空间名称

        :return: The destination_dataspace_name of this CreateShipperBodyShipperDestination.
        :rtype: str
        """
        return self._destination_dataspace_name

    @destination_dataspace_name.setter
    def destination_dataspace_name(self, destination_dataspace_name):
        r"""Sets the destination_dataspace_name of this CreateShipperBodyShipperDestination.

        目标数据空间名称

        :param destination_dataspace_name: The destination_dataspace_name of this CreateShipperBodyShipperDestination.
        :type destination_dataspace_name: str
        """
        self._destination_dataspace_name = destination_dataspace_name

    @property
    def destination_identity_role(self):
        r"""Gets the destination_identity_role of this CreateShipperBodyShipperDestination.

        目标身份角色

        :return: The destination_identity_role of this CreateShipperBodyShipperDestination.
        :rtype: str
        """
        return self._destination_identity_role

    @destination_identity_role.setter
    def destination_identity_role(self, destination_identity_role):
        r"""Sets the destination_identity_role of this CreateShipperBodyShipperDestination.

        目标身份角色

        :param destination_identity_role: The destination_identity_role of this CreateShipperBodyShipperDestination.
        :type destination_identity_role: str
        """
        self._destination_identity_role = destination_identity_role

    @property
    def destination_table(self):
        r"""Gets the destination_table of this CreateShipperBodyShipperDestination.

        目标表ID

        :return: The destination_table of this CreateShipperBodyShipperDestination.
        :rtype: str
        """
        return self._destination_table

    @destination_table.setter
    def destination_table(self, destination_table):
        r"""Sets the destination_table of this CreateShipperBodyShipperDestination.

        目标表ID

        :param destination_table: The destination_table of this CreateShipperBodyShipperDestination.
        :type destination_table: str
        """
        self._destination_table = destination_table

    @property
    def destination_table_name(self):
        r"""Gets the destination_table_name of this CreateShipperBodyShipperDestination.

        目标表名称

        :return: The destination_table_name of this CreateShipperBodyShipperDestination.
        :rtype: str
        """
        return self._destination_table_name

    @destination_table_name.setter
    def destination_table_name(self, destination_table_name):
        r"""Sets the destination_table_name of this CreateShipperBodyShipperDestination.

        目标表名称

        :param destination_table_name: The destination_table_name of this CreateShipperBodyShipperDestination.
        :type destination_table_name: str
        """
        self._destination_table_name = destination_table_name

    @property
    def destination_pipe(self):
        r"""Gets the destination_pipe of this CreateShipperBodyShipperDestination.

        目标管道ID

        :return: The destination_pipe of this CreateShipperBodyShipperDestination.
        :rtype: str
        """
        return self._destination_pipe

    @destination_pipe.setter
    def destination_pipe(self, destination_pipe):
        r"""Sets the destination_pipe of this CreateShipperBodyShipperDestination.

        目标管道ID

        :param destination_pipe: The destination_pipe of this CreateShipperBodyShipperDestination.
        :type destination_pipe: str
        """
        self._destination_pipe = destination_pipe

    @property
    def destination_pipe_name(self):
        r"""Gets the destination_pipe_name of this CreateShipperBodyShipperDestination.

        目标管道名称

        :return: The destination_pipe_name of this CreateShipperBodyShipperDestination.
        :rtype: str
        """
        return self._destination_pipe_name

    @destination_pipe_name.setter
    def destination_pipe_name(self, destination_pipe_name):
        r"""Sets the destination_pipe_name of this CreateShipperBodyShipperDestination.

        目标管道名称

        :param destination_pipe_name: The destination_pipe_name of this CreateShipperBodyShipperDestination.
        :type destination_pipe_name: str
        """
        self._destination_pipe_name = destination_pipe_name

    @property
    def destination_region(self):
        r"""Gets the destination_region of this CreateShipperBodyShipperDestination.

        目标区域信息

        :return: The destination_region of this CreateShipperBodyShipperDestination.
        :rtype: str
        """
        return self._destination_region

    @destination_region.setter
    def destination_region(self, destination_region):
        r"""Sets the destination_region of this CreateShipperBodyShipperDestination.

        目标区域信息

        :param destination_region: The destination_region of this CreateShipperBodyShipperDestination.
        :type destination_region: str
        """
        self._destination_region = destination_region

    @property
    def destination_shipper_type(self):
        r"""Gets the destination_shipper_type of this CreateShipperBodyShipperDestination.

        目标投递类型

        :return: The destination_shipper_type of this CreateShipperBodyShipperDestination.
        :rtype: int
        """
        return self._destination_shipper_type

    @destination_shipper_type.setter
    def destination_shipper_type(self, destination_shipper_type):
        r"""Sets the destination_shipper_type of this CreateShipperBodyShipperDestination.

        目标投递类型

        :param destination_shipper_type: The destination_shipper_type of this CreateShipperBodyShipperDestination.
        :type destination_shipper_type: int
        """
        self._destination_shipper_type = destination_shipper_type

    @property
    def destination_workspace(self):
        r"""Gets the destination_workspace of this CreateShipperBodyShipperDestination.

        目标工作空间ID

        :return: The destination_workspace of this CreateShipperBodyShipperDestination.
        :rtype: str
        """
        return self._destination_workspace

    @destination_workspace.setter
    def destination_workspace(self, destination_workspace):
        r"""Sets the destination_workspace of this CreateShipperBodyShipperDestination.

        目标工作空间ID

        :param destination_workspace: The destination_workspace of this CreateShipperBodyShipperDestination.
        :type destination_workspace: str
        """
        self._destination_workspace = destination_workspace

    @property
    def destination_workspace_name(self):
        r"""Gets the destination_workspace_name of this CreateShipperBodyShipperDestination.

        目标工作空间名称

        :return: The destination_workspace_name of this CreateShipperBodyShipperDestination.
        :rtype: str
        """
        return self._destination_workspace_name

    @destination_workspace_name.setter
    def destination_workspace_name(self, destination_workspace_name):
        r"""Sets the destination_workspace_name of this CreateShipperBodyShipperDestination.

        目标工作空间名称

        :param destination_workspace_name: The destination_workspace_name of this CreateShipperBodyShipperDestination.
        :type destination_workspace_name: str
        """
        self._destination_workspace_name = destination_workspace_name

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
        if not isinstance(other, CreateShipperBodyShipperDestination):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
