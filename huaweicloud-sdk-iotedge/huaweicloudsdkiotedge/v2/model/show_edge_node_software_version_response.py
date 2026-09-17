# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEdgeNodeSoftwareVersionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'software_version': 'str'
    }

    attribute_map = {
        'software_version': 'software_version'
    }

    def __init__(self, software_version=None):
        r"""ShowEdgeNodeSoftwareVersionResponse

        The model defined in huaweicloud sdk

        :param software_version: 边缘应用id，只允许数字、英文小写、中划线，切必须以字母或数字结尾
        :type software_version: str
        """
        
        super().__init__()

        self._software_version = None
        self.discriminator = None

        if software_version is not None:
            self.software_version = software_version

    @property
    def software_version(self):
        r"""Gets the software_version of this ShowEdgeNodeSoftwareVersionResponse.

        边缘应用id，只允许数字、英文小写、中划线，切必须以字母或数字结尾

        :return: The software_version of this ShowEdgeNodeSoftwareVersionResponse.
        :rtype: str
        """
        return self._software_version

    @software_version.setter
    def software_version(self, software_version):
        r"""Sets the software_version of this ShowEdgeNodeSoftwareVersionResponse.

        边缘应用id，只允许数字、英文小写、中划线，切必须以字母或数字结尾

        :param software_version: The software_version of this ShowEdgeNodeSoftwareVersionResponse.
        :type software_version: str
        """
        self._software_version = software_version

    def to_dict(self):
        import warnings
        warnings.warn("ShowEdgeNodeSoftwareVersionResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowEdgeNodeSoftwareVersionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
