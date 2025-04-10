# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AntiVirusVO:

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
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'anti_virus_status': 'anti_virus_status',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, anti_virus_status=None, id=None, name=None):
        r"""AntiVirusVO

        The model defined in huaweicloud sdk

        :param anti_virus_status: 反病毒开关状态，0表示关闭，1表示开启
        :type anti_virus_status: int
        :param id: 防护对象id
        :type id: str
        :param name: 
        :type name: str
        """
        
        

        self._anti_virus_status = None
        self._id = None
        self._name = None
        self.discriminator = None

        if anti_virus_status is not None:
            self.anti_virus_status = anti_virus_status
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def anti_virus_status(self):
        r"""Gets the anti_virus_status of this AntiVirusVO.

        反病毒开关状态，0表示关闭，1表示开启

        :return: The anti_virus_status of this AntiVirusVO.
        :rtype: int
        """
        return self._anti_virus_status

    @anti_virus_status.setter
    def anti_virus_status(self, anti_virus_status):
        r"""Sets the anti_virus_status of this AntiVirusVO.

        反病毒开关状态，0表示关闭，1表示开启

        :param anti_virus_status: The anti_virus_status of this AntiVirusVO.
        :type anti_virus_status: int
        """
        self._anti_virus_status = anti_virus_status

    @property
    def id(self):
        r"""Gets the id of this AntiVirusVO.

        防护对象id

        :return: The id of this AntiVirusVO.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AntiVirusVO.

        防护对象id

        :param id: The id of this AntiVirusVO.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this AntiVirusVO.

        :return: The name of this AntiVirusVO.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AntiVirusVO.

        :param name: The name of this AntiVirusVO.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, AntiVirusVO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
