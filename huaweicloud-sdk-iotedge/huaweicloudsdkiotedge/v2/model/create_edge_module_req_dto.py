# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateEdgeModuleReqDTO:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'edge_app_id': 'str',
        'app_version': 'str'
    }

    attribute_map = {
        'edge_app_id': 'edge_app_id',
        'app_version': 'app_version'
    }

    def __init__(self, edge_app_id=None, app_version=None):
        """CreateEdgeModuleReqDTO - a model defined in huaweicloud sdk"""
        
        

        self._edge_app_id = None
        self._app_version = None
        self.discriminator = None

        self.edge_app_id = edge_app_id
        self.app_version = app_version

    @property
    def edge_app_id(self):
        """Gets the edge_app_id of this CreateEdgeModuleReqDTO.

        边缘应用名称

        :return: The edge_app_id of this CreateEdgeModuleReqDTO.
        :rtype: str
        """
        return self._edge_app_id

    @edge_app_id.setter
    def edge_app_id(self, edge_app_id):
        """Sets the edge_app_id of this CreateEdgeModuleReqDTO.

        边缘应用名称

        :param edge_app_id: The edge_app_id of this CreateEdgeModuleReqDTO.
        :type: str
        """
        self._edge_app_id = edge_app_id

    @property
    def app_version(self):
        """Gets the app_version of this CreateEdgeModuleReqDTO.

        边缘应用版本

        :return: The app_version of this CreateEdgeModuleReqDTO.
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        """Sets the app_version of this CreateEdgeModuleReqDTO.

        边缘应用版本

        :param app_version: The app_version of this CreateEdgeModuleReqDTO.
        :type: str
        """
        self._app_version = app_version

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
        if not isinstance(other, CreateEdgeModuleReqDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
