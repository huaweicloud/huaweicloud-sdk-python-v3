# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDeploymentResponse(SdkResponse):

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
        'locations': 'list[Location]'
    }

    attribute_map = {
        'id': 'id',
        'locations': 'locations'
    }

    def __init__(self, id=None, locations=None):
        """CreateDeploymentResponse

        The model defined in huaweicloud sdk

        :param id: 部署计划ID。
        :type id: str
        :param locations: 部署位置信息列表。
        :type locations: list[:class:`huaweicloudsdkiec.v1.Location`]
        """
        
        super(CreateDeploymentResponse, self).__init__()

        self._id = None
        self._locations = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if locations is not None:
            self.locations = locations

    @property
    def id(self):
        """Gets the id of this CreateDeploymentResponse.

        部署计划ID。

        :return: The id of this CreateDeploymentResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateDeploymentResponse.

        部署计划ID。

        :param id: The id of this CreateDeploymentResponse.
        :type id: str
        """
        self._id = id

    @property
    def locations(self):
        """Gets the locations of this CreateDeploymentResponse.

        部署位置信息列表。

        :return: The locations of this CreateDeploymentResponse.
        :rtype: list[:class:`huaweicloudsdkiec.v1.Location`]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """Sets the locations of this CreateDeploymentResponse.

        部署位置信息列表。

        :param locations: The locations of this CreateDeploymentResponse.
        :type locations: list[:class:`huaweicloudsdkiec.v1.Location`]
        """
        self._locations = locations

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
        if not isinstance(other, CreateDeploymentResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
