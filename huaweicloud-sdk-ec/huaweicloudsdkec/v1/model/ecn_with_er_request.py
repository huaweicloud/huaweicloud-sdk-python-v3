# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EcnWithErRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'er_id': 'str',
        'region_project_id': 'str',
        'region_id': 'str'
    }

    attribute_map = {
        'er_id': 'er_id',
        'region_project_id': 'region_project_id',
        'region_id': 'region_id'
    }

    def __init__(self, er_id=None, region_project_id=None, region_id=None):
        """EcnWithErRequest

        The model defined in huaweicloud sdk

        :param er_id: 企业路由器ID
        :type er_id: str
        :param region_project_id: 企业路由器区域项目ID
        :type region_project_id: str
        :param region_id: 区域ID
        :type region_id: str
        """
        
        

        self._er_id = None
        self._region_project_id = None
        self._region_id = None
        self.discriminator = None

        self.er_id = er_id
        self.region_project_id = region_project_id
        self.region_id = region_id

    @property
    def er_id(self):
        """Gets the er_id of this EcnWithErRequest.

        企业路由器ID

        :return: The er_id of this EcnWithErRequest.
        :rtype: str
        """
        return self._er_id

    @er_id.setter
    def er_id(self, er_id):
        """Sets the er_id of this EcnWithErRequest.

        企业路由器ID

        :param er_id: The er_id of this EcnWithErRequest.
        :type er_id: str
        """
        self._er_id = er_id

    @property
    def region_project_id(self):
        """Gets the region_project_id of this EcnWithErRequest.

        企业路由器区域项目ID

        :return: The region_project_id of this EcnWithErRequest.
        :rtype: str
        """
        return self._region_project_id

    @region_project_id.setter
    def region_project_id(self, region_project_id):
        """Sets the region_project_id of this EcnWithErRequest.

        企业路由器区域项目ID

        :param region_project_id: The region_project_id of this EcnWithErRequest.
        :type region_project_id: str
        """
        self._region_project_id = region_project_id

    @property
    def region_id(self):
        """Gets the region_id of this EcnWithErRequest.

        区域ID

        :return: The region_id of this EcnWithErRequest.
        :rtype: str
        """
        return self._region_id

    @region_id.setter
    def region_id(self, region_id):
        """Sets the region_id of this EcnWithErRequest.

        区域ID

        :param region_id: The region_id of this EcnWithErRequest.
        :type region_id: str
        """
        self._region_id = region_id

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
        if not isinstance(other, EcnWithErRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
