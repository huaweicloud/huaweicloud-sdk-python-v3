# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteComponentRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'application_id': 'str',
        'component_id': 'str',
        'force': 'bool'
    }

    attribute_map = {
        'application_id': 'application_id',
        'component_id': 'component_id',
        'force': 'force'
    }

    def __init__(self, application_id=None, component_id=None, force=None):
        """DeleteComponentRequest

        The model defined in huaweicloud sdk

        :param application_id: 应用ID。
        :type application_id: str
        :param component_id: 组件ID。
        :type component_id: str
        :param force: 是否强制删除。
        :type force: bool
        """
        
        

        self._application_id = None
        self._component_id = None
        self._force = None
        self.discriminator = None

        self.application_id = application_id
        self.component_id = component_id
        if force is not None:
            self.force = force

    @property
    def application_id(self):
        """Gets the application_id of this DeleteComponentRequest.

        应用ID。

        :return: The application_id of this DeleteComponentRequest.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this DeleteComponentRequest.

        应用ID。

        :param application_id: The application_id of this DeleteComponentRequest.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def component_id(self):
        """Gets the component_id of this DeleteComponentRequest.

        组件ID。

        :return: The component_id of this DeleteComponentRequest.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        """Sets the component_id of this DeleteComponentRequest.

        组件ID。

        :param component_id: The component_id of this DeleteComponentRequest.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def force(self):
        """Gets the force of this DeleteComponentRequest.

        是否强制删除。

        :return: The force of this DeleteComponentRequest.
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        """Sets the force of this DeleteComponentRequest.

        是否强制删除。

        :param force: The force of this DeleteComponentRequest.
        :type force: bool
        """
        self._force = force

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
        if not isinstance(other, DeleteComponentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
