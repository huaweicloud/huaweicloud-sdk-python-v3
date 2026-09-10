# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Vpc:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'subnets': 'list[Subnet]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'subnets': 'subnets'
    }

    def __init__(self, id=None, name=None, subnets=None):
        r"""Vpc

        The model defined in huaweicloud sdk

        :param id: VPC 的 ID
        :type id: str
        :param name: VPC 的名字
        :type name: str
        :param subnets: VPC 下的可用子网列表
        :type subnets: list[:class:`huaweicloudsdkrds.v3.Subnet`]
        """
        
        

        self._id = None
        self._name = None
        self._subnets = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if subnets is not None:
            self.subnets = subnets

    @property
    def id(self):
        r"""Gets the id of this Vpc.

        VPC 的 ID

        :return: The id of this Vpc.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Vpc.

        VPC 的 ID

        :param id: The id of this Vpc.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this Vpc.

        VPC 的名字

        :return: The name of this Vpc.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Vpc.

        VPC 的名字

        :param name: The name of this Vpc.
        :type name: str
        """
        self._name = name

    @property
    def subnets(self):
        r"""Gets the subnets of this Vpc.

        VPC 下的可用子网列表

        :return: The subnets of this Vpc.
        :rtype: list[:class:`huaweicloudsdkrds.v3.Subnet`]
        """
        return self._subnets

    @subnets.setter
    def subnets(self, subnets):
        r"""Sets the subnets of this Vpc.

        VPC 下的可用子网列表

        :param subnets: The subnets of this Vpc.
        :type subnets: list[:class:`huaweicloudsdkrds.v3.Subnet`]
        """
        self._subnets = subnets

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
        if not isinstance(other, Vpc):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
