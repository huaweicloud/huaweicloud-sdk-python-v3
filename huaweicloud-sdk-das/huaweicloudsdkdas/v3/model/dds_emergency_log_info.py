# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DDSEmergencyLogInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'int',
        'execute_sql': 'str',
        'create_at': 'int'
    }

    attribute_map = {
        'id': 'id',
        'execute_sql': 'execute_sql',
        'create_at': 'create_at'
    }

    def __init__(self, id=None, execute_sql=None, create_at=None):
        r"""DDSEmergencyLogInfo

        The model defined in huaweicloud sdk

        :param id: ID
        :type id: int
        :param execute_sql: 执行SQL
        :type execute_sql: str
        :param create_at: 创建时间
        :type create_at: int
        """
        
        

        self._id = None
        self._execute_sql = None
        self._create_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if execute_sql is not None:
            self.execute_sql = execute_sql
        if create_at is not None:
            self.create_at = create_at

    @property
    def id(self):
        r"""Gets the id of this DDSEmergencyLogInfo.

        ID

        :return: The id of this DDSEmergencyLogInfo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this DDSEmergencyLogInfo.

        ID

        :param id: The id of this DDSEmergencyLogInfo.
        :type id: int
        """
        self._id = id

    @property
    def execute_sql(self):
        r"""Gets the execute_sql of this DDSEmergencyLogInfo.

        执行SQL

        :return: The execute_sql of this DDSEmergencyLogInfo.
        :rtype: str
        """
        return self._execute_sql

    @execute_sql.setter
    def execute_sql(self, execute_sql):
        r"""Sets the execute_sql of this DDSEmergencyLogInfo.

        执行SQL

        :param execute_sql: The execute_sql of this DDSEmergencyLogInfo.
        :type execute_sql: str
        """
        self._execute_sql = execute_sql

    @property
    def create_at(self):
        r"""Gets the create_at of this DDSEmergencyLogInfo.

        创建时间

        :return: The create_at of this DDSEmergencyLogInfo.
        :rtype: int
        """
        return self._create_at

    @create_at.setter
    def create_at(self, create_at):
        r"""Sets the create_at of this DDSEmergencyLogInfo.

        创建时间

        :param create_at: The create_at of this DDSEmergencyLogInfo.
        :type create_at: int
        """
        self._create_at = create_at

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
        if not isinstance(other, DDSEmergencyLogInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
