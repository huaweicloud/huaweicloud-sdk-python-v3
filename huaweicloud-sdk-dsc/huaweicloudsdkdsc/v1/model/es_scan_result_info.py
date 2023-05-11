# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EsScanResultInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'task_id': 'str',
        'index_name': 'str',
        'type_id': 'str',
        'type_name': 'str',
        'risk_level': 'int',
        'sensitive_data_type': 'list[str]',
        'match_info': 'list[EsMatchInfo]'
    }

    attribute_map = {
        'task_id': 'task_id',
        'index_name': 'index_name',
        'type_id': 'type_id',
        'type_name': 'type_name',
        'risk_level': 'risk_level',
        'sensitive_data_type': 'sensitive_data_type',
        'match_info': 'match_info'
    }

    def __init__(self, task_id=None, index_name=None, type_id=None, type_name=None, risk_level=None, sensitive_data_type=None, match_info=None):
        """EsScanResultInfo

        The model defined in huaweicloud sdk

        :param task_id: 任务ID
        :type task_id: str
        :param index_name: 索引名
        :type index_name: str
        :param type_id: 类型ID
        :type type_id: str
        :param type_name: 类型名
        :type type_name: str
        :param risk_level: 风险等级
        :type risk_level: int
        :param sensitive_data_type: 敏感数据类型
        :type sensitive_data_type: list[str]
        :param match_info: 规则匹配具体信息
        :type match_info: list[:class:`huaweicloudsdkdsc.v1.EsMatchInfo`]
        """
        
        

        self._task_id = None
        self._index_name = None
        self._type_id = None
        self._type_name = None
        self._risk_level = None
        self._sensitive_data_type = None
        self._match_info = None
        self.discriminator = None

        if task_id is not None:
            self.task_id = task_id
        if index_name is not None:
            self.index_name = index_name
        if type_id is not None:
            self.type_id = type_id
        if type_name is not None:
            self.type_name = type_name
        if risk_level is not None:
            self.risk_level = risk_level
        if sensitive_data_type is not None:
            self.sensitive_data_type = sensitive_data_type
        if match_info is not None:
            self.match_info = match_info

    @property
    def task_id(self):
        """Gets the task_id of this EsScanResultInfo.

        任务ID

        :return: The task_id of this EsScanResultInfo.
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this EsScanResultInfo.

        任务ID

        :param task_id: The task_id of this EsScanResultInfo.
        :type task_id: str
        """
        self._task_id = task_id

    @property
    def index_name(self):
        """Gets the index_name of this EsScanResultInfo.

        索引名

        :return: The index_name of this EsScanResultInfo.
        :rtype: str
        """
        return self._index_name

    @index_name.setter
    def index_name(self, index_name):
        """Sets the index_name of this EsScanResultInfo.

        索引名

        :param index_name: The index_name of this EsScanResultInfo.
        :type index_name: str
        """
        self._index_name = index_name

    @property
    def type_id(self):
        """Gets the type_id of this EsScanResultInfo.

        类型ID

        :return: The type_id of this EsScanResultInfo.
        :rtype: str
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this EsScanResultInfo.

        类型ID

        :param type_id: The type_id of this EsScanResultInfo.
        :type type_id: str
        """
        self._type_id = type_id

    @property
    def type_name(self):
        """Gets the type_name of this EsScanResultInfo.

        类型名

        :return: The type_name of this EsScanResultInfo.
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        """Sets the type_name of this EsScanResultInfo.

        类型名

        :param type_name: The type_name of this EsScanResultInfo.
        :type type_name: str
        """
        self._type_name = type_name

    @property
    def risk_level(self):
        """Gets the risk_level of this EsScanResultInfo.

        风险等级

        :return: The risk_level of this EsScanResultInfo.
        :rtype: int
        """
        return self._risk_level

    @risk_level.setter
    def risk_level(self, risk_level):
        """Sets the risk_level of this EsScanResultInfo.

        风险等级

        :param risk_level: The risk_level of this EsScanResultInfo.
        :type risk_level: int
        """
        self._risk_level = risk_level

    @property
    def sensitive_data_type(self):
        """Gets the sensitive_data_type of this EsScanResultInfo.

        敏感数据类型

        :return: The sensitive_data_type of this EsScanResultInfo.
        :rtype: list[str]
        """
        return self._sensitive_data_type

    @sensitive_data_type.setter
    def sensitive_data_type(self, sensitive_data_type):
        """Sets the sensitive_data_type of this EsScanResultInfo.

        敏感数据类型

        :param sensitive_data_type: The sensitive_data_type of this EsScanResultInfo.
        :type sensitive_data_type: list[str]
        """
        self._sensitive_data_type = sensitive_data_type

    @property
    def match_info(self):
        """Gets the match_info of this EsScanResultInfo.

        规则匹配具体信息

        :return: The match_info of this EsScanResultInfo.
        :rtype: list[:class:`huaweicloudsdkdsc.v1.EsMatchInfo`]
        """
        return self._match_info

    @match_info.setter
    def match_info(self, match_info):
        """Sets the match_info of this EsScanResultInfo.

        规则匹配具体信息

        :param match_info: The match_info of this EsScanResultInfo.
        :type match_info: list[:class:`huaweicloudsdkdsc.v1.EsMatchInfo`]
        """
        self._match_info = match_info

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
        if not isinstance(other, EsScanResultInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
