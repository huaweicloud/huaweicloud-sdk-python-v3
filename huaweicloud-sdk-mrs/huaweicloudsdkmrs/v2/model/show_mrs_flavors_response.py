# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMrsFlavorsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version_name': 'str',
        'available_flavors': 'list[AzFlavors]'
    }

    attribute_map = {
        'version_name': 'version_name',
        'available_flavors': 'available_flavors'
    }

    def __init__(self, version_name=None, available_flavors=None):
        r"""ShowMrsFlavorsResponse

        The model defined in huaweicloud sdk

        :param version_name: 版本名称
        :type version_name: str
        :param available_flavors: 不同可用区支持的规格列表
        :type available_flavors: list[:class:`huaweicloudsdkmrs.v2.AzFlavors`]
        """
        
        super(ShowMrsFlavorsResponse, self).__init__()

        self._version_name = None
        self._available_flavors = None
        self.discriminator = None

        if version_name is not None:
            self.version_name = version_name
        if available_flavors is not None:
            self.available_flavors = available_flavors

    @property
    def version_name(self):
        r"""Gets the version_name of this ShowMrsFlavorsResponse.

        版本名称

        :return: The version_name of this ShowMrsFlavorsResponse.
        :rtype: str
        """
        return self._version_name

    @version_name.setter
    def version_name(self, version_name):
        r"""Sets the version_name of this ShowMrsFlavorsResponse.

        版本名称

        :param version_name: The version_name of this ShowMrsFlavorsResponse.
        :type version_name: str
        """
        self._version_name = version_name

    @property
    def available_flavors(self):
        r"""Gets the available_flavors of this ShowMrsFlavorsResponse.

        不同可用区支持的规格列表

        :return: The available_flavors of this ShowMrsFlavorsResponse.
        :rtype: list[:class:`huaweicloudsdkmrs.v2.AzFlavors`]
        """
        return self._available_flavors

    @available_flavors.setter
    def available_flavors(self, available_flavors):
        r"""Sets the available_flavors of this ShowMrsFlavorsResponse.

        不同可用区支持的规格列表

        :param available_flavors: The available_flavors of this ShowMrsFlavorsResponse.
        :type available_flavors: list[:class:`huaweicloudsdkmrs.v2.AzFlavors`]
        """
        self._available_flavors = available_flavors

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
        if not isinstance(other, ShowMrsFlavorsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
