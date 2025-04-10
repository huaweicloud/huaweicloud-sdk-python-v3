# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AntiVirusSwitchDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'anti_virus_status': 'int',
        'object_id': 'str'
    }

    attribute_map = {
        'anti_virus_status': 'anti_virus_status',
        'object_id': 'object_id'
    }

    def __init__(self, anti_virus_status=None, object_id=None):
        r"""AntiVirusSwitchDto

        The model defined in huaweicloud sdk

        :param anti_virus_status: 反病毒开关状态
        :type anti_virus_status: int
        :param object_id: 防护对象ID
        :type object_id: str
        """
        
        

        self._anti_virus_status = None
        self._object_id = None
        self.discriminator = None

        if anti_virus_status is not None:
            self.anti_virus_status = anti_virus_status
        if object_id is not None:
            self.object_id = object_id

    @property
    def anti_virus_status(self):
        r"""Gets the anti_virus_status of this AntiVirusSwitchDto.

        反病毒开关状态

        :return: The anti_virus_status of this AntiVirusSwitchDto.
        :rtype: int
        """
        return self._anti_virus_status

    @anti_virus_status.setter
    def anti_virus_status(self, anti_virus_status):
        r"""Sets the anti_virus_status of this AntiVirusSwitchDto.

        反病毒开关状态

        :param anti_virus_status: The anti_virus_status of this AntiVirusSwitchDto.
        :type anti_virus_status: int
        """
        self._anti_virus_status = anti_virus_status

    @property
    def object_id(self):
        r"""Gets the object_id of this AntiVirusSwitchDto.

        防护对象ID

        :return: The object_id of this AntiVirusSwitchDto.
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        r"""Sets the object_id of this AntiVirusSwitchDto.

        防护对象ID

        :param object_id: The object_id of this AntiVirusSwitchDto.
        :type object_id: str
        """
        self._object_id = object_id

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
        if not isinstance(other, AntiVirusSwitchDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
