# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateProjectResponse(SdkResponse):

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
        'clone_url': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'clone_url': 'clone_url'
    }

    def __init__(self, id=None, name=None, clone_url=None):
        """CreateProjectResponse

        The model defined in huaweicloud sdk

        :param id: 项目ID。
        :type id: str
        :param name: 项目名称。
        :type name: str
        :param clone_url: 项目的clone url路径。
        :type clone_url: str
        """
        
        super(CreateProjectResponse, self).__init__()

        self._id = None
        self._name = None
        self._clone_url = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if clone_url is not None:
            self.clone_url = clone_url

    @property
    def id(self):
        """Gets the id of this CreateProjectResponse.

        项目ID。

        :return: The id of this CreateProjectResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateProjectResponse.

        项目ID。

        :param id: The id of this CreateProjectResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this CreateProjectResponse.

        项目名称。

        :return: The name of this CreateProjectResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateProjectResponse.

        项目名称。

        :param name: The name of this CreateProjectResponse.
        :type name: str
        """
        self._name = name

    @property
    def clone_url(self):
        """Gets the clone_url of this CreateProjectResponse.

        项目的clone url路径。

        :return: The clone_url of this CreateProjectResponse.
        :rtype: str
        """
        return self._clone_url

    @clone_url.setter
    def clone_url(self, clone_url):
        """Sets the clone_url of this CreateProjectResponse.

        项目的clone url路径。

        :param clone_url: The clone_url of this CreateProjectResponse.
        :type clone_url: str
        """
        self._clone_url = clone_url

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
        if not isinstance(other, CreateProjectResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
