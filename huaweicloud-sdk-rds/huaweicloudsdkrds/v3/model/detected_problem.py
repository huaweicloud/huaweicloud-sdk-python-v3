# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DetectedProblem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'db_object': 'str',
        'level': 'str',
        'description': 'str'
    }

    attribute_map = {
        'db_object': 'db_object',
        'level': 'level',
        'description': 'description'
    }

    def __init__(self, db_object=None, level=None, description=None):
        r"""DetectedProblem

        The model defined in huaweicloud sdk

        :param db_object: 存在问题的数据库对象
        :type db_object: str
        :param level: 告警级别
        :type level: str
        :param description: 检查项描述
        :type description: str
        """
        
        

        self._db_object = None
        self._level = None
        self._description = None
        self.discriminator = None

        if db_object is not None:
            self.db_object = db_object
        if level is not None:
            self.level = level
        if description is not None:
            self.description = description

    @property
    def db_object(self):
        r"""Gets the db_object of this DetectedProblem.

        存在问题的数据库对象

        :return: The db_object of this DetectedProblem.
        :rtype: str
        """
        return self._db_object

    @db_object.setter
    def db_object(self, db_object):
        r"""Sets the db_object of this DetectedProblem.

        存在问题的数据库对象

        :param db_object: The db_object of this DetectedProblem.
        :type db_object: str
        """
        self._db_object = db_object

    @property
    def level(self):
        r"""Gets the level of this DetectedProblem.

        告警级别

        :return: The level of this DetectedProblem.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this DetectedProblem.

        告警级别

        :param level: The level of this DetectedProblem.
        :type level: str
        """
        self._level = level

    @property
    def description(self):
        r"""Gets the description of this DetectedProblem.

        检查项描述

        :return: The description of this DetectedProblem.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this DetectedProblem.

        检查项描述

        :param description: The description of this DetectedProblem.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, DetectedProblem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
