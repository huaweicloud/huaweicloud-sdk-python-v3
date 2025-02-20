# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplicationModelQueryResponseData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sub_applications': 'list[ApplicationInfo]',
        'components': 'list[ComponentInfo]',
        'groups': 'list[GroupInfo]'
    }

    attribute_map = {
        'sub_applications': 'sub_applications',
        'components': 'components',
        'groups': 'groups'
    }

    def __init__(self, sub_applications=None, components=None, groups=None):
        """ApplicationModelQueryResponseData

        The model defined in huaweicloud sdk

        :param sub_applications: 
        :type sub_applications: list[:class:`huaweicloudsdkcoc.v1.ApplicationInfo`]
        :param components: 
        :type components: list[:class:`huaweicloudsdkcoc.v1.ComponentInfo`]
        :param groups: 
        :type groups: list[:class:`huaweicloudsdkcoc.v1.GroupInfo`]
        """
        
        

        self._sub_applications = None
        self._components = None
        self._groups = None
        self.discriminator = None

        if sub_applications is not None:
            self.sub_applications = sub_applications
        if components is not None:
            self.components = components
        if groups is not None:
            self.groups = groups

    @property
    def sub_applications(self):
        """Gets the sub_applications of this ApplicationModelQueryResponseData.

        :return: The sub_applications of this ApplicationModelQueryResponseData.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ApplicationInfo`]
        """
        return self._sub_applications

    @sub_applications.setter
    def sub_applications(self, sub_applications):
        """Sets the sub_applications of this ApplicationModelQueryResponseData.

        :param sub_applications: The sub_applications of this ApplicationModelQueryResponseData.
        :type sub_applications: list[:class:`huaweicloudsdkcoc.v1.ApplicationInfo`]
        """
        self._sub_applications = sub_applications

    @property
    def components(self):
        """Gets the components of this ApplicationModelQueryResponseData.

        :return: The components of this ApplicationModelQueryResponseData.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.ComponentInfo`]
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this ApplicationModelQueryResponseData.

        :param components: The components of this ApplicationModelQueryResponseData.
        :type components: list[:class:`huaweicloudsdkcoc.v1.ComponentInfo`]
        """
        self._components = components

    @property
    def groups(self):
        """Gets the groups of this ApplicationModelQueryResponseData.

        :return: The groups of this ApplicationModelQueryResponseData.
        :rtype: list[:class:`huaweicloudsdkcoc.v1.GroupInfo`]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this ApplicationModelQueryResponseData.

        :param groups: The groups of this ApplicationModelQueryResponseData.
        :type groups: list[:class:`huaweicloudsdkcoc.v1.GroupInfo`]
        """
        self._groups = groups

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
        if not isinstance(other, ApplicationModelQueryResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
