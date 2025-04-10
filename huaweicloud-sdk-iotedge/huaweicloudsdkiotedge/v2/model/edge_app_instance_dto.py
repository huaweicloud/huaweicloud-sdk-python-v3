# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EdgeAppInstanceDTO:

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
        r"""EdgeAppInstanceDTO

        The model defined in huaweicloud sdk

        :param edge_app_id: 边缘应用id，只允许数字、英文小写、中划线，切必须以字母或数字结尾
        :type edge_app_id: str
        :param app_version: 边缘应用版本，只允许数字、英文小写、中划线，切必须以字母或数字结尾
        :type app_version: str
        """
        
        

        self._edge_app_id = None
        self._app_version = None
        self.discriminator = None

        self.edge_app_id = edge_app_id
        if app_version is not None:
            self.app_version = app_version

    @property
    def edge_app_id(self):
        r"""Gets the edge_app_id of this EdgeAppInstanceDTO.

        边缘应用id，只允许数字、英文小写、中划线，切必须以字母或数字结尾

        :return: The edge_app_id of this EdgeAppInstanceDTO.
        :rtype: str
        """
        return self._edge_app_id

    @edge_app_id.setter
    def edge_app_id(self, edge_app_id):
        r"""Sets the edge_app_id of this EdgeAppInstanceDTO.

        边缘应用id，只允许数字、英文小写、中划线，切必须以字母或数字结尾

        :param edge_app_id: The edge_app_id of this EdgeAppInstanceDTO.
        :type edge_app_id: str
        """
        self._edge_app_id = edge_app_id

    @property
    def app_version(self):
        r"""Gets the app_version of this EdgeAppInstanceDTO.

        边缘应用版本，只允许数字、英文小写、中划线，切必须以字母或数字结尾

        :return: The app_version of this EdgeAppInstanceDTO.
        :rtype: str
        """
        return self._app_version

    @app_version.setter
    def app_version(self, app_version):
        r"""Sets the app_version of this EdgeAppInstanceDTO.

        边缘应用版本，只允许数字、英文小写、中划线，切必须以字母或数字结尾

        :param app_version: The app_version of this EdgeAppInstanceDTO.
        :type app_version: str
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
        if not isinstance(other, EdgeAppInstanceDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
