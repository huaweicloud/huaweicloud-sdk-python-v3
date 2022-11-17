# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Error:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'detail': 'str',
        'ief_instance_id': 'str',
        'project_id': 'str',
        'rule_id': 'str',
        'time': 'str'
    }

    attribute_map = {
        'detail': 'detail',
        'ief_instance_id': 'ief_instance_id',
        'project_id': 'project_id',
        'rule_id': 'rule_id',
        'time': 'time'
    }

    def __init__(self, detail=None, ief_instance_id=None, project_id=None, rule_id=None, time=None):
        """Error

        The model defined in huaweicloud sdk

        :param detail: 错误详情
        :type detail: str
        :param ief_instance_id: 铂金版实例ID，如果为空则表示是专业版实例。
        :type ief_instance_id: str
        :param project_id: 项目ID
        :type project_id: str
        :param rule_id: 规则ID
        :type rule_id: str
        :param time: 错误发生的时间
        :type time: str
        """
        
        

        self._detail = None
        self._ief_instance_id = None
        self._project_id = None
        self._rule_id = None
        self._time = None
        self.discriminator = None

        self.detail = detail
        self.ief_instance_id = ief_instance_id
        self.project_id = project_id
        self.rule_id = rule_id
        self.time = time

    @property
    def detail(self):
        """Gets the detail of this Error.

        错误详情

        :return: The detail of this Error.
        :rtype: str
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this Error.

        错误详情

        :param detail: The detail of this Error.
        :type detail: str
        """
        self._detail = detail

    @property
    def ief_instance_id(self):
        """Gets the ief_instance_id of this Error.

        铂金版实例ID，如果为空则表示是专业版实例。

        :return: The ief_instance_id of this Error.
        :rtype: str
        """
        return self._ief_instance_id

    @ief_instance_id.setter
    def ief_instance_id(self, ief_instance_id):
        """Sets the ief_instance_id of this Error.

        铂金版实例ID，如果为空则表示是专业版实例。

        :param ief_instance_id: The ief_instance_id of this Error.
        :type ief_instance_id: str
        """
        self._ief_instance_id = ief_instance_id

    @property
    def project_id(self):
        """Gets the project_id of this Error.

        项目ID

        :return: The project_id of this Error.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Error.

        项目ID

        :param project_id: The project_id of this Error.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def rule_id(self):
        """Gets the rule_id of this Error.

        规则ID

        :return: The rule_id of this Error.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this Error.

        规则ID

        :param rule_id: The rule_id of this Error.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def time(self):
        """Gets the time of this Error.

        错误发生的时间

        :return: The time of this Error.
        :rtype: str
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this Error.

        错误发生的时间

        :param time: The time of this Error.
        :type time: str
        """
        self._time = time

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
        if not isinstance(other, Error):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
