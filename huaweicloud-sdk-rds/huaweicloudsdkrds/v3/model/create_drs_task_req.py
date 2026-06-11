# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDrsTaskReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'target_instance_id': 'str',
        'target_user_name': 'str',
        'target_user_password': 'str',
        'source_user_name': 'str',
        'source_user_password': 'str',
        'enterprise_project_id': 'str',
        'drs_node_type': 'str',
        'database_list': 'list[str]'
    }

    attribute_map = {
        'target_instance_id': 'target_instance_id',
        'target_user_name': 'target_user_name',
        'target_user_password': 'target_user_password',
        'source_user_name': 'source_user_name',
        'source_user_password': 'source_user_password',
        'enterprise_project_id': 'enterprise_project_id',
        'drs_node_type': 'drs_node_type',
        'database_list': 'database_list'
    }

    def __init__(self, target_instance_id=None, target_user_name=None, target_user_password=None, source_user_name=None, source_user_password=None, enterprise_project_id=None, drs_node_type=None, database_list=None):
        r"""CreateDrsTaskReq

        The model defined in huaweicloud sdk

        :param target_instance_id: 目标实例id
        :type target_instance_id: str
        :param target_user_name: 目标实例用户账号
        :type target_user_name: str
        :param target_user_password: 目标实例用户密码
        :type target_user_password: str
        :param source_user_name: 源实例用户账号
        :type source_user_name: str
        :param source_user_password: 源实例用户密码
        :type source_user_password: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        :param drs_node_type: Drs实例规格
        :type drs_node_type: str
        :param database_list: 数据库名称
        :type database_list: list[str]
        """
        
        

        self._target_instance_id = None
        self._target_user_name = None
        self._target_user_password = None
        self._source_user_name = None
        self._source_user_password = None
        self._enterprise_project_id = None
        self._drs_node_type = None
        self._database_list = None
        self.discriminator = None

        self.target_instance_id = target_instance_id
        self.target_user_name = target_user_name
        self.target_user_password = target_user_password
        self.source_user_name = source_user_name
        self.source_user_password = source_user_password
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.drs_node_type = drs_node_type
        self.database_list = database_list

    @property
    def target_instance_id(self):
        r"""Gets the target_instance_id of this CreateDrsTaskReq.

        目标实例id

        :return: The target_instance_id of this CreateDrsTaskReq.
        :rtype: str
        """
        return self._target_instance_id

    @target_instance_id.setter
    def target_instance_id(self, target_instance_id):
        r"""Sets the target_instance_id of this CreateDrsTaskReq.

        目标实例id

        :param target_instance_id: The target_instance_id of this CreateDrsTaskReq.
        :type target_instance_id: str
        """
        self._target_instance_id = target_instance_id

    @property
    def target_user_name(self):
        r"""Gets the target_user_name of this CreateDrsTaskReq.

        目标实例用户账号

        :return: The target_user_name of this CreateDrsTaskReq.
        :rtype: str
        """
        return self._target_user_name

    @target_user_name.setter
    def target_user_name(self, target_user_name):
        r"""Sets the target_user_name of this CreateDrsTaskReq.

        目标实例用户账号

        :param target_user_name: The target_user_name of this CreateDrsTaskReq.
        :type target_user_name: str
        """
        self._target_user_name = target_user_name

    @property
    def target_user_password(self):
        r"""Gets the target_user_password of this CreateDrsTaskReq.

        目标实例用户密码

        :return: The target_user_password of this CreateDrsTaskReq.
        :rtype: str
        """
        return self._target_user_password

    @target_user_password.setter
    def target_user_password(self, target_user_password):
        r"""Sets the target_user_password of this CreateDrsTaskReq.

        目标实例用户密码

        :param target_user_password: The target_user_password of this CreateDrsTaskReq.
        :type target_user_password: str
        """
        self._target_user_password = target_user_password

    @property
    def source_user_name(self):
        r"""Gets the source_user_name of this CreateDrsTaskReq.

        源实例用户账号

        :return: The source_user_name of this CreateDrsTaskReq.
        :rtype: str
        """
        return self._source_user_name

    @source_user_name.setter
    def source_user_name(self, source_user_name):
        r"""Sets the source_user_name of this CreateDrsTaskReq.

        源实例用户账号

        :param source_user_name: The source_user_name of this CreateDrsTaskReq.
        :type source_user_name: str
        """
        self._source_user_name = source_user_name

    @property
    def source_user_password(self):
        r"""Gets the source_user_password of this CreateDrsTaskReq.

        源实例用户密码

        :return: The source_user_password of this CreateDrsTaskReq.
        :rtype: str
        """
        return self._source_user_password

    @source_user_password.setter
    def source_user_password(self, source_user_password):
        r"""Sets the source_user_password of this CreateDrsTaskReq.

        源实例用户密码

        :param source_user_password: The source_user_password of this CreateDrsTaskReq.
        :type source_user_password: str
        """
        self._source_user_password = source_user_password

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateDrsTaskReq.

        企业项目id

        :return: The enterprise_project_id of this CreateDrsTaskReq.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateDrsTaskReq.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this CreateDrsTaskReq.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def drs_node_type(self):
        r"""Gets the drs_node_type of this CreateDrsTaskReq.

        Drs实例规格

        :return: The drs_node_type of this CreateDrsTaskReq.
        :rtype: str
        """
        return self._drs_node_type

    @drs_node_type.setter
    def drs_node_type(self, drs_node_type):
        r"""Sets the drs_node_type of this CreateDrsTaskReq.

        Drs实例规格

        :param drs_node_type: The drs_node_type of this CreateDrsTaskReq.
        :type drs_node_type: str
        """
        self._drs_node_type = drs_node_type

    @property
    def database_list(self):
        r"""Gets the database_list of this CreateDrsTaskReq.

        数据库名称

        :return: The database_list of this CreateDrsTaskReq.
        :rtype: list[str]
        """
        return self._database_list

    @database_list.setter
    def database_list(self, database_list):
        r"""Sets the database_list of this CreateDrsTaskReq.

        数据库名称

        :param database_list: The database_list of this CreateDrsTaskReq.
        :type database_list: list[str]
        """
        self._database_list = database_list

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
        if not isinstance(other, CreateDrsTaskReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
