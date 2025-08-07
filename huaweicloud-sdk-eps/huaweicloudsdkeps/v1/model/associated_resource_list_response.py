# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssociatedResourceListResponse:

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
        'eip': 'str',
        'resource_type': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'eip': 'eip',
        'resource_type': 'resource_type'
    }

    def __init__(self, id=None, name=None, eip=None, resource_type=None):
        r"""AssociatedResourceListResponse

        The model defined in huaweicloud sdk

        :param id: 资源ID
        :type id: str
        :param name: 资源名称
        :type name: str
        :param eip: eip信息
        :type eip: str
        :param resource_type: 资源类型
        :type resource_type: str
        """
        
        

        self._id = None
        self._name = None
        self._eip = None
        self._resource_type = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if eip is not None:
            self.eip = eip
        if resource_type is not None:
            self.resource_type = resource_type

    @property
    def id(self):
        r"""Gets the id of this AssociatedResourceListResponse.

        资源ID

        :return: The id of this AssociatedResourceListResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AssociatedResourceListResponse.

        资源ID

        :param id: The id of this AssociatedResourceListResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this AssociatedResourceListResponse.

        资源名称

        :return: The name of this AssociatedResourceListResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AssociatedResourceListResponse.

        资源名称

        :param name: The name of this AssociatedResourceListResponse.
        :type name: str
        """
        self._name = name

    @property
    def eip(self):
        r"""Gets the eip of this AssociatedResourceListResponse.

        eip信息

        :return: The eip of this AssociatedResourceListResponse.
        :rtype: str
        """
        return self._eip

    @eip.setter
    def eip(self, eip):
        r"""Sets the eip of this AssociatedResourceListResponse.

        eip信息

        :param eip: The eip of this AssociatedResourceListResponse.
        :type eip: str
        """
        self._eip = eip

    @property
    def resource_type(self):
        r"""Gets the resource_type of this AssociatedResourceListResponse.

        资源类型

        :return: The resource_type of this AssociatedResourceListResponse.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this AssociatedResourceListResponse.

        资源类型

        :param resource_type: The resource_type of this AssociatedResourceListResponse.
        :type resource_type: str
        """
        self._resource_type = resource_type

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
        if not isinstance(other, AssociatedResourceListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
