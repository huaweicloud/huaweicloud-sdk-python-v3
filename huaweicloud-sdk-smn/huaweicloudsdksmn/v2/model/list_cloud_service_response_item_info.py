# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCloudServiceResponseItemInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'show_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'show_name': 'show_name'
    }

    def __init__(self, name=None, show_name=None):
        r"""ListCloudServiceResponseItemInfo

        The model defined in huaweicloud sdk

        :param name: 云服务名称。
        :type name: str
        :param show_name: 云服务显示名称。
        :type show_name: str
        """
        
        

        self._name = None
        self._show_name = None
        self.discriminator = None

        self.name = name
        self.show_name = show_name

    @property
    def name(self):
        r"""Gets the name of this ListCloudServiceResponseItemInfo.

        云服务名称。

        :return: The name of this ListCloudServiceResponseItemInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListCloudServiceResponseItemInfo.

        云服务名称。

        :param name: The name of this ListCloudServiceResponseItemInfo.
        :type name: str
        """
        self._name = name

    @property
    def show_name(self):
        r"""Gets the show_name of this ListCloudServiceResponseItemInfo.

        云服务显示名称。

        :return: The show_name of this ListCloudServiceResponseItemInfo.
        :rtype: str
        """
        return self._show_name

    @show_name.setter
    def show_name(self, show_name):
        r"""Sets the show_name of this ListCloudServiceResponseItemInfo.

        云服务显示名称。

        :param show_name: The show_name of this ListCloudServiceResponseItemInfo.
        :type show_name: str
        """
        self._show_name = show_name

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
        if not isinstance(other, ListCloudServiceResponseItemInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
