# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplicationProfileDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'status': 'str',
        'profile_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'status': 'status',
        'profile_id': 'profile_id'
    }

    def __init__(self, name=None, status=None, profile_id=None):
        r"""ApplicationProfileDto

        The model defined in huaweicloud sdk

        :param name: 关联关系名称，默认为Default
        :type name: str
        :param status: 关联关系状态，默认为ENABLED
        :type status: str
        :param profile_id: 实体与应用程序关联ID
        :type profile_id: str
        """
        
        

        self._name = None
        self._status = None
        self._profile_id = None
        self.discriminator = None

        self.name = name
        self.status = status
        self.profile_id = profile_id

    @property
    def name(self):
        r"""Gets the name of this ApplicationProfileDto.

        关联关系名称，默认为Default

        :return: The name of this ApplicationProfileDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ApplicationProfileDto.

        关联关系名称，默认为Default

        :param name: The name of this ApplicationProfileDto.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this ApplicationProfileDto.

        关联关系状态，默认为ENABLED

        :return: The status of this ApplicationProfileDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ApplicationProfileDto.

        关联关系状态，默认为ENABLED

        :param status: The status of this ApplicationProfileDto.
        :type status: str
        """
        self._status = status

    @property
    def profile_id(self):
        r"""Gets the profile_id of this ApplicationProfileDto.

        实体与应用程序关联ID

        :return: The profile_id of this ApplicationProfileDto.
        :rtype: str
        """
        return self._profile_id

    @profile_id.setter
    def profile_id(self, profile_id):
        r"""Sets the profile_id of this ApplicationProfileDto.

        实体与应用程序关联ID

        :param profile_id: The profile_id of this ApplicationProfileDto.
        :type profile_id: str
        """
        self._profile_id = profile_id

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
        if not isinstance(other, ApplicationProfileDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
