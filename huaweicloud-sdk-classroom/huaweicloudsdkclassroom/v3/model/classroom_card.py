# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClassroomCard:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'classroom_id': 'str',
        'name': 'str',
        'description': 'str',
        'credit': 'float',
        'status': 'str'
    }

    attribute_map = {
        'classroom_id': 'classroom_id',
        'name': 'name',
        'description': 'description',
        'credit': 'credit',
        'status': 'status'
    }

    def __init__(self, classroom_id=None, name=None, description=None, credit=None, status=None):
        r"""ClassroomCard

        The model defined in huaweicloud sdk

        :param classroom_id: 课堂ID
        :type classroom_id: str
        :param name: 课堂名称
        :type name: str
        :param description: 课堂描述
        :type description: str
        :param credit: 课堂学分
        :type credit: float
        :param status: 课堂当前的状态，normal：课堂处于正常状态，archive：课堂已归档
        :type status: str
        """
        
        

        self._classroom_id = None
        self._name = None
        self._description = None
        self._credit = None
        self._status = None
        self.discriminator = None

        self.classroom_id = classroom_id
        self.name = name
        self.description = description
        self.credit = credit
        self.status = status

    @property
    def classroom_id(self):
        r"""Gets the classroom_id of this ClassroomCard.

        课堂ID

        :return: The classroom_id of this ClassroomCard.
        :rtype: str
        """
        return self._classroom_id

    @classroom_id.setter
    def classroom_id(self, classroom_id):
        r"""Sets the classroom_id of this ClassroomCard.

        课堂ID

        :param classroom_id: The classroom_id of this ClassroomCard.
        :type classroom_id: str
        """
        self._classroom_id = classroom_id

    @property
    def name(self):
        r"""Gets the name of this ClassroomCard.

        课堂名称

        :return: The name of this ClassroomCard.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ClassroomCard.

        课堂名称

        :param name: The name of this ClassroomCard.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ClassroomCard.

        课堂描述

        :return: The description of this ClassroomCard.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ClassroomCard.

        课堂描述

        :param description: The description of this ClassroomCard.
        :type description: str
        """
        self._description = description

    @property
    def credit(self):
        r"""Gets the credit of this ClassroomCard.

        课堂学分

        :return: The credit of this ClassroomCard.
        :rtype: float
        """
        return self._credit

    @credit.setter
    def credit(self, credit):
        r"""Sets the credit of this ClassroomCard.

        课堂学分

        :param credit: The credit of this ClassroomCard.
        :type credit: float
        """
        self._credit = credit

    @property
    def status(self):
        r"""Gets the status of this ClassroomCard.

        课堂当前的状态，normal：课堂处于正常状态，archive：课堂已归档

        :return: The status of this ClassroomCard.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ClassroomCard.

        课堂当前的状态，normal：课堂处于正常状态，archive：课堂已归档

        :param status: The status of this ClassroomCard.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ClassroomCard):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
