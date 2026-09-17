# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFullSqlSampleRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'sql_template_id': 'str',
        'start_at': 'int',
        'end_at': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'sql_template_id': 'sql_template_id',
        'start_at': 'start_at',
        'end_at': 'end_at'
    }

    def __init__(self, instance_id=None, sql_template_id=None, start_at=None, end_at=None):
        r"""ShowFullSqlSampleRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param sql_template_id: SQL模板ID
        :type sql_template_id: str
        :param start_at: 开始时间戳（ms）
        :type start_at: int
        :param end_at: 结束时间戳（ms）
        :type end_at: int
        """
        
        

        self._instance_id = None
        self._sql_template_id = None
        self._start_at = None
        self._end_at = None
        self.discriminator = None

        self.instance_id = instance_id
        self.sql_template_id = sql_template_id
        self.start_at = start_at
        self.end_at = end_at

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowFullSqlSampleRequest.

        实例ID

        :return: The instance_id of this ShowFullSqlSampleRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowFullSqlSampleRequest.

        实例ID

        :param instance_id: The instance_id of this ShowFullSqlSampleRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def sql_template_id(self):
        r"""Gets the sql_template_id of this ShowFullSqlSampleRequest.

        SQL模板ID

        :return: The sql_template_id of this ShowFullSqlSampleRequest.
        :rtype: str
        """
        return self._sql_template_id

    @sql_template_id.setter
    def sql_template_id(self, sql_template_id):
        r"""Sets the sql_template_id of this ShowFullSqlSampleRequest.

        SQL模板ID

        :param sql_template_id: The sql_template_id of this ShowFullSqlSampleRequest.
        :type sql_template_id: str
        """
        self._sql_template_id = sql_template_id

    @property
    def start_at(self):
        r"""Gets the start_at of this ShowFullSqlSampleRequest.

        开始时间戳（ms）

        :return: The start_at of this ShowFullSqlSampleRequest.
        :rtype: int
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        r"""Sets the start_at of this ShowFullSqlSampleRequest.

        开始时间戳（ms）

        :param start_at: The start_at of this ShowFullSqlSampleRequest.
        :type start_at: int
        """
        self._start_at = start_at

    @property
    def end_at(self):
        r"""Gets the end_at of this ShowFullSqlSampleRequest.

        结束时间戳（ms）

        :return: The end_at of this ShowFullSqlSampleRequest.
        :rtype: int
        """
        return self._end_at

    @end_at.setter
    def end_at(self, end_at):
        r"""Sets the end_at of this ShowFullSqlSampleRequest.

        结束时间戳（ms）

        :param end_at: The end_at of this ShowFullSqlSampleRequest.
        :type end_at: int
        """
        self._end_at = end_at

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
        if not isinstance(other, ShowFullSqlSampleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
