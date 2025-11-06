# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchTokenResponseAk:

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
        'id': 'str',
        'status': 'str'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'status': 'status'
    }

    def __init__(self, name=None, id=None, status=None):
        r"""SwitchTokenResponseAk

        The model defined in huaweicloud sdk

        :param name: ak名称
        :type name: str
        :param id: ak id
        :type id: str
        :param status: ak状态
        :type status: str
        """
        
        

        self._name = None
        self._id = None
        self._status = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if status is not None:
            self.status = status

    @property
    def name(self):
        r"""Gets the name of this SwitchTokenResponseAk.

        ak名称

        :return: The name of this SwitchTokenResponseAk.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SwitchTokenResponseAk.

        ak名称

        :param name: The name of this SwitchTokenResponseAk.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this SwitchTokenResponseAk.

        ak id

        :return: The id of this SwitchTokenResponseAk.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SwitchTokenResponseAk.

        ak id

        :param id: The id of this SwitchTokenResponseAk.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this SwitchTokenResponseAk.

        ak状态

        :return: The status of this SwitchTokenResponseAk.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SwitchTokenResponseAk.

        ak状态

        :param status: The status of this SwitchTokenResponseAk.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, SwitchTokenResponseAk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
