# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeInstanceRequest:


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
        'instance_id': 'str',
        'body': 'InstanceModify'
    }

    attribute_map = {
        'application_id': 'application_id',
        'component_id': 'component_id',
        'instance_id': 'instance_id',
        'body': 'body'
    }

    def __init__(self, application_id=None, component_id=None, instance_id=None, body=None):
        """ChangeInstanceRequest - a model defined in huaweicloud sdk"""
        
        

        self._application_id = None
        self._component_id = None
        self._instance_id = None
        self._body = None
        self.discriminator = None

        self.application_id = application_id
        self.component_id = component_id
        self.instance_id = instance_id
        if body is not None:
            self.body = body

    @property
    def application_id(self):
        """Gets the application_id of this ChangeInstanceRequest.

        应用ID。

        :return: The application_id of this ChangeInstanceRequest.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this ChangeInstanceRequest.

        应用ID。

        :param application_id: The application_id of this ChangeInstanceRequest.
        :type: str
        """
        self._application_id = application_id

    @property
    def component_id(self):
        """Gets the component_id of this ChangeInstanceRequest.

        组件ID。

        :return: The component_id of this ChangeInstanceRequest.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        """Sets the component_id of this ChangeInstanceRequest.

        组件ID。

        :param component_id: The component_id of this ChangeInstanceRequest.
        :type: str
        """
        self._component_id = component_id

    @property
    def instance_id(self):
        """Gets the instance_id of this ChangeInstanceRequest.

        组件实例ID。

        :return: The instance_id of this ChangeInstanceRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ChangeInstanceRequest.

        组件实例ID。

        :param instance_id: The instance_id of this ChangeInstanceRequest.
        :type: str
        """
        self._instance_id = instance_id

    @property
    def body(self):
        """Gets the body of this ChangeInstanceRequest.


        :return: The body of this ChangeInstanceRequest.
        :rtype: InstanceModify
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ChangeInstanceRequest.


        :param body: The body of this ChangeInstanceRequest.
        :type: InstanceModify
        """
        self._body = body

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
        import simplejson as json
        return json.dumps(sanitize_for_serialization(self))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ChangeInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
