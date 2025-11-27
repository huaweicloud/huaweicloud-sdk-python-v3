# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConnectEndpoint:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'name': 'str',
        'id': 'str',
        'region': 'str'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'id': 'id',
        'region': 'region'
    }

    def __init__(self, type=None, name=None, id=None, region=None):
        r"""ConnectEndpoint

        The model defined in huaweicloud sdk

        :param type: 取值：当前仅支持 VPCEP
        :type type: str
        :param name: 资源名称，当type是VPCEP时为VPCEP Service的名称
        :type name: str
        :param id: 资源id，当type是VPCEP时为VPCEP Service的id
        :type id: str
        :param region: 资源所在的region
        :type region: str
        """
        
        

        self._type = None
        self._name = None
        self._id = None
        self._region = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if region is not None:
            self.region = region

    @property
    def type(self):
        r"""Gets the type of this ConnectEndpoint.

        取值：当前仅支持 VPCEP

        :return: The type of this ConnectEndpoint.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ConnectEndpoint.

        取值：当前仅支持 VPCEP

        :param type: The type of this ConnectEndpoint.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        r"""Gets the name of this ConnectEndpoint.

        资源名称，当type是VPCEP时为VPCEP Service的名称

        :return: The name of this ConnectEndpoint.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ConnectEndpoint.

        资源名称，当type是VPCEP时为VPCEP Service的名称

        :param name: The name of this ConnectEndpoint.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this ConnectEndpoint.

        资源id，当type是VPCEP时为VPCEP Service的id

        :return: The id of this ConnectEndpoint.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ConnectEndpoint.

        资源id，当type是VPCEP时为VPCEP Service的id

        :param id: The id of this ConnectEndpoint.
        :type id: str
        """
        self._id = id

    @property
    def region(self):
        r"""Gets the region of this ConnectEndpoint.

        资源所在的region

        :return: The region of this ConnectEndpoint.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this ConnectEndpoint.

        资源所在的region

        :param region: The region of this ConnectEndpoint.
        :type region: str
        """
        self._region = region

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
        if not isinstance(other, ConnectEndpoint):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
